import cv2
import numpy as np

img1 = cv2.imread("sample.jpg",1)
img2 = cv2.imread("4.2.01.tiff",1)



output = cv2.add(img1,img2)
print(output)



cv2.imshow("add",output)
cv2.waitKey(0)
cv2.destroyAllWindows()
