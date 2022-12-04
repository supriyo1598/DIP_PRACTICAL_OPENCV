import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt
img=cv.imread("Ch3-images/cameraman.jpg")
img1=img[:,:,0]
hist = cv.calcHist(images=[img1], channels=[0],mask=None,histSize=[256],ranges=[0,255])
plt.plot(hist, color="black")
plt.xlim([0, 256])
plt.show()