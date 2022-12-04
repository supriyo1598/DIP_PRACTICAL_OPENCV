import cv2 as cv
import numpy as np

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
filepath="Ch3-images/moon.jpg"
img = cv.imread(filepath,0)
kernal1 = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]
kernal2 = [[1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1]]
kernal3 = [[1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1]]
blurred_img1 = blur(kernal1, img)
blurred_img2 = blur(kernal2, img)
blurred_img3 = blur(kernal3, img)
imgs=np.hstack((img,blurred_img1,blurred_img2,blurred_img3))
cv.imshow("Color:: A)Original image B)3*3 Box filter C)5*5 Box filter D)7*7 Box filter ",imgs)
cv.waitKey(0)