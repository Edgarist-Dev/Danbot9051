import urllib.request
import re
from PIL import Image
import sys

def splatoonget():
    user_agent = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7'

    headers={'User-Agent':user_agent,} 

    request=urllib.request.Request('https://splatoon.ink/schedule2',None,headers)
    response = urllib.request.urlopen(request)
    data = response.read()
    
    stages = ["The Reef","Musselforge Fitness","Starfish Mainstage",
    "Humpback Pump Track","Inkblot Art Academy","Moray Towers","Port Mackerel",
    "Sturgeon Shipyard","Shifty Station","Manta Maria","Kelp Dome",
    "Snapper Canal","Blackbelly Skatepark","MakoMart","Walleye Warehouse",
    "Shellendorf Institute","Arowana Mall","Goby Arena","Piranha Pit",
    "Camp Triggerfish","Wahoo World","New Albacore Hotel","Ancho-V Games",
    "Skipper Pavilion"]

    modes = ["Rainmaker", "Splat Zones", "Tower Control", "Clam Blitz"]

    current = str(data).split(",")

    currentmode = ['']
    currentmaps = ['']
    currentleague = ['']

    for i in current:
        if i[:7] == '"gachi"':
            for x in range(6):
                #print(current[current.index(i)+x])
                currentmode.append(current[current.index(i)+x])
            break
    for i in current:
        if i[:18] == '"modes":{"regular"':
            for x in range(6):
                #print(current[current.index(i)+x])
                currentmaps.append(current[current.index(i)+x])
            break
    for i in current:
        if i[:8] == '"league"':
            for x in range(6):
                #print(current[current.index(i)+x])
                currentleague.append(current[current.index(i)+x])
            break
    rankedmode = currentmode[6][8:len(currentmode[6])-1]
    leaguemode = currentleague[6][8:len(currentleague[6])-1]

    regular = "The Current Regular TURF WAR stages are " + currentmaps[3][9:len(currentmaps[3])-1] + " and " + currentmaps[4][1:len(currentmaps[4])-2]
    ranked = "The Current Ranked " + rankedmode.upper() + " stages are " + currentmode[3][9:len(currentmode[3])-1] + " and " + currentmode[4][1:len(currentmode[4])-2]
    league = "The Current League " + leaguemode.upper() + " stages are " + currentleague[3][9:len(currentleague[3])-1] + " and " + currentleague[4][1:len(currentleague[4])-2]
    #print(regular,'\n',ranked,'\n',league)
    f = open("stages.txt", "w")
    f.truncate(0)
    f.write(regular+'\n'+ranked+'\n'+league)
    f.close

    image1 = Image.open('stages/'+currentmaps[3][9:len(currentmaps[3])-1]+'.png')
    image2 = Image.open('stages/'+currentmaps[4][1:len(currentmaps[4])-2]+'.png')
    image3 = Image.open('stages/Regular.png')
    image4 = Image.open('stages/Ranked.png')
    image5 = Image.open('stages/League.png')
    image6 = Image.open('stages/'+currentmode[3][9:len(currentmode[3])-1]+'.png')
    image7 = Image.open('stages/'+currentmode[4][1:len(currentmode[4])-2]+'.png')
    image8 = Image.open('stages/'+currentleague[3][9:len(currentleague[3])-1]+'.png')
    image9 = Image.open('stages/'+currentleague[4][1:len(currentleague[4])-2]+'.png')
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

    stack = Image.open('regularimg.png')
    stack.paste(image3, (320, 0), mask=image3)
    stack.save('regularstage.png')
    stack = Image.open('rankedimg.png')
    stack.paste(image4, (320, 0), mask=image4)
    stack.save('rankedstage.png')
    stack = Image.open('leagueimg.png')
    stack.paste(image5, (320, 0), mask=image5)
    stack.save('leaguestage.png')

    triplestack = Image.new('RGB', (result_width, 1080))
    triplestack.paste(im=Image.open('regularstage.png'), box=(0,0))
    triplestack.paste(im=Image.open('rankedstage.png'), box=(0,360))
    triplestack.paste(im=Image.open('leaguestage.png'), box=(0,720))
    triplestack = triplestack.resize((320,270),Image.ANTIALIAS)
    triplestack.save('triplestack.png')
    

