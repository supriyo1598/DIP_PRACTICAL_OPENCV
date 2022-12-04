import cv2 as cv
import numpy as np
filepath="Ch2-images/child_3.jpg"
img=cv.imread(filepath,0)
h,w=img.shape
# scale up
img_scaledup=cv.resize(img,(2*h,2*w))
#scale down
nh=int(h/2)
nw=int(w/2)
img_scaleddown=cv.resize(img,(nh,nw))
cv.imshow("Original Image",img)
cv.imshow("Scaled Up Image",img_scaledup)
cv.imshow("Scaled Down Image",img_scaleddown)
cv.waitKey(0)