import cv2
import numpy as np
import math


#creating a video capture object 
cap = cv2.VideoCapture(0)

#if we give second argument as 1 camera will be the input

if(cap.isOpened()):

    ret,frame = cap.read()
   # print(ret)
    #print(frame)

#cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)


while ret:

    cv2.imshow("AAA",frame)
    if cv2.waitKey(1) == 27:
        break
     

cv2.destroyWindows("AAA")

cap.release()







     


    
