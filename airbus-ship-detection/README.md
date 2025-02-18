# 🚢 Airbus Ship Detection Challenge  

This project focuses on **ship detection in satellite imagery** using deep learning. It is based on the **Airbus Ship Detection Challenge**, leveraging **ResNet-101 U-Net** for segmentation. The repository includes a **Jupyter Notebook for training and inference** and a **Streamlit dashboard** for real-time segmentation visualization.

---

## 💡 Project Overview  
- **🔍 Goal:** Detect ships in satellite images using deep learning.  
- **📄 Dataset:** [Airbus Ship Detection Challenge](https://www.kaggle.com/competitions/airbus-ship-detection).  
- **🧠 Model:** Trained **ResNet-101 U-Net** for segmentation.  
- **🛠️ Tools Used:** PyTorch, Streamlit, OpenCV, NumPy.  

---

## 🛠️ How to Run  
### **1️⃣ Running the Jupyter Notebook**  
- The notebook can be executed on **Google Colab** or **Kaggle**.  
- If using **Colab**, run the *"Kaggle function to run on Colab"* cell.  
- If using **Kaggle**, ensure the dataset is loaded into the environment.

### **2️⃣ Running the Streamlit Dashboard**  
1. Install dependencies:  
   ```bash
   pip install torch torchvision streamlit segmentation-models-pytorch
   ```  
2. Run the **Streamlit app**:  
   ```bash
   streamlit run main.py
   ```  
3. **Note**: The trained model weights (`ResNet101.pth`) **are not included in this repository due to file size limitations**. Download them separately from Kaggle:  
   - **Kaggle Model Path:** [alessiodeluca12/resnet101deluca](https://www.kaggle.com/alessiodeluca12/resnet101deluca)  
   - Place the downloaded weights in the appropriate directory and update the model path in `StreamlitDashboard.py` (line 105).  

---

## 🖼️ Test Images  
- A folder named **`DashboardImages/`** contains test images for inference.  
- The model works best on **satellite images** of ships.  

⚠️ **Using random images (e.g., a family dinner) may result in false ship detections!**  

---


## 🎯 Future Improvements  
- Enhance segmentation accuracy using **data augmentation**.  
- Experiment with **transformer-based vision models**.  
- Optimize inference speed for **real-time applications**.  



