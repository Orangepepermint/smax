import tensorflow as tf
import numpy as np



def create_model():
    model = Sequential()
    model.add(Dense(10, activation='softmax'))
    model.add(Dense(10, activation='softmax'))
    return model


def compile_model(model):
    opitmizer='adam'
    loss='mse'
    metrics=['accuracy']
    model.compile(optimizer=opitmizer, loss=loss, metrics=metrics)



def train_modelmodel, X_train, y_train):
    return model.fit(X_train, y_train, epochs=8, verbose=1, validation_split=0.2)

def save_model(model, filename):
    model.save(fileName + '.h5')

def load_trained_model(fileName):
    return load_model(fileName + '.h5')

