import urllib.request
import re

def splatoonget():
    user_agent = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7'

    url = "http://en.wikipedia.org/wiki/List_of_TCP_and_UDP_port_numbers"
    headers={'User-Agent':user_agent,} 

    request=urllib.request.Request('https://splatoon.ink/schedule2',None,headers) #The assembled request
    response = urllib.request.urlopen(request)
    data = response.read() # The data u need
    #print(data)

    stages = ["The Reef","Musselforge Fitness","Starfish Mainstage",
    "Humpback Pump Track","Inkblot Art Academy","Moray Towers","Port Mackerel",
    "Sturgeon Shipyard","Shifty Station","Manta Maria","Kelp Dome",
    "Snapper Canal","Blackbelly Skatepark","MakoMart","Walleye Warehouse",
    "Shellendorf Institute","Arowana Mall","Goby Arena","Piranha Pit",
    "Camp Triggerfish","Wahoo World","New Albacore Hotel","Ancho-V Games",
    "Skipper Pavilion"]

    modes = ["Rainmaker", "Splat Zones", "Tower Control", "Clam Blitz"]

    current = str(data).split(",")

    #newlines = "\n".join(current)
    #print(newlines)

    currentmode = ['']
    #print(currentmode)
    currentmaps = ['']
    #print(currentmaps)
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
    leaguemode = currentleague[6][7:len(currentleague[6])-1]

    regular = "The Current Regular TURF WAR stages are " + currentmaps[3][9:len(currentmaps[3])-1] + " and " + currentmaps[4][1:len(currentmaps[4])-2]
    ranked = "The Current Ranked " + rankedmode.upper() + " stages are " + currentmode[3][9:len(currentmode[3])-1] + " and " + currentmode[4][1:len(currentmode[4])-2]
    league = "The Current League " + leaguemode.upper() + " stages are " + currentleague[3][9:len(currentleague[3])-1] + " and " + currentleague[4][1:len(currentleague[4])-2]
    
    f = open("stages.txt", "w")
    f.truncate(0)
    f.write(regular+'\n'+ranked+'\n'+league)
    f.close


    
    
