# Author: German Beyger <germanbeyger@icloud.com>

import argparse

from model_loader import TensorflowLoader
from predictors import ImagePredictor


if __name__ == "__main__":
    # Create model loader
    loader = TensorflowLoader("/Users/germanbeiger/project-huinya/test_models/tensorflow/image/model.hdf5")
    # Add it to predictor
    predictor = ImagePredictor(loader)
    # return results
    # !!! right now simply prints results. !!!
    predictor.predict()
