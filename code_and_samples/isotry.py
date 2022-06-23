import cv2
#import numpy 
import numpy as np
im=cv2.imread("i (21).jpg")


iimm=cv2.ximgproc.anisotropicDiffusion(im,0.125,0.04,1)
cv2.imwrite("s_4_1(22).jpg",iimm)
iimm=cv2.ximgproc.anisotropicDiffusion(im,0.125,0.04,5)
cv2.imwrite("s_4_5(22).jpg",iimm)
iimm=cv2.ximgproc.anisotropicDiffusion(im,0.125,0.04,10)
cv2.imwrite("s_4_10(22).jpg",iimm)
iimm=cv2.ximgproc.anisotropicDiffusion(im,0.125,0.9,1)
cv2.imwrite("s_90_1(22).jpg",iimm)
iimm=cv2.ximgproc.anisotropicDiffusion(im,0.125,0.9,5)
cv2.imwrite("s_90_5(22).jpg",iimm)
iimm=cv2.ximgproc.anisotropicDiffusion(im,0.125,0.9,10)
cv2.imwrite("s_90_10(22).jpg",iimm)

cv2.imshow('i',iimm)
# 
cv2.waitKey(0)
cv2.destroyAllWindows()