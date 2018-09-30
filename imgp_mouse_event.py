
import cv2
import numpy as np


#mouse callback function

def draw_circle(event,x,y,flags,param):
    if event == cv2.EVENT_LBUTTONDBLCLK:
        cv2.circle(img,(x,y),50,(255,0,234),-1)
        cv2.imshow('assasa',img)
        print('clicked')


#creating a black image using numpy


img = np.zeros((2048,2048,3),np.uint8)

cv2.namedWindow("assasa")
cv2.setMouseCallback('assasa',draw_circle)

while(1):
    cv2.imshow('assasa',img)

    if cv2.waitKey(0):
        break

cv2.destroyAllWindows()


#cv2.COLOR_BGR2GRAY converts any normal image into grayscale image

#cv2.imwrite saves the imagea the image with the given arguments
#arguments in cv2.imwrite
#(name by whch image is to be saved,image to be saved)



    

