import cv2
import numpy as np

cap = cv2.VideoCapture(0)

cap.set(3,240)
cap.set(4,360) #86400 maximum frame area

for i in range (2):

    ret_trash , frame_trash = cap.read()

while(cap.isOpened()):

    ret , img = cap.read()

    gray = cv2.cvtColor(img , cv2.COLOR_BGR2GRAY)

    gray = cv2.GaussianBlur(gray , (7,7) , 0)

    ret , thresh = cv2.threshold(gray , 127 , 255 , cv2.THRESH_BINARY)#'to be changed'

    _, contours , hierarchy = cv2.findContours(thresh.copy() , cv2.RETR_TREE , cv2.CHAIN_APPROX_SIMPLE)

    cv2.imshow("white_line" , thresh)
    
    if(cv2.waitKey(1) == 27):

        cap.release()
        cv2.destroyAllWindows()
        break


    
