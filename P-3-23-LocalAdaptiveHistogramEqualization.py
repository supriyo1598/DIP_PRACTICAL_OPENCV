import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

img=cv.imread("Ch3-images/modelinveil.jpg",0)
clahe = cv.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
cl1 = clahe.apply(img)
cl2=clahe.apply(cl1)
cl3=clahe.apply(cl2)
imgs=np.hstack((img,cl1,cl2,cl3))
cv.imshow("Adaptive local histogram Equalization. A)Image B)Single CLAHE C)Double CLAHE D)Tripple CLAHE",imgs)
cv.waitKey(0)
