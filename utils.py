import cv2 
import imageio
import numpy as np
import tensorflow as tf # type: ignore
from tensorflow.keras.models import load_model  # type: ignore

IMG_SIZE = (299, 299)

def load_xception_model(model_path):
    return load_model(model_path)

def preprocess_image(img):
    img = cv2.resize(img, IMG_SIZE)
    img = img / 255.0
    return np.expand_dims(img, axis=0)

def predict_image(model, img):
    processed_img = preprocess_image(img)
    pred = model.predict(processed_img)[0][0]
    return pred

def extract_first_frame(video_path):
    reader = imageio.get_reader(video_path)
    frame = reader.get_data(0)  # first frame
    reader.close()
    return frame
