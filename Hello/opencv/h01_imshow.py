import cv2

img = cv2.imread('images/MyBeauty.jpg')
cv2.imshow('my image', img)
cv2.waitKey()
cv2.destroyAllWindows()
