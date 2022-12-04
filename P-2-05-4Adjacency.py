import cv2 as cv
filepath="Ch2-images/cameraman.jpg"
img=cv.imread(filepath,0)
row=int(input("Enter x-coordinate of reference pixel::"))
col=int(input("Enter y-coordinate of reference pixel::"))
print(img[row-1,col])
print(img[row+1,col])
print(img[row,col-1])
print(img[row,col+1])