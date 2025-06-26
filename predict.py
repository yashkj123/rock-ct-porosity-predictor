##This is the Script that allows running prediction from terminal or Jupyter cell:
import os
import cv2
import torch
import numpy as np
import argparse
import sys
sys.path.append(os.path.abspath("utils"))
from unet_model import UNet

# --------------------------
# Step 1: Setup + Load Model
# --------------------------
model = UNet()
model.load_state_dict(torch.load("model/unet_rock_model.pth", map_location='cpu'))
model.eval()
os.makedirs("outputs", exist_ok=True)

# --------------------------
# Step 2: Parse Optional Arg
# --------------------------
parser = argparse.ArgumentParser()
parser.add_argument('--img', type=str, help='Path to a single input image')
args = parser.parse_args()

# --------------------------
# Step 3: Define image list
# --------------------------
image_list = []

if args.img:
    # User gave one image
    image_list = [args.img]
else:
    # No image specified — process all in folder
    input_folder = "user_inputs"
    image_list = [
        os.path.join(input_folder, f)
        for f in sorted(os.listdir(input_folder))
        if f.lower().endswith((".png", ".jpg"))
    ]
    if not image_list:
        print("⚠️ No images found in user_inputs/ folder.")
        exit()

# --------------------------
# Step 4: Loop and Predict
# --------------------------
for img_path in image_list:
    img_name = os.path.basename(img_path)
    print(f"\n🖼️ Processing: {img_name}")

    # Load image
    img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)
    if img is None:
        print(f"❌ Image not found or unreadable: {img_path}")
        continue

    img_resized = cv2.resize(img, (128, 128))
    img_norm = img_resized / 255.0
    img_tensor = torch.tensor(img_norm, dtype=torch.float32).unsqueeze(0).unsqueeze(0)

    # Predict
    with torch.no_grad():
        pred_mask = model(img_tensor).squeeze().numpy()

    binary_mask = (pred_mask > 0.5).astype(np.uint8)
    porosity = (np.sum(binary_mask) / binary_mask.size) * 100
    print(f"✅ Porosity for {img_name}: {porosity:.2f}%")

    # Save predicted mask
    mask_path = f"outputs/predicted_{img_name}"
    cv2.imwrite(mask_path, (pred_mask * 255).astype(np.uint8))
    print(f"🖼️ Saved predicted mask to: {mask_path}")

    # Save side-by-side comparison
    comparison = np.hstack([
        cv2.resize(img, (128, 128)),
        (pred_mask * 255).astype(np.uint8)
    ])
    comp_path = f"outputs/comparison_{img_name}"
    cv2.imwrite(comp_path, comparison)
    print(f"🖼️ Saved side-by-side comparison to: {comp_path}")



