import cv2

img = cv2.imread("house.jpeg")

watermark = "SAVEETHA"
cv2.putText(img, watermark, (50, 80),
            cv2.FONT_HERSHEY_SIMPLEX, 1.5,
            (255, 255, 255), 3)

cv2.imshow("Watermarked Image", img)

cv2.waitKey(0)
cv2.destroyAllWindows()