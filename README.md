# Malaria Cell Image Classification

This project classifies malaria cell images into **Parasitized** and **Uninfected** categories.  
It uses a **Feedforward Neural Network (FFN)** with regularization techniques and compares it to a **Support Vector Machine (SVM)** baseline with PCA.

The dataset can be downloaded from Kaggle:  
👉 [Cell Images for Detecting Malaria](https://www.kaggle.com/datasets/iarunava/cell-images-for-detecting-malaria/)


---

## 📂 Files Overview

- **`split_dataset.py`**  
  Splits the original malaria dataset into training, validation, and test sets.  

- **`resize_images.py`**  
  Resizes all dataset images to **64×64 RGB** for consistent input to the models.  

- **`main.ipynb`**  
  Main notebook that:  
  - Trains the baseline FFN.  
  - Applies L2, Dropout, and Early Stopping regularization.  
  - Trains an SVM with PCA.  
  - Compares FFN vs. SVM results and generates plots.  

---

Install dependencies with:
```bash
pip install -r requirements.txt
## ⚙️ How to Run

### 1. Split the dataset
Run the script to create **train**, **valid**, and **test** splits:
```bash
python split_dataset.py

python resize_images.py

jupyter notebook main.ipynb

