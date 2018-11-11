import cv2
import numpy as np

img = cv2.imread("5.1.11.tiff")


#output data =  depth should be taken as -1 for extracting absolute border
#cv2.sobel
#arguments cv2.sobel(img , output data type eg: cv2.CV_64F , xorder,yorder,ksize)


#it is better option to convert the output data type to cv2.CV_64S because it gives
#better reasult in both transition from black to white and white to black
#while uint8 converts white to black transition as zero
#if we want to detedct both edges then it is a better a option to take absolute
#value in cv2.CV_64S and then to convert it back into cv.CV_8U


#arguments in cv2.Sobel(image, datatype , dx,dy,ksize)

sobelx = cv2.Sobel(img,-1,1 ,0 ,3 )
sobely = cv2.Sobel(img,-1,0 ,1 ,3)

sobel = sobelx+sobely


cv2.imshow("normal" ,img )
cv2.imshow("sobelx" , sobelx)

cv2.imshow("sobely" , sobely)
cv2.imshow("sobel" , sobel)


#scharr filter

#cv2.Scharr(img , datatype , dx , dy ,borderType)
#dx+dy = 1

schaarx = cv2.Scharr(img ,-1 , 1 , 0 )
schaary = cv2.Scharr(img , -1 , 0 , 1 )

schaar = schaarx+schaary

cv2.imshow("schaar" , schaar)
cv2.imshow("schaarx" , schaarx)
cv2.imshow("schaary" , schaary)





cv2.waitKey(0)

cv2.destroyAllWindows()


