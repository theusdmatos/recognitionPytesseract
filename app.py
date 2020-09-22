#https://pypi.org/project/pytesseract/

import cv2 
import pytesseract

from PIL import Image, ImageDraw
 
image = cv2.imread('images/img.png')

recognition = pytesseract.image_to_string(image, lang='eng')

print(recognition)
