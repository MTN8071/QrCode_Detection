import cv2
import numpy as np
from pyzbar import pyzbar

# Initialize the QR code detector
detector = cv2.QRCodeDetector()

# Open the webcam
cap = cv2.VideoCapture(0)

while True:
    # Read a frame from the webcam
    ret, frame = cap.read()

    # Convert to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect the QR code
    data, bbox, _ = detector.detectAndDecode(gray)

    # Draw the bounding box
    if bbox is not None:
        # Display the decoded data
        print("Data:", data)

        for i in range(len(bbox)):
            # Draw the bounding box
            cv2.rectangle(frame, bbox[i][0], bbox[i][1], (255, 0, 0), 2)

    # Show the output image
    cv2.imshow("QR code detection", frame)

    # Break the loop if the 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

#Release the webcam
#cap.release()
cv2.destroyAllWindows()
