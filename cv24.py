import cv2
import numpy as np

img = cv2.imread("house.jpeg")

A = 2

kernel = np.array([[0, -1, 0],
                   [-1, A + 4, -1],
                   [0, -1, 0]])

sharp = cv2.filter2D(img, -1, kernel)

cv2.imshow("Original", img)
cv2.imshow("High-Boost", sharp)

cv2.waitKey(0)
cv2.destroyAllWindows()