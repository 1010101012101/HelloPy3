import cv2

img = cv2.imread('images/MyBeauty.jpg')
cv2.putText(img, "beauty", (20, 20), cv2.FONT_HERSHEY_SIMPLEX, 1, 255, 2)
cv2.putTextZH()
cv2.imshow('my image', img)


cv2.waitKey()
cv2.destroyAllWindows()
