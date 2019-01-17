import numpy as np
import cv2

cap = cv2.VideoCapture(1)
cap.set(3,360)
cap.set(4,240)

while(True):

    #capture the frames
    ret , frame = cap.read()
    
    #crop the image
    crop_img = frame[120:320,0:240]

    #convert the image into gray

    gray = cv2.cvtColor(crop_img , cv2.COLOR_BGR2GRAY)

    #decresing noise through guassian blur
    blur = cv2.GaussianBlur(gray  ,(5,5) , 0)

    #thresholding image into binary inverse image
    ret , thresh = cv2.threshold(blur , 100 ,255 , cv2.THRESH_BINARY_INV)

    #finding contours in  the image
    crop_image_1,contours ,hierarchy = cv2.findContours(thresh.copy() , cv2.RETR_LIST ,  cv2.CHAIN_APPROX_SIMPLE)

    if(len(contours) > 0):

        c = max(contours , key = cv2.contourArea)
        M = cv2.moments(c)

        #finding centroid of the contour
        
        cx = int(M['m10']/M['m00'])
        cy = int(M['m01']/M['m00'])

        #always marking the centre of the contour
    
        cv2.line(crop_image_1 , (cx,0),(cx,240),(255,0,0) , 4)
        cv2.line(crop_image_1 , (0,cy),(360,cy),(255,0,0) , 4)


        #drawing contours in the image
        cv2.drawContours(crop_image_1 , contours , -1 , (0,255,255) , 2)
        
        
        
    cv2.imshow("line_follow" ,crop_image_1)

    if(cv2.waitKey(1) == 27):
        break
    
cap.release()

cv2.destroyAllWindows()
