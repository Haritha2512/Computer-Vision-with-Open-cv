import cv2

image = cv2.imread("photo2.jpg")

cv2.imshow("Original Image", image)
cv2.moveWindow("Original Image", 100, 100)

cv2.waitKey(0)
cv2.destroyAllWindows()