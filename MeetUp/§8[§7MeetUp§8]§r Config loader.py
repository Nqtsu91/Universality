import random
import math
import os
#API Link :http://www.kodevelopment.nl/customnpcs/api/1.8.9/
#Credits : Script UHC vs Bots config loader By Natsu91

#===================================#
#_______{ Creating Algorithm }______#
#===================================#


def LoadConfig(e):
    if e.npc.getTempdata().get("ConfigToRead") == None :
        e.npc.getTempdata().put("ConfigToRead", 0)

    List = ["UHC+","BadlionBorder","FinalUHC","NoEnchant","Snowball","DiamondKit"]

    e.npc.world.getTempdata().put("CurrentGame", List[int(e.npc.getTempdata().get("ConfigToRead"))])
    Path = os.path.dirname(os.path.abspath("__file__"))
    Path += "\\CustomNPC Config\\MeetUp\\configs\\"
    Path = Path.replace("\\", str(os.path.sep))
    with open (str(Path)+str(List[int(e.npc.getTempdata().get("ConfigToRead"))])+".txt", "r") as Config :
        Config = Config.read()
        Config = Config.split(u'\n')
        Name = Config[0]
        e.npc.world.getStoreddata().put("ConfigName", str(Name))
        del Config[0]
        ToConfigList = ["TeamSize","TeamAliveLimit","NoCleanUpEnabled","CatEyes","Rodless","AbsoLess","WaterAllowed","ForcedType","BadlionKB","RedditUHCDisplay","BadlionKillsSystem","ThunderStrike","WitherSoundI","WitherSoundII","IronGolemSound","VanillaDeathStyle","ExplodeOnDeath","ScatterMessageEnabled","NoCleanRegen"]

    for i in range (len(Config)-1, -1, -1):
        if Config[i] == "" :
            del Config[i]
        elif Config[i] == " " :
            del Config[i]
        elif Config[i][0] == "#" :
            del Config[i]
        elif Config[i] == u'\r' :
            del Config[i]

    for i in range (0, len(ToConfigList)):
        List = Config[i].split(":")
        try :
            e.npc.world.getTempdata().put(str(ToConfigList[i]), int(List[1]))
        except:
            if List[1] == "True":
                List[1] = True
            else :
                List[1] = False  
            e.npc.world.getTempdata().put(str(ToConfigList[i]), List[1])
    e.npc.executeCommand('/tellraw @a ["",{"text":"[","color":"dark_gray"},{"text":"Arena","color":"dark_red"},{"text":"]","color":"dark_gray"},{"text":"[","color":"dark_gray"},{"text":"Config","color":"purple"},{"text":"]","color":"dark_gray"},{"text":" Loaded config ","color": green,"bold":true,"italic":false},{"text":"'+str(Name)+'", "color" : dark_green, "underlined" : true} , { "text" :" succesfully", "color" : green, "bold":true}]')


def interact(e):
    e.npc.world.getStoreddata().clear()
    LoadConfig(e)
    e.setCanceled(True)

def damaged(e):
    e.setCanceled(True)
    List = ["UHC+","BadlionBorder","FinalUHC","NoEnchant","Snowball","DiamondKit"]
    if e.npc.getTempdata().get("ConfigToRead") == None :
        e.npc.getTempdata().put("ConfigToRead", 0)
    elif e.npc.getTempdata().get("ConfigToRead") == 5:
        e.npc.getTempdata().put("ConfigToRead", 0)
    else:
        e.npc.getTempdata().put("ConfigToRead", int(e.npc.getTempdata().get("ConfigToRead"))+1)

    e.npc.executeCommand('/tellraw @a ["",{"text":"[","color":"dark_gray"},{"text":"UHC","color":"dark_red"},{"text":"]","color":"dark_gray"},{"text":"[","color":"dark_gray"},{"text":"Config","color":"purple"},{"text":"]","color":"dark_gray"},{"text":" Ready to load config number ","color": green,"bold":true,"italic":false},{"text":"'+str(List[int(e.npc.getTempdata().get("ConfigToRead"))])+'", "color" : dark_green, "underlined" : true}]')



def Despawn(e):
    if e.npc.world.getTempdata().get("ConfigMode") != True:
        e.npc.despawn()


def tick(e):
    Despawn(e)
