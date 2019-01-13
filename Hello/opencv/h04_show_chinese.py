
from Hello.opencv.h00_utils import *


cv2.imshow("img",  putTextZH(cv2.imread('images/MyBeauty.jpg'), "美女", (100, 200)))


cv2.waitKey()
cv2.destroyAllWindows()
