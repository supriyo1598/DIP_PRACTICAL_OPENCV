import matplotlib.pyplot as plt
import numpy as np
import cv2 as cv
img=cv.imread("Ch3-images/cameraman.jpg",0)
bins=np.zeros(256)
for i in range(256):
      bins[i]=np.sum(img==i)
levels=range(256)
bins=bins/(img.shape[0]*img.shape[1]) # bins normalization
print(bins)
plt.plot(levels,bins)
# uncommenting the following code will show black vertical lines too
#for i in range(256):
#    plt.vlines(x=i, ymin=0, ymax=bins[i])
plt.show()