import cv2
import numpy as np

#  abs(takes number as argument) returns number as reasult
#logical operations on the images
 

img1 = cv2.imread('sample.jpg',1)
img2 = cv2.imread('4.2.01.tiff',1)


#img1 = cv2.cvtColor(img1,cv2.COLOR_BGR2RGB)
#img2 = cv2.cvtColor(img2,cv2.COLOR_BGR2RGB)

img3 = cv2.bitwise_not(img1)
img4 = cv2.bitwise_and(img1,img2)
img5 = cv2.bitwise_or(img1,img2)
img6 = cv2.bitwise_xor(img1,img2)

title = ['img1','img2','NOT','AND','OR','XOR']

image = [img1,img2,img3,img4,img5,img6]

#not is equivalent to computing negative of the image


for i in range (6):

    cv2.imshow(title[i],image[i])



cv2.waitKey(0)
cv2.destroyAllWindows()


