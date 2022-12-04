import cv2 as cv
import numpy as np
img=np.zeros([100,100])
img[:,:]=255
img=img.astype(np.uint8)
img[30:80,30:80]=0
cv.imshow("Array image",img)
cv.waitKey(0)