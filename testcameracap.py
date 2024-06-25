import cv2
import os
cam = cv2.VideoCapture(0)
cv2.namedWindow("Frame capture")
oppath=input("Enter the output path: ")
directory = "Normal_Image"
directory2 = "Gray_scale_Iamge"
parent_dir = oppath
path1 = os.path.join(parent_dir, directory)
path2 = os.path.join(parent_dir, directory2)
os.mkdir(path1)
os.mkdir(path2)
count=1
n=1
while True:
    ret, frame = cam.read()
    if not ret:
        print("Failed to grab frame")
        break
    cv2.imshow("Frame capture", frame)

    k = cv2.waitKey(1)
    if (k%256 == 27):
        print("Escape hit, closing...")
        break
    else:
        invert_img=cv2.bitwise_not(frame)
        cv2.imwrite((path1+"/%d.jpeg") % count,frame)
        cv2.imwrite((path2+"/Gray"+"%d.jpeg") % count,invert_img)
        print("saved image number - ",n)
        n+=1
        count+=1
cam.release()
cv2.destroyAllWindows()
"""img_name = f"opencv_frame_{img_counter}.png"
        cv2.imwrite(img_name, frame)
        print(f"{img_name} written!")
        img_counter += 1"""

"""
a,b,c=frame.shape
        x=frame
        for i in range(0,c):
            for j in range(0,b):
                for k in range(0,a):
                    x[k,j,i]=255-frame[k,j,i]
                    pass
                pass
            pass"""
