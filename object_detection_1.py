import cv2
import numpy as np

cap = cv2.VideoCapture(0)

for i in range(0,2):
    ret , trash_frame = cap.read()


while(1):

    ret , frame = cap.read()

    img = cv2.GaussianBlur(frame , (5,5) , 0)

    hsv = cv2.cvtColor(img , cv2.COLOR_BGR2HSV)
    
    H , S , V = cv2.split(img)

    hsv_min = np.array([136 , 87 , 111] , np.uint8)

    hsv_max = np.array([180 , 255 , 255] , np.uint8)


    hsv_range = cv2.inRange(hsv , hsv_min , hsv_max)

    cv2.imshow("frame" , frame)

    cv2.imshow("hsv" , hsv)

    cv2.imshow("hsv_range" , hsv_range)

    if(cv2.waitKey(1) == 27 ):
        cap.release()
        cv2.destroyAllWindows()
        break
    
    
        
    


    
