import cv2 as cv
import numpy as np
filepath="Ch2-images/child_small.jpg"
img=cv.imread(filepath,0)
r,c=img.shape
noise=np.random.randint(0,50,[r,c],np.uint8)
img2=img+noise
diff=np.abs(img-img2)
all_images=np.hstack((img,img2,diff))
cv.imshow("A) Original Image B)Noisy Image C)Original image-Noisy image",all_images)
cv.waitKey(0)
#test