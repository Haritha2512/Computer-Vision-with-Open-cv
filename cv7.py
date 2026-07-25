import cv2
img = cv2.imread('photo2.jpg')
height, width = img.shape[:2]

scale_factor1 = 3.0
bigger_image =  cv2.resize(img,(int(width*scale_factor1),int(height*scale_factor1)))

scale_factor = 0.5
smaller_image = cv2.resize(img,(int(width*scale_factor),int(height*scale_factor)))

cv2.imshow('Original image',img)
cv2.imshow("Bigger image",bigger_image)
cv2.imshow('Smaller image',smaller_image)
cv2.imwrite("Bigger_image.jpg",bigger_image)
cv2.imwrite("Smaller_image.jpg",smaller_image)