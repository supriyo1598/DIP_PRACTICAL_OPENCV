import numpy as np
import cv2 as cv
filepath="Ch3-images/moon.jpg"
img = cv.imread(filepath,0)
kernal = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]
m = int(np.floor(len(kernal) / 2))
n = int(np.floor(len(list(zip(*kernal)))) / 2)
k = np.sum(kernal)
rows, cols = img.shape  # no of rows and cols
max_img = np.zeros((rows, cols), np.uint8)  # new integer image is created
for i in range(m, rows - m):
    for j in range(n, cols - n):
        max = []
        for x in range(-m, m + 1, 1):
            for y in range(-n, n + 1, 1):
                max.append(img[i + x, j + y])
        max.sort()
        max_img[i, j] = max[8]
imgs=np.hstack((img,max_img))
cv.imshow("A)Original image B)filtered image with 3*3 max filter",imgs)
cv.waitKey(0)