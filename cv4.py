import cv2
import numpy as np

img = cv2.imread('photo.jpg')

if img is None:
    print("Image not found!")
    exit()

kernel = np.ones((5,5), np.uint8)
dilated_img = cv2.dilate(img, kernel, iterations=1)

cv2.imwrite("Dilated_Image.jpg", dilated_img)