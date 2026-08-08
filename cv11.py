import cv2
import numpy as np

img = cv2.imread("house.jpeg")

p1 = np.float32([[50,50], [200,50], [50,200]])
p2 = np.float32([[20,80], [200,50], [80,220]])

M = cv2.getAffineTransform(p1, p2)
result = cv2.warpAffine(img, M, (img.shape[1], img.shape[0]))

cv2.imshow("Original", img)
cv2.imshow("Affine", result)

cv2.waitKey(0)
cv2.destroyAllWindows()