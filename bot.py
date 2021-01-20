import discord
from juice import *
from alone import *
from sploon import *
from codec import *
from PIL import Image, ImageDraw, ImageFont
import random
import textwrap
import os
import calendar
import datetime
import sched
import time
from discord.ext import commands

tokenfile = open("C:\\token.txt", "r")
TOKEN = tokenfile.read()

client = discord.Client()
print(tokenfile.read())
prefix = '&'
file = open('msgs.txt', 'r')
data = file.readlines()
commands = []
for i in data:
    temp = i.strip().split(',')
    commands.append(temp)
file.close()


@client.event
async def on_message(message):
#message.channel.send(str(message.author) + ' says:\n' + str(message.content) + '\n.')
    if message.author != client.user and str(message.channel) == "cool_toolbars":
        mirrorChannel = client.get_channel(671680652839485445)
        mirrorMessageContent = str(message.author) + ' says:\n' + str(message.content) + '\n.'
        #print(message.attachments[0].size)
        #urllib.request.urlretrieve(message.attachments[0].url, 'temp.png')
        try:
            await mirrorChannel.send(mirrorMessageContent)
            await mirrorChannel.send(message.attachments[0].url)
        except IndexError:
            #await mirrorChannel.send(mirrorMessageContent)
            pass

            
    if str(message.author) == "joestaen#6969" and message.content.startswith('$$') :
        print(message.content[2:])
        sendChannel = client.get_channel(264282364543238145)
        sendMessageContent = str(message.content[2:])
        await sendChannel.send(sendMessageContent)
    if message.author == client.user:
        return
    m = str(message).lower()

    for i in commands:
        if message.content == i[0]:
            msg = i[1]
            await message.channel.send(msg)

    if message.content == (prefix + "ritter"):
        msg = '**trains** \n <:rit1:264632942733557761><:rit2:264632943144730644><:rit3:264632943476080640> \n <:rit4:264632943639527434><:rit5:264632943421554691><:rit6:264632945367580672> \n <:rit7:264632944755212289><:rit8:264632945401135104><:rit9:264632945115922434>'.format(
            message)
        await message.channel.send(msg)

    if message.content == (prefix + "marie"):
        #msg = '**Now this bitch I would fuck her so hard her kids would feel it. Plz Nintendo give me a Marie fucking sim I would pay mountains of cash.** \n <:marie1:405326048872366090><:marie2:405326051758178314><:marie3:405326050050965504><:marie4:405326049098858498> \n <:marie5:405326050923511808><:marie6:405326052479598592><:marie7:405326050810396673><:marie8:405326049291927552> \n <:marie9:405326050877374464><:marie10:405326052425072641><:marie11:405326052974657537><:marie12:405326050655076363> \n <:marie13:405326050042576896><:marie14:405326051095347200><:marie15:405326050059354125><:marie16:405326049795112962>'.format(message)
        msg = 'Now this bitch I would fuck her so hard her kids would feel it. Plz Nintendo give me a Marie fucking sim I would pay mountains of cash.'.format(
            message)
        await message.channel.send(msg)

    if message.content == (prefix + 'chelsea'):
        msg = "Remember when you asked me who I liked in term 2? Well, I have a confession to make... The person I like is you, Chelsea. From when I first talked to you, I saw you as a kind, intelligent, pretty, funny and strong-opinioned person. From then on, I liked you for your personality and kindness towards everyone. After careful thought, I have decided that my secret cannot be held back anymore, and I would like to know if you would like to be my first girlfriend.".format(
            message)
        await message.channel.send(msg)

    if message.content == (prefix + 'lollie'):
        msg = "Can please get rid of the dumb fucking lollie bot. It's fucking stupid it makes it sound like we are super desperate to find a fucking date and the dumb fucking images that pop up".format(
            message)
        await message.channel.send(msg)

    if message.content == (prefix + 'loos'):
        msg = "{0.author.mention} have you seen what's going on in the world right now.\nYour saying you get kick out of saying something racist is disgusting.\nIt doesn't matter why you are saying something racist, it's the fact you a racist is disgusting. Keep this up you will loos everyone is your life. You will loos everything. You will feel the pain of all of those who you brought pain to.".format(
            message)
        await message.channel.send(msg)

    if message.content == (prefix + 'pasta'):
        msg = "chelsea - George's letter \nlollie - Cotton's sperg \n".format(
            message)
        await message.channel.send(msg)

    if message.content == (prefix + 'lewd'):
        await message.channel.send(file=discord.File('images/hinokalewd.png'))

    if message.content == ('harry wallace help'):
        msg = 'right so\n&fc - friend codes for 3DS\nritter - its ritter\'s face\nmarie - marie copypasta\nchelsea - chelsea copypasta\nlollie - cotton\nlewd - lewd\nalone - alone on a X Y?\njuice - &juice [text]\ndab - &dab [text]\ncodec - &codec [name] [text]\n\tcurrent portraits:\n\t\tcolonel\n\t\tnaomi\n\t\tmei ling\n\t\tmeryl\n\t\tmiller\n\t\twolf\n\t\ttom\n\t\tben'.format(
            message)
        await message.channel.send(msg)

    if message.content.startswith(prefix + 'fc'):
        msg = "0361-9574-6041 dan\n3153-9628-9995 may\n0920-5030-1151 joe\n1306-4931-3543 gin\n3866-9206-5223 ang\n4124-5082-9752 aki \n1564-3621-7080 tom ashoo8 \n1521-7977-4558 tom bleach".format(
            message)
        await message.channel.send(msg)

    if message.content.upper().startswith('I THINK'):
        randy = random.randint(1, 2)
        if randy == 1:
            msg = 'WHO CARES WHAT YOU THINK, YOU ARE NOT MY MOTHER!'.format(message)
        if randy == 2:
            msg = 'WHO CARES WHAT YOU THINK, YOU ARE NOT MY FATHER!'.format(message)
        await message.channel.send(msg)
    if message.content.startswith('hey dan'):
        msg = '{0.author.mention} yeah?'.format(message)
        await message.channel.send(msg)
    if "😁" in message.content:
        await message.add_reaction("😁")
    if message.content.startswith(prefix+'alone'):
        alone()
        await message.channel.send(file=discord.File('aloneout.png'))
    if message.content.startswith(prefix+'nagatoro'):
        face = random.randint(1, 531)
        faceimage = 'nagatoro/('+str(face)+').png'
        await message.channel.send(file=discord.File(str(faceimage)))

    if message.content.startswith(prefix+'juice'):
        W = 140
        Ws = 65
        juice(str(message.content[7:]))
        await message.channel.send(file=discord.File('juiceout.png'))
    if message.content.startswith(prefix+'dab'):
        Wdab = 140

        def dab(dabname):
            dabImage = Image.open('images/dabblank.jpg')
            font_type = ImageFont.truetype("segoeprb.ttf", 30)
            draw = ImageDraw.Draw(dabImage)
            widthdab = font_type.getsize(dabname)[0]
            # print(widthdab)
            draw.text((675+(Wdab-widthdab)/2, 48), text=dabname,
                      font=font_type, fill=(0, 0, 0))
            dabImage.save("dabout.png")
        dab(str(message.content[4:])+',')
        await message.channel.send(file=discord.File('dabout.png'))


    if message.content.startswith('&codec'):
        codec(message.content)
        await message.channel.send(file=discord.File('codecout.png'))

    if message.content.startswith('&splatoon'):
        W = 800

        def splatoon(splatoontext):
            toprint = textwrap.fill(splatoontext, width=60)
            if message.content.startswith('&splatoon marie'):
                splatoonImage = Image.open('images/marietext.png')
            elif message.content.startswith('&splatoon callie'):
                splatoonImage = Image.open('images/callietext.png')
            font_type = ImageFont.truetype("Splatoon2.otf", 30)
            draw = ImageDraw.Draw(splatoonImage)
            width = font_type.getsize(splatoontext)[0]
            draw.text((150, 70), text=toprint,
                      font=font_type, fill=(255, 255, 255))
            splatoonImage.save("splatoonout.png")
        if message.content.startswith('&splatoon marie'):
            splatoon(str(message.content[16:]))
            await message.channel.send(file=discord.File('splatoonout.png'))
        elif message.content.startswith('&splatoon callie'):
            splatoon(str(message.content[17:]))
            await message.channel.send(file=discord.File('splatoonout.png'))

    if message.content.startswith('&mat'):
        Wmat = 140

        def mat(matname):
            matImage = Image.open('images/matblank.png')
            font_type = ImageFont.truetype("segoeprb.ttf", 30)
            draw = ImageDraw.Draw(matImage)
            widthmat = font_type.getsize(matname)[0]
            # print(widthmat)
            draw.text((675+(Wmat-widthmat)/2, 290), text=matname,
                      font=font_type, fill=(0, 0, 0))
            matImage.save("matout.png")
        mat(str(message.content[4:]))
        await message.channel.send(file=discord.File('matout.png'))
    if message.content.startswith('&roggerism'):
        roggerPrefix = ['Le', 'Slicka\'', 'Mister', 'Uh oh... ']
        consSyls = ['gr','bl','p','kl','k','gl','sh','shl','b','kr','j','w','dr','d','pl','n','g', 'shn']
        vowSyls  = ['oo','i','ee','er','or','öo','ü', 'u','o']
        endSyls  = ['ble','bert','ple','pert','turd','p','b','py','bit','bé','be', 'zz', 'pers', 'ber']
        # print(('Maximum possibilities'), len(consSyls) * len(vowSyls) * len(endSyls) * len(roggerPrefix))
        numChoice = random.randint(0, 4)
        if numChoice == 4:
            prefixChosen = random.choice(roggerPrefix)
        else:
            prefixChosen = ''
        msg = (prefixChosen+ ' ' + random.choice(consSyls) + random.choice(vowSyls) + random.choice(endSyls)).format(message)
        # print(msg)
        await message.channel.send(msg)
    if message.content.startswith('&stages'):
        now = datetime.datetime.now()
# progress bar
        if now.hour % 2 == 0:
            progress = ('●'*int(str(now.minute)[0])) + \
                (('○'*(12-int(str(now.minute)[0]))))
        else:
            progress = ('●'*6)+('●'*int(str(now.minute)
                                        [0]))+(('○'*(6-int(str(now.minute)[0]))))

        splatoonget()
        splatoonfile = open("stages.txt", "r")
        stages = splatoonfile.read()
        splatoonfile.close
        await message.channel.send(stages+'\n'+progress)
        await message.channel.send(file=discord.File('triplestack.png'))


@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run(TOKEN)
