
import cv2
img = cv2.imread("images/lena.jpg")
img = cv2.resize(img, (96, 96), interpolation=cv2.INTER_CUBIC)
cv2.imwrite("images/lena_resize.jpg", img)
cv2.imshow('', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
