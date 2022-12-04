import cv2 as cv
import numpy as np
filepath="Ch2-images/child_3.jpg"
img=cv.imread(filepath,0)
h,w=img.shape
center = (h / 2, w / 2)
angle30,angle60,angle90 = 30,60,90
scale = 1.0
M = cv.getRotationMatrix2D(center, angle30, scale)
rotated30 = cv.warpAffine(img, M, (h, w))
M = cv.getRotationMatrix2D(center, angle60, scale)
rotated60 = cv.warpAffine(img, M, (h, w))
M = cv.getRotationMatrix2D(center, angle90, scale)
rotated90 = cv.warpAffine(img, M, (h, w))
all_images=np.hstack((rotated30,rotated60,rotated90))
cv.imshow("The child",all_images)
cv.waitKey(0)