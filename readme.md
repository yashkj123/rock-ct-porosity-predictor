# 🧠 Rock CT Porosity Predictor  

A deep learning-based tool to predict **pore structure** and estimate **porosity** from grayscale **CT scan images** of rock samples.  
Built using Python and a U-Net model trained on real rock CT data.

---

## 🚀 Features

- Upload one or many `.png` / `.jpg` rock CT scan images
- Segment pore regions using a trained U-Net model
- Estimate porosity percentage automatically
- Save outputs:
  - Predicted pore mask
  - Side-by-side comparison (input + predicted)
- Command-line or batch folder support
- Ready for GitHub and deployment

---

## 📂 Folder Structure

```
rock-ct-porosity-predictor/
├── model/
│   └── unet_rock_model.pth
├── user_inputs/
│   └── rock_01.png, rock_02.png ...
├── outputs/
│   └── predicted_rock_01.png
│   └── comparison_rock_01.png
├── utils/
│   └── unet_model.py
├── predict.py
├── main.ipynb
├── README.md
├── requirements.txt
```

---

## 🔧 How to Use

### ▶️ Option 1: Predict a Single Image
```bash
python predict.py --img user_inputs/rock_01.png
```

### 🔁 Option 2: Predict All Images in `user_inputs/` Folder
```bash
python predict.py
```

---
🚧 Local Demo Only (Testing Mode)

This application is currently running locally using Gradio. You can test it by running the following command:

```bash
python app.py


## 📤 Output Example

For each image:
- ✅ `outputs/predicted_<filename>.png` → binary pore mask
- ✅ `outputs/comparison_<filename>.png` → side-by-side comparison

Example output in terminal:
```
🖼️ Processing: rock_01.png
✅ Porosity for rock_01.png: 23.45%
🖼️ Saved predicted mask to: outputs/predicted_rock_01.png
🖼️ Saved side-by-side comparison to: outputs/comparison_rock_01.png
```

---

## 📦 Installation

### 🔹 Install all required packages:
```bash
pip install -r requirements.txt
```

### `requirements.txt` should include:
```
torch
torchvision
opencv-python
matplotlib
numpy
```

---

## 🌐 Coming Soon

- [ ] Web UI using Gradio for interactive image upload
- [ ] Hugging Face Spaces deployment for public demo

---

## 🔓 License

This project is open-source and free to use for academic, research, and demo purposes with proper attribution to the author.

