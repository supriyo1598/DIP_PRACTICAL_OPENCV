import cv2 as cv
import numpy as np
filepath="Ch2-images/child_3.jpg"
img=cv.imread(filepath,0)
h,w=img.shape
translation_matrix = np.float32([ [1,0,70], [0,1,110] ])
img_translation = cv.warpAffine(img,translation_matrix, (h, w))
cv.imshow("Scaled Down Image",img_translation)
cv.waitKey(0)