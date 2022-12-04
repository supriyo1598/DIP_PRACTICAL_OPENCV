import cv2 as cv
filepath="Ch2-images/cameraman.jpg"
img=cv.imread(filepath,0)
row=int(input("Enter x-coordinate of reference pixel::"))
col=int(input("Enter y-coordinate of reference pixel::"))
for r in range(row-1,row+2):
    for c in range(col-1,col+2):
        print(r,c,img[r,c])