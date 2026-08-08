import cv2
import numpy as np

img = cv2.imread("house.jpeg")

h, w = img.shape[:2]

p1 = np.float32([[50,50], [w-50,50], [w-50,h-50], [50,h-50]])
p2 = np.float32([[20,80], [w-20,50], [w-50,h-30], [50,h-50]])

M = cv2.getPerspectiveTransform(p1, p2)
result = cv2.warpPerspective(img, M, (w, h))

cv2.imshow("Original", img)
cv2.imshow("Perspective", result)

cv2.waitKey(0)
cv2.destroyAllWindows()