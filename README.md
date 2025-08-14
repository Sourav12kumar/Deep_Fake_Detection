# Deep Fake Detection 🔍

A deep learning project to detect fake videos and images using **XceptionNet**.

---

## 📌 Features
- Detects deepfake images & videos  
- Supports `.jpg`, `.png`, `.mp4` formats  
- Uses **Xception model** trained on Deepfake Detection Challenge dataset  
- Provides **explainable AI** results with LIME  

---

## 📂 Project Structure
deepfake_detection/
│-- app.py # Streamlit application
│-- requirements.txt # Project dependencies
│-- models/ # Model folder
│ ├── train_model.ipynb # Notebook to train your own model
│ ├── xception_deepfake_image.h5 # Pretrained model (after download)
│-- src/ # Source code
│-- README.md

**train your own model** in the model folder where is a .ipynb file to train the model in kaggle and with it dataset
link to download the pretrain model (i.e. .h5 ) - https://drive.google.com/file/d/14D7gb2BE25rCvFR5IJUtuh0SMjGPa-ir/view?usp=drive_link

---

## ⚙️ Installation & Setup

### **Optional**: Create and activate a virtual environment
---
python -m venv samplename
samplename\Scripts\activate.bat


**optional** :  python -m venv samplename
            samplename\Scripts\activate.bat   
               **step 1**: download the pretrain model link given above or train the own model using the .ipynb file given under models folder and placed the .h5 in models folder               **step 2**: pip install -r requirements.txt
               **step 3**: streamlit run app.py

            Step 1: Download or Train Model

You have two options:

Download the pretrained model (.h5) from:
Download Here
Place it in the models/ folder.

Train your own model using the .ipynb file provided in the models/ folder (use Kaggle or Jupyter Notebook).
Save the trained model as .h5 inside the models/ folder.                      
 Step 2: Install dependencies
            pip install -r requirements.txt

 Step 3: Run the Streamlit App
            streamlit run app.py
