import numpy as np
import cv2 as cv
filepath="../Ch3-images/cross-roads.jpg"
img=cv.imread(filepath,0)
img2=img.copy()
img_min=np.min(img2)
img_max=np.max(img2)
band_min=0
band_max=255
nimg=(img2-img_min)*((band_max-band_min)/(img_max-img_min))+band_min
print(np.min(nimg),np.max(nimg))
nimg=nimg.astype(np.uint8)
imgs=np.hstack((img,nimg))
cv.imshow("Color:: A)Low contrast image B)Contrast Stretched ",imgs)
cv.waitKey(0)