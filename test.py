#-*- coding:utf-8 -*-
from PIL import Image
import pytesseract
imageObject=Image.open('images/7.gif')
print (imageObject)
print (pytesseract.image_to_string(imageObject))
#print (pytesseract.image_to_string(Image.open('/root/Desktop/pythoncode/test.png')))
#print (open('test.png').read())
