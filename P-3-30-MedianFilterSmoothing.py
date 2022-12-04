import numpy as np
import cv2 as cv
filepath="Ch3-images/moon.jpg"
img = cv.imread(filepath,0)
kernal = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]
m = int(np.floor(len(kernal) / 2))
n = int(np.floor(len(list(zip(*kernal)))) / 2)
k = np.sum(kernal)
rows, cols = img.shape  # no of rows and cols
median_img = np.zeros((rows, cols), np.uint8)  # new integer image is created
for i in range(m, rows - m):
    for j in range(n, cols - n):
        median = []
        for x in range(-m, m + 1, 1):
            for y in range(-n, n + 1, 1):
                median.append(img[i + x, j + y])
        median.sort()
        median_img[i, j] = median[4]
imgs=np.hstack((img,median_img))
cv.imshow("A)Original image B)filtered image with 3*3 median filter",imgs)
cv.waitKey(0)