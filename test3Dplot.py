import matplotlib.pyplot as plt
import cv2
from mpl_toolkits.mplot3d import axes3d

plt.style.use('_mpl-gallery')
x=cv2.imread('C:/Users/yashs/Desktop/video image capture/hello_level.jpeg')#path+"\\"+image_name)
a,b,c=x.shape
print(a,b,c)
"""
X=Y=Z=[]
for i in range(0,c):
    for j in range(0,b):
        for k in range(0,a):
            if (c==0):
                X.append(x[k,j,i])
                pass
            elif (c==1):
                Y.append(x[k,j,i])
                pass
            else:
                Z.append(x[k,j,i])
# Make data
#X, Y, Z = axes3d.get_test_data(0.05)

# Plot
fig, ax = plt.subplots(subplot_kw={"projection": "3d"})
ax.plot_wireframe(X, Y, Z, rstride=10, cstride=10)

ax.set(xticklabels=[],
       yticklabels=[],
       zticklabels=[])

plt.show()
"""
