import cv2 as cv
import numpy as np
filepath="Ch2-images/child_small.jpg"
img=cv.imread(filepath,0)
img2=255-img
two_images=np.hstack((img,img2))
cv.imshow("A)Original Image B)Its Negative",two_images)
cv.waitKey(0)
