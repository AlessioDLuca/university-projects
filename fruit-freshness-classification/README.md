# 🍏 Deep Learning for Fruit Classification and Freshness Detection  

## 📃 Project Overview  
This project explores **deep learning techniques** for **fruit classification and freshness detection** using **Convolutional Neural Networks (CNNs)**. The study evaluates a **custom CNN model** and a **fine-tuned ResNet-18**, incorporating **pruning techniques** to enhance computational efficiency. Additionally, **Explainable AI (XAI) techniques** are used to improve model interpretability, analyzing decision-making patterns.

---

## 🔍 Objectives  
- 🌟 **Classify fruits and vegetables** into categories (apples, bananas, cucumbers, etc.).  
- 🌟 **Assess freshness** (fresh vs. rotten) using deep learning models.  
- 🌟 **Optimize model performance** by applying pruning techniques at **30%, 50%, and 70%**.  
- 🌟 **Utilize Explainable AI (XAI)** to analyze model decision-making.  

---

## 📝 Dataset & Preprocessing  
### 🌍 **Fresh and Rotten Classification Dataset**  
- **Training set**: 23,619 images.  
- **Test set**: 6,738 images.  
- **Labels**: Each image has two labels:
  - **Category label** (e.g., apple, banana, potato, etc.).
  - **Freshness label** (0 = fresh, 1 = rotten).  

### 🛠️ **Data Processing Steps**  
- **Error Correction**: Fixed incorrect fruit and vegetable names in labels.
- **Class Balancing**: Adjusted dataset distribution by redistributing **capsicum** and **bitter gourd** samples.
- **Image Standardization**:
  - Resized all images to **224x224 pixels**.
  - Applied **pixel intensity normalization** (mean = 0, std = 1).

---

## 🎨 Model Development  
### 🛡️ **Custom CNN Model**  
- A **lightweight CNN** designed for this task.
- Architecture includes **3 convolutional layers** followed by fully connected layers.
- Model branches into **two classification heads**: one for fruit type, one for freshness detection.
- **Total parameters**: **1,638,315**.

### 🌐 **Fine-Tuned ResNet-18**  
- Modified **ResNet-18** pre-trained model.
- Separate classification branches for **fruit type** and **freshness detection**.
- **Total parameters**: **11,361,771**.

### 🔄 **Pruned ResNet-18 Models**  
- **Global L1 unstructured pruning** applied at **30%, 50%, and 70%**.
- Evaluates the trade-off between **accuracy and computational efficiency**.

---

## 📊 Training & Results  
| Model                     | Fruit Classification Accuracy | Freshness Classification Accuracy |
|---------------------------|------------------------------|-----------------------------------|
| **Custom CNN**            | 74.29%                       | 76.27%                            |
| **Fine-Tuned ResNet-18**  | 92.24%                       | 92.53%                            |
| **Pruned ResNet-18 (30%)**| 98.41%                       | 96.18%                            |
| **Pruned ResNet-18 (50%)**| 97.86%                       | 97.14%                            |
| **Pruned ResNet-18 (70%)**| 97.57%                       | 96.55%                            |

- **Fine-tuned ResNet-18 significantly outperformed the Custom CNN.**
- **Pruned models showed improved accuracy**, with **30% pruning** achieving the best balance between size and performance.

---

## 🔬 Explainable AI (XAI)  
- **Class Activation Mapping (CAM)** used to visualize regions influencing model decisions.
- **CNN Model**: Focused on **high-contrast areas**, sometimes misclassifying due to **lighting variations**.
- **ResNet-18 Model**: Showed a **broader focus**, analyzing **entire fruit regions**, reducing misclassification errors.

---

## 🎨 Future Work  
- **Implement an object detection model** to classify multiple fruits in a single image.  
- **Expand dataset diversity** to improve model robustness.  
- **Develop an online application** for real-time classification using live camera feeds.  
- **Integrate continual learning** to allow adaptation to new fruit types and specific industry applications.  

---

## 📚 Acknowledgments  
This project was in collaboration with **Luca Pivetti**.

---
