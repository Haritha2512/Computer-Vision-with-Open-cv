import cv2

img = cv2.imread("house.jpeg")

# Crop a part of the image
crop = img[50:200, 50:200]

# Copy the cropped part
copy = crop.copy()

# Paste inside the same image
img[220:370, 220:370] = copy

cv2.imshow("Cropped and Pasted", img)

cv2.waitKey(0)
cv2.destroyAllWindows()