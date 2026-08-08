import cv2

img = cv2.imread("house.jpeg")

blur = cv2.GaussianBlur(img, (5,5), 0)
mask = cv2.subtract(img, blur)
sharp = cv2.add(img, mask)

cv2.imshow("Original", img)
cv2.imshow("Unsharp Masking", sharp)

cv2.waitKey(0)
cv2.destroyAllWindows()