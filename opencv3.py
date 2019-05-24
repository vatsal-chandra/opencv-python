import cv2
import numpy as np
image1= cv2.imread('clock.jpg',cv2.IMREAD_COLOR)
#px=image1[100,90]             #pixels of image coordinate
#print(px)
#region of image:
roi=image1[10:150,10:150]
print(roi)
roi=[255,255,255]
cv2.imshow('image',image1)
cv2.waitKey(0)
cv2.destroyAllWindows
#print(roi)
