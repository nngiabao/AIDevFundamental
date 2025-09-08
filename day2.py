import numpy as np
import tensorflow as tf
from tensorflow.keras import datasets, layers, models
from tensorflow.keras.utils import to_categorical

#Load the MNIST dataset
(train_images, train_labels), (test_images, test_labels) = datasets.cifar10.load_data()
#prepprocessing
train_images = train_images / 255.0
test_images = test_images / 255.0
#Reshape the img to (28,28,1) => grayscale
train_images = train_images.reshape(train_images.shape[0], 28, 28, 1)
test_images = test_images.reshape(test_images.shape[0], 28, 28, 1)

#convert the labels to one-hot
train_labels = to_categorical(train_labels)
test_labels = to_categorical(test_labels)
#Build CNN model
model = models.Sequential()

#First convolutional layer
model.add(layers.Conv2D(32, (3, 3), activation='relu', input_shape=(28, 28, 1)))

#Second convolutional layer
model.add(layers.MaxPooling2D((2, 2)))
model.add(layers.Conv2D(64, (3, 3), activation='relu'))
model.add(layers.MaxPooling2D((2, 2)))

#Third Convolutional layer
model.add(layers.Conv2D(64, (3, 3), activation='relu'))