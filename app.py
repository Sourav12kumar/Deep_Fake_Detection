# import streamlit as st
# import numpy as np
# import cv2
# from utils import load_xception_model, predict_image, extract_first_frame
# from PIL import Image

# # Load model once
# MODEL_PATH = "model/xception_deepfake_image.h5"
# model = load_xception_model(MODEL_PATH)

# st.title("🕵 Deepfake Detection (Image & Video)")

# option = st.radio("Select Input Type:", ("Image", "Video"))

# if option == "Image":
#     uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])
#     if uploaded_file:
#         image = Image.open(uploaded_file).convert('RGB')
#         img_array = np.array(image)
#         pred = predict_image(model, img_array)
        
#         label = "FAKE" if pred > 0.5 else "REAL"
#         st.image(image, caption=f"Prediction: {label} ({pred:.2f})", use_column_width=True)

# elif option == "Video":
#     uploaded_video = st.file_uploader("Upload a video", type=["mp4", "avi", "mov"])
#     if uploaded_video:
#         video_path = f"temp_video.mp4"
#         with open(video_path, "wb") as f:
#             f.write(uploaded_video.read())

#         first_frame = extract_first_frame(video_path)
#         pred = predict_image(model, first_frame)

#         label = "FAKE" if pred > 0.5 else "REAL"
#         st.image(first_frame, caption=f"Prediction: {label} ({pred:.2f})", use_column_width=True)

# pyright: ignore[reportMissingImports]
import streamlit as st
import numpy as np
import cv2
from utils import load_xception_model, predict_image, extract_first_frame
from PIL import Image

# Load model once
MODEL_PATH = "model/xception_deepfake_image.h5"
model = load_xception_model(MODEL_PATH)

st.title("🕵 Deepfake Detection (Image & Video)")

option = st.radio("Select Input Type:", ("Image", "Video"))

if option == "Image":
    uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])
    if uploaded_file:
        image = Image.open(uploaded_file).convert('RGB')
        img_array = np.array(image)
        pred = predict_image(model, img_array)
        
        label = "FAKE" if pred > 0.5 else "REAL"
        st.image(image, caption=f"Prediction: {label} ({pred:.2f})", use_column_width=True)

elif option == "Video":
    uploaded_video = st.file_uploader("Upload a video", type=["mp4", "avi", "mov"])
    if uploaded_video:
        video_path = f"temp_video.mp4"
        with open(video_path, "wb") as f:
            f.write(uploaded_video.read())

        first_frame = extract_first_frame(video_path)
        pred = predict_image(model, first_frame)

        label = "FAKE" if pred > 0.5 else "REAL"
        st.image(first_frame, caption=f"Prediction: {label} ({pred:.2f})", use_container_width=True)
