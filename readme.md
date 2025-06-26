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

## ✍️ Credits

- U-Net implementation in PyTorch  
- Developed by **Yash Kumar Jha**  

---

## 🔓 License

This project is open-source and free to use for academic, research, and demo purposes with proper attribution to the author.

---

## 🌍 Live Demo (Web App)

✅ You can try the Rock CT Porosity Predictor directly in your browser:  
🔗 **[Launch Live App](https://yashkj123-rock-ct-porosity-predictor.hf.space)** *(hosted on Hugging Face Spaces)*

No installation required — just upload your `.png` rock CT scan and get instant predictions with visual results.

---

## 🧪 Local Demo (Terminal Version)

To run the project locally:

1. Clone this repository
2. Install dependencies using:
   ```bash
   pip install -r requirements.txt
   ```
3. Launch local app:
   ```bash
   python app.py
   ```

Open your browser and visit:  
👉 `http://127.0.0.1:7860/` to use the app locally
