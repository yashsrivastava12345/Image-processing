import cv2
import os
import numpy as np
path=input("Enter the path and name of the video with its formate: ")
vidcap = cv2.VideoCapture(path)
success,image=vidcap.read()
count=1
n=1
oppath=input("Enter the output path: ")
directory = "Normal_Image"
directory2 = "Gray_scale_Iamge"
directory3 = "Gray_scale_Iamge_Inbuilt"
parent_dir = oppath
path1 = os.path.join(parent_dir, directory)
path2 = os.path.join(parent_dir, directory2)
path3 = os.path.join(parent_dir, directory3)
os.mkdir(path1)
os.mkdir(path2)
os.mkdir(path3)
print(path1)
print(path2)
print(path3)
while vidcap.isOpened():
    success,image=vidcap.read()
    invert_img=cv2.bitwise_not(image)
    cv2.imwrite((path1+"/%d.jpeg") % count,image)
    a,b,c=image.shape
    x=image
    for i in range(0,c):
        for j in range(0,b):
            for k in range(0,a):
                x[k,j,i]=255-image[k,j,i]
                pass
            pass
        pass
    cv2.imwrite((path3+"/Gray"+"%d.jpeg") % count,invert_img)
    cv2.imwrite((path2+"/MyGray"+"%d.jpeg") % count,x)
    print("saved image number - ",n)
    n+=1
    count+=1
