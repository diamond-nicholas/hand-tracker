import cv2
import mediapipe as mp
import time

cap = cv2.VideoCapture(0)

while True:
    isTrue, frame = cap.read()
    if isTrue:
        cv2.imshow('Video', frame)
        if cv2.waitKey(20) & 0xFF==ord('d'):
            break
    else:
        break

cap.release()
cv2.destroyAllWindows()