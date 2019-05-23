import cv2
import numpy as np


video=cv2.VideoCapture(0)
#fourcc=cv2.VideoWriter_fourcc(*'XVID')
#out=cv2.VideoWriter('output.avi', fourcc, 20.0, (680,480)

while True:
    ret,frame=video.read()
    cv2.imshow('frame',frame)                       #show real
    gray=cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow('gray',gray)                     #show gray

    if cv2.waitKey(1) & 0xFF == ord(' '):       #take spacebar to quit
        break
video.release()
out.release()
cv2.destroyAllWindows()
