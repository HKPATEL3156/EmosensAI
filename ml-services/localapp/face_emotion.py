import streamlit as st
import tensorflow as tf
import numpy as np
import cv2
from PIL import Image


# loading trained model

model = tf.keras.models.load_model(
    
    "../saved_models/emotion_model.h5"
    
)


# emotion labels

emotion_labels = [
    
    "angry",
    "disgust",
    "fear",
    "happy",
    "neutral",
    "sad",
    "surprise"
    
]


# page title

st.title("emoSense ai")

st.subheader("facial emotion recognition system")


# image uploader

uploaded_file = st.file_uploader(
    
    "upload a face image",
    
    type = ["jpg", "jpeg", "png"]
    
)


# prediction logic

if uploaded_file is not None:
    
    # showing uploaded image
    
    image = Image.open(uploaded_file)
    
    st.image(
        
        image,
        
        caption = "uploaded image",
        
        width = "stretch"
        
    )
    
    
    # convert image for opencv
    
    image_array = np.array(image)
    
    
    # grayscale conversion

    
    if len(image_array.shape) == 3:
    
      gray = cv2.cvtColor(
         
         image_array,
         
         cv2.COLOR_RGB2GRAY
         
      )

    else:
      
          gray = image_array
    
    # resize image
    
    resized = cv2.resize(
        
        gray,
        
        (48,48)
        
    )
    
    
    # normalization
    
    normalized = resized / 255.0
    
    
    # reshaping for cnn
    
    reshaped = normalized.reshape(
        
        1,
        48,
        48,
        1
        
    )
    
    
    # prediction
    
    prediction = model.predict(reshaped)
    
    
    predicted_index = np.argmax(prediction)
    
    predicted_emotion = emotion_labels[predicted_index]
    
    
    confidence = np.max(prediction) * 100
    
    
    # showing results
    
    st.success(
        
        f"predicted emotion : {predicted_emotion}"
        
    )
    
    
    st.info(
        
        f"confidence score : {confidence:.2f}%"
        
    )