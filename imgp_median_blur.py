import cv2
import numpy as np
import random

#salt and pepper noise can be handled efficiently with the help of cv2.medianblur()

#excellent for the image with salt and pepper noise


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
            

#cv2.imshow("salt and pepper noise",output)

output1 = cv2.medianBlur(output,5)

cv2.imshow("median blur",output1)

cv2.waitKey(0)

cv2.destroyAllWindows()


