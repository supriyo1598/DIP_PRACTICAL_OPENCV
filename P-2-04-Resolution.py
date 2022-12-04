import numpy as np
import cv2 as cv
filepath="Ch2-images/child_1.jpg"
img=cv.imread(filepath)
print("Spatial Resolution::",img.shape)
print("Intensity Resolution::",np.min(img),np.max(img))
