import cv2
import numpy as np


#step1
cv2.namedWindow("line_follow")
img = cv2.imread("line_follow.png",0) #reading the image in grayscale

blur = cv2.GaussianBlur(img , (5,5) ,0 )



#step2
#ret , binary = cv2.threshold(blur , 127 , 255 , cv2.THRESH_BINARY + cv2.THRESH_OTSU)


#step3
#new_binary = cv2.erode(binary , None , iterations = 25)

#ret1 , new_binary = cv2.threshold(binary , 200 , 255, cv2.THRESH_BINARY_INV)


def get_points(event , x,y ,flags ,param):
    
    if event == cv2.EVENT_LBUTTONDBLCLK:
        points = [(x,y)]
        print(points)
        print(new_binary[x][y])

cv2.setMouseCallback("line_follow",get_points)


#step4
#width = 786        #heigth = 392
#h,w = img.shape
#print(h,w)


cv2.imshow("line_follow",new_binary)

cv2.waitKey(0)
cv2.destroyAllWindows()
