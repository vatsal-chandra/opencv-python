import cv2
import numpy as np


img1=cv2.imread('graph1.jpg')
img2=cv2.imread('graph2.jpg')


#add=img1+img2         # puts the 2 images together
add=cv2.add(img1,img2)      #adds respective pixels
weight=cv2.addWeighted(img1,0.3,img2,0.6,0)
cv2.imshow('weight',weight)
cv2.waitKey(0)
cv2.destroyAllWindows()
