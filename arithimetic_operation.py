import cv2
import numpy as np

#arithmethic operations on the images
#arithmetic operations are done in matplotlib library

img1 = cv2.imread("4.2.01.tif")
img2 = cv2.imread("sample.jpg")

add = 3 + 2
sub = img1 - img2
div = img1/img2
multi = img1*img2

windowname = ['add','sub','mul','div']
images = ['add','sub','div','multi']


for i in range(4):

    cv2.imshow(windowname[i],images[i])



cv2.waitKey(0)
cv2.destroyAllWindows()

