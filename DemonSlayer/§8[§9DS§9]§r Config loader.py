import random
import math
import os
#API Link :http://www.kodevelopment.nl/customnpcs/api/1.8.9/
#Credits : Script DS vs Bots config loader By Natsu91

#===================================#
#_______{ Creating Algorithm }______#
#===================================#


def LoadConfig(e):
    Path = os.path.dirname(os.path.abspath("__file__"))
    Path += "\\CustomNPC Config\\DS\\config\\config"
    Path = Path.replace("\\", str(os.path.sep))
    with open (str(Path)+".txt", "r") as Config :
        Config = Config.read()
        Config = Config.split(u'\n')
        Name = Config[0]
        e.npc.world.getStoreddata().put("ConfigName", str(Name))
        del Config[0]
        ToConfigList = ["BotNumber","PvPTime","FinalBorder","SecondBorder","FirstBorder","TimeBomb","CutClean","HasteyBoys","NoCleanUpEnabled","CatEyes","MasterLevel","SuperHeroes","BookCeption","DoubleHealth","BleedingSweets","Rodless","OneShot","GoldenHeads","AbsoLess","WaterAllowed","ForcedType","KBValue","ArcticMeta","XpMultiplicator","LoadTeams","AppleRate","FlintRate","ThunderStrike","WitherSoundI","WitherSoundII","IronGolemSound","VanillaDeathStyle","ExplodeOnDeath","NoCleanRegen","BleedingDiamond","BleedingIron","BleedingGold","TimeBombExplode","TimeBombTime"]
        RoleList = ["Tanjiro","Zenitsu","Inosuke","Kagaya","Tomioka","Shinobu","Kyojuro","Tengen","Muichiro","Mitsuri","Sanemi","Obanai","Gyomei","Urokodaki","Kanae","Sabito","Kanao","Genya","Hotaru","Slayer","Jigoro","Yoriichi","Shinjuro","Muzan","Nakime","Kokushibo","Doma","Akaza","Gyokko","Daki","Gyutaro","Rui","Kaigaku","Sasumaru","Kyogai","Yahaba","Kumo","Furuto","Nezuko","Demon"]
        NewRolesList = []

    for i in range (len(Config)-1, -1, -1):
        if Config[i] == "" :
            del Config[i]
        elif Config[i] == " " :
            del Config[i]
        elif Config[i][0] == "#" :
            del Config[i]
        elif Config[i] == u'\r' :
            del Config[i]
        elif Config[i] == u'\n' :
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

        if i == len(ToConfigList)-1:            #Start Loading Roles
            for j in range(i, len(RoleList)+i):
                List = Config[j+1].split(":")
                for k in range(0, int(List[1])):
                    NewRolesList.append(RoleList[j-i])
            
            e.npc.world.getTempdata().put("RolesList", NewRolesList)

    e.npc.world.getTempdata().put("ListOfTakenNames", [])
    e.npc.executeCommand('/tellraw @a ["",{"text":"[","color":"dark_gray"},{"text":"DS","color":"dark_red"},{"text":"]","color":"dark_gray"},{"text":"[","color":"dark_gray"},{"text":"Config","color":"purple"},{"text":"]","color":"dark_gray"},{"text":" Loaded config ","color": green,"bold":true,"italic":false},{"text":"'+str(Name)+'", "color" : dark_green, "underlined" : true} , { "text" :" succesfully", "color" : green, "bold":true}]')


def interact(e):
    e.npc.world.getStoreddata().clear()
    LoadConfig(e)
    e.setCanceled(True)

def damaged(e):
    e.setCanceled(True)

    e.npc.executeCommand('/tellraw @a ["",{"text":"[","color":"dark_gray"},{"text":"DS","color":"dark_red"},{"text":"]","color":"dark_gray"},{"text":"[","color":"dark_gray"},{"text":"Config","color":"purple"},{"text":"]","color":"dark_gray"},{"text":" Ready to load config number ","color": green,"bold":true,"italic":false},{"text":"1", "color" : dark_green, "underlined" : true}]')



def Despawn(e):
    if e.npc.world.getTempdata().get("ConfigMode") != True:
        e.npc.despawn()


def tick(e):
    Despawn(e)
