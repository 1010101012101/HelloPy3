import cv2
from PIL import Image, ImageDraw, ImageFont
import numpy as np


def putTextZH(img, text, org):
    frame_cv2 = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    frame_pil = Image.fromarray(frame_cv2)  # 转为PIL的图片格式

    draw = ImageDraw.Draw(frame_pil)
    font = ImageFont.truetype("simhei.ttf", 50, encoding="utf-8")
    # 第一个参数为字体，中文黑体
    # 第二个为字体大小
    ImageDraw.Draw(frame_pil).text(org, text, (0, 0, 255), font)
    '''
        frame_pil:目标图像
        第一个参数为打印的坐标
        第二个为打印的文本
        第三个为字体颜色
        第四个为字体
    '''

    return cv2.cvtColor(np.array(frame_pil), cv2.COLOR_RGB2BGR)