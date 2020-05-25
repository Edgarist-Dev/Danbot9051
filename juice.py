from PIL import Image, ImageDraw, ImageFont
#juicebox = 'Average'
W = 140
Ws = 65
def juice(juicebox):
            juiceImage = Image.open('images/juiceblank.png')
            font_type_s = ImageFont.truetype("segoeprb.ttf", 16)
            font_type_l = ImageFont.truetype("segoeprb.ttf", 30)
            draw = ImageDraw.Draw(juiceImage)
            widths = font_type_s.getsize(juicebox)[0]
            draw.text((188+(Ws-widths)/2, 360),
                      text=juicebox, font=font_type_s)
            width = font_type_l.getsize(juicebox)[0]
            w = draw.textsize(juicebox)
            # print(width)
            # print(widths)
            draw.text((550+(W-width)/2, 325), juicebox, font=font_type_l)
            juiceImage.save("juiceout.png")
#juice()
