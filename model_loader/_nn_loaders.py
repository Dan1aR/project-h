# Author: German Beyger <germanbeyger@icloud.com>

import os
from typing import Dict, List, Union

import numpy as np
import tensorflow as tf
#from predictors import ImagePredictor

"""
    This class is used to load models and provide convenient way of interacting with them.
    Model can use other model as input or even use multiple models at once.
    Since models interact between each other via our API, 
        it doesn't matter if model is from TensorFlow or Torch.
"""

__all__ = ["Loader", "TensorflowLoader", "TorchLoader"]

class Loader:
    def __init__(self, ):
        pass

class TensorflowLoader:
    def __init__(self, path : str):
        self.model = self.load_model_from_file(path)

    # Simple keras model load
    def load_model_from_file(self, path: str) -> tf.keras.Model:
        return tf.keras.models.load_model(path, compile=False)

    def predict(self, image_tensor: Union[np.ndarray, List[np.ndarray]]) -> np.ndarray:
        if type(image_tensor) == np.ndarray:
            # Simple input
            return self.model.predict(image_tensor)
        elif type(image_tensor) == list:
            # Multiple inputs in one model
            return self.model.predict()
        else:
            # We can use model as input to another model if output shape fits input.
            raise NotImplementedError()


class TorchLoader:
    def __init__(self, ):
        pass