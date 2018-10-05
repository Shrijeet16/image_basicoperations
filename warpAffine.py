import cv2
import numpy as np

img = cv2.imread("sample.jpg")

point1 = np.float32([[1.2,1.4,0.2],[1.5,0.2,1.4]])

point2 = np.float32([[0.6,1.2,1.22],[1.4,1.1,5]])

output = cv2.warpAffine(img, point1,(512,512),flags = cv2.INTER_LINEAR,
                        borderMode = cv2.BORDER_REFLECT)


output1 = cv2.warpAffine(img, point2,(512,512),flags = cv2.INTER_LINEAR,
                        borderMode = cv2.BORDER_REFLECT_101)


cv2.imshow("output",output)

cv2.imshow("output1",output1)

cv2.waitKey(0)

cv2.destroyAllWindows()


#on choosing 3 non collinear points in the image and by using getAffineTransform()
#we can determine which transform is related with the images given in the arguments

