import cv2 as cv
img=cv.imread("ch2-images/cameraman.jpg")
img=img[:,:,0]
print("Original Pixel Value at location (10,10):",img[10,10])
img_a=img+10
print("Updated Pixel Value at location (10,10):",img_a[10,10])
img_b=img-10
print("Updated Pixel Value at location (10,10):",img_b[10,10])
img_c=img*10
print("Updated Pixel Value at location (10,10):",img_c[10,10])
img_d=img/10
print("Updated Pixel Value at location (10,10):",img_d[10,10])
