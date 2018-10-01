#scaling or resizing operations on a image

import cv2
import numpy as np

img = cv2.imread("sample.jpg")

#cv2.resize()
#arguments to be passed
#(image,none,scaling on x-axis fx,scaling on y-axis,interpolation methods)
#different interpolation method
""""
interpolation is how the new pixel would look like based on the pixels in the neighbourhood
various interpolation methods
1)linear
2)nearest
3)area  shrinking operation
4)cubic zooming, works on 4X4 area

"""

cv2.resize(img,None,fx=1.4,fy=1.2,interpolation=cv2.INTER_CUBIC)

crop = img[10:210,10:370]



cv2.imshow("image",crop)

cv2.waitKey(0)
cv2.destroyAllWindows()



