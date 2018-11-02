import cv2
import numpy as np



def red_function():
    
    pass
    
def green_function():

    pass

def blue_function():
    pass





img = np.zeros((512,512,3),np.uint8)

windowname = 'color pallete'

cv2.namedWindow(windowname)

#parameters in cv2.CreateTrackbar(trackbarname,windowname,value,count,onchange)
#windowname is the window in which trackbar will be there i.e window will be parent of the trackbar
#value optional pointer to an integer variable whose value is used to determine the position of the slider
#count maximum position of the counter
#onchange pointer to the function to be called when there is change in the position of the slider 
#userdata that is passed as to callback the trackbar event



cv2.createTrackbar('RED',windowname,0,255,red_function)
cv2.createTrackbar('BLUE',windowname,0,255,blue_function)
cv2.createTrackbar('GREEN',windowname,0,255,green_function)

while(True):

    green = cv2.getTrackbarPos('GREEN',windowname)
    red = cv2.getTrackbarPos('RED',windowname)
    blue = cv2.getTrackbarPos('BLUE',windowname)

    img[:] = [blue , green , red]
    cv2.imshow(windowname,img)
    print(blue,green,red)
    
    if(cv2.waitKey(1) == 27):
        break

   

cv2.destroyAllWindows()
