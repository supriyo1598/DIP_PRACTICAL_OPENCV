import numpy as np
import cv2 as cv
filepath="Ch3-images/moon.jpg"
img = cv.imread(filepath,0)
blur = cv.GaussianBlur(img,(5,5),0)
imgs=np.hstack((img,blur))
cv.imshow("A)Original image B)5*5 Gaussian filter",imgs)
cv.waitKey(0)