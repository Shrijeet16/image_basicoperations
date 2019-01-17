import cv2
import numpy

import math

cap = cv2.VideoCapture(0)
cap.set(3,160)
cap.set(4,120)

while(1):
    ret , frame  = cap.read()

    cv2.imshow("normal" , frame)
    
    crop_image = frame[60:120 , 0:160]
    gray = cv2.cvtColor(crop_image , cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray , (5,5) , 1)
    ret , thresh = cv2.threshold(blur , 60, 255 , cv2.THRESH_BINARY_INV)
    image , contours , hiearchy = cv2.findContours(thresh.copy() , 1 , cv2.CHAIN_APPROX_NONE)


    if(len(contours) > 0):

        c = max(contours , key = cv2.contourArea)
        M = cv2.moments(c)
        print("cont"+str(contours))
        print("cv2.Area"+ str(cv2.contourArea(c)))   
        if(M['m00'] != 0):
        
            cx = int(M['m10']/M['m00'])
            cy = int(M['m01']/M['m00'])

            
            y = c[0:35]

            #print(y)
            
            cv2.line(crop_image , (cx,0) , (cx,720) , (255,0,0) ,1)
            cv2.line(crop_image , (0,cy) , (1280,cy) , (0 ,255,0) ,1)

            cv2.drawContours(crop_image , contours ,-1, (0,0,255))

            x1 = y[0][0][0]
            x2 = y[1][0][0]

            y1 = y[0][0][1]
            y2 = y[1][0][1]

            u = ((y2-y1)/(x2-x1))

            l = math.atan2(u,1)

            l = l*(57.30)       #180/pi

            l = 90 - l

            print(l)

        else:
            pass

    else:
        print("sada")

    cv2.imshow("image" , crop_image)

    if(cv2.waitKey(1) == 27):
        cap.release()
        cv2.destroyAllWindows()
        break


        
        
