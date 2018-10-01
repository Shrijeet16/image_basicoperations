import cv2
import math
import numpy as np




def drawcircle(event,x,y,flag,parameter):

    global radius,a1,b1,a2,b2
    
    if event == cv2.EVENT_LBUTTONDOWN:

        a1,b1 = x,y
        cv2.circle(img,(a1,b1),3,(255,0,0),3)
        
    elif event == cv2.EVENT_LBUTTONUP:

        a2,b2 = x,y

        radius = math.sqrt(math.pow((a1-a2),2)  +  math.pow((b1-b2),2))
        #print(radius)
        cv2.circle(img,(a1,b1),int (radius),(255,255,0),4)
        cv2.imshow("AAAA",img)


img = np.zeros((512,512,3),np.uint8)

cv2.namedWindow("AAAA")
cv2.setMouseCallback("AAAA",drawcircle)



while(1):

    cv2.imshow("AAAA",img)

    cv2.waitKey(0)
    break

    

#print(radius)

cv2.destroyAllWindows()








