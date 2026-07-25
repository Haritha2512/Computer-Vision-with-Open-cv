import cv2
cap = cv2.VideoCapture("video1.mp4")
slow_factor = 0.5
fast_factor = 2.0
ret, frame = cap.read()
while ret:
    cv2.imshow('Slow Motion', cv2.resize(frame,None,fx=slow_factor,fy=slow_factor))

    cv2.imshow('Fast Motion',cv2.resize(frame,None,fx=fast_factor,fy=fast_factor))

    if cv2.waitKey(1)&0xFF == ord('q'):
        break
    ret, frame = cap.read()
cap.release()
cv2.destroyAllWindows()