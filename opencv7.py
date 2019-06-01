import cv2
import numpy as np

fc = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
ec = cv2.CascadeClassifier('haarcascade_eye.xml')
vid=cv2.VideoCapture(0)
while True:
    ret, img=vid.read()
    gray=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    face=fc.detectMultiScale(gray,1.3,5)
    for (x,y,w,h) in face:
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
        roi_gray = gray[y:y+h,x:x+w]
        roi_color = img[y:y+h,x:x+w]
        eye=ec.detectMultiScale(roi_gray)
        for(ex,ey,ew,eh) in eye:
            cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
    cv2.imshow('img',img)
    if cv2.waitKey(1) & 0xff==ord(' '):
        break
cv2.destroyAllWindows()
vid.release()

        
 
