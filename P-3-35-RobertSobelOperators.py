import numpy as np
import cv2 as cv

def filter(kx, ky, img):
    m = int(np.floor(len(kx) / 2))
    n = int(np.floor(len(list(zip(*kx)))) / 2)
    rows, cols = img.shape                                                            # no of rows and cols
    filtered_img = np.zeros((rows, cols), np.uint8)                                    # new integer image is created
    for i in range(m, rows - m):
        for j in range(n, cols - n):
            sumx = sumy = 0
            for x in range(-m, m + 1, 1):
                for y in range(-n, n + 1, 1):
                    sumx = sumx + (img[i + x, j + y] * kx[m + x][n + y])            # sum of product of kernal elements with corresponding image elements
                    sumy = sumy + (img[i + x, j + y] * ky[m + x][n + y])
            filtered_img[i, j] = abs(sumx) + abs(sumy)
    return filtered_img

filepath="Ch3-images/goggles.jpg"
img = cv.imread(filepath,0)
y = [[0, 0, 0], [0, -1, 0], [0, 0, 1]]
x = [[0, 0, 0], [0, 0, -1], [0, 1, 0]]
robert = filter(x, y, img)
y = [[-1, -2, -1], [0, 0, 0], [1, 2, 1]]
x = [[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]]
sobel = filter(x, y, img)
imgs=np.hstack((img,robert, sobel))
cv.imshow("A)Original image B)Robert operator C)Sobel Filter",imgs)
cv.waitKey(0)