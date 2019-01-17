import cv2
import numpy

cap =cv2.VideoCapture(0)

cv2.namedWindow("result")

cv2.namedWindow("result_H")

cv2.namedWindow("result_S")

cv2.namedWindow("result_V")

def None_change():
    pass

"""
cv2.createTrackbar('H_max' , 'result_H'  , 0 , 179 , None_change)

cv2.createTrackbar('H_min' , 'result_H'  , 0 , 179 , None_change)

cv2.createTrackbar('S_max' , 'result_S'  , 0 , 255 , None_change)

cv2.createTrackbar('S_min' , 'result_S'  , 0 , 255 , None_change)

cv2.createTrackbar('V_max' , 'result_V'  , 0 , 255 , None_change)

cv2.createTrackbar('V_min' , 'result_V'  , 0 , 255 , None_change)
"""
for i in range (0,2):

    ret ,Trash_frame = cap.read()



while(1):

    ret , frame = cap.read()

    img = cv2.cvtColor(frame , cv2.COLOR_BGR2HSV)



#-------------------------------------------------------------------------------

    h_max = cv2.getTrackbarPos('H_max' , 'result_H')
    
    h_min = cv2.getTrackbarPos('H_min' , 'result_H')

    s_max = cv2.getTrackbarPos('S_max' , 'result_S')

    s_min = cv2.getTrackbarPos('S_min' , 'result_S')

    v_max = cv2.getTrackbarPos('V_max' , 'result_V')

    v_min = cv2.getTrackbarPos('V_min' , 'result_V')

#-------------------------------------------------------------------------------------
    #cv2.imshow("frame" , frame)

    H , S , V = cv2.split(img)

    ret_H , thresh_H = cv2.threshold(H , h_min , h_max , cv2.THRESH_BINARY )    #151,171

    ret_S , thresh_S = cv2.threshold(S , s_min , s_max , cv2.THRESH_BINARY )    #108,255

    ret_V , thresh_V = cv2.threshold(V , v_min , v_max , cv2.THRESH_BINARY )    #223,255

#---------------------------------------------------------------------------------    

    cv2.imshow("result" , frame)

    cv2.imshow("result_H" , thresh_H )
    
    cv2.imshow("result_S" , thresh_S )

    cv2.imshow("result_V" , thresh_V )
    

    if(cv2.waitKey(1) == 27):

        cap.release()
        cv2.destroyAllWindows()
        break

    
