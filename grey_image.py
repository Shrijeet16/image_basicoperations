import cv2
import numpy as mu


img = cv2.imread("sample.jpg",1)

p = img[100][120]

print(p)

cv2.imshow("Frame",img)

cv2.waitKey(0)

cv2.destroyAllWindows()





