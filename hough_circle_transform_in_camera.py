import cv2

# Initialize video capture from default camera
cap = cv2.VideoCapture(0)

# Set camera resolution
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

# Define the Hough Circle Transform parameters
dp = 1
minDist = 50
param1 = 200
param2 = 100
minRadius = 0
maxRadius = 0

while True:
    # Capture a frame from the camera
    ret, frame = cap.read()

    # Convert the frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Apply Gaussian blur to reduce noise
    gray = cv2.GaussianBlur(gray, (9, 9), 2)

    # Detect circles using Hough Circle Transform
    circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, dp, minDist, param1=param1, param2=param2, minRadius=minRadius,
                               maxRadius=maxRadius)

    # If circles are detected, draw them on the frame
    if circles is not None:
        circles = circles[0]
        for circle in circles:
            center = (int(circle[0]), int(circle[1]))
            radius = int(circle[2])
            cv2.circle(frame, center, radius, (0, 255, 0), 2)

    # Show the resulting frame
    cv2.imshow('frame', frame)

    # Exit if the 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video capture and close all windows
cap.release()
cv2.destroyAllWindows()
