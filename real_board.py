import numpy as np
import cv2 as cv
import glob
import matplotlib.pyplot as plt
# termination criteria
criteria = (cv.TERM_CRITERIA_EPS + cv.TERM_CRITERIA_MAX_ITER, 30, 0.001)
# prepare object points, like (0,0,0), (1,0,0), (2,0,0) ....,(6,5,0)
objp = np.zeros((5*7,3), np.float32)
objp[:,:2] = np.mgrid[0:7,0:5].T.reshape(-1,2)
# Arrays to store object points and image points from all the images.
objpoints = [] # 3d point in real world space
imgpoints = [] # 2d points in image plane.

images = glob.glob('*.jpg')

for fname in images:
    img = cv.imread(fname)
    cropped_image = img[75:475, 100:600]
    gray_image = cv.cvtColor(cropped_image, cv.COLOR_BGR2GRAY)

    # plt.imshow(cropped_image, cmap="gray", vmin=0, vmax=255)
    # plt.show()
    # Find the chess board corners
    ret, corners = cv.findChessboardCorners(gray_image, (7, 5), None)
    # If found, add object points, image points (after refining them)
    if ret == True:
        print("HEj")
        objpoints.append(objp)
        corners2 = cv.cornerSubPix(gray_image, corners, (11, 11), (-1, -1), criteria)
        imgpoints.append(corners2)
        # Draw and display the corners
        cv.drawChessboardCorners(cropped_image, (7, 5), corners2, ret)
        cv.imshow('img', cropped_image)
        cv.waitKey(500)

        ret, mtx, dist, rvecs, tvecs = cv.calibrateCamera(objpoints, imgpoints, gray_image.shape[::-1], None, None)
        print(mtx)

        cv.waitKey(0)
cv.destroyAllWindows()