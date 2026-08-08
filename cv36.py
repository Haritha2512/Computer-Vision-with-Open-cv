import cv2

img = cv2.imread("watch.png")

if img is None:
    print("Image not found!")
    exit()

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

blur = cv2.GaussianBlur(gray, (5, 5), 0)

_, thresh = cv2.threshold(blur, 120, 255, cv2.THRESH_BINARY)

contours, _ = cv2.findContours(
    thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE
)

for c in contours:
    x, y, w, h = cv2.boundingRect(c)

    if w > 50 and h > 50:
        cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)
        cv2.putText(img, "Watch", (x, y-10),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0), 2)

cv2.imshow("Watch Recognition", img)
cv2.waitKey(0)
cv2.destroyAllWindows()