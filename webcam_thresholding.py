import cv2
import numpy as np

cap = cv2.VideoCapture(0)

windowname = "AAA"

if (cap.isOpened()):

    ret,img = cap.read()


while ret:

    ret,img = cap.read()

    th_value = 160

    max_value = 255

    #cv2.threshold() function's arguments()
    #(source image , threshold value ,max_vlaue, threshold algorithm )
    #max_value = the value given to pixel if it is grater than threshold value

    ret , thresh1 = cv2.threshold(img,th_value,max_value,cv2.THRESH_BINARY)
    ret , thresh2 = cv2.threshold(img,th_value,max_value,cv2.THRESH_BINARY_INV)
    ret , thresh3 = cv2.threshold(img,th_value,max_value,cv2.THRESH_TOZERO)
    ret , thresh4 = cv2.threshold(img,th_value,max_value,cv2.THRESH_TOZERO_INV)
    ret , thresh5 = cv2.threshold(img,th_value,max_value,cv2.THRESH_TRUNC)


    cv2.imshow(windowname,thresh1)
    cv2.imshow(windowname + '1',thresh2)
    cv2.imshow(windowname+ '2',thresh3)
    cv2.imshow(windowname+ '3',thresh4)
    cv2.imshow(windowname+ '4',thresh5)


    if(cv2.waitKey(1) == 27):
        break

cap.release()
cv2.destroyAllWindows()
