import cv2
import numpy as np
def detect_shapes(frame,count):
    # Convert the frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Apply GaussianBlur to reduce noise and help with edge detection
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)

    # Use Canny edge detector to find edges
    edges = cv2.Canny(blurred, 50, 150)

    # Find contours in the edged image
    contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Loop over the contours
    path1="C:/Users/yashs/Desktop/video image capture/Test"
    for contour in contours:
        # Approximate the contour to a polygon
        epsilon = 0.04 * cv2.arcLength(contour, True)
        approx = cv2.approxPolyDP(contour, epsilon, True)

        # Get the number of vertices
        vertices = len(approx)

        # Determine the shape based on the number of vertices
        shape_name = None
        if vertices == 4:
            print("true")
            cv2.imwrite((path1+"/%d.jpeg") % count,frame)
            count+=1#if cv2.isContourConvex(approx) else "Quadrilateral"
            pass
        

        # Draw the shape name on the frame
        cv2.putText(frame, shape_name, (approx[0][0][0], approx[0][0][1] - 10),cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

        # Draw the contours and the shape
        cv2.drawContours(frame, [approx], 0, (0, 255, 0), 2)

    return (frame,count)

# Open a video capture object (0 for default camera)
cap = cv2.VideoCapture(0)
count=0
while True:
    # Capture frame-by-frame
    ret, frame = cap.read()
    frames,count=detect_shapes(frame,count)
    # Detect shapes
    processed_frame = frames 

    # Display the resulting frame
    cv2.imshow('Real-time Shape Detection', processed_frame)

    # Break the loop if 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video capture object and close all windows
cap.release()
cv2.destroyAllWindows()
"""
if vertices == 3:
            shape_name = "Triangle"

elif vertices == 5:
            shape_name = "Pentagon"
        else:
            shape_name = "Circle"
            """
