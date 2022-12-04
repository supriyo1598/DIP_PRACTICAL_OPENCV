import cv2 as cv
filepath="Ch2-images/child_1.jpg"
img=cv.imread(filepath,0)
print(img)
print(img.shape)
print(img.dtype)
print(img.size)
print(img[0,:])
print(img[:,0])
print(img[0,0])