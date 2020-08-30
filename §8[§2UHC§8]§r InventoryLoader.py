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
    Path += "\\CustomNPC Config\\UHC\\inventories\\inventory_"
    Path = Path.replace("\\", str(os.path.sep))
    with open (str(Path)+str(e.npc.getTempdata().get("InvToRead"))+".txt", "w") as Config :
        for i in range(0, len(e.player.getInventory())):
            try:
                Config.write(str(e.player.getInventory()[i].getName()))
                Config.write("//")
                Config.write(str(e.player.getInventory()[i].getStackSize()))
                Config.write("//")
                Config.write(str(e.player.getInventory()[i].getItemDamage()))
                Config.write("//")
                Config.write(str(e.player.getInventory()[i].getTag("ench")))
                Config.write(u'\n')
            except:
                pass
    e.npc.executeCommand('/tellraw @p ["",{"text":"[","color":"dark_gray"},{"text":"UHC","color":"dark_red"},{"text":"]","color":"dark_gray"},{"text":"[","color":"dark_gray"},{"text":"Inventory","color":"light_purple"},{"text":"]","color":"dark_gray"},{"text":" Saved inventory in slot ","color": aqua,"bold":true,"italic":false},{"text":"'+str(e.npc.getTempdata().get("InvToRead"))+'", "color" : blue, "underlined" : true}]')

def interact(e):
    SaveInventory(e)
    e.setCanceled(True)

def damaged(e):
    if e.npc.getTempdata().get("InvToRead") == None :
        e.npc.getTempdata().put("InvToRead", 1)
    if e.npc.getTempdata().get("InvToRead") == 10 :
        e.npc.getTempdata().put("InvToRead", 1)
    else:
        e.npc.getTempdata().put("InvToRead", e.npc.getTempdata().get("InvToRead")+1)
    e.npc.executeCommand('/tellraw @p ["",{"text":"[","color":"dark_gray"},{"text":"UHC","color":"dark_red"},{"text":"][","color":"dark_gray"},{"text":"Inventory","color":"light_purple"},{"text":"]","color":"dark_gray"},{"text":" Slot selected :","color":"gray"},{"text":" '+str(e.npc.getTempdata().get("InvToRead"))+'","color":"aqua"}]')
    e.setCanceled(True)

def Despawn(e):
    if e.npc.world.getTempdata().get("InvMode") != True:
        e.npc.despawn()


def tick(e):
    Despawn(e)
