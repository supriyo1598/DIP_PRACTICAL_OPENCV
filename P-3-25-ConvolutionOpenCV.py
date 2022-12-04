import cv2 as cv
import scipy.signal as sig
import numpy as np
img=np.asarray([[1,2,0,1,2],
              [2,3,1,1,2],
              [1,4,2,2,0],
              [3,2,3,3,0],
              [1,0,0,2,1]
              ],dtype=np.float32)

w=np.asarray([[1,1,1],
              [1,1,2],
              [2,1,1]],dtype=np.float32)
print("kernel::",w)
print("rotated kernel::",cv.flip(w,-1))
print("zero padded same size",cv.filter2D(img, -1, cv.flip(w, -1), borderType=cv.BORDER_CONSTANT))
print("replicated border same size",cv.filter2D(img, -1, cv.flip(w, -1), borderType=cv.BORDER_REPLICATE))
print("reflected border same size",cv.filter2D(img, -1, cv.flip(w, -1), borderType=cv.BORDER_REFLECT))
print("reflected border 101 same size",cv.filter2D(img, -1, cv.flip(w, -1), borderType=cv.BORDER_REFLECT101))
#print("wrapped border 101 same size",cv.filter2D(img, -1, cv.flip(w, -1), borderType=cv.BORDER_WRAP))
# full size convolution
additional_rows=w.shape[0]-1
additional_cols=w.shape[1]-1
img2=cv.copyMakeBorder(img,
                  int((additional_rows+1)/2),
                  int((additional_rows+1)/2),
                  int((additional_cols+1)/2),
                  int((additional_cols+1)/2),
                  borderType=cv.BORDER_CONSTANT,
                  value=int(0)
                  )
print(img2.shape)
print(cv.filter2D(img2,-1,cv.flip(w,-1),borderType=cv.BORDER_CONSTANT))
# valid size convolution
# it is very easy: compute same size convolution and remove
# specific rows and columns
exclude_row=int((w.shape[0]-1)/2)
exclude_col=int((w.shape[1]-1)/2)
result=cv.filter2D(img,-1,cv.flip(w,-1),borderType=cv.BORDER_CONSTANT)
valid_result=result[exclude_row:-exclude_row,exclude_col:-exclude_col]
print(valid_result)
