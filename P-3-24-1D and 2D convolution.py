import cv2 as cv
import numpy as np
filepath="Ch3-images/moon.jpg"
img = cv.imread(filepath,0)
rows,cols = img.shape                                               #no of rows and cols
kernal = [[2, 2, 2], [4, 4, 4], [2, 2, 2]]                          #2-D kernal/filter
m = int(np.floor(len(kernal)/2))
n = int(np.floor(len(list(zip(*kernal))))/2)
blurred_img = np.zeros((rows,cols), np.uint8)                       #new integer image is created
for i in range(m, rows - m):
    for j in range(n, cols - n):
        sum = 0
        for x in range(-m, m+1, 1):
            for y in range(-n, n+1, 1):
                sum = sum + (img[i + x, j + y] * kernal[m - x][n - y])          #sum of product of kernal elements with corresponding image elements
        sum = sum / 24                                                          # 24 is the scaling factor which is sum of kernal elements
        blurred_img[i, j] = sum

#Blurring by 1-D kernal
kernal2 = [1, 2, 4, 2, 1]
k = np.sum(kernal2)
blurred_img2 = np.zeros((rows,cols), np.uint8)
n = int(np.floor(len(list(zip(*kernal))))/2)
for i in range(rows):
    for j in range(n, cols-n):
        sum = 0
        for y in range(-n, n+1, 1):
            sum = sum + (img[i, j + y] * kernal2[n - y])                        #sum of product of kernal elements with corresponding image elements
        sum = sum / k                                                           # 24 is the scaling factor which is sum of kernal elements
        blurred_img2[i, j] = sum


imgs=np.hstack((img,blurred_img,blurred_img2))
cv.imshow("Color:: A)Original image B)Blurred image with 3*3 2-D filter C)Blurred image with 1*5 1-D filter ",imgs)
cv.waitKey(0)