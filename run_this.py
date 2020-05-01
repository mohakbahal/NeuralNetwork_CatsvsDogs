from keras.models import load_model
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import matplotlib.patches as patches

classifier = load_model('mohak_catvsdog_cnn.h5')

import numpy as np
from keras.preprocessing import image
test_image =image.load_img('test_image_address',target_size =(64,64))
test_image =image.img_to_array(test_image)
test_image =np.expand_dims(test_image, axis =0)
result = classifier.predict(test_image)
if result[0][0] >= 0.5:
    prediction = 'dog'
else:
    prediction = 'cat'
print(prediction)

img=mpimg.imread('C:/Users/Human Being/Documents/GitHub/NeuralNetwork_CatsvsDogs/test_images/catvsdog.jpg')
fig,ax = plt.subplots(1)
ax.imshow(img)
centerx = centery = 50
plt.text(centerx,centery,prediction,fontsize='20',color='red')