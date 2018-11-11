import cv2
import numpy as np


img  = cv2.imread("sample.jpg",0)

img1 = cv2.imread("sample.jpg",1)


hist , bins =  np.histogram(img.ravel ,256 , (0,255) )

print(hist)



print(bins)


#img.ravel = flattened image
