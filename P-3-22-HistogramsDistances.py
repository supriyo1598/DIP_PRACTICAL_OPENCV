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
distance1 = distance2 = distance3 = 0
for i in range(256):
    if H1[i] == 0:
        distance1 = distance1 + 0
    else:
        distance1 = distance1 + (((H1[i] - H2[i]) ** 2)/ H1[i])
    distance2 = distance2 + (min(H1[i], H2[i]))
    distance3 = distance3 + (H1[i] * H2[i]) ** 0.5
distance3 = np.sqrt(1 - (distance3 / np.sqrt(H1_mean * H2_mean * (len(H1) ** 2))))
print("Chi-Square Distance = ", distance1)
print("Intersection based Distance = ", distance2)
print("Bhattacharyya Distance = ", distance3)



