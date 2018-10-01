import cv2
import numpy as np


img = cv2.imread("sample.jpg",1)

#(img.shape)  show the dimensions of the image

#translation of a image is done using cv2.wrapaffine() function

rows,columns,channels = img.shape

T = np.float32([[1,0,40],[0,1,-40]])

#print(T)

print(img)

img = cv2.warpAffine(img,T,(columns,rows))

cv2.imshow("mohit",img)


cv2.waitKey(0)

cv2.destroyAllWindows()
