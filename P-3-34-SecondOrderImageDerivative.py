import numpy as np
import cv2 as cv
filepath="Ch3-images/holes.png"
img = cv.imread(filepath,0)
rows, cols = img.shape
img2 = np.zeros((rows, cols), np.uint8)
img3 = np.zeros((rows, cols), np.float)
for i in range(rows):
    for j in range(1, cols-1):
        img2[i,j] = img[i,j+1] - (2 * img[i,j]) + img[i,j-1]
        img3[i, j] = img[i, j + 1] - (2 * img[i, j]) + img[i, j - 1]
imgs=np.hstack((img,img2,img3))
cv.imshow("A)Original image B)second order difference",imgs)
cv.waitKey(0)