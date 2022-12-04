import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt
def histogram(img):
    bins = np.zeros(256)
    for i in range(256):
        bins[i] = np.sum(img == i)
    print(bins.astype(np.uint8))
    levels = range(256)
    plt.plot(levels, bins)
    plt.show()
    return bins


img1 = cv.imread("Ch3-images/moon.jpg", 0)
img2 = cv.imread("Ch3-images/armxray.jpg", 0)
H1 = histogram(img1)
H2 = histogram(img2)
H1_mean = (np.sum(H1)/len(H1))
H2_mean = (np.sum(H2)/len(H2))
sum1 = sum2 = sum3 = 0
for i in range(256):
    sum1 = sum1 + ((H1[i]-H1_mean)*(H2[i]-H2_mean))
    sum2 = sum2 + (H1[i] - H1_mean) ** 2
    sum3 = sum3 + (H2[i] - H2_mean) ** 2
    result = sum1 / (sum2 * sum3) ** 0.5
print("distance = ",result)

