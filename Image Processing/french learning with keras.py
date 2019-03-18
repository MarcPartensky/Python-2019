#!/usr/bin/env python3.6

"""import os
os.environ["PYTHONIOENCODING"] =""" "utf-8"

import io
import sys
sys.stdout = io.open(sys.stdout.fileno(), 'w', encoding='utf8')
import keras

with io.open("Raps randoms.txt","r",encoding="utf8") as file:
    text=file.read()#.decode("utf8")
    print(type(file))
    print(type(text))

print(text)


"""
data=[]
(x_train,y_train),(x_test,y_test)=mnist.load_data()
x_train

x_train=tf.keras.utils.normalize(x_train,axis=1)
x_test=tf.keras.utils.normalize(x_test,axis=1)

model=tf.keras.models.Sequential()
model.add(tf.keras.layers.Flatten())
for i in range(4):
    model.add(tf.keras.layers.Dense(128,activation=tf.nn.relu))
model.add(tf.keras.layers.Dense(10,activation=tf.nn.softmax))

model.compile(optimizer="adam",
              loss="sparse_categorical_crossentropy",
              metrics=["accuracy"])
model.fit(x_train,y_train,epochs=3)
"""
