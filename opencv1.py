import cv2
import numpy as np
import matplotlib.pyplot as plt
image1=cv2.imread('clock.jpg',cv2.IMREAD_GRAYSCALE)
#plt.imshow(image,cmap='gray',interpolation='bicubic')
#plt.plot([30,100],[50,50])
#plt.show
cv2.imshow('image1',image1)

image2=cv2.imread('clock.jpg',cv2.IMREAD_COLOR)
cv2.line(image2,(0,0),(1000,1000),(1255,1255,1255),16)
cv2.circle(image2,(100,560),50,(0,0,255),-1)
cv2.imshow('image2',image2)

cv2.polylines(img,[pts],True,(0,255,255)

cv2.waitkey(0)
cv2.destroyAllWindows()
