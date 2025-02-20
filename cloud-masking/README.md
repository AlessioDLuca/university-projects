☁️ Cloud Masking in Satellite Images: A Comparison Between U-Net and K-Means Clustering

📃 Project Overview

This project explores cloud segmentation in satellite images by comparing a fine-tuned ResNet-based U-Net with K-Means clustering. The study also introduces Guided K-Means, which enhances traditional clustering by incorporating NDVI (Normalized Difference Vegetation Index) and NDWI (Normalized Difference Water Index) to improve cloud differentiation from snow and land surfaces.

The analysis is conducted on the 38-Cloud Dataset from Landsat 8 satellite imagery, and model performances are evaluated using IoU (Intersection over Union), Dice Score, and Accuracy.

🔍 Objectives

🌟 Develop an accurate cloud segmentation model using deep learning (U-Net) and clustering (K-Means).

🌟 Compare supervised vs. unsupervised approaches for cloud masking.

🌟 Improve K-Means clustering by incorporating spectral indices like NDVI & NDWI.

🌟 Evaluate the feasibility of using K-Means for semi-supervised learning in cloud segmentation.

📝 Dataset & Preprocessing

🌍 38-Cloud Dataset (Landsat 8 Satellite)

Training set: 5,880 images

Validation set: 1,680 images

Test set: 840 images

Spectral bands used:

Red (B4): Useful for vegetation and land classification.

Green (B3): Contributes to vegetation indices.

Blue (B2): Standard RGB composition.

Near-Infrared (NIR, B8): Enhances cloud differentiation from other surfaces.

🛠️ Preprocessing Steps

Standardized pixel values across all spectral bands.

Kept all images despite minor labeling errors in ground truth masks.

No additional data augmentation required due to dataset diversity.

🎨 Model Development

🛡️ Fine-Tuned ResNet-Based U-Net

Encoder: ResNet-101 backbone, fine-tuned on satellite imagery.

Decoder: Upsampling layers with skip connections for high-resolution segmentation.

Binary classification output (Cloud vs. Non-cloud).

Trained for 10 epochs with Binary Cross-Entropy loss & Adam optimizer.

🔄 K-Means Clustering Approaches

1️⃣ Basic K-Means Clustering

Groups pixels into two clusters (Cloud / Non-cloud) based on spectral values.

Lacks contextual understanding, leading to misclassification (e.g., confusing clouds with snow).

2️⃣ Guided K-Means Clustering

Incorporates NDVI and NDWI to enhance cloud differentiation.

Predefined centroids based on spectral properties improve initial cluster assignments.

Achieves better segmentation accuracy than basic K-Means.

📊 Results

Model

IoU

Dice Score

Precision

Recall

Accuracy

Fine-Tuned U-Net

0.8416

0.8737

0.9357

0.8488

96.70%

Basic K-Means

0.3228

0.3900

0.4575

0.4268

44.09%

Guided K-Means

0.6567

0.7222

0.7789

0.7708

78.95%

Fine-tuned U-Net achieves the highest accuracy, leveraging deep spatial understanding.

Guided K-Means significantly improves segmentation compared to basic K-Means.

K-Means still struggles with cloud/snow differentiation, but NDVI & NDWI improve performance.

🔬 Key Findings

U-Net consistently outperforms clustering methods for cloud segmentation.

Guided K-Means is a viable alternative when labeled training data is unavailable.

K-Means clustering could generate pseudo-labels for training deep learning models in semi-supervised settings.

🎨 Future Work

Enhance U-Net efficiency via quantization & knowledge distillation.

Experiment with other unsupervised methods, such as Gaussian Mixture Models (GMMs) or Self-Organizing Maps (SOMs).

Use K-Means-generated masks for semi-supervised deep learning.

Explore alternative spectral indices, such as Cloud Optical Thickness (COT), to refine K-Means segmentation.
