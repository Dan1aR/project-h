# Author: German Beyger <germanbeyger@icloud.com>

from typing import Union, List, Dict

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

    def predict(self, data: Union[np.ndarray, List[np.ndarray], Dict[str, np.ndarray]]) -> np.array:
        if type(data) == np.ndarray:
            return self.loader.predict(data)
        else:
            raise NotImplementedError()
