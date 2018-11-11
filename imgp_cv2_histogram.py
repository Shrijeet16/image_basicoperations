import cv2
import numpy as np

#to calculate histogram the function used is cv2.calcHist()
#cv2.calcHist([img] , [channel no] , mask(none) , [beans] , [range])



img = cv2.imread("sample.jpg",1)

red_Hist  = (img , 2 ,None , 256 , (0,255))

print(red_Hist)

#cv2.imshow("AAA",red_Hist)

#cv2.waitKey(0)

#cv2.destroyAllWindows()
