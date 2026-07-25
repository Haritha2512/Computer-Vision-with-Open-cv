import cv2
import numpy as np

img = cv2.imread('photo.jpg')
gray_img = cv2.cvtColor(img, cv2.COLOR_BGRA2GRAY)
kernel = cv2.getStructuringElement(cv2.MORPH_RECT,(5,5))
eroded_img = cv2.erode(gray_img, kernel, iterations=1)
cv2.imwrite("eroded_image.jpg", eroded_img)
