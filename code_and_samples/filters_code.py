import cv2 
import numpy as np
from glob import glob
from matplotlib import pyplot as plt



img_paths=glob('*.jpg') #get paths of all all images
for path in img_paths:
    im=cv2.imread(path)
    bb=cv2.GaussianBlur(im,(5,5),0)
    b1=cv2.bilateralFilter(im,5,5,5)
    iimm=cv2.ximgproc.anisotropicDiffusion(im,0.1,0.05,2)
    plt.subplot(2, 2, 1)
    plt.imshow(im)
    plt.title('original')
    plt.subplot(2, 2, 2)
    plt.imshow(bb)
    plt.title('gaussian')
    plt.subplot(2, 2, 3)
    plt.imshow(b1)
    plt.title('bilateral')
    plt.subplot(2, 2, 4)
    plt.imshow(iimm)
    plt.title('anisotropic')
    plt.show()
    cv2.waitKey(0)                 

   

cv2.waitKey(0)
cv2.destroyAllWindows()