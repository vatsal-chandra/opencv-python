#masking using opencv
import cv2
import numpy as np

img1=cv2.imread('graph1.jpg')
img2=cv2.imread('graph2.jpg')
img3=cv2.imread('pythonlogo.png')
#cv2.imshow('img3',img3)
rows,cols,channels=img3.shape
roi=img1[0:rows,0:cols]
gray=cv2.cvtColor(img3,cv2.COLOR_BGR2GRAY)
ret, mask = cv2.threshold(gray,200,255,cv2.THRESH_BINARY_INV)

inverse=cv2.bitwise_not(mask)

bg=cv2.bitwise_and(roi,roi,mask=inverse)     #backgrnd of img1
fg=cv2.bitwise_and(img3,img3,mask=mask)      #foreground of img3
dst= cv2.add(bg,fg)
roi=dst

cv2.imshow('new',img1)
#cv2.imshow('inverse',inverse)
#cv2.imshow('bg',bg)
#cv2.imshow('fg',fg)

cv2.waitKey(0)
cv2.destroyAllWindows()

