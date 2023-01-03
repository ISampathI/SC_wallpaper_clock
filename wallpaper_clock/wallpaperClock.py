from PIL import Image, ImageDraw, ImageFont
from datetime import datetime
import ctypes, os, time

bg = Image.open("background.jpg")
font = ImageFont.truetype("OCRAEXT", 190)
path = r"%s/newbg.png"%(os.getcwd())
pTime = ""
while True:
    cTime = datetime.now().strftime("%H:%M")
    if cTime != pTime:
        print(cTime)
        newbg = bg.copy()
        draw = ImageDraw.Draw(newbg)
        draw.text((800,560), cTime, (255, 255, 255), font=font)
        newbg.save(path, quality=95)
        newbg.close()
        ctypes.windll.user32.SystemParametersInfoW(20, 0, path, 0)
        pTime = cTime
        time.sleep(1)
