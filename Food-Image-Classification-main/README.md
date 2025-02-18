# Comparative Analysis of SIFT/BoW, CNNs, and SSL Techniques for Image Classification

## Description
This project compares three different techniques for food image classification on the iFood-2019 dataset: SIFT with Bag-of-Words (BoW), Convolutional Neural Networks (CNNs), and Self-Supervised Learning (SSL). Each method addresses the challenge of classifying food images into 251 categories, focusing on capturing relevant features and improving model accuracy despite class similarities and variations.

## Objectives
- **Classify food images** into one of the 251 categories using three distinct methods.
- **Explore the effectiveness** of traditional and deep learning models in handling the complexity of food classification.
- **Handle class imbalance** and optimize model performance within a _constraint of fewer than one million parameters_.

## The Dataset
The iFood-2019 dataset is used for the classification task, consisting of:
- **Training set**: 118,475 samples.
- **Validation set**: 11,994 images (used as the test set in this project).
- **Test set**: 28,377 images (not used as ground truth labels are unavailable).

To handle **class imbalance**, downsampling was applied to over-represented classes, and upsampling with transformations like rotation and color jittering was used for under-represented classes.

## Methodologies

### 1. Feature Extraction Approach (SIFT + BoW)
- **SIFT (Scale-Invariant Feature Transform)** was used to extract keypoints from images, invariant to scale and rotation.
- A **Bag-of-Words (BoW)** model was applied to quantize these features into visual words, creating a histogram for each image.
- A traditional classifier was then trained on these histograms for classification.

### 2. Convolutional Neural Networks (CNNs)
- A CNN architecture was built with fewer than one million parameters, using **depthwise separable convolutions** to reduce computational costs.
- **Data augmentation** was applied during training to enhance the model's generalization, including operations like flipping, rotation, and color jitter.
- The final CNN architecture achieved the best performance after 50 epochs of training.

### 3. Self-Supervised Learning (SSL)
- A **pretext task** was used to train the model to solve a Jigsaw Puzzle (dividing images into patches and shuffling them).
- The features learned through the SSL task were extracted and used to train a logistic regression classifier for the final classification task.

## Key Steps

### Data Preparation
- **Class imbalance was addressed** using downsampling and upsampling with transformations.
- The images were resized to **256x256 pixels**, normalized, and augmented to improve generalization.

### SIFT + BoW Approach
- **Keypoint extraction**: The SIFT algorithm was used to extract keypoints from each image, focusing on edges and textures.
- **Clustering**: Keypoint descriptors were quantized into **visual words** using MiniBatch K-means clustering.
- **BoW Model**: Each image was represented as a histogram of visual words, capturing the distribution of features in the image.
- **Classification**: A traditional classifier was trained on these histograms to classify the food images into 251 categories.

### CNN Design
- The CNN used **depthwise separable convolutions** and **Global Average Pooling (GAP)** to reduce the number of parameters.
- The final model consisted of **983,323 parameters**, meeting the project’s constraint.

### SSL Task
- A **Jigsaw Puzzle pretext task** was implemented, where the model learned to predict the correct positions of shuffled image patches, extracting meaningful spatial features.

## Results

| Model             | Accuracy (Test Set) |
|-------------------|---------------------|
| SIFT + BoW        | 6.26%               |
| CNN (50 Epochs)   | 36.84%              |
| SSL               | 9.52%               |

- **CNN** outperformed both the feature extraction and SSL approaches, achieving an accuracy of **36.84%** after 50 epochs.
- The SSL approach showed that models trained for fewer epochs on the pretext task provided better features for classification.

## Conclusion
The CNN approach proved most effective for food image classification, benefiting from deep feature extraction and data augmentation. The SSL method, while less effective than CNN, demonstrated potential for further exploration with different pretext tasks. The SIFT + BoW method struggled due to the complexity of the dataset, highlighting the limitations of traditional feature extraction in fine-grained visual categorization tasks.

## Acknowledgments
The detailed methodology, results, and scientific analysis of this project are thoroughly presented in the accompanying [report](https://github.com/ywdavi/Food-Image-Classification/blob/main/Report.pdf). This project was developed with the help and collaboration of **Alessio De Luca** and **Simone Vaccari**.


