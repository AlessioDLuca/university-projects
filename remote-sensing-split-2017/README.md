# 🌳 Vegetation Damage Assessment from the 2017 Split Fire (Sentinel-2 Remote Sensing)

## 📃 Project Overview
This project investigates the impact of the **2017 wildfire near Split, Croatia**, on vegetation using **remote sensing techniques**. Sentinel-2 satellite imagery was utilized to analyze pre- and post-fire conditions, assessing the extent of **vegetation loss and recovery** through indices such as **NDVI (Normalized Difference Vegetation Index)** and **NBR (Normalized Burn Ratio)**.

Additionally, **unsupervised clustering methods** were applied to categorize fire-affected areas, offering deeper insights into the wildfire's environmental consequences.

---

## 🔍 Objectives
- 🌟 **Assess vegetation loss** using Sentinel-2 satellite imagery.
- 🌟 **Utilize NDVI and NBR indices** to quantify burn severity and post-fire vegetation recovery.
- 🌟 **Apply unsupervised clustering techniques** to identify affected regions.
- 🌟 **Compare the study results** with actual damage assessments.

---

## 📝 Dataset and Methodology
### 🌍 **Sentinel-2 Imagery**
- Data from the **Copernicus Sentinel-2 mission** was used.
- Three timeframes analyzed: **Pre-Fire (07/07/2017), During-Fire (07/17/2017), and Post-Fire (08/06/2017).**
- Satellite bands: **RGB (B2, B3, B4)** for visualization, **NIR (B8)** and **SWIR (B12)** for vegetation analysis.

### 🛠️ **Techniques Used**
#### 1️⃣ NDVI and NBR Index Analysis
- **NDVI** (Normalized Difference Vegetation Index) was used to assess vegetation health before and after the fire.
- **NBR** (Normalized Burn Ratio) quantified the burn severity by analyzing spectral differences in vegetation structure.
- **Comparison of pre- and post-fire indices** helped visualize fire-affected zones.

#### 2️⃣ Unsupervised Clustering for Burn Area Identification
- **K-Means Clustering**: Classified the landscape into categories, effectively highlighting burnt areas.
- **Cascade K-Means**: Improved upon K-Means by dynamically adjusting the number of clusters.
- **LVQ (Learning Vector Quantization)**: Provided accurate delineation of fire-affected regions.
- **X-Means Clustering**: Explored optimal clustering but showed limitations compared to other methods.

---

## 📊 Results
| Analysis Method            | Key Findings |
|----------------------------|--------------|
| **NDVI Analysis**          | Significant vegetation loss post-fire, visible in red areas. |
| **NBR Analysis**           | Burnt areas identified with high accuracy, contrasting pre- and post-fire conditions. |
| **K-Means Clustering**     | Effectively categorized burnt vs. unburnt regions. |
| **LVQ & Cascade K-Means**  | Showed high accuracy in fire-affected region identification. |
| **X-Means Clustering**     | Less effective in comparison to other clustering techniques. |

---

## 📝 Conclusion
- **Remote sensing techniques successfully assessed fire impact** by leveraging Sentinel-2 data.
- **NDVI and NBR indices provided accurate insights** into vegetation loss and regrowth.
- **Unsupervised clustering approaches** were highly effective in mapping fire-affected areas.
- **The study offers a foundation for monitoring ecosystem recovery** and informs post-fire land management.

---

## 🎨 Future Work
- **Financial evaluation of vegetation damage**, using economic valuation models to estimate financial loss.
- **Comparison of identified burn areas with official damage reports**, validating the accuracy of satellite-based assessments.
- **Exploration of alternative remote sensing methods**, such as **deep learning-based segmentation** for improved wildfire analysis.

---

