import numpy as np
import cv2 as cv
img=np.zeros([16,16])
print(img.shape)
for i in range(16):
    for j in range(16):
        img[i,j]=i*16+j
print(img)
img=img.astype(np.uint8)

img1=cv.resize(img,(256,256))
cv.imshow("GrayMatrix 256x256",img1)
cv.imshow("GrayMatrix 16x16",img)
cv.waitKey(0)