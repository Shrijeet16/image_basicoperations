import cv2
import numpy as np


cap = cv2.VideoCapture(0)

while(1):

    ret , img = cap.read()

    img1 = cv2.GaussianBlur(img , (5,5) , 1 , 1) 

    hsv = cv2.cvtColor(img1 , cv2.COLOR_BGR2HSV)

    lower_white = np.array([0 , 0 , 215 ])

    upper_white = np.array([0 , 0 , 255 ])

    white_range = cv2.inRange(hsv , lower_white , upper_white)

    white_only = cv2.bitwise_and(img1 , img1 , mask = white_range)

    _ , contours , hierarchy = cv2.findContours(white_range , cv2.RETR_TREE , cv2.CHAIN_APPROX_SIMPLE)

    #if len(contours) >0:
     #   white_color = max(contours , key = cv2.contourArea)

    #cv2.drawContours(white_range , contours , -1 , (0,255,0) , 2)
    

    cv2.imshow("frame" , img1)

    cv2.imshow("white_range" , white_range)

    cv2.imshow("white_only" , white_only)    
    
    if(cv2.waitKey(1) == 27):

        cap.release()
        cv2.destroyAllWindows()
        break

    
