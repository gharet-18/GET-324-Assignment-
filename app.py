import streamlit as st
from tensorflow.keras.models import load_model
from PIL import Image
import numpy as np

# LOAD MODEL
model = load_model("blight_model.h5")
class_names = ["early_blight", "late_blight"]

#APP UI
st.title("🥔 Potato Blight Classifier")
st.write("Upload a potato leaf image to check if it shows signs of Early Blight or Late Blight.")

file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

if file is not None:
    img = Image.open(file).convert("RGB")
    st.image(img, caption="Uploaded Image", width="stretch")

    # PREPROCESS
    img_resized = img.resize((224, 224))
    img_array = np.array(img_resized) / 255.0
    img_array = np.expand_dims(img_array, axis=0)

    #PREDICT
    prediction = model.predict(img_array)[0][0]

    if prediction > 0.5:
        label = "Late Blight"
        confidence = prediction
    else:
        label = "Early Blight"
        confidence = 1 - prediction

    st.subheader(f"Prediction: {label}")
    st.write(f"Confidence: {confidence:.2%}")
