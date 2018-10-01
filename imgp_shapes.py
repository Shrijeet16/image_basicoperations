import cv2
import numpy as np

#will draw various shapes such as lines,circle,rectangle etc


#creating a black image

img = np.zeros((512,512,3),np.uint8)

cv2.line(img,(0,0),(255,255),(255,0,0),4)
#parameters
#(image,init pt, final pt, color shade, thickness)


cv2.circle(img,(480,55),50,(0,255,255),-1)
#parameters
#(image,centre pt, radius , color shade, thickness)



#if thickness is -1 then it\ is solid fil image


cv2.rectangle(img,(155,90),(254,190),(0,113,255),5)

#parameters
#image,left_corner,right worner,color ,thickness)


cv2.ellipse(img,(225,225),(200,100),0,0,360,(222,123,54),4)


"""To draw the ellipse, we need to pass several arguments.
One argument is the center location (x,y).
Next argument is axes lengths (major axis length, minor axis length).
angle is the angle of rotation of ellipse in anti-clockwise direction.
startAngle and endAngle denotes the starting and ending of ellipse arc
measured in clockwise direction from major axis. i.e. giving values 0 and 360
gives the full ellipse. For more details, check the
documentation of cv2.ellipse(). Below example draws a half ellipse
at the center of the image.
"""


#polygom

pts = np.array([[10,2],[23,11],[22,56],[33,43]],np.int32)
pts = pts.reshape((-1,1,2))
cv2.polylines(img,[pts],False,(222,222,1))


# cv2.polylines() can be used to draw multiple lines.
#Just create a list of all the lines you want to draw and
#pass it to the function. All lines will be drawn individually.
#It is a much better and faster way to draw a group of lines
#than calling cv2.line() for each line.


#if the third argument is false then it will make a shape joining all the points
#instead of the polygon




#adding text to the images

font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img,"aosjdo",(10,480),font,2,(222,222,222))




cv2.imshow("shape",img)

cv2.waitKey(0)

cv2.destroyAllWindows()




