import random
import math
import os
#API Link :http://www.kodevelopment.nl/customnpcs/api/1.8.9/
#Credits : Script UHC vs Bots config loader By Natsu91

#===================================#
#_______{ Creating Algorithm }______#
#===================================#


def SaveInventory(e):
    Path = os.path.dirname(os.path.abspath("__file__"))
    Path += "\\CustomNPC Config\\FFA\\Ally\\"
    Path = Path.replace("\\", str(os.path.sep))
    with open (str(Path)+"Team.txt", "r") as Config :
        try:
            Config = Config.read()

            TeamMode = e.npc.world.getTempdata().get("TeamSize")
            IdHere = 26   
            X = e.npc.getX()
            Z = e.npc.getZ()
            for i in range (0, TeamMode):
                e.npc.world.spawnClone( 30, 203, 0, 3, "DisabledAlly").setFaction(int(IdHere))             #Spawning a team with the deleted faction id
                e.npc.world.getTempdata().put("26Team", Config)
                e.npc.executeCommand('/give @p customnpcs:npcSoulstoneEmpty')
                e.npc.executeCommand('/setblock 32 201 8 minecraft:ender_chest 4')
        except Exception as eee:
            e.npc.executeCommand('/tellraw @a ["",{"text":"[","color":"dark_gray"},{"text":"Arena","color":"dark_red"},{"text":"][","color":"dark_gray"},{"text":"Team","color":"dark_purple"},{"text":"]","color":"dark_gray"},{"text":" Make sure to load a config first !","color":"gray"}]')
    e.npc.executeCommand('/tellraw @a ["",{"text":"[","color":"dark_gray"},{"text":"Arena","color":"dark_red"},{"text":"][","color":"dark_gray"},{"text":"Ally","color":"yellow"},{"text":"]","color":"dark_gray"},{"text":" - Use the ","color":"gray"},{"text":"SoulStone","color":"white"},{"text":" on your Ally to put them in your pocket !","color":"gray"},{"text":"\n"},{"text":"[","color":"dark_gray"},{"text":"UHC","color":"dark_red"},{"text":"][","color":"dark_gray"},{"text":"Ally","color":"yellow"},{"text":"] ","color":"dark_gray"},{"text":"- Do not forget to put the ","color":"gray"},{"text":"Filled SoulStone","color":"light_purple"},{"text":" in the ","color":"gray"},{"text":"ender chest !","color":"dark_blue"}]')

def interact(e):
    SaveInventory(e)
    e.setCanceled(True)

def damaged(e):
    e.setCanceled(True)

def Despawn(e):
    if e.npc.world.getTempdata().get("InvMode") != True:
        e.npc.despawn()


def tick(e):
    Despawn(e)
