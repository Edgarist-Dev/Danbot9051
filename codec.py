from PIL import Image, ImageDraw, ImageFont
import textwrap
import re
def codec(codectext):
            W = 640
            messageContent = re.findall('(?<=c )[^\ ]+', codectext)
            textContent = re.search('(&codec)(.+? )(.*)', codectext).group(3)
            name = messageContent[0]
            codecImage = Image.open('images/'+name+'codec.png')
            font_type = ImageFont.truetype("arial.ttf", 25)
            (width, height) = font_type.getsize(textContent)
            draw = ImageDraw.Draw(codecImage)
            textprint = textwrap.fill(textContent, width=45)
            # print(width)
            if len(textprint) < 45:
                draw.text(((W-width)/2, 280), text=textprint,
                          font=font_type, fill=(255, 255, 255))
            else:
                draw.text(((W-500)/2, 280), text=textprint,
                          font=font_type, fill=(255, 255, 255))
            codecImage.save("codecout.png")