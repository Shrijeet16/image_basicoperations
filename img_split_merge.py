import cv2
import numpy as np

#cv2.split()
#parameters is image only
#it splits the B,G,R images into single planes

img = cv2.imread("sample.jpg")

b,g,r = cv2.split(img)

windowname = ['normal','b','g','r']

image = [img , b,g ,r ]


for i in range(4):

    cv2.imshow(windowname[i],image[i])


output = cv2.merge((b,g,r),img)
cv2.imshow("AAA",output)


cv2.waitKey(0)
cv2.destroyAllWindows()

