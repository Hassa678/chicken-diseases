import numpy as np
import tensorflow as tf
import os
import sys

# Get the absolute path of the project root directory
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..'))

# Add the project root to the Python path
sys.path.insert(0, project_root)

class PredictionPipeline:
    def __init__(self):
        pass

    @staticmethod
    def model_predict(img_path, model):
        # Load and preprocess the image
        img = tf.keras.preprocessing.image.load_img(img_path, target_size=(224, 224))
        x = tf.keras.preprocessing.image.img_to_array(img)
        x = x / 255.0  # Scale the image
        x = np.expand_dims(x, axis=0)

        # Make prediction
        preds = model.predict(x)
        preds = np.argmax(preds, axis=1)  # Get the class with the highest probability

        # Mapping predictions to labels
        if preds == 0:
            prediction = 'coccidiosis'
        elif preds == 1:
            prediction = 'Healthy'

        return prediction
