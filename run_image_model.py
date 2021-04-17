# Author: German Beyger <germanbeyger@icloud.com>

import argparse

from model_loader import TensorflowLoader
from predictors import ImagePredictor

from tensorflow.keras.datasets import cifar10

from warnings import filterwarnings

if __name__ == "__main__":
    filterwarnings("ignore")

    # Load test data
    (X_train, _), _ = cifar10.load_data()
    X_train = X_train - X_train.mean()
    X_train /= X_train.std()

    # Create model loader
    loader = TensorflowLoader("/Users/germanbeiger/project-huinya/test_models/tensorflow/image/model.hdf5")
    # Add it to predictor
    predictor = ImagePredictor()

    # return results
    # !!! right now simply prints results. !!!
    print(predictor.predict(X_train[:10]))
    
