import cv2 as cv
import numpy as np
filepath1="Ch2-images/eye_small.jpg"
filepath2="Ch2-images/flower.jpg"
img1=cv.imread(filepath1,0)
img2=cv.imread(filepath2,0)
# Union
img_union=img1
idxs=np.where(img2>img1)
img_union[idxs]=img2[idxs]
cv.imshow("Union",img_union)
# Intersection
img_intersection=img1
idxs=np.where(img2<img1)
img_intersection[idxs]=img2[idxs]
cv.imshow("Intersection",img_intersection)
# Set Complement
img_comp=255-img1
cv.imshow("Complement",img_comp)
# Set Difference
img_diff=img2-img1
cv.imshow("Difference",img_diff)
cv.waitKey(0)
