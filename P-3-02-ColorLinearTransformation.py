# grayscale image upscaling
import numpy as np
import cv2 as cv
filepath="../Ch3-images/nature.jpg"
img=cv.imread(filepath)
idxs=np.where(img<200)
img2=img.copy()
img2[idxs]=img[idxs]+40
imgs=np.hstack((img,img2))
cv.imshow("A)Image B)Upscaled Intensity image",imgs)
cv.waitKey(0)