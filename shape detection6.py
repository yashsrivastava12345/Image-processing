import cv2
import numpy as np

# Define a function to detect quadrilaterals
def detect_quadrilaterals(frame):
  # Convert the frame to grayscale
  gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

  # Blur the image to reduce noise
  blurred = cv2.GaussianBlur(gray, (5, 5), 0)

  # Detect edges in the blurred image
  edges = cv2.Canny(blurred, 100, 200)

  # Find contours in the edge map
  contours, hierarchy = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

  # Filter the contours to only include quadrilaterals
  quadrilaterals = []
  for contour in contours:
    approx = cv2.approxPolyDP(contour, 0.02, True)
    if len(approx) == 4:
        print("True")
        quadrilaterals.append(approx)

  return quadrilaterals

# Define a function to draw quadrilaterals on an image
def draw_quadrilaterals(frame, quadrilaterals):
  for quadrilateral in quadrilaterals:
    cv2.drawContours(frame, [quadrilateral], 0, (0, 0, 255), 2)

# Create a video capture object
cap = cv2.VideoCapture(0)

# Loop until the user presses the Esc key
while True:
  # Capture a frame
  ret, frame = cap.read()

  # Detect quadrilaterals in the frame
  quadrilaterals = detect_quadrilaterals(frame)

  # Draw quadrilaterals on the frame
  draw_quadrilaterals(frame, quadrilaterals)

  # Display the frame
  cv2.imshow('Quadrilateral Detection', frame)

  # Press the Esc key to exit
  if cv2.waitKey(1) & 0xFF == 27:
    break

# Release the video capture object
cap.release()

# Close all windows
cv2.destroyAllWindows()
