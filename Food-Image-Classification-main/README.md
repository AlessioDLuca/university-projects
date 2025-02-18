# 🍔 Comparative Analysis of SIFT/BoW, CNNs, and SSL Techniques for Image Classification

## 📃 Project Overview
This project explores three different techniques for **food image classification** on the **iFood-2019 dataset**: 
- **SIFT with Bag-of-Words (BoW)** 
- **Convolutional Neural Networks (CNNs)** 
- **Self-Supervised Learning (SSL)**

Each method addresses the challenge of classifying food images into **251 categories**, with a focus on extracting relevant features and improving model accuracy despite class similarities and variations.

---

## 🔍 Objectives
- 🌟 **Classify food images** into 251 categories using three distinct methods.
- 🌟 **Compare traditional vs. deep learning approaches** in handling fine-grained food classification.
- 🌟 **Optimize model performance** while maintaining a constraint of **fewer than one million parameters**.

---

## 📝 Dataset
The **iFood-2019 dataset** consists of:
- **Training set**: 118,475 images
- **Validation set**: 11,994 images _(used as the test set in this project)_
- **Test set**: 28,377 images _(not used due to unavailable ground truth labels)_

To handle **class imbalance**:
- Over-represented classes were **downsampled**.
- Under-represented classes were **upsampled** using transformations like rotation and color jittering.

---

## 🛠️ Methodologies

### 🛡️ SIFT + BoW Approach
- **Feature Extraction**: SIFT (Scale-Invariant Feature Transform) was used to extract keypoints, capturing essential image structures.
- **Clustering**: MiniBatch K-means clustering was applied to create a vocabulary of **visual words**.
- **BoW Model**: Each image was represented as a histogram of visual words, used as input for a traditional classifier.

### 🌐 Convolutional Neural Networks (CNNs)
- A CNN architecture was designed using **depthwise separable convolutions** to reduce computational costs.
- **Data augmentation** techniques (flipping, rotation, color jitter) were applied to improve generalization.
- The final model had **983,323 parameters**, staying within the constraint.

### 🧩 Self-Supervised Learning (SSL)
- A **Jigsaw Puzzle pretext task** was implemented, where images were divided into patches and shuffled.
- The model was trained to predict the correct positions of these patches, learning meaningful **spatial features**.
- Extracted features were used to train a logistic regression classifier for the final classification task.

---

## 📊 Results
| Model             | Accuracy (Test Set) |
|-------------------|---------------------|
| 🛡️ SIFT + BoW        | 6.26%               |
| 🌐 CNN (50 Epochs)   | 36.84%              |
| 🧩 SSL               | 9.52%               |

- **CNN** significantly outperformed the other methods, achieving **36.84% accuracy** after 50 epochs.
- The **SSL method** showed potential but needs further refinement.
- The **SIFT + BoW** approach struggled due to the dataset's complexity, emphasizing the limitations of traditional feature extraction.

---

## 📝 Conclusion
- **CNNs were the most effective** due to their ability to extract high-level features and leverage data augmentation.
- **SSL showed promise** but needs improved pretext tasks for better feature learning.
- **Traditional feature extraction (SIFT + BoW) struggled** with this fine-grained classification task.

---

## 📚 Acknowledgments
This project was developed with the collaboration of **Davide Vettore** and **Simone Vaccari**. A detailed explanation of the methodology and results can be found in the full [report](https://github.com/ywdavi/Food-Image-Classification/blob/main/Report.pdf).

---
