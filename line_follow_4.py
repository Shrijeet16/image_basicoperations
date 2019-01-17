import cv2
import numpy as np


def get_points(event , x,y ,flags ,param):
    
    if event == cv2.EVENT_LBUTTONDBLCLK:
        points = [(x,y)]
        print(points)
        print(img2[x][y])


cv2.namedWindow("line_follow")

#capture the image
img =  cv2.imread("line_follow.jpg",0)

#680 is heigth  and   510 is the width
#deafult shape of image is 680,510

#cropthe image

#############crop_img = img[0:680,140:370]

#croped shape of image is height 680, width 240

#blur the image

blur = cv2.GaussianBlur(img , (9,9) , 0)

#print(blur)

#thresholding the image to reduce noise

ret , img1 = cv2.threshold(blur,170,255,cv2.THRESH_BINARY)

img2 = cv2.erode(img1 , None , iterations = 4)

#cv2.imshow("line_follow",img2)
#find the contours of the the image img2

#cv2.setMouseCallback("line_follow",get_points)
cv2.setMouseCallback("line_follow1",get_points)

cv2.imshow("line_follow1", img2)

img3 ,contours , hierarchy = cv2.findContours(img2,cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

if len(contours) > 0 :

    c = max(contours  , key = cv2.contourArea)
    M = cv2.moments(c)
    
    cx = int(M['m10']/M['m00'])  #centre wrt to width according to contour and frame

    cy = int(M['m01']/M['m00'])  #centre wrt to height according to contour and frame

    cv2.line(img3 , (cx ,0) , (cx , 680) , (255,0,0) , 2)

    cv2.line(img3 , (0, cy) , (510, cy) , (255,0,0) , 2)

    cv2.drawContours(img3 , contours , -1 , (0,255,0) , 2)

cv2.line(img3 , (20,20) , (110,110), (255,0,0) , 2)

cv2.imshow("line_follow",img3)

cv2.waitKey(0)

cv2.destroyAllWindows()


