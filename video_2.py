import cv2
import numpy as mp

filename ="C:\Users\Sinal\Documents\opencv_proj\1. Arduino for Production! A Beginner's Guide - Intro and How to Use the AVR Atmega32 (1).mp4"

cap = cv2.VideoCapture(filename)

if(cap.isOpened()== False):
    print("sasd")

while(cap.isOpened()):


    ret,frame = cap.read()
    print(ret) 

    if ret == True:
        cv2.imshow('Frame',frame)
        if cv2.waitKey(25) & 0xFF == 27:
            break

        else:
            break


                            

                              

cap.release()

cv2.destroyAllWindows()




         
