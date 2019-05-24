import cv2
import numpy as np

vid=cv2.VideoCapture(0)
while True:
    ret,frame=vid.read()     #input as original video
    hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    low=np.array([150,50,0])     #lower limit of hue
    high=np.array([255,255,255])   #upper limit of hue


    search= cv2.inRange(hsv,low,high)    #filter
    final= cv2.bitwise_and(frame,frame,mask=search)   #final result

    cv2.imshow('frame',frame)
    cv2.imshow('mask',search)
    cv2.imshow('final',final)
    if cv2.waitKey(1) & 0xFF == ord(' '):       #take spacebar to quit
        break
cv2.destroyAllWindows()
vid.release()
