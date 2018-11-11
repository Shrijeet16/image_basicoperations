import cv2
import numpy as np
import random

#salt and pepper noise

img = cv2.imread("sample.jpg")

rows , coloumns , channels =  img.shape

p = 0.05

output = np.zeros(img.shape,np.uint8)

for i in range(rows):

    for j in range(coloumns):

        r = random.random()

        if (r <= p/2 ):

            output[i][j] = img[i][j]

        elif (r < p):
            output[i][j] = [255,255,255]

        else:
            output[i][j] = img[i][j]
            

cv2.imshow("salt and pepper noise",output)

cv2.waitKey(0)

cv2.destroyAllWindows()


            

#SNR signal to noise ratio
#SNR = signal power/noise power





