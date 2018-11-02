import cv2
import numpy as np

#opencv reads image in BGR format but matplollib computes the image in RGB
#colorspaces in opencv
#color conversion flags are listed in this program


j = 0

for filename in dir(cv2):

    if filename.startswith('COLOR_'):
        print filename
        j=j+1


print(j)
