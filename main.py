import cv2

inputPath = 'static/img1.jpg'

originalImage = cv2.imread(inputPath)

# ------------Convert image to Grayscale --------------

# Convert the color image to grayscale image


# # ----------------- Convert image to Sketch Image ---------------

# Invert the grayscale image


# Apply Gaussian blur


# Blend the grayscale image and the blurred image using the color dodge blend mode


# Save the sketch image to disk


# Display the converted image

cv2.waitKey(0)

# Display a message indicating that the image has been saved