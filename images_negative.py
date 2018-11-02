import cv2
import numpy as np

#the negative of image is the image in which the lightest area of the photographed
#image appear darkest and the darkest appear lightest
#in case of color negatives the colors are reversed into their complimentary colors


img = cv2.imread("sample.jpg")

img1 = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)

img2 = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

img3 = abs(255 - img1)

img4 = abs(255 - img2)


titles = ['normal','RGB','Gray','COLOR_negative','GRAY_negative']

images = [img,img1,img2,img3,img4]


for i in range(5):

    cv2.imshow(titles[i],images[i])


cv2.waitKey(0)

cv2.destroyAllWindows()

