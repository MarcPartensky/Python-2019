"""
#Vgg-16 architecture
from keras.models import Sequential
from keras.layers import Conv2D,MaxPooling2D,Flatten,Dense

my_VGG16=Sequential()
my_VGG16.add(Conv2D(64,(3,3),input_shape=(224,224,3),padding="same",activation="relu"))
my_VGG16.add(Conv2D(64,(3,3),padding="same"),activation="relu")
my_VGG16.add(MaxPooling2D(pool_size=(2,2),strides=(2,2)))
my_VGG16.add(Flatten())
my_VGG16.add(Dense(4096,activation="relu"))
my_VGG16.add(Dense(4096,activation="relu"))
my_VGG16.add(Dense(100,activation="softmax"))



from PIL import Image

img=Image.open("simba.png")
img.show()
"""


import keras

from keras.preprocessing.image import load_img, img_to_array
from keras.applications.vgg16 import VGG16, preprocess_input,decode_predictions
model=VGG16()

img=load_img("simba.png",target_size=(224,224))
img=img_to_array(img)
img=img.reshape((1,img.shape[0],img.shape[0],img.shape[2]))
img=preprocess_input(img)

y=model.predict(img)

print("top3:",decode_predictions(y,top=3)[0])
