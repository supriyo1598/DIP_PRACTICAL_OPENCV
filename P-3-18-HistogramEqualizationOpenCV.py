import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt
img=cv.imread("../Ch3-images/cameraman.jpg",0)
hist_before = cv.calcHist(images=[img], channels=[0],mask=None,histSize=[256],ranges=[0,255])
histImage=np.zeros(img.shape,np.uint8)
bin_w_img = int(np.round( img.shape[1]/255 ))
cv.normalize(hist_before, hist_before, alpha=0, beta=img.shape[0], norm_type=cv.NORM_MINMAX)
for i in range(1, 256):
    cv.line(histImage, ( bin_w_img*(i-1), img.shape[0] - int(np.round(hist_before[i-1])) ),
            ( bin_w_img*(i), img.shape[0] - int(np.round(hist_before[i])) ),
            ( 255, 0, 0), thickness=2)

imgeq = cv.equalizeHist(img)
hist_after = cv.calcHist(images=[imgeq], channels=[0],mask=None,histSize=[256],ranges=[0,255])
histImage_eq=np.zeros(imgeq.shape,np.uint8)
bin_w_img_eq = int(np.round( imgeq.shape[1]/255 ))
cv.normalize(hist_after, hist_after, alpha=0, beta=imgeq.shape[0], norm_type=cv.NORM_MINMAX)
for i in range(1, 256):
     cv.line(histImage_eq, ( bin_w_img_eq*(i-1), imgeq.shape[0] - int(np.round(hist_after[i-1])) ),
             ( bin_w_img_eq*(i), imgeq.shape[0] - int(np.round(hist_after[i])) ),
             ( 255, 0, 0), thickness=2)
imgs=np.hstack((histImage,img,imgeq,histImage_eq))
cv.imshow("A)Histogram of Original Image, B)Original Image, C)Equalized Image, D)Histogram of Equilized Image",imgs)
cv.waitKey(0)


