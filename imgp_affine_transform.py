import cv2
import numpy as np



#affine transformation

#1) cv2.warpAffine()
#2) cv2.getAffineTransform() 

img = cv2.imread("sample.jpg",1)

dim = img.shape     #dim== dimensions

#print(parm[0])

rotationangle = 60
scale = 1

rotationMatrix = cv2.getRotationMatrix2D((dim[1]/2,dim[2]/2),rotationangle,scale)

point1 = np.float32([[100,100],[300,100], [100,300]])

point2 = np.float32([[200,150],[400,150], [400,300]])

A = cv2.getAffineTransform(point1 , point2)

print(A)


img = cv2.warpAffine(img,A,(dim[1],dim[0]))

#parameters are (source,rotationMatrix,centre )


cv2.imshow("ssss",img)
cv2.waitKey(0)
cv2.destroyAllWindows()

