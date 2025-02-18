# ⚕️ AI Solutions for Healthcare  


This repository contains two **AI-driven healthcare projects**, developed during the **second semester of the 2023/24 Master's program**. The focus is on leveraging **machine learning and deep learning** to enhance **diagnostic capabilities** in two critical domains:
- **Epilepsy symptom recognition from EEG signals**.
- **Breast cancer mass detection through ultrasound imaging**.

---

## 🎨 Project 1: **Epilepsy Detection via EEG Analysis**  
### 🔍 Objectives  
- Automate the recognition of **epilepsy symptoms** from EEG signals.
- Provide neurologists with a **reliable** and **efficient diagnostic tool**.

### 🛠️ Key Steps  
#### **1️⃣ Data Preparation**  
- **Dataset**: 500 EEG signals, each containing **4,094 measurements**.
- **Preprocessing**: Z-score normalization & outlier detection (**1 & 2 standard deviations** thresholds).

#### **2️⃣ Machine Learning Models**  
- Classified EEG signals into **mild** and **mild-severe epilepsy**.
- Used **Support Vector Machines (SVM)** and **Random Forests**.
- Hyperparameter tuning via **5-fold cross-validation** and **grid search**.

#### **3️⃣ Feature Engineering**  
- **Principal Component Analysis (PCA)** and **K-Best** for feature selection.

### 📊 Results  
| Model | Accuracy | Sensitivity | Specificity |
|--------|------------|------------|------------|
| **Random Forest (200 estimators, log-loss criterion)** | **90.3%** | **93.7%** | **87.0%** |

- **Significant improvement** in diagnostic accuracy, especially for **severe cases of epilepsy**.

---

## 🏢 Project 2: **Breast Cancer Detection via Ultrasound Imaging**  
### 🔍 Objectives  
- Develop an **AI tool** to classify **breast lumps** as **cancerous or non-cancerous**.
- Integrate models into a **user-friendly interface** for **global oncologists**.

### 🛠️ Key Steps  
#### **1️⃣ Image Preprocessing**  
- **Resized** ultrasound images to **128x128**, converted to **grayscale**, and **normalized**.
- **Data augmentation** (horizontal flip & slight rotation) to **increase training data**.

#### **2️⃣ Image Segmentation**  
- **U-Net Convolutional Neural Network** for **mass segmentation**.
- Trained for **100 epochs** using **Adam optimizer**, achieving:
  - **Mean IoU**: **75%**
  - **DICE Coefficient**: **72%**
  - **Precision/Recall/F1**: **72%**

#### **3️⃣ Classification**  
- **Support Vector Machine (SVM)** with **RBF kernel** for classification.
- Hyperparameter tuning achieved:
  - **Accuracy**: **97%**
  - **Sensitivity**: **95%**
  - **Specificity**: **98%**

#### **4️⃣ Dashboard**  
- A **Streamlit dashboard** with an intuitive **diagnostic interface**.

### 📊 Results  
- The **integrated AI tool** significantly enhances **breast cancer diagnosis**.
- Provides **accurate classification** & **segmentation** of breast lumps from ultrasound images.

---

## 📝 Conclusion  
Both projects highlight the power of **machine learning** in **healthcare diagnostics** by automating complex tasks, ultimately improving **early detection and treatment outcomes** for **epilepsy** and **breast cancer patients**.

---

## 📚 Acknowledgments  
This project was developed in collaboration with **Simone Vaccari** and **Davide Vettore**.
---

