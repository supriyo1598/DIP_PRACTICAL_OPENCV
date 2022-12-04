import numpy as np
import cv2 as cv
filepath="../Ch3-images/5000.jpg"
img=cv.imread(filepath,0)
img1=img & 1
img2=img & 2
img4=img & 4
img8=img & 8
img16=img & 16
img32=img & 32
img64=img & 64
img128=img & 128
images1=np.hstack((img128,img64,img32,img16))
images2=np.hstack((img8,img4,img2,img1))
images=np.vstack((images1,images2))
cv.imshow("Image",images)

cv.waitKey(0)