import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
import cv2
import PIL #matplotlib supports only PNG images

#%matplotlib inline
img = cv2.imread('crown.PNG')
#print(img)

imgplot = plt.imshow(img)
