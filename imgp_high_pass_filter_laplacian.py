import cv2
import numpy as np

#noise and edges are high freq in the image
#high pass are very good for finding edges


#reduce noise using low pass filter and then pass the same argument to the image and
#apply high pass filter to detect the edges

# 3 high pass filter 1)laplacian  2)sobel 3)scharr


img = cv2.imread("5.1.11.tiff")

#img = cv2.cvtColor(img , cv2.COLOR_BGR2GRAY)

edges = cv2.Laplacian(img , -1 , ksize = 3 , scale=7)
#for 
#depth is deafault -1
#delta should not be given as argument
#arguments in cv2.laplacian(image , depth , kernel_size ,scale , delta ,bordertype)


cv2.imshow('normal', img)

cv2.imshow('laplacian' , edges )

cv2.waitKey(0)


cv2.destroyAllWindows()

