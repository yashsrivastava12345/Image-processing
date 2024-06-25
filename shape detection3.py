import cv2
import numpy as np

def detect_and_draw_shapes(frame):
    # Convert the frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Apply GaussianBlur to reduce noise and help with edge detection
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)

    # Use Canny edge detector to find edges
    edges = cv2.Canny(blurred, 50, 150)

    # Find contours in the edged image
    contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

    # Loop over the contours
    for contour in contours:
        # Draw the contours
        cv2.drawContours(frame, [contour], 0, (0, 255, 0), 2)

            # Draw vertices of the polygon
        if (len(contour)==4):
            for point in contour:
                x, y = point[0]
                cv2.circle(frame, (x, y), 3, (0, 0, 255), -1)  # Draw a red circle at each vertex

    return frame

# Open a video capture object (0 for default camera)
cap = cv2.VideoCapture(0)

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Detect and draw shapes
    processed_frame = detect_and_draw_shapes(frame)

    # Display the resulting frame
    cv2.imshow('Exact Polygon Vertices', processed_frame)

    # Break the loop if 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video capture object and close all windows
cap.release()
cv2.destroyAllWindows()
