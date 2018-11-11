import cv2
import numpy as np

#cv2.namedWindow("line_follow")  #creating a window
#step1
img = cv2.imread("line_follow.png",0)   #reading the image

blur = cv2.GaussianBlur(img , (5,5) ,0 )

#step2
ret , binary = cv2.threshold(blur , 200 , 255 , cv2.THRESH_BINARY + cv2.THRESH_OTSU)
ret_inv , binary_inv = cv2.threshold(blur , 200 , 255 , cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)

#new_image_erode = cv2.erode(binary_inv , None , iterations = 4)
#useful image
new_image_dilate = cv2.dilate(binary , None , iterations = 25) #thinning the line

h,w = new_image_dilate.shape  #recieving the values of the dimensions of the image
#print(h,w)


if(len(contours) > 0):

    c = max(contours , key = cv2.contourArea)
    cv2.drawContours(img2 , c ,-1 ,(255,0,0) , 5)    

    





while(1):

    #for i in range (0,6):
        

    image ,contours ,hierarchy = cv2.findContours(new_image_dilate , cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

    print (contours)

   # cv2.drawContours(img ,25,  -1 , (0,255,255), 12)
        
        
        






    #cv2.imshow("line_follow_normalerode",new_image_erode)
    cv2.imshow("line_follow",new_image_dilate)   #showing the image

    
    if (cv2.waitKey(0) == 27):
        break   #stop showing when Esc is presseed

    

cv2.destroyAllWindows()
