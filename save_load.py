'''
Data Scientist Jr.: Dr.Eddy Giusepe Chirinos Isidro
'''

from hashlib import new
import os
from pickletools import optimize
from pyexpat import model
from tabnanny import verbose
from numpy import dtype
from sklearn import metrics, neural_network
from sklearn.utils import shuffle
os.environ["TF_CPP_MIN_LOG_LEVEL"] = "2"

import tensorflow as tf 
from tensorflow import keras
import numpy as np

mnist = keras.datasets.mnist

(x_train, y_train), (x_test, y_test) = mnist.load_data()

print("Shape de y_train: ", y_train.shape)
print("Shape de y_test: ", y_test.shape)
print("Shape de x_train: ", x_train.shape)
print("Shape de x_test: ", x_test.shape)

# Normalizamos nossos Dados
x_train, x_test = x_train/255.0, x_test/255.0 

# Rede neural de feed-forward
model = keras.models.Sequential([
    keras.layers.Flatten(input_shape = (28, 28)),
    keras.layers.Dense(128, activation = 'relu'),
    keras.layers.Dense(10),
])

# Config
loss = keras.losses.SparseCategoricalCrossentropy(from_logits = True)
optim = keras.optimizers.Adam(learning_rate = 0.001) # Adam
metrics = [keras.metrics.SparseCategoricalAccuracy()] # accuracy

# Compile
model.compile(loss=loss, optimizer=optim, metrics=metrics)

# fit/training
model.fit(x_train, y_train, batch_size=64, epochs=5, shuffle=True, verbose=2)

print("")
print("Evaluate")
model.evaluate(x_test, y_test, verbose=2)

# 1.- Save whole model (Salvar todo o modelo)
# SavedModel or HDF5
model.save("neuralNetwork.h5")
model.save("Neural_net") # Cria uma pasta

# Testando o que salvamos
print("Importamos nosso modelo salvado: ")
new_model = keras.models.load_model("neuralNetwork.h5")
new_model.evaluate(x_test, y_test, verbose=2)

# 2.- Save only weights
model.save_weights("nn_weights.h5")
# Inicializar
model.load_weights("nn_weights.h5")

# 3.- Save only arqchitecture, to_json
json_string = model.to_json()

with open("neuralNetwork", "w") as f:
    f.write(json_string)

with open("neuralNetwork", "r") as f:
    loaded_json_string = f.read()

new_model = keras.models.model_from_json(loaded_json_string)
print(new_model.summary())         














