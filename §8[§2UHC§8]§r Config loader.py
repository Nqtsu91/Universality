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
        e.npc.getTempdata().put("ConfigToRead", 1)
    Path = os.path.dirname(os.path.abspath("__file__"))
    Path += "\\CustomNPC Config\\UHC\\configs\\config_"
    Path = Path.replace("\\", str(os.path.sep))
    with open (str(Path)+str(e.npc.getTempdata().get("ConfigToRead"))+".txt", "r") as Config :
        Config = Config.read()
        Config = Config.split(\n)
        Name = Config[0]
        e.npc.world.getStoreddata().put("ConfigName", str(Name))
        del Config[0]
        ToConfigList = ["CutClean","NoCleanUpEnabled","CatEyes","MasterLevel","SuperHeroes","BookCeption","DoubleHealth","OneShot","BleedingSweets","Rodless","Mole","GoldenHeads","FireAspectAllowed","AbsoLess","RedditUHCDisplay","BadlionKillsSystem","ThunderStrike","WitherSoundI","WitherSoundII","IronGolemSound","VanillaDeathStyle","ExplodeOnDeath","BotNumber","TeamSize","PvPTime","MinTimeSpread","MaxTimeSpread","NoCleanRegen","DiamondProbability","BleedingDiamond","BleedingIron","BleedingGold","MolePerTeam","WaterAllowed","ForcedType","BadlionKB","ArcticMeta","ScatterMessageEnabled","XpMultiplicator","LoadTeams","FinalBorder","SecondBorder","FirstBorder","AppleRate","FlintRate","LoadInventory"]

    for i in range (len(Config)-1, -1, -1):
        if Config[i][0] == "#" :
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
    e.npc.executeCommand('/tellraw @a ["",{"text":"[","color":"dark_gray"},{"text":"UHC","color":"dark_red"},{"text":"]","color":"dark_gray"},{"text":"[","color":"dark_gray"},{"text":"Config","color":"purple"},{"text":"]","color":"dark_gray"},{"text":" Loaded config ","color": green,"bold":true,"italic":false},{"text":"'+str(Name)+'", "color" : dark_green, "underlined" : true} , { "text" :" succesfully", "color" : green, "bold":true}]')


def interact(e):
    e.npc.world.getStoreddata().clear()
    LoadConfig(e)
    e.setCanceled(True)

def damaged(e):
    e.setCanceled(True)
    if e.npc.getTempdata().get("ConfigToRead") == None :
        e.npc.getTempdata().put("ConfigToRead", 1)
    if e.npc.getTempdata().get("ConfigToRead") == 10 :
        e.npc.getTempdata().put("ConfigToRead", 1)
    else:
        e.npc.getTempdata().put("ConfigToRead", e.npc.getTempdata().get("ConfigToRead")+1)

    e.npc.executeCommand('/tellraw @a ["",{"text":"[","color":"dark_gray"},{"text":"UHC","color":"dark_red"},{"text":"]","color":"dark_gray"},{"text":"[","color":"dark_gray"},{"text":"Config","color":"purple"},{"text":"]","color":"dark_gray"},{"text":" Ready to load config number ","color": green,"bold":true,"italic":false},{"text":"'+str(e.npc.getTempdata().get("ConfigToRead"))+'", "color" : dark_green, "underlined" : true}]')

