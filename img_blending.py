import cv2
import numpy as np

img1 = cv2.imread("sample.jpg",1)
img2 = cv2.imread("4.2.01.tiff",1)


#image blending : this is also a image addition but it gives a transparent effect
#to the resultant image by giving approximate values to alpha,beta,gamma

#cv2.addWeigthed  is the function used for image blending and the arguments given are as below
#cv2.addWeigthed(img1,alpha,img2,bete,gamma)

output = cv2.addWeighted(img1,0.9,img2,1.5,0)

#for good blending effect we should use the condition as alpha + beta = 1

#time.sleep() stops the program for the given amount of time in the argument
#the time of the argument is in seconds
#for using time.sleep we need to import time library



print(output)


cv2.imshow("blending",output)

cv2.waitKey(0)
cv2.destroyAllWindows()


