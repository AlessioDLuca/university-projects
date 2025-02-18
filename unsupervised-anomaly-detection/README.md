# 🛠️ Unsupervised Anomaly Detection  

## 📃 Project Overview  
This project applies **unsupervised anomaly detection techniques** to a **hypothyroidism dataset** containing **7,200 records** and **21 features**. The aim is to identify **outliers** using different machine learning approaches without predefined labels, making it a purely **unsupervised learning** problem.

The dataset consists of **15 categorical** and **6 continuous** features, with various preprocessing steps such as **correlation analysis** and **Gower's distance computation** to manage mixed data types effectively.

---

## 🔍 Objectives  
- 🌟 **Detect anomalies in hypothyroidism data** using unsupervised learning.  
- 🌟 **Compare multiple anomaly detection techniques** to evaluate performance.  
- 🌟 **Convert anomaly scores into probabilities** using logistic regression.  
- 🌟 **Analyze feature importance** in identifying anomalies.

---

## 📝 Dataset & Preprocessing  
### 🌐 **Dataset Description**  
- **7,200 samples**, **21 features** (15 categorical, 6 continuous).  
- **Duplicates detected**: 71 (not removed due to potential significance).  
- **Feature analysis**: Pearson correlation identified highly correlated variables.  
- **Dissimilarity Measure**: Gower’s distance was applied due to the mix of categorical and continuous features.

### 🛠️ **Techniques Used**  
#### 1️⃣ Anomaly Detection Algorithms  
- **COF (Connectivity-Based Outlier Factor):** Identifies anomalies using the density of nearest neighbors.  
- **PCA (Principal Component Analysis):** Detects anomalies based on reconstruction error in reduced dimensional space.  
- **K-Nearest Neighbors (KNN):** Assigns anomaly scores based on distance from neighbors.  
- **DBSCAN (Density-Based Spatial Clustering of Applications with Noise):** Identifies anomalies as points not belonging to any dense cluster.  

#### 2️⃣ Anomaly Identification  
- **Knee Locator Method:** Determines threshold at the point of maximum curvature.  
- **Top 5% Criterion:** Labels the highest-scoring 5% of points as anomalies.  

#### 3️⃣ Anomaly Score Conversion  
- A logistic regression model was trained on detected anomalies to assign **anomaly probabilities** to each data point.  

---

## 📊 Results  
| Algorithm | Anomalies (Knee Locator) | Anomalies (Top 5%) |  
|-----------|--------------------------|----------------------|  
| **COF**   | 210                      | 360                  |  
| **PCA**   | 127                      | 360                  |  
| **KNN**   | 153                      | 360                  |  
| **DBSCAN**| 322                      | -                    |  

- **DBSCAN & KNN** produced similar anomaly distributions (IoU = 0.894).  
- **PCA showed the clearest anomaly distinction** based on reconstruction error analysis.  
- **Final step:** PCA results were used for probability conversion, leading to **127 high-probability anomalies**.

---

## 📝 Conclusion  
- **Anomaly detection successfully identified outliers** in the dataset using multiple techniques.  
- **PCA provided the best results**, effectively capturing anomaly distributions.  
- **Gower's distance was an effective dissimilarity measure** for mixed-type data.  

---

## 🎨 Future Work  
- **Refine the probability estimation model** using alternative classification techniques.  
- **Apply deep learning approaches** like autoencoders for anomaly detection.  
- **Validate anomaly findings with expert domain knowledge** to ensure real-world relevance.  

---

## 📚 Acknowledgments  
This project was conducted as part of the **Artificial Intelligence for Science and Technology Master's Program** by **Alessio De Luca** and **Camilla Tomasoni**. The full report detailing methodology, analysis, and results is available for further insights.

---

