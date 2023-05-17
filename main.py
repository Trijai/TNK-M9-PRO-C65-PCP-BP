# Importing Library
import cv2

# Define the input path
inputPath = 'static/img1.jpg'

# Load the color image
orignalImage = cv2.imread(inputPath)

# ------------Convert image to Grayscale --------------

# Convert the color image to grayscale image
grayscaleImage = cv2.cvtColor(orignalImage, cv2.COLOR_BGR2GRAY)

# # ----------------- Convert image to Sketch Image ---------------

# Invert the grayscale image


# Apply Gaussian blur


# Blend the grayscale image and the blurred image using the color dodge blend mode


# Save the sketch image to disk
outputPath = 'converted/sketch.png'

# Display the converted image


# Display a message indicating that the image has been saved
print('Converted Sketch image saved to disk: ' + outputPath)
