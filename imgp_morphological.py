import cv2
import numpy as np

#morphological transformation
#border reduces while applying erosion operations
#dilation reduces the black bordr of the image to white

#On applying cv2.MORPH_GRADIENT it calculates the difference of eroded and dilated image


#k =  cv2.getStructuringElement(cv2.MORPH_RECT ,(5,5))

#makes a kernel of a 5X5 matrix

#k =  cv2.getStructuringElement(cv2.MORPH_ellipse ,(5,5))
#makes a kernel of a 5X5 as of shape of ellipse and makes other entries as zeros

#k =  cv2.getStructuringElement(cv2.MORPH_CROSS,(5,5))
#makes a kernel of a 5X5 matrix of a shape of cross

img = cv2.imread("sample.jpg",0)

th = 0
max_value = 255

ret, binary_inv = cv2.threshold(img , th , max_value , cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)

k = cv2.getStructuringElement(cv2.MORPH_CROSS , (5,5))

print(k)

#erosion = cv2.erode()


cv2.imshow ("binaaid",binary_inv)

cv2.waitKey(0)

cv2.destroyAllWindows()
