import torch
from torchvision import transforms
import streamlit as st
import matplotlib.pyplot as plt
from skimage.measure import find_contours
import numpy as np
from PIL import Image
import segmentation_models_pytorch as smp
import tempfile
import base64


# Function to load and preprocess the image
def load_and_preprocess_image(image_file):
    image = Image.open(image_file)
    # Ensure the image is in RGB mode
    if image.mode != 'RGB':
        image = image.convert('RGB')
    # Resize image if necessary (e.g., to 768x768)
    image = image.resize((768, 768))
    # Apply necessary transformations, e.g., normalization
    transform = transforms.ToTensor()
    image = transform(image).unsqueeze(0)  # Add batch dimension
    return image


# Function to predict masks using the model
def predict(image, model, threshold=0.3):
    model.eval()
    with torch.no_grad():
        predicted_masks = model(image)
    return predicted_masks


# Function to visualize output of segmentation
def visualize_output(original_image, predicted_masks, threshold=0.3):
    num_samples = predicted_masks.size(0)

    for i in range(num_samples):
        fig, axes = plt.subplots(1, 3, figsize=(18, 8))

        # Original image
        axes[0].imshow(original_image.squeeze().permute(1, 2, 0))
        axes[0].set_title('Original Image')
        axes[0].axis('off')

        # Predicted mask
        predicted_mask = predicted_masks[i].squeeze().cpu()  # Remove extra dimension
        predicted_mask_binary = (predicted_mask > threshold).float()
        axes[1].imshow(predicted_mask_binary, cmap='gray')
        axes[1].set_title('Predicted Mask')
        axes[1].axis('off')

        # Original image with overlaid contours
        axes[2].imshow(original_image.squeeze().permute(1, 2, 0))
        contours = find_contours(predicted_mask_binary.numpy(), level=0.5)
        for contour in contours:
            axes[2].plot(contour[:, 1], contour[:, 0], linewidth=2, color='red')
        axes[2].set_title('Image with Contours')
        axes[2].axis('off')

        # Save the figure to a temporary file
        with tempfile.NamedTemporaryFile(delete=False, suffix=".png") as tmpfile:
            fig.savefig(tmpfile.name)
            plt.close(fig)

            # Convert image to base64
            with open(tmpfile.name, "rb") as image_file:
                encoded_string = base64.b64encode(image_file.read()).decode()

            # Display each image in its own container
            with st.container():
                st.markdown(
                    f"""
                    <div style="display: flex; justify-content: center;">
                        <img src="data:image/png;base64,{encoded_string}" />
                    </div>
                    """,
                    unsafe_allow_html=True
                )


# Main function for Streamlit
def main():
    st.title('Ship Detection Image Segmentation App')
    uploaded_image = st.file_uploader("Upload an image", type=['jpg', 'png', 'jpeg'])

    if uploaded_image is not None:
        # Load and preprocess the image
        image = load_and_preprocess_image(uploaded_image)

        # Load your trained model
        model = load_model()

        # Predict using the model
        predicted_masks = predict(image, model)

        # Visualize segmentation output
        visualize_output(image, predicted_masks, threshold=0.5)


# Function for loading your trained model
def load_model():
    # Replace with the actual path to your model
    model_path = 'C:/Users/alede/OneDrive/Desktop/università/Magistrale/Primo Anno/Secondo Semestre/Advanced Computational Techniques for Big Imaging and Signal Data/ProgettoEsame/DashboardStreamlit/ResNet101.pth'

    # Create an instance of your model
    model = smp.Unet(
        encoder_name="resnet101",  # choose encoder
        encoder_weights="imagenet",  # use `imagenet` pre-trained weights for encoder initialization
        in_channels=3,  # model input channels (1 for grayscale images, 3 for RGB, etc.)
        classes=1  # model output channels (number of classes in your dataset)
    )

    # Load the state_dict
    state_dict = torch.load(model_path, map_location=torch.device('cpu'))
    model.load_state_dict(state_dict)

    return model


# Run the Streamlit application
if __name__ == '__main__':
    main()

