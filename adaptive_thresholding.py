import cv2
import numpy as np

img = cv2.imread("4.1.05.tiff",0)

#if the image have different lighting conditions in different areas , in such cases
#we should go for adaptive thresholding
#in this algorithm we find different value of thrshold for each region and then combine
#the whole image so that it give a better reasult with varying illumination


#it has three 'special' input params and only one output arguments

#adaptive method : it decides how to calculate the value of threshold
# 1) cv2.ADAPTIVE_THRESH_MEAN_C : threshold value is the mean of the neighbourhood area
# 2) cv2.ADAPTIVE_THRESH_GAUSSIAN_C : thrshold value is the weigthed sum of neighbourhood values
#       where weights are a gaussian window

#block size : it decides the size of the neighbourhood area

# C : it is the value of the constant which is subtracted fron the mean or weigthed mean calculated

#parameters of the AdaptiveThreshold(img , 255(max_value) , adaptive method , thrshold type , block_size, constant)

#on changing the value of block_size different effects on the image can be seen
#i.e the computing area of the algorithm changes which differs the output


block_size = 11
constant = 2

th1 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,block_size,constant)

th2 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,block_size,constant)


windowname = ['normal','th1','th2']
image = [img,th1,th2]



for i in range(3):

    cv2.imshow(windowname[i],image[i])

      



cv2.waitKey(0)

cv2.destroyAllWindows()



