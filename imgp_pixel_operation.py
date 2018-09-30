import cv2
import numpy as np

img = cv2.imread("sample.jpg")

#px = img[55][254]  to show the values of pixel of any image

img[55][254] =  [255,255,255]

cv2.namedWindow("image")

#roi = img[100:102,100:102]

img[100:152,100:152] = [0,0,0]
#above selects the region in the image  i.e  image in a image 

print()


cv2.imshow("image",img)

cv2.waitKey(0)
cv2.destroyAllWindows()


#ROI region of image
#print(px)

