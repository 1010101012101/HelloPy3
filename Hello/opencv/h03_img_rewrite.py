

import cv2
img = cv2.imread("images/mc.meng03.png")
img = cv2.resize(img, (96, 96), interpolation=cv2.INTER_CUBIC)
cv2.imwrite("images/mc.meng03.jpg", img)
cv2.imshow('', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
