import cv2
import numpy as np

img = cv2.imread("house.jpeg")

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

gx = cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=3)
gy = cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksize=3)

gradient = cv2.magnitude(gx, gy)
gradient = cv2.convertScaleAbs(gradient)

sharp = cv2.addWeighted(gray, 1, gradient, 1, 0)

cv2.imshow("Original", gray)
cv2.imshow("Gradient Masking", sharp)

cv2.waitKey(0)
cv2.destroyAllWindows()