import cv2
import numpy as np
import cv2 as cv
filepath="Ch2-images/child_3.jpg"
img=cv.imread(filepath,0)
rows, cols = img.shape

src_points = np.float32([[0,0], [cols-1,0], [0,rows-1]])
dst_points = np.float32([[0,0], [int(0.6*(cols-1)),0], [int(0.4*(cols-1)),rows-1]])
affine_matrix = cv2.getAffineTransform(src_points, dst_points)
img_output = cv2.warpAffine(img, affine_matrix, (cols,rows))

cv2.imshow('Original Image', img)
cv2.imshow('Affine Transformed Image', img_output)
cv2.waitKey()