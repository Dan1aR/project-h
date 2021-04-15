# Author: German Beyger <germanbeyger@icloud.com>

from typing import Union, List

import tensorflow as tf
import numpy as np

from model_loader import Loader

"""
    Class for image data predictions
    Data can be very different and output can be different too.
    This class covers different cases and can be used as input for other models.
    
""" 

class ImagePredictor:
    def __init__(self, loader: Loader):
        self.loader = loader

    def predict(self, data: Union[np.array, List[np.array]]):
        data = data.reshape(-1, self.loader.model.layers[0].input_shape)
