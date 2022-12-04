import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt
filepath="Ch3-images/xray.jpg"  # for log transform
img=cv.imread(filepath,0)
img2=img.copy()
idxs=np.where(img2<105)
img2[idxs]=0
img3=img2.copy()
img3[img3>0]=255
imgs=np.hstack((img,img2,img3))
cv.imshow("A)X-ray Image B)One sided Thresholded image C)Both sided thresholded image",imgs)
cv.waitKey(0)