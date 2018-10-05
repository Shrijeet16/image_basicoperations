import cv2
import numpy as np

#thresholding and segementation

#segementation means dividing the image into various regions

#thresholdoing is basic form of segmentation

#mostly apllied i=on gray scale images

#in thresholding we need to choose a threshold value and corresponding pixels are
#changed into binary vales i.e (0 & 255)

#in inverse thresholding the binary values are inverrsed corresponding to the
#value of the threshold value given
#reasult is inverse according to the algorithm therefore it is inverse thresholding


img = cv2.imread("lena.tif",0)

th_value = 160

max_value = 255

#cv2.threshold() function's arguments()
#(source image , threshold value ,max_vlaue, threshold algorithm )
#max_value = the value given to pixel if it is grater than threshold value

ret , thresh1 = cv2.threshold(img,th_value,max_value,cv2.THRESH_BINARY)
ret , thresh2 = cv2.threshold(img,th_value,max_value,cv2.THRESH_BINARY_INV)
ret , thresh3 = cv2.threshold(img,th_value,max_value,cv2.THRESH_TOZERO)
ret , thresh4 = cv2.threshold(img,th_value,max_value,cv2.THRESH_TOZERO_INV)
ret , thresh5 = cv2.threshold(img,th_value,max_value,cv2.THRESH_TRUNC)

windowname = ['normal','binary','binary_inv','tozero','tozero_inv','trunc']
image = [img,thresh1,thresh2,thresh3,thresh4,thresh5]


for i in range(5):

    cv2.imshow(windowname[i],image[i])

      



cv2.waitKey(0)

cv2.destroyAllWindows()

