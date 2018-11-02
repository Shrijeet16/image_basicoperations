import cv2
import numpy as np

img = cv2.imread("7.1.10.tiff",0)



th_value = 0
max_value = 255

ret , thresh1 = cv2.threshold(img,th_value,max_value,cv2.THRESH_BINARY + cv2.THRESH_OTSU)
ret , thresh2 = cv2.threshold(img,th_value,max_value,cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
ret , thresh3 = cv2.threshold(img,th_value,max_value,cv2.THRESH_TOZERO + cv2.THRESH_OTSU)
ret , thresh4 = cv2.threshold(img,th_value,max_value,cv2.THRESH_TOZERO_INV + cv2.THRESH_OTSU)
ret , thresh5 = cv2.threshold(img,th_value,max_value,cv2.THRESH_TRUNC + cv2.THRESH_OTSU)

windowname = ['normal','binary','binary_inv','tozero','tozero_inv','trunc']
image = [img,thresh1,thresh2,thresh3,thresh4,thresh5]


for i in range(6):

    cv2.imshow(windowname[i],image[i])

      



cv2.waitKey(0)

cv2.destroyAllWindows()



