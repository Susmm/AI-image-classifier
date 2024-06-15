import streamlit as st
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import numpy as np
import os
import random

@st.cache_data
def load_trained_model():
    model_path = os.path.join('model', 'insightnet.h5')
    return load_model(model_path)

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

# Function to check if file extension is allowed
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# Function to preprocess image
def preprocess_image(img_path, target_size=(224, 224)):
    img = image.load_img(img_path, target_size=target_size)
    # Check if the image has an alpha channel (RGBA)
    if img.mode == 'RGBA':
        img = img.convert('RGB')  # Convert RGBA to RGB
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array /= 255.0  # Normalize pixel values
    return img_array

# Main function to run the Streamlit app
def main():
    st.title('AI Image Classifier')
    
    # Load the model
    model = load_trained_model()
    
    # Upload image through the file uploader widget
    uploaded_file = st.file_uploader("Upload an image of a person", type=ALLOWED_EXTENSIONS)
    
    if uploaded_file is not None:
        # Check if the file extension is allowed
        if allowed_file(uploaded_file.name):
            # Save the uploaded file temporarily
            #img_path = os.path.join('temp', uploaded_file.name)
            #with open(img_path, 'wb') as f:
            #    f.write(uploaded_file.getvalue())
            
            # Display the uploaded image
            st.image(uploaded_file, caption='Uploaded Image', use_column_width=True)
            
            img_array = preprocess_image(uploaded_file)
            
            prediction = model.predict(img_array)
            
            class_indices = {0: 'ai-generated', 1: 'real'}
            
            #random.seed(uploaded_file.name)
            # Get predicted class label
            predicted_class = class_indices[int(prediction[0][0]+random.uniform(-0.2, 0.2)<=0.5)]
            
            # Display the prediction
            st.success(f"This image is {predicted_class}.")
        else:
            st.error("Invalid file type. Please upload a PNG or JPEG file.")
    
if __name__ == '__main__':
    main()

