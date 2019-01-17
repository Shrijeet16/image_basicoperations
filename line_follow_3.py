import cv2
import numpy as np


#step1
img = cv2.imread("line_follow.jpg",0)
edges = cv2.Laplacian(img , -1 , ksize = 3 , scale=1)

blur = cv2.GaussianBlur(edges , (5,5) ,0 )


#step2
#ret , binary = cv2.threshold(blur , 50 , 255 , cv2.THRESH_BINARY + cv2.THRESH_OTSU)



#step3
#new_binary = cv2.erode(binary , None , iterations = 5)


cv2.imshow("line_follow",blur)

cv2.waitKey(0)

cv2.destroyAllWindows()


