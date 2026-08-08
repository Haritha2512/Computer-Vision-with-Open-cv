import cv2
import numpy as np

cap = cv2.VideoCapture("video.mp4")

while True:
    ret, frame = cap.read()
    if not ret:
        break

    h, w = frame.shape[:2]

    p1 = np.float32([[50,50], [w-50,50], [w-50,h-50], [50,h-50]])
    p2 = np.float32([[20,80], [w-20,50], [w-50,h-30], [50,h-50]])

    M = cv2.getPerspectiveTransform(p1, p2)
    result = cv2.warpPerspective(frame, M, (w, h))

    cv2.imshow("Original Video", frame)
    cv2.imshow("Perspective Video", result)

    if cv2.waitKey(30) & 0xFF == 'q':
        break

cap.release()
cv2.destroyAllWindows()