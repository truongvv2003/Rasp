import cv2
import os

path = r'D:\PBL4\pic\aHalf.png'
path1 = r'D:\PBL4\pic'

img = cv2.imread(path)
cv2.imshow('1/2',img)


R, G, B = cv2.split(img);

cv2.imshow('Red',R);
cv2.imshow('Blue',B);
cv2.imshow('Green',G);

cv2.waitKey()
# return true cv.imwrite if it save sucessfully and os.chdir is function to change direction before it saved
#os.chdir(path1)
#if(cv2.imwrite("aHalf2.jpg",img)):
#    print("Thanh cong")




