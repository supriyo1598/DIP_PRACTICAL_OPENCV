import numpy as np
import cv2 as cv
img=np.zeros([256,256],np.uint8)
bg=np.zeros([256,256],np.uint8)
fg=np.zeros([256,256],np.uint8)
img[:,:]=50
img[10:50,10:50]=100
img[80:200,80:200]=150
img[220:240,220:240]=200
idxs=np.where(img==50)
bg[idxs]=255
idxs1=np.where(img==100)
idxs2=np.where(img==150)
idxs3=np.where(img==200)
fg[idxs1]=255
fg[idxs2]=255
fg[idxs3]=255
cv.imshow("mat",img)
cv.imshow("background",bg)
cv.imshow("foreground",fg)
cv.waitKey(0)
