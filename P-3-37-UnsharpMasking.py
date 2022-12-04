import numpy as np
import cv2 as cv

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

filepath="Ch3-images/intensity-level-slicing.jpg"
img = cv.imread(filepath,0)
kernal = [[1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1]]
blurred_img = blur(kernal, img)
mask = cv.subtract(img,blurred_img)
unsharped_img = cv.add(img,1*mask)
unsharped_img2 = cv.add(img,2*mask)
unsharped_img3 = cv.add(img,3*mask)
imgs1=np.hstack((img,blurred_img,mask))
imgs2=np.hstack((unsharped_img, unsharped_img2, unsharped_img3))
imgs3=np.vstack((imgs1,imgs2))
cv.imshow("A)Original image B)Blurred image C)Mask image D)unsharped k=1 E)unsharped k=2 F)unsharped k=3",imgs3)
cv.waitKey(0)