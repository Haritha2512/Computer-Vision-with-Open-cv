import cv2

img = cv2.imread("house.jpeg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

x = cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=3)
y = cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksize=3)

xy = cv2.magnitude(x, y)
xy = cv2.convertScaleAbs(xy)

cv2.imshow("Original", img)
cv2.imshow("Sobel XY", xy)

cv2.waitKey(0)
cv2.destroyAllWindows()