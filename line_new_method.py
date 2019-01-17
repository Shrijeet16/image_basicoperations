import cv2
import numpy as np

capture = cv2.VideoCapture(0)

capture.set(3,320)
capture.set(4,240)

#capture.set(5,X) setting the frame rate

for i in range(0,2):

    ret , trash_image = capture.read()

while(1):

    ret , frame = capture.read()    #capturing from the camera

    gray = cv2.cvtColor(frame  , cv2.COLOR_BGR2GRAY)

    blur = cv2.GaussianBlur(gray , (7,7) ,0)

    ret1 , th1 = cv2.threshold(blur , 200 , 255 ,cv2.THRESH_BINARY + cv2.THRESH_OTSU)

    ret2 , th2 = cv2.threshold(th1 , 180 , 255 , cv2.THRESH_BINARY_INV)

    #cv2.imshow("frame" , frame)
    
    #cv2.imshow("th2" , th2)

    _, contours , hierarchy = cv2.findContours(th2 , cv2.RETR_TREE , cv2.CHAIN_APPROX_SIMPLE)

    contours[0] = max(contours , key = cv2.contourArea)
    
    cv2.drawContours(frame , contours , 0 , (255,0,0) ,2)




    cv2.imshow("frame" , frame)

    
    
