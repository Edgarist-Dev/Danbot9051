import urllib.request
import re
from PIL import Image
import sys
import datetime
def splatoonget():
    now = datetime.datetime.now()
    user_agent = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7'

    headers={'User-Agent':user_agent,} 

    request=urllib.request.Request('https://splatoon.ink/schedule2',None,headers)
    response = urllib.request.urlopen(request)
    data = response.read()

###don't know why this is here
    stages = ["The Reef","Musselforge Fitness","Starfish Mainstage",
    "Humpback Pump Track","Inkblot Art Academy","Moray Towers","Port Mackerel",
    "Sturgeon Shipyard","Shifty Station","Manta Maria","Kelp Dome",
    "Snapper Canal","Blackbelly Skatepark","MakoMart","Walleye Warehouse",
    "Shellendorf Institute","Arowana Mall","Goby Arena","Piranha Pit",
    "Camp Triggerfish","Wahoo World","New Albacore Hotel","Ancho-V Games",
    "Skipper Pavilion"]

    modes = ["Rainmaker", "Splat Zones", "Tower Control", "Clam Blitz"]

###DO NOT TOUCH
    current = str(data).split(",")
###DO NOT TOUCH

    currentmode = ['']
    currentmaps = ['']
    currentleague = ['']

###this part finds the relevant parts to be used later
    for i in current:
        if i[:7] == '"gachi"':
            for x in range(9):
                #print(current[current.index(i)+x])
                currentmode.append(current[current.index(i)+x])
            break
        elif i[:17] == '"modes":{"gachi":':
            for x in range(9):
                currentmode.append(current[current.index(i)+x])
            break
    for i in current:
        if i[:9] == '"regular"':
            for x in range(6):
                #print(current[current.index(i)+x])
                currentmaps.append(current[current.index(i)+x])
            break
        elif i[:18] == '"modes":{"regular"':
            for x in range(6):
                currentmaps.append(current[current.index(i)+x])
    for i in current:
        if i[:8] == '"league"':
            for x in range(8):
                #print(current[current.index(i)+x])
                currentleague.append(current[current.index(i)+x])
            break
    for i in current:
        if i[:17] == '"modes":{"league"':
            for x in range(8):
                currentleague.append(current[current.index(i)+x])

##    print(currentmode)
##    print(currentleague)
##    print(currentmaps)


### this part finds what the current mode is for ranked and league
    for i in currentmode:
        if i[:7] == '"name":':
            print(i)
            rankedmode = i[8:len(i)-1]
            break
        elif i[:8] == '"gachi":':
            for i in currentmode:
                if i[:7] == '"name":':
                    rankedmode = i[8:len(i)-1]
                    break
            break

    for i in currentleague:
        if i[:7] == '"name":':
            leaguemode = i[8:len(i)-1]
            break
        elif i[:9] == '"league":':
            leaguemode = current[current.index(i)+5][8:len(current[current.index(i)+5])-1]
        elif i[:15] == '"rule":{"name":':
            leaguemode = i[16:len(i)-1]
            
### this part is the text the bot sends
    regular = "The Current <:regular:497307744248791041> Regular TURF WAR stages are " + currentmaps[3][9:len(currentmaps[3])-1] + " and " + currentmaps[4][1:len(currentmaps[4])-2]
    ranked = "The Current <:ranked:497307749911363594> Ranked " + rankedmode.upper() + " stages are " + currentmode[3][9:len(currentmode[3])-1] + " and " + currentmode[4][1:len(currentmode[4])-2]
    league = "The Current <:league:497307738112524298> League " + leaguemode.upper() + " stages are " + currentleague[3][9:len(currentleague[3])-1] + " and " + currentleague[4][1:len(currentleague[4])-2]
    #print(regular,'\n',ranked,'\n',league)
    f = open("stages.txt", "w")
    f.truncate(0)
    f.write(regular+'\n'+ranked+'\n'+league)
    f.close


####this part makes the image
    image1 = Image.open('images/stages/'+currentmaps[3][9:len(currentmaps[3])-1]+'.png')
    image2 = Image.open('images/stages/'+currentmaps[4][1:len(currentmaps[4])-2]+'.png')
    image3 = Image.open('images/stages/Regular.png')
    image4 = Image.open('images/stages/Ranked.png')
    image5 = Image.open('images/stages/League.png')
    image6 = Image.open('images/stages/'+currentmode[3][9:len(currentmode[3])-1]+'.png')
    image7 = Image.open('images/stages/'+currentmode[4][1:len(currentmode[4])-2]+'.png')
    image8 = Image.open('images/stages/'+currentleague[3][9:len(currentleague[3])-1]+'.png')
    image9 = Image.open('images/stages/'+currentleague[4][1:len(currentleague[4])-2]+'.png')
    (width1, height1) = image1.size
    (width2, height2) = image2.size

    result_width = width1 + width2
    result_height = max(height1, height2)

    result = Image.new('RGB', (result_width, result_height))
    result.paste(im=image1, box=(0, 0))
    result.paste(im=image2, box=(width1, 0))
    result.save('regularimg.png')

    result = Image.new('RGB', (result_width, result_height))
    result.paste(im=image6, box=(0, 0))
    result.paste(im=image7, box=(width1, 0))
    result.save('rankedimg.png')

    result = Image.new('RGB', (result_width, result_height))
    result.paste(im=image8, box=(0, 0))
    result.paste(im=image9, box=(width1, 0))
    result.save('leagueimg.png')

    stack = Image.open('images/regularimg.png')
    stack.paste(image3, (320, 0), mask=image3)
    stack.save('regularstage.png')
    stack = Image.open('images/rankedimg.png')
    stack.paste(image4, (320, 0), mask=image4)
    stack.save('rankedstage.png')
    stack = Image.open('images/leagueimg.png')
    stack.paste(image5, (320, 0), mask=image5)
    stack.save('leaguestage.png')

    triplestack = Image.new('RGB', (result_width, 1080))
    triplestack.paste(im=Image.open('images/regularstage.png'), box=(0,0))
    triplestack.paste(im=Image.open('images/rankedstage.png'), box=(0,360))
    triplestack.paste(im=Image.open('images/leaguestage.png'), box=(0,720))
    triplestack = triplestack.resize((320,270),Image.ANTIALIAS)
    triplestack.save('triplestack.png')
    

