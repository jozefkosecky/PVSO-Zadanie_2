# import required libraries
import numpy as np
import cv2 as cv
import glob

chessboardSize = (7, 6)
frameSize = (398, 454)

# termination criteria
criteria = (cv.TERM_CRITERIA_EPS + cv.TERM_CRITERIA_MAX_ITER, 30, 0.001)

# prepare object points, like (0,0,0), (1,0,0), (2,0,0) ....,(6,5,0)
objp = np.zeros((chessboardSize[0] * chessboardSize[1], 3), np.float32)
objp[:,:2] = np.mgrid[0:chessboardSize[0], 0:chessboardSize[1]].T.reshape(-1, 2)

# Arrays to store object points and image points from all the images.
objpoints = [] # 3d point in real world space
imgpoints = [] # 2d points in image plane.

# read input image
img = cv.imread('chessboard.jpg')

# convert the input image to a grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

# plt.imshow(gray)
# plt.show()

# Find the chess board corners
ret, corners = cv.findChessboardCorners(gray, (7, 6), None)

# if chessboard corners are detected
if ret == True:
    # Draw and display the corners
    objpoints.append(objp)
    corners2 = cv.cornerSubPix(gray, corners, (11, 11), (-1, -1), criteria)
    imgpoints.append(corners2)

    # Draw and display the corners
    cv.drawChessboardCorners(img, chessboardSize, corners2, ret)
    cv.imshow('img', img)
    cv.imshow('Chessboard', img)
    cv.waitKey(0)
cv.destroyAllWindows()


img = cv.imread('chessboard.jpg')
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
ret, cameraMatrix, dist, rvecs, tvecs = cv.calibrateCamera(objpoints, imgpoints, gray.shape[::-1], None, None)
print("cameraMatrix:", cameraMatrix)
print("fx:", cameraMatrix.item(0, 0), "fy:", cameraMatrix.item(1, 1))
print("cx:", cameraMatrix.item(0, 2), "cy:", cameraMatrix.item(1, 2))
# print("Distortion parameters:", dist)
# print("Rotation vectors:", rvecs)
# print("Translation vectors:", tvecs)

############ Undistortion ######################


cv.imshow("camera14.jpg", img)
h,  w = img.shape[:2]
print("image size", img.shape[::-1])
print("h", h)
print("w", w)
newCameraMatrix, roi = cv.getOptimalNewCameraMatrix(cameraMatrix, dist, (w, h), 1, (w, h))

# Undistort
dst = cv.undistort(img, cameraMatrix, dist, None, newCameraMatrix)
# crop the image
x, y, w, h = roi
print("roi", roi)
dst = dst[y:y + h, x:x + w]
cv.imwrite('calibResult1.png', dst)
# img2 = cv.imread('calibResult1.jpg')
# cv.imshow("calibResult1.jpg", img2)