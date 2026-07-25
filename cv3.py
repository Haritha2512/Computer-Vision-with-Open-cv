import cv2
image = cv2.imread('test.jpg.png')
gray = cv2.cvtColor(image,cv2.COLOR_BGR2RGB)
edges = cv2.Canny(gray,100,200)
cv2.imwrite('Canny_Edges_3rd.test.jpg.png',edges)
cv2.imshow('Edges',edges)
cv2.waitKey(0)
cv2.destroyAllWindows()