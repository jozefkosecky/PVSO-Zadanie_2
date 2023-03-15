import cv2
import matplotlib.pyplot as plt
import numpy as np

import keyboard as keyboard

# create an instance of cv2.VideoCapture() to capture video from the default camera (notebook camera)
cap = cv2.VideoCapture(0)

# set the exposure, image format, and white balance of the camera (if applicable)
# you may need to adjust these settings based on your camera
cap.set(cv2.CAP_PROP_EXPOSURE, 0.1)
# cap.set(cv2.CAP_PROP_CONVERT_RGB, 0.1)
cap.set(cv2.CAP_PROP_AUTO_WB, 1)

counter = 0
imageName = "camera"

while counter != 1:
    # capture a frame from the camera
    ret, frame = cap.read()

    # resize the frame (if desired)
    frame = cv2.resize(frame, (600, 600))

    # display the frame in a window
    cv2.imshow("test", frame)

    key = cv2.waitKey(1)

    if key == ord(' '):
        filename = imageName + "{}.jpg".format(counter)
        cv2.imwrite(filename, frame)
        counter += 1
        print("Saved image to {}".format(filename))

    elif key == ord('q'):
        break
