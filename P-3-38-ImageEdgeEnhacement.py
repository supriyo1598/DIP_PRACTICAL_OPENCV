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
def blur(kernal, img):
    m = int(np.floor(len(kernal) / 2))
    n = int(np.floor(len(list(zip(*kernal)))) / 2)
    k = np.sum(kernal)
    rows, cols = img.shape                                                            # no of rows and cols
    blurred_img = np.zeros((rows, cols), np.uint8)                                    # new integer image is created
    for i in range(m, rows - m):
        for j in range(n, cols - n):
            sum = 0
            for x in range(-m, m + 1, 1):
                for y in range(-n, n + 1, 1):
                    sum = sum + (img[i + x, j + y] * kernal[m - x][n - y])            # sum of product of kernal elements with corresponding image elements
            sum = sum / k
            blurred_img[i, j] = sum
    return blurred_img


filepath="Ch3-images/armxray.jpg"
img = cv.imread(filepath,0)
k1 = [[0, 1, 0], [1, -4, 1], [0, 1, 0]]
kernal = [[1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1]]
Edge_img = filter(k1, img)
blurred_img = blur(kernal, img)
mask = cv.subtract(img,blurred_img)
improved_edge = cv.add(Edge_img, 3*mask)
imgs=np.hstack((img,Edge_img,blurred_img,mask,improved_edge))
cv.imshow("A)Original image B)Laplacian image C)Blurred image D)Mask image E)(Original + 3*Mask Image)", imgs)
cv.waitKey(0)