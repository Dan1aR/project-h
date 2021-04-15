import numpy as np
import tensorflow as tf
from tensorflow.keras.models import Model
from tensorflow.keras.layers import *
from tensorflow.keras.applications import MobileNetV2
from tensorflow.keras.datasets import cifar10

def create_model():
    mnet = MobileNetV2(input_shape=(32, 32, 3), weights='imagenet')
    inp = Input((32, 32, 3))
    x = mnet(inp)
    x = Dense(10, activation='softmax')(x)
    

if __name__ == "__main__":
    