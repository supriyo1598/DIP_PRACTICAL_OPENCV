import numpy as np
import cv2 as cv
filepath="Ch2-images/child_1.jpg"
img=cv.imread(filepath,0)
print(img.shape)
noisy_imgs=[]
for i in range(10):
    noise=np.random.randint(i,(i+1)*5,[1280,960])
    im_noise=img+noise
    noisy_imgs.append(im_noise)
new_img=np.zeros([1280,960])
for i in range(len(noisy_imgs)):
    new_img+=noisy_imgs[i]
    nimg=noisy_imgs[i].astype(np.uint8)
    cv.imshow("imge",nimg)
    #cv.waitKey(0)
img_f=new_img/10
img_f=img_f.astype(np.uint8)
cv.imshow("Noise Removed",img_f)
cv.waitKey(0)