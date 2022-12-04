import numpy as np
import cv2 as cv

def filter(k, img):
    m = int(np.floor(len(k) / 2))
    n = int(np.floor(len(list(zip(*k)))) / 2)
    rows, cols = img.shape                                                            # no of rows and cols
    filtered_img = np.zeros((rows, cols), np.uint8)                                    # new integer image is created
    for i in range(m, rows - m):
        for j in range(n, cols - n):
            sum = 0
            for x in range(-m, m + 1, 1):
                for y in range(-n, n + 1, 1):
                    sum = sum + (img[i + x, j + y] * k[m + x][n + y])            # sum of product of kernal elements with corresponding image elements
            filtered_img[i, j] = abs(sum)
    return filtered_img

filepath="Ch3-images/goggles.jpg"
img = cv.imread(filepath,0)
k1 = [[0, 1, 0], [1, -4, 1], [0, 1, 0]]
k2= [[0, -1, 0], [-1, 4, -1], [0, -1, 0]]
k3 = [[1, 1, 1], [1, -8, 1], [1, 1, 1]]
k4= [[-1, -1, -1], [-1,8, -1], [-1, -1, -1]]

img1 = filter(k1, img)
img2 = filter(k2, img)
img3 = filter(k3, img)
img4 = filter(k4, img)
imgs=np.hstack((img,img1, img2, img3, img4))
cv.imshow("A)Original image B)Laplacian1 C)Laplacian2 D)Laplacian3 E)Laplacian4",imgs)
cv.waitKey(0)