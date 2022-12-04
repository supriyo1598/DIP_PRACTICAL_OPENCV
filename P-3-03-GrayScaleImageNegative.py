# image negative
import cv2 as cv
import numpy as np
filepath="../Ch3-images/mris.jpg"
img=cv.imread(filepath,0)
img2=255-img
imgs=np.hstack((img,img2))
cv.imshow("A)Image B)Negative",imgs)
cv.waitKey(0)