import numpy as np
import cv2

cv2.namedWindow("normal")


cap = cv2.VideoCapture(0) #why is argument passed as zero

#4 parameters need to be passed
#1) filename
#2) codec
#3) framerate
#4) resolution

filename = "output.mp4"
codec = cv2.VideoWriter_fourcc('X','V','I','D')

#different codec available are

"""
1) WMV2
2) WMV1
3) MJPG
4) DIVX
5) XVID
6) H246

"""

framerate = 30
resolution = (640,480)

output = cv2.VideoWriter(filename,codec,framerate,resolution)


if(cap.isOpened()):
    ret,frame = cap.read()

while(ret):

    ret,frame = cap.read()

    output.write(frame)
    
    cv2.imshow("normal",frame)

    if(cv2.waitKey(1)==27):
        break

cv2.destroyAllWindows()

output.release()
  
cap.release()
        








