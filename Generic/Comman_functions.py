import time
from tkinter import Image
from selenium.webdriver.common.by import By
from PIL import Image, ImageDraw, ImageFont
import pytz
from datetime import datetime


def boopage(v,list):
    from Deed import driver
    l = driver.find_element(By.XPATH, v)
    data = l.text
    for i in list:
        l.clear()
        l.send_keys(i)
        time.sleep(2)

def add_time(img_path):
    """
    Adds date and time for the screenshots whose path are passed through img_path parameter

    param arg1: Path of the image that needs the time to be added
    type arg1: String
    """
    im = Image.open(img_path)
    width, height = im.size
    draw = ImageDraw.Draw(im)
    converted_tz = pytz.timezone('Asia/Kolkata')
    datetime_object = datetime.now(converted_tz)
    est_date = datetime_object.replace(microsecond=0, tzinfo=None)
    text = str(est_date)
    font = ImageFont.truetype('arial.ttf', 36)
    textwidth, textheight = draw.textsize(text, font)
    margin = 10
    x = width - textwidth - margin
    y = height - textheight - margin
    draw.text((x, y), text, font=font, fill=(0, 0, 0))
    im.save(img_path)




