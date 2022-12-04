import cv2 as cv
import numpy as np
filepath="../Ch3-images/intensity-level-slicing.jpg"
img=cv.imread(filepath,0)
t1=100
t2=180
img2=np.zeros((img.shape))
idxs1=np.where(img<t1)
idxs2=np.where(img>t2)
img2[idxs1]=img[idxs1]
img2[idxs2]=img[idxs2]
cv.imshow("Image",img)
cv.imshow("Thresholded Image",img2)
cv.waitKey(0)