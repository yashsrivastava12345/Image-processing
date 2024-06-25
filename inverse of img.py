#F:\New folder (19)\imageprocessing workshop 29-04-23
#'C:/Users/yashs/Desktop/video image capture/plates/2.jpg'
import cv2
import numpy as np
import matplotlib.pyplot as plt
oppath=path=r"""C:\Users\yashs\Desktop\video image capture"""
image_name="IMG_20210415_014254.jpg"
x=cv2.imread('C:/Users/yashs/Desktop/video image capture/plates/r.jpg')#path+"\\"+image_name)
a,b,c=x.shape
#e=f=cv2.resize(x,(a,b))
#e=cv2.cvtColor(e,cv2.COLOR_BGR2GRAY)
n=0
for i in range(0,c):
    for j in range(0,b):
        for k in range(0,a):
            x[k,j,i]=255-x[k,j,i]
y=cv2.resize(x,(b,a))
z=cv2.cvtColor(y,cv2.COLOR_BGR2GRAY)
#z[z[:,:]<180]=0
#d=e[::]/z
#cv2.imshow("My first image",np.concatenate((e,z),1))
#cv2.waitKey(0)
#cv2.destroyAllWindows()
cv2.imwrite((oppath+"/%d.jpeg") %n,y)
cv2.imshow("My first image",y)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imwrite("Inverted imageRedinv.jpeg",y)
plt.hist(y.flatten(), bins=256, range=[0,256])
plt.show()
"""fig,((jj,kk),(jj1,kk1))=plt.subplots(nrows=2,ncols=2)
jj=plt.hist(e,e)
kk=plt.hist(z,z)
jj1=plt.hist(f,f)
kk1=plt.hist(y,y)
fig.tight_layout()
plt.show()"""
