import cv2
import numpy as np

img = cv2.imread("house.jpeg")

p1 = np.float32([[50,50], [250,50], [250,250], [50,250]])
p2 = np.float32([[20,80], [280,50], [250,280], [50,250]])

H, _ = cv2.findHomography(p1, p2)

result = cv2.warpPerspective(img, H, (img.shape[1], img.shape[0]))

cv2.imshow("Original", img)
cv2.imshow("Homography", result)

cv2.waitKey(0)
cv2.destroyAllWindows()