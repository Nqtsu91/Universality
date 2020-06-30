import random
import math
#API Link :http://www.kodevelopment.nl/customnpcs/api/1.8.9/
#Credits : Script UHC vs Bots config loader By Natsu91

#===================================#
#_______{ Creating Algorithm }______#
#===================================#


def LoadConfig(e):
    with open ("C:\\Program Files (x86)\\CustomNPC Config\\UHC\\config.txt", "r") as Config :
        Config = Config.read()
        Config = Config.split(\n)
        Name = Config[0]
        del Config[0]
        ToConfigList = ["NoCleanUpEnabled","CatEyes","MasterLevel","SuperHeroes","BookCeption","DoubleHealth","OneShot","BleedingSweets","Rodless","Mole","GoldenHeads","FireAspectAllowed","AbsoLess","RedditUHCDisplay","BadlionKillsSystem","ThunderStrike","WitherSoundI","WitherSoundII","IronGolemSound","VanillaDeathStyle","ExplodeOnDeath","BotNumber","TeamSize","PvPTime","MinTimeSpread","MaxTimeSpread","NoCleanRegen","DiamondProbability","BleedingDiamond","BleedingIron","BleedingGold","MolePerTeam","WaterAllowed","ForcedType","BadlionKB","ArcticMeta","ScatterMessageEnabled","CreateBorder","LoadTeams"]

    for i in range (len(Config)-1, -1, -1):
        if Config[i][0] == "#" :
            del Config[i]
    for i in range (0, len(ToConfigList)):
        List = Config[i].split(":")
        try :
            e.npc.world.getTempdata().put(str(ToConfigList[i]), int(List[1]))
            e.npc.say(str(ToConfigList[i]))
        except:
            if List[1] == "True":
                List[1] = True
            else :
                List[1] = False  
            e.npc.world.getTempdata().put(str(ToConfigList[i]), List[1])
    e.npc.executeCommand('/tellraw @a ["",{"text":"Loaded config ","color": green,"bold":true,"italic":true},{"text":"'+str(Name)+' ", "color" : dark_green} , { "text" :"succesfully", "color" : green, "bold":true}]')


def interact(e):
    e.npc.world.getStoreddata().clear()
    LoadConfig(e)

