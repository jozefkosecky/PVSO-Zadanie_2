# import required libraries
import cv2
import matplotlib.pyplot as plt

# read input image
img = cv2.imread('left01.jpg')

# convert the input image to a grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# plt.imshow(gray)
# plt.show()

# Find the chess board corners
ret, corners = cv2.findChessboardCorners(gray, (7, 6), None)

# if chessboard corners are detected
if ret == True:
    # Draw and display the corners
    img = cv2.drawChessboardCorners(img, (7, 6), corners, ret)
    cv2.imshow('Chessboard', img)
    cv2.waitKey(0)
cv2.destroyAllWindows()