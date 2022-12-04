import numpy as np
import cv2 as cv
img=cv.imread("Ch3-images/cameraman.jpg",0)
img2=cv.imread("Ch3-images/cameraman.jpg",0)
img3=cv.imread("Ch3-images/forest2.jpg",0)
hist_img1 = cv.calcHist(images=[img], channels=[0],mask=None,histSize=[256],ranges=[0,255])
hist_img2 = cv.calcHist(images=[img2], channels=[0],mask=None,histSize=[256],ranges=[0,255])
hist_img3 = cv.calcHist(images=[img3], channels=[0],mask=None,histSize=[256],ranges=[0,255])
d1 = cv.compareHist(hist_img1, hist_img2, cv.HISTCMP_CORREL)
d2 = cv.compareHist(hist_img1,hist_img3,  cv.HISTCMP_CORREL)
imgs=np.hstack((img,img2,img3))
strTitle="A)Image1 B)Image2 C)Image3 - Matching(img1,img2)="+str(d1)+" Matching(img1,img3)="+str(d2)
cv.imshow(strTitle,imgs)
cv.waitKey(0)