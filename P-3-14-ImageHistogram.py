import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt
img=cv.imread("Ch3-images/cameraman.jpg",0)
bins=np.zeros(256)
for i in range(256):
      bins[i]=np.sum(img==i)
print(bins.astype(np.uint8))
levels=range(256)
plt.plot(levels,bins)
# uncommenting the following code will show black vertical lines too
#for i in range(256):
#    plt.vlines(x=i, ymin=0, ymax=bins[i])
plt.show()
