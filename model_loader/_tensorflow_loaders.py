# Author: German Beyger <germanbeyger@icloud.com>

import os
import tensorflow as tf
import numpy as np

class TensorflowLoader:
    def __init__(self, path : str):
        self.path = path

    # Simple keras model load
    def load_model_from_file(self,) -> None:
        self.model = tf.keras.models.load_model(self.path, compile=False)

    def predict(self, image_tensor : np.array) -> np.array:
        return self.model.predict(image_tensor)
