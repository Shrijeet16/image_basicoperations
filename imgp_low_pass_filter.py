import cv2
import numpy as np

#low pass filter
#1)blurring
#2)Denoising
#3)smoothing
# a filter which allows only low frequency components is called low pass filter
# kernels are internally created when using cv2.filter2D


img = cv2.imread("sample.jpg",1)

#cv2.namedWindow("low pass filter")

box = cv2.boxFilter(img , -1 , (50,50))

blur = cv2.blur(img , (30,30))

gaussian = cv2.GaussianBlur(img , (7,7), 0)  #the width and length of the kernel in box filter must be always odd

#in gaussian blur
#third argument can be zero so that the it will calculate the devaition in x and y directions automatically


windowname = ['normal','box blur','blur','gaussian blur']

image = [img,box,blur,gaussian]


for i in range(4):

    cv2.imshow(windowname[i],image[i])
    

cv2.waitKey(0)
cv2.destroyAllWindows()

