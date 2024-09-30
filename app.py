from __future__ import division, print_function
# coding=utf-8
import sys
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
import glob
import re
import numpy as np
import tensorflow
from src.chicken_project.pipeline.predict import PredictionPipeline





# Keras
import tensorflow as tf

# Flask utils
from flask import Flask, redirect, url_for, request, render_template
from werkzeug.utils import secure_filename
#from gevent.pywsgi import WSGIServer

# Define a flask app
app = Flask(__name__)



# Model saved with Keras model.save()
MODEL_PATH ='model/model.h5'

# Load your trained model
model = tf.keras.models.load_model(MODEL_PATH)
#


@app.route('/', methods=['GET'])
def index():
    # Main page
    return render_template('index.html')

@app.route("/train", methods=['GET','POST'])
def trainRoute():
    os.system("python main.py")
    return "Training done successfully!"


@app.route('/predict', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        # Get the file from post request
        f = request.files['file']

        # Save the file to ./uploads
        basepath = os.path.dirname(__file__)
        file_path = os.path.join(
            basepath, 'uploads', secure_filename(f.filename))
        f.save(file_path)

        # Make prediction
        preds = PredictionPipeline.model_predict(file_path, model)
        result=preds
        return str(result)
    return None


if __name__ == '__main__':
    #
    #for aws
    app.run(host='0.0.0.0', port=8080)
#fff