import cv2
import numpy as np

def detect_and_draw_quadrilaterals(frame):
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
        # Filter contours based on the number of vertices
        if len(contour) == 4:
            # Calculate the bounding rectangle
            x, y, w, h = cv2.boundingRect(contour)

            # Calculate the aspect ratio of the bounding rectangle
            aspect_ratio = float(w) / h

            # Adjust this threshold based on your specific needs
            aspect_ratio_threshold = 0.8

            # Filter out contours with aspect ratios outside the threshold
            if 0.8 <= aspect_ratio <= 1.2:
                # Draw the contours
                cv2.drawContours(frame, [contour], 0, (0, 255, 0), 2)

                # Draw vertices of the quadrilateral
                for point in contour:
                    print("True")
                    x, y = point[0]
                    cv2.circle(frame, (x, y), 3, (0, 0, 255), -1)  # Draw a red circle at each vertex

    return frame

# Open a video capture object (0 for default camera)
cap = cv2.VideoCapture(0)

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Detect and draw quadrilaterals
    processed_frame = detect_and_draw_quadrilaterals(frame)

    # Display the resulting frame
    cv2.imshow('Exact Quadrilaterals', processed_frame)

    # Break the loop if 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video capture object and close all windows
cap.release()
cv2.destroyAllWindows()
