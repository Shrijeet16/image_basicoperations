import cv2
import numpy


imagename = "C:\Users\Sinal\Documents\opencv_proj\lena_color_256.tif"

image = cv2.imread(imagename,0)

image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

cv2.namedWindow("NEW")
cv2.imshow("NEW",image)

cv2.waitKey(0)

cv2.destroyAllWindows()
