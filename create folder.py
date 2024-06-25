# Python program to explain os.mkdir() method 
	
# importing os module 
import os 
	
# Directory 
directory = "GeeksForGeeks"
	
# Parent Directory path 
parent_dir = "C:/Users/yashs/Desktop/video image capture/New folder"
	
# Path 
path = os.path.join(parent_dir, directory) 
	
# Create the directory 
# 'GeeksForGeeks' in 
# '/home / User / Documents' 
os.mkdir(path) 
print("Directory '% s' created" % directory) 
	
# if directory / file that 
# is to be created already 
# exists then 'FileExistsError' 
# will be raised by os.mkdir() method 
	
# Similarly, if the specified path 
# is invalid 'FileNotFoundError' Error 
# will be raised 

