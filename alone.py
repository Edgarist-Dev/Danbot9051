from PIL import Image, ImageDraw, ImageFont
import datetime
import calendar


def alone():
    W=160
    now = datetime.datetime.now()
    aloneImage = Image.open('images/alone blank.png')
    font_type = ImageFont.truetype("segoeprb.ttf", 20)
    draw = ImageDraw.Draw(aloneImage)
    (dwidth,dheight) = font_type.getsize(str(now.strftime('%A')))
    (mwidth,mheight) = font_type.getsize("morning?")
    (awidth,mheight) = font_type.getsize("afternoon?")
    (nwidth,mheight) = font_type.getsize("night?")
    draw.text(xy=(340,70),text="Alone on a",font=font_type)
    draw.text(xy=(315+(W-dwidth)/2,95),text=str(now.strftime('%A')),font=font_type)
    if now.hour >=0 and now.hour < 12:
        draw.text(xy=((W-mwidth)/2+315,120),text="morning?",font=font_type)
    if now.hour >=12 and now.hour < 18:
        draw.text(xy=((W-awidth)/2+315,120),text="afternoon?",font=font_type)
    if now.hour >=18 and now.hour < 24:
        draw.text(xy=((W-nwidth)/2+315,120),text="night?",font=font_type)
    #image.show()
    aloneImage.save("aloneout.png")
alone()
