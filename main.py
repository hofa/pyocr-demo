#-*- coding = utf-8 -*-
import sys
import pyocr
import pyocr.builders
from PIL import Image
import logger

dir = './images/'
def image_to_string(content):
    tools = pyocr.get_available_tools()
    if len(tools) == 0:
        logger.critical("No OCR tool found")
        sys.exit(1)
    # The tools are returned in the recommended order of usage
    tool = tools[1]
    # logger.debug("Will use tool '%s'" % (tool.get_name()))
    # Ex: Will use tool 'libtesseract'

    langs = tool.get_available_languages()
    if len(langs) == 0:
        logger.critical("No OCR lang found")
        sys.exit(1)
    lang = langs[0]

    im = Image.open(io.BytesIO(content))

    return tool.image_to_string(im, lang, pyocr.builders.TextBuilder())

if __name__ == "__main__":
    # print(dir)
	con = open(dir + '1.jpg', "rb").read()
	rand = image_to_string(con)
	print(rand)
	
