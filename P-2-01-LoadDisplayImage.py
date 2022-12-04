import cv2 as cv
filepath="Ch2-images/child_1.jpg"
img=cv.imread(filepath)
cv.imshow("The child",img)
cv.waitKey(0)
