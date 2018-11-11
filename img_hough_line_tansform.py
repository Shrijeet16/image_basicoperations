import cv2
import numpy as np

cap = cv2.VideoCapture(0)

if(cap.isOpened()):
    ret , frame = cap.read()

while (ret):

    ret , frame = cap.read()

    gray = cv2.cvtColor(frame , cv2.COLOR_BGR2GRAY)

    edges = cv2.Canny(gray ,100 , 200 , apertureSize = 5 ,L2gradient =  True)

    lines = cv2.HoughLines(edges , 1, np.pi/180 , 20)

    #cv2.houghlines (image , rho_value ,thete ,threshold value)
    

    #rho value  = distance accuraacy of the accumalator
    #theta = angle accuracy of the accumalator
    
    #the lines obtain are in polar form so we need to convert them iin cartesian form


    if lines is not None:

        for rho,theta in lines[0]:

            a = np.cos(theta)
            b = np.sin(theta)

            x0 = a*rho
            y0 = b*rho

            pts1 = (int(x0 + 1000*(-b)) , int(y0 + 1000*(a)))
            pts2 = (int(x0 - 1000*(-b)) , int(y0 - 1000*(a)))

            cv2.line(frame,pts1,pts2,(255,0,0) ,4)



    cv2.imshow("aaa",frame)

    if(cv2.waitKey(1) == 27):
        break

cap.release()
cv2.destroyAllWindows()
