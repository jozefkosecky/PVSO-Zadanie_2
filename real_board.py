import numpy as np
import cv2 as cv
import glob
import matplotlib.pyplot as plt
# termination criteria
criteria = (cv.TERM_CRITERIA_EPS + cv.TERM_CRITERIA_MAX_ITER, 30, 0.001)
# prepare object points, like (0,0,0), (1,0,0), (2,0,0) ....,(6,5,0)
objp = np.zeros((6*7,3), np.float32)
objp[:,:2] = np.mgrid[0:7,0:6].T.reshape(-1,2)
# Arrays to store object points and image points from all the images.
objpoints = [] # 3d point in real world space
imgpoints = [] # 2d points in image plane.

images = glob.glob('*.jpg')

for fname in images:
    img = cv.imread(fname)
    gray_image = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    plt.imshow(gray_image, cmap="gray", vmin=0, vmax=255)
    plt.show()
    # Find the chess board corners
    ret, corners = cv.findChessboardCorners(gray_image, (8, 6), None)
    # If found, add object points, image points (after refining them)
    if ret == True:
        print("HEj")
        objpoints.append(objp)
        corners2 = cv.cornerSubPix(gray_image, corners, (11, 11), (-1, -1), criteria)
        imgpoints.append(corners2)
        # Draw and display the corners
        cv.drawChessboardCorners(img, (7, 6), corners2, ret)

        ret, mtx, dist, rvecs, tvecs = cv.calibrateCamera(objpoints, imgpoints, gray_image.shape[::-1], None, None)

        cv.imshow('img', img)
        cv.waitKey(500)

cv.destroyAllWindows()