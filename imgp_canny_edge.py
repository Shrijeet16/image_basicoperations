import cv2
import numpy as np


#canny edge detector - coustomised alogorithm

# 4 steps
#1)denoising using gaussian kernel
#2)intensity gradient is calculated using L1 norm and L2 norm
#3)non-maximum supperesion is applied to the output of the seconfd step

#4)using the gradient threshold the final edge is detected

"""
    a) any pixel less than gardient 1 is excluded
    b) any pixel more then gradient 2 is included
    c) for any pixel in between two gradients only the pixels is directly connected to the pixels in set b are included
    in the final image set
"""
#applying L2 gradient gives more accuracy and better reasults

#arguments of cv2.Canny( image , minvalue , maxvalue , aperature_size, L2gradient)

#by deafault its size is 3 it the size of the sobel kernel used for finding image gradients


img = cv2.imread("lena.tif",0)

L1 = cv2.Canny(img , 100, 200 , False)

L2 = cv2.Canny(img , 100 , 200 , True)

windowname = ['normal','L1','L2']

image = [img , L1 ,L2]


for i in range(3):

    cv2.imshow(windowname[i],image[i])

    
cv2.waitKey(0)
cv2.destroyAllWindows()
