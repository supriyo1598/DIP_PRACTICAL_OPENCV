import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt
levels=np.array([0,1,2,3,4,5,6,7])
input_image=np.array([790,1023,850,656,329,245,122,81])
output_img=np.zeros(len(input_image))
pdfs=input_image/4096
cdfs=np.zeros([len(pdfs)])
for i in range(len(pdfs)):
    for j in range(0,i+1):
        cdfs[i]+=pdfs[j]
cdfs=7*cdfs
cdfs=np.round(cdfs)
for i in range(len(input_image)):
     output_img[i]+=np.sum(input_image[cdfs==i])
np.set_printoptions(precision=2)
print("Input::",input_image)
print("pdfs ::",pdfs)
print("cdfs ::",cdfs)
print("output::",output_img)
