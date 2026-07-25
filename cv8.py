import cv2
img = cv2.imread("photo.jpg")
rotated_img1 = cv2.rotate(img,cv2.ROTATE_90_CLOCKWISE)
rotated_img2 = cv2.rotate(img,cv2.ROTATE_90_COUNTERCLOCKWISE)
cv2.imwrite("Rotated_image1.jpg",rotated_img1)
cv2.imwrite("Rotated_image2.jpg",rotated_img2)