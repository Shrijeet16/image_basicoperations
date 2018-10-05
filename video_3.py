import numpy as np
import cv2

cv2.namedWindow("normal")
cv2.namedWindow("gray")


#starts capturing the video
cap = cv2.VideoCapture(0)

cap.set(3,1024)
cap.set(4,1024)


print("width:" + str(cap.get(3)))
print("height:" + str(cap.get(4)))

if(cap.isOpened()): #checks that camera attached to the device is opened 

    ret,frame = cap.read()
    #gives the value of the parameters given bby video capture feature


while ret:

    ret,frame = cap.read()

    output0 = frame
    output1 = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    cv2.imshow("normal",output0)

    cv2.imshow("gray",output1)

    if(cv2.waitKey(1)==27):
        break
    
cv2.destroyAllWindows()

cap.release()

