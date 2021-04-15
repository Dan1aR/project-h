import numpy as np
import tensorflow as tf
from tensorflow.keras.models import Model
from tensorflow.keras.layers import *
from tensorflow.keras.applications import MobileNetV2
from tensorflow.keras.datasets import cifar10

def create_model() -> Model:
    mnet = MobileNetV2(input_shape=(32, 32, 3), weights='imagenet', include_top=False, alpha=0.35)
    inp = Input((32, 32, 3))
    x = mnet(inp)
    x = Flatten()(x)
    x = Dropout(0.5)(x)
    x = Dense(10, activation='softmax')(x)
    return Model(inp, x)


if __name__ == "__main__":
    (X_train, y_train), (X_test, y_test) = cifar10.load_data()
    X_train = X_train - X_train.mean()
    X_test = X_test - X_test.mean()
    X_train = X_train / X_train.std()
    X_test = X_test / X_test.std()

    model = create_model()
    model.compile(loss="sparse_categorical_crossentropy", optimizer="Adam", metrics=['sparse_categorical_accuracy'])
    model.fit(X_train, y_train, validation_data=(X_test, y_test), epochs=3, batch_size=32)

    model.save("model.hdf5")
    model.save("pb_model/model")