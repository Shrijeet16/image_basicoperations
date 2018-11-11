import cv2
import numpy as np

img = cv2.imread("sample.jpg",1)

cv2.imshow("normal",img)

k = np.array(([0,-1,0],
             [-1,5,-1],
             [0,-1,0]),np.float32)


#cv2.filter2D(img,depth,kernel or convolution matrix)

output = cv2.filter2D(img,-1,k)

cv2.imshow("output",output)

cv2.waitKey(0)
cv2.destroyAllWindows()
