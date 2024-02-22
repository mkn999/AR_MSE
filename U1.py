import cv2
import numpy as np


cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    

    if not ret:
        print("Failed to capture frame")
        break

    # Convert BGR to HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Define range of green color in HSV
    lower_green = np.array([40, 100, 20])
    upper_green = np.array([70, 255, 255])

    # Threshold the HSV image to get only green colors
    mask = cv2.inRange(hsv, lower_green, upper_green)

    # Find contours of the green object
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Check if contours are found
    if contours:
        # Find the contour with the largest area to avoid many rectangle formation
        max_contour = max(contours, key=cv2.contourArea)
        
        # Get bounding box coordinates of the largest contour
        x, y, w, h = cv2.boundingRect(max_contour)
        
        # Draw rectangle around the largest contour
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

    else:
        print("No contours found")

    # Display the resulting frame
    cv2.imshow('Green Object Tracking', frame)

  
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


cap.release()
cv2.destroyAllWindows()
