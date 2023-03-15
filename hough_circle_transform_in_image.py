import cv2
import numpy as np
import glob

# Load the image
img = cv2.imread('gulicky.jpg')

# Convert the image to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Apply Gaussian blur to reduce noise
gray = cv2.GaussianBlur(gray, (9, 9), 2)

edges = cv2.Canny(gray, 50, 100, apertureSize = 3)

cv2.imshow("edges", edges)

# Detect circles using Hough Circle Transform
circles = cv2.HoughCircles(edges, cv2.HOUGH_GRADIENT, 1, 20, param1=100, param2=30, minRadius=0, maxRadius=0)
print(circles)
# If circles are detected, draw them on the image
if circles is not None:
    circles = circles[0]
    for circle in circles:
        center = (int(circle[0]), int(circle[1]))
        radius = int(circle[2])
        cv2.circle(img, center, radius, (0, 255, 0), 2)
        cv2.circle(img, center, 2, (0, 0, 255), 3)

# Show the resulting image
cv2.imshow("image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Define the Hough Circle Transform parameters
dp = 1
minDist = 50
param1 = 200
param2 = 100
minRadius = 0
maxRadius = 0

images = glob.glob('*.jpg')

for image in images:
    print(image)
    # Convert the image to grayscale
    img = cv2.imread(image)
    # cropped_image = img[75:475, 100:600]
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Apply Gaussian blur to reduce noise
    gray = cv2.GaussianBlur(gray, (9, 9), 2)

    # Detect circles using Hough Circle Transform
    circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, dp, minDist, param1=param1, param2=param2, minRadius=minRadius,
                               maxRadius=maxRadius)

    print(image, "\n", circles, "\n----------------------------")
    # If circles are detected, draw them on the frame
    if circles is not None:
        circles = circles[0]
        for circle in circles:
            center = (int(circle[0]), int(circle[1]))
            radius = int(circle[2])
            cv2.circle(img, center, radius, (0, 255, 0), 2)

        cv2.imshow(image, img)

cv2.waitKey(0)
cv2.destroyAllWindows()
