import cv2 as cv
import numpy as np
filepath="Ch2-images/child_1.jpg"
#img=cv.imread(filepath,0)
img=np.asarray([[1,1,1,1],[2,2,2,2],[3,3,3,3],[4,4,4,4]])
height,width=img.shape
new_img=np.zeros([height,width])
padded_img=np.zeros([height+2,width+2])
padded_img[1:-1,1:-1]=img
def get8Adj(row,col):
    adj8=[]
    for r in range(row-1,row+2):
        for c in range(col-1,col+2):
            adj8.append([r,c])
    return adj8
def getAverage(img,n8):
    sum=0
    for i in range(len(n8)):
        r,c=n8[i]
        sum+=img[r,c]
    return sum/9

def getMedian(img,n8):
    #implement it yourself
    pass

def getMode(img,n8):
    #implement it yourself
    pass

for i in range(height):
     for j in range(width):
         n8=get8Adj(i+1,j+1)
         new_img[i,j]= getAverage(padded_img,n8)

np.set_printoptions(2)
print(new_img)
new_img=new_img.astype(np.uint8)
cv.imshow("test",new_img)
cv.waitKey(0)