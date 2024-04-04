import cv2
import os
import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf

mnist=tf.keras.datasets.mnist
(X_train ,Y_train),(X_test , Y_test)=mnist.load_data()

X_train=tf.keras.utils.normalize(X_train,axis=1)
X_test = tf.keras.utils.normalize(X_test , axis=1)

model = tf.keras.models.Sequential()
model.add(tf.keras.layers.Flatten(input_shape=(28,28)))
model.add(tf.keras.layers.Dense(256,activation='relu'))
model.add(tf.keras.layers.Dense(256,activation='relu'))
model.add(tf.keras.layers.Dense(256,activation='relu'))
model.add(tf.keras.layers.Dense(256,activation='relu'))
model.add(tf.keras.layers.Dense(256,activation='relu'))
model.add(tf.keras.layers.Dense(10,activation='softmax'))

model.compile(optimizer='adam',loss='sparse_categorical_crossentropy',metrics=['accuracy'])

callback = tf.keras.callbacks.EarlyStopping(monitor='loss', patience=3)

model.fit(X_train,Y_train,epochs=50, callbacks=[callback])

model.save('handwrittenco.keras')

