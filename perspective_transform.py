import cv2
import numpy as np

img = cv2.imread("sample.jpg")



point1 = np.float32([[100,0],[200,0],[200,200],[100,200]])

point2 = np.float32([[100,0],[200,50],[180,230],[70,120]])


P = cv2.getPerspectiveTransform(point1,point2)

print(P)

output = cv2.warpPerspective(img, P , (512,512))

cv2.imshow("A",img)
cv2.imshow("AA",output)

cv2.waitKey(0)

cv2.destroyAllWindows()

