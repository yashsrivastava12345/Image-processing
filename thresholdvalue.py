"""import cv2
import matplotlib.pyplot as plt

# Read the image in grayscale
image = cv2.imread('C:/Users/yashs/Desktop/video image capture/plates/rec.jpg', cv2.IMREAD_GRAYSCALE)

# Plot histogram
plt.hist(image.flatten(), bins=256, range=[0,256])
plt.show()
"""

import cv2
import numpy as np
import matplotlib.pyplot as plt

# Read the image in grayscale
image = cv2.imread('C:/Users/yashs/Desktop/video image capture/plates/rec.jpg', cv2.IMREAD_GRAYSCALE)

# Calculate histogram
hist, bins = np.histogram(image.flatten(), 256, [0, 256])

# Calculate cumulative distribution function (CDF)
cdf = hist.cumsum()

# Normalize CDF
cdf_normalized = cdf * hist.max() / cdf.max()

# Plot histogram and CDF
plt.plot(cdf_normalized, color='b')
plt.hist(image.flatten(), 256, [0, 256], color='r')
plt.xlim([0, 256])
plt.legend(('CDF', 'Histogram'), loc='upper left')
plt.show()

# Apply Otsu's thresholding
_, thresholded_image = cv2.threshold(image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

# Display the original and thresholded images
cv2.imshow('Original Image', image)
cv2.imshow('Thresholded Image', thresholded_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
