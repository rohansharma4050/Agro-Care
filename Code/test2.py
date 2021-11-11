import json
import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf
import keras
from keras.layers import *
from keras.models import * 
from keras.preprocessing import image
from keras.preprocessing.image import ImageDataGenerator
from keras.applications import imagenet_utils
with open('test.txt', 'r') as f:
    classes = json.loads(f.read())

def load_image(img_path, show=False):
    img = image.load_img(img_path, target_size=(150, 150))
    img_tensor = image.img_to_array(img)                    # (height, width, channels)
    img_tensor = np.expand_dims(img_tensor, axis=0)         # (1, height, width, channels), add a dimension because the model expects this shape: (batch_size, height, width, channels)
    img_tensor /= 255.                                      # imshow expects values in the range [0, 1]

    if show:
        plt.imshow(img_tensor[0])                           
        plt.axis('off')
        plt.show()

    return img_tensor
  
#img_path = 'C:/Users/Ferhat/Python Code/Workshop/Tensoorflow transfer learning/blue_tit.jpg'
img_path = "opencv_frame_0.png"
new_image = load_image(img_path)

models = load_model('mobilenet-fine-tuned.h5')
pred = models.predict(new_image)


classresult=np.argmax(pred,axis=1)
print(classes[classresult[0]])