import cv2
from cvzone.FaceDetectionModule import FaceDetector
import numpy as np

# Initialize the camera
cap = cv2.VideoCapture(0)
ws, hs = 1280, 720
cap.set(3, ws)
cap.set(4, hs)

if not cap.isOpened():
    print("Camera couldn't Access!!!")
    exit()

# Initialize face detector
detector = FaceDetector()

while True:
    success, img = cap.read()
    if not success:
        break

    # Detect faces
    img, bboxs = detector.findFaces(img, draw=False)

    if bboxs:
        # Get the coordinates of the detected face
        fx, fy = bboxs[0]["center"][0], bboxs[0]["center"][1]
        pos = [fx, fy]

        # Draw gun target design
        # Concentric circles
        cv2.circle(img, (fx, fy), 60, (0, 0, 255), 2)
        cv2.circle(img, (fx, fy), 40, (0, 0, 255), 2)
        cv2.circle(img, (fx, fy), 20, (0, 0, 255), 2)
        
        # Crosshair lines
        cv2.line(img, (fx - 80, fy), (fx - 20, fy), (0, 0, 255), 2)
        cv2.line(img, (fx + 20, fy), (fx + 80, fy), 2)
        cv2.line(img, (fx, fy - 80), (fx, fy - 20), (0, 0, 255), 2)
        cv2.line(img, (fx, fy + 20), (fx, fy + 80), (0, 0, 255), 2)
        
        # Black dot in the middle
        cv2.circle(img, (fx, fy), 5, (0, 0, 0), cv2.FILLED)

        cv2.putText(img, str(pos), (fx + 15, fy - 15), cv2.FONT_HERSHEY_PLAIN, 2, (255, 0, 0), 2)
        cv2.putText(img, "TARGET LOCKED", (850, 50), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 255), 3)

    else:
        # No face detected annotations
        cv2.putText(img, "NO TARGET", (880, 50), cv2.FONT_HERSHEY_PLAIN, 3, (0, 0, 255), 3)
        # Concentric circles at the center
        cv2.circle(img, (640, 360), 60, (0, 0, 255), 2)
        cv2.circle(img, (640, 360), 40, (0, 0, 255), 2)
        cv2.circle(img, (640, 360), 20, (0, 0, 255), 2)
        
        # Crosshair lines at the center
        cv2.line(img, (640 - 80, 360), (640 - 20, 360), (0, 0, 255), 2)
        cv2.line(img, (640 + 20, 360), (640 + 80, 360), (0, 0, 255), 2)
        cv2.line(img, (640, 360 - 80), (640, 360 - 20), (0, 0, 255), 2)
        cv2.line(img, (640, 360 + 20), (640, 360 + 80), (0, 0, 255), 2)
        
        # Black dot in the middle
        cv2.circle(img, (640, 360), 5, (0, 0, 0), cv2.FILLED)

    # Show the image
    cv2.imshow("Image", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
