import cv2
import numpy as np

#cap = cv2.VideoCapture()

img = cv2.imread("line_follow.png")
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)


cv2.namedWindow("line_follow",cv2.WINDOW_FULLSCREEN)

flag = 1

while (flag):

    cv2.imshow("line_follow",gray)
    

    
    if(cv2.waitKey(1)==27):

        flag = 0


    
cv2.destroyAllWindows()
