import numpy as np
import cv2 as cv
filepath="Ch3-images/holes.png"
img = cv.imread(filepath,0)
rows, cols = img.shape      # no of rows and cols
print(rows*cols)
#img2 = np.zeros((rows, cols), np.uint8) #why this statement produces only left edges
img2 = np.zeros((rows, cols), np.float) # why this statement creates both sided edges
# for i in range(0,256):
#     a=np.where(img==i)
#     print(len(a[0]))
#32072=28134+3938
for i in range(rows):
    for j in range(cols-1):
        diff=np.subtract(img[i,j+1],img[i,j])
        if(diff!=0):
            print(diff)
            img2[i,j] = diff

print(img2)
imgs=np.hstack((img,img2))
cv.imshow("A)Original image B)first order difference",imgs)
cv.waitKey(0)