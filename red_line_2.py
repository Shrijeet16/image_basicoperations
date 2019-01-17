import cv2
import numpy as np

img = cv2.imread("sample.jpg")

B,G,R =  cv2.split(img)

print(R)

#print(a)

cv2.imshow("frame", G)

cv2.waitKey(0)

cv2.destroyAllWindows()


