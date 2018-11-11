import cv2
import numpy as np

#contour is a curve joining all  the continous points of same colour value in a image

img = cv2.imread("sample.jpg")

"""
functions which will help in finding and drawing contours
cv2.findContours()
three argumrents
img , contour retrival mode , contour approximation mode

contour retrival mode
1)RETR_EXTERNAL
2)RETR_LIST
3)RETR_TREE
4)RETR_CCOMP


CONTOUR APPROX  MODE
1)CHAIN_APPROX_NONE
2)CHAIN_APPROX_SIMPLE
3)CHAIN_APPROX_TC89_L1
4)CHAIN_APPROX_TC89_KCOS
"""

cv2.drawcontours()

