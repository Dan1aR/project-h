# Author: German Beyger <germanbeyger@icloud.com>

from typing import List, Union

import os
import tensorflow as tf
import numpy as np

from predictors import ImagePredictor

"""
    This class is used to load models and provide convenient way of interacting with them.
    Model can use other model as input or even use multiple models at once.
    Since models interact between each other via our API, 
        it doesn't matter if model is from TensorFlow or Torch.
"""

class Loader:
    pass

class TensorflowLoader(Loader):
    def __init__(self, path : str):
        self.model = self.load_model_from_file(path)

    # Simple keras model load
    def load_model_from_file(self,) -> tf.keras.Model:
        return tf.keras.models.load_model(self.path, compile=False)

    def predict(self, image_tensor: Union[np.array, ImagePredictor, List[np.array]] ) -> np.array:
        if type(image_tensor) == np.array:
            # Simple input
            return self.model.predict(image_tensor)
        elif type(image_tensor) == list:
            # Multiple inputs in one model
            return self.model.predict(image_tensor)
        else:
            # We can use model as input to another model if output shape fits input.
            raise NotImplementedError()

class TorchLoader(Loader):
    pass