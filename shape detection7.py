# Python code to detect an arrow (seven-sided shape) from an image. 
import numpy as np 
import cv2 

# Reading image 
img2 = cv2.imread('C:/Users/yashs/Desktop/video image capture/plates/2.jpg', cv2.IMREAD_COLOR) 

# Reading same image in another variable and 
# converting to gray scale. 
img = cv2.imread('C:/Users/yashs/Desktop/video image capture/plates/2.jpg', cv2.IMREAD_GRAYSCALE) 

# Converting image to a binary image 
# (black and white only image). 
_,threshold = cv2.threshold(img, 224, 252, cv2.THRESH_BINARY_INV) 

# Detecting shapes in image by selecting region 
# with same colors or intensity. 
contours,_=cv2.findContours(threshold, cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
print(threshold,"\n",contours,"\n",_)
# Searching through every region selected to 
# find the required polygon. 
for cnt in contours : 
	area = cv2.contourArea(cnt) 

	# Shortlisting the regions based on there area. 
	if area > 400: 
		approx = cv2.approxPolyDP(cnt, 0.009 * cv2.arcLength(cnt, True), True) 

		# Checking if the no. of sides of the selected region is 7. 
		if(len(approx) == 4): 
			cv2.drawContours(img2, [approx], 0, (255, 0, 255), 1) 

# Showing the image along with outlined arrow. 
cv2.imwrite("testimage.jpeg",img2)
cv2.imshow('image2', img2) 

# Exiting the window if 'q' is pressed on the keyboard. 
if cv2.waitKey(0) & 0xFF == ord('q'): 
	cv2.destroyAllWindows() 
