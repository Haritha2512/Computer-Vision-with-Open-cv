import cv2

img = cv2.imread("house.jpeg")

# Draw rectangle around the object
cv2.rectangle(img, (50, 50), (250, 250), (0, 255, 0), 2)

# Extract object inside rectangle
object = img[50:250, 50:250]

cv2.imshow("Rectangle", img)
cv2.imshow("Extracted Object", object)

cv2.waitKey(0)
cv2.destroyAllWindows()