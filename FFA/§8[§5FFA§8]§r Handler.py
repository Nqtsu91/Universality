
import os
import math
import random

def Config(e):
    # Filling zone
    e.npc.executeCommand('/fill -20 200 10 -40 200 -10 minecraft:stained_glass')
    e.npc.executeCommand('/fill -20 201 10 -20 205 -10 minecraft:stained_glass_pane 5')
    e.npc.executeCommand('/fill -20 201 10 -40 205 10 minecraft:stained_glass_pane 5')
    e.npc.executeCommand('/fill -20 201 -10 -40 205 -10 minecraft:stained_glass_pane 5')
    e.npc.executeCommand('/fill -40 201 -10 -40 205 10 minecraft:stained_glass_pane 5')
    e.npc.executeCommand('/fill -30 200 0 -30 201 0 minecraft:bedrock')
    e.npc.executeCommand("/setblock -31 201 0 minecraft:stone_slab")
    e.npc.executeCommand("/setblock -29 201 0 minecraft:stone_slab")
    e.npc.executeCommand("/setblock -30 201 -1 minecraft:stone_slab")
    e.npc.executeCommand("/setblock -30 201 1 minecraft:stone_slab")

    # Teleporting Host
    e.npc.executeCommand('/tp '+str(e.source.getName())+' -30 203 0')
    e.npc.executeCommand('/title '+str(e.source.getName())+' times 20 40 20')
    e.npc.executeCommand('/title '+str(e.source.getName())+' subtitle ["",{"text":"You can now ","color":"gray"},{"text":"edit","color":"green"},{"text":" or ","color":"gray"},{"text":"load","color":"aqua"},{"text":" a config","color":"gray"}]')
    e.npc.executeCommand('/title '+str(e.source.getName())+' title {"text":"Config Mode","color":"gold"}')


    e.npc.world.getTempdata().put("ConfigMode", True)
    e.npc.executeCommand('/fill -22 200 0 -22 201 0 minecraft:bedrock')
    e.npc.executeCommand("/setblock -23 201 0 minecraft:stone_slab")
    e.npc.executeCommand("/setblock -21 201 0 minecraft:stone_slab")
    e.npc.executeCommand("/setblock -22 201 -1 minecraft:stone_slab")
    e.npc.executeCommand("/setblock -22 201 1 minecraft:stone_slab")

    Total = 0
    TierToList = ["NoobTier","CasualTier","CommonTier","GoodTier","ProTier","UHCEliteTier"]
    ToSend = ["NameTierNoobTier","NameTierCasualTier","NameTierCommonTier","NameTierGoodTier","NameTierProTier","NameTierUHCEliteTier"]
    for i in range (0, len(TierToList)):
        Path = os.path.dirname(os.path.abspath("__file__"))
        Path += "\\CustomNPC Config\\FFA\\Pseudos\\"
        Path = Path.replace("\\", str(os.path.sep))
        with open (str(Path)+str(TierToList[i])+".txt", "r") as TierList :
            TierList = TierList.read()
            TierList = TierList.split(u"\n")
            e.npc.world.getTempdata().put(str(ToSend[i]), TierList)
            Total += len(TierList)

    # Spawning NPCs
    e.npc.world.spawnClone(-22, 203, 0, 3, "Handler").getDisplay().setName("Ready")
    e.npc.executeCommand('/gamemode 2 @a')
    e.npc.world.spawnClone(-30, 203, -8, 3, "Config Loader")

def Inv(e):
    # Filling zone
    e.npc.executeCommand('/fill 20 200 10 40 200 -10 minecraft:stained_glass')
    e.npc.executeCommand('/fill 20 201 10 20 205 -10 minecraft:stained_glass_pane 3')
    e.npc.executeCommand('/fill 20 201 10 40 205 10 minecraft:stained_glass_pane 3')
    e.npc.executeCommand('/fill 20 201 -10 40 205 -10 minecraft:stained_glass_pane 3')
    e.npc.executeCommand('/fill 40 201 -10 40 205 10 minecraft:stained_glass_pane 3')
    e.npc.executeCommand('/fill 30 200 0 30 201 0 minecraft:bedrock')
    e.npc.executeCommand("/setblock 31 201 0 minecraft:stone_slab")
    e.npc.executeCommand("/setblock 29 201 0 minecraft:stone_slab")
    e.npc.executeCommand("/setblock 30 201 -1 minecraft:stone_slab")
    e.npc.executeCommand("/setblock 30 201 1 minecraft:stone_slab")

    # Teleporting Host
    e.npc.executeCommand('/tp '+str(e.source.getName())+' 30 203 0')
    e.npc.executeCommand('/title '+str(e.source.getName())+' times 20 40 20')
    e.npc.executeCommand('/title '+str(e.source.getName())+' subtitle ["",{"text":"You can now ","color":"gray"},{"text":"custom","color":"green"},{"text":" or ","color":"gray"},{"text":"load","color":"aqua"},{"text":" an inventory","color":"gray"}]')
    e.npc.executeCommand('/title '+str(e.source.getName())+' title {"text":"Inventory Mode","color":"gold"}')


    e.npc.world.getTempdata().put("InvMode", True)
    e.npc.executeCommand('/fill 22 200 0 22 201 0 minecraft:bedrock')
    e.npc.executeCommand("/setblock 23 201 0 minecraft:stone_slab")
    e.npc.executeCommand("/setblock 21 201 0 minecraft:stone_slab")
    e.npc.executeCommand("/setblock 22 201 -1 minecraft:stone_slab")
    e.npc.executeCommand("/setblock 22 201 1 minecraft:stone_slab")

    e.npc.executeCommand('/fill 38 200 0 38 201 0 minecraft:bedrock')
    e.npc.executeCommand("/setblock 39 201 0 minecraft:stone_slab")
    e.npc.executeCommand("/setblock 37 201 0 minecraft:stone_slab")
    e.npc.executeCommand("/setblock 38 201 -1 minecraft:stone_slab")
    e.npc.executeCommand("/setblock 38 201 1 minecraft:stone_slab")

    # Spawning NPCs
    e.npc.world.spawnClone(22, 203, 0, 3, "Handler").getDisplay().setName("Inv Ready")
    if e.npc.world.getTempdata().get("CurrentGame") == "bow":
        e.npc.world.spawnClone(38, 203, 0, 3, "Bow mode")
    else:
        e.npc.world.spawnClone(38, 203, 0, 3, "Melee mode")

    e.npc.executeCommand('/gamemode 2 @a')
    

def ClearConfig(e):
    # Teleporting Host
    e.npc.executeCommand('/tp '+str(e.source.getName())+' 0 201 0')
    e.npc.executeCommand('/tellraw '+str(e.source.getName())+' ["",{"text":"[","color":"dark_gray"},{"text":"FFA","color":"dark_red"},{"text":"]","color":"dark_gray"},{"text":" Changes saved ","color":"gray"},{"text":"successfully","color":"dark_green"}]')
    # Clearing hub
    e.npc.executeCommand('/fill -19 200 11 -40 205 -11 minecraft:air')
    e.npc.world.getTempdata().put("ConfigMode", False)


def ClearInv(e):
    # Teleporting Host
    e.npc.executeCommand('/tp '+str(e.source.getName())+' 0 201 0')
    e.npc.executeCommand('/tellraw '+str(e.source.getName())+' ["",{"text":"[","color":"dark_gray"},{"text":"FFA","color":"dark_red"},{"text":"]","color":"dark_gray"},{"text":" Changes saved ","color":"gray"},{"text":"successfully","color":"dark_green"}]')

    # Clearing hub
    e.npc.executeCommand('/fill 19 200 11 40 205 -11 minecraft:air')
    e.npc.world.getTempdata().put("InvMode", False)
    e.npc.executeCommand('/gamemode 2 @a')




#=================================
# Utility


def Despawn(e):
    Name = str(e.npc.getDisplay().getName())
    if (Name == "Ready") and ( e.npc.world.getTempdata().get("ConfigMode") != True):
        e.npc.despawn()
    elif (Name == "Inv Ready") and ( e.npc.world.getTempdata().get("InvMode") != True):
        e.npc.despawn()   

def Redirect(e):
    Name = str(e.npc.getDisplay().getName())
    if Name == "Config" :
        Config(e)
    elif Name == "Ready" :
        ClearConfig(e)
    elif Name == "See inventories":
        Inv(e)
    elif Name == "Inv Ready":
        ClearInv(e)



#=================================
# Hooks



def damaged(e):
    try:
        Redirect(e)
    except:
        pass
    e.setCanceled(True)


def tick(e):
    Despawn(e)


def interact(e):
    e.npc.executeCommand('/tellraw @a ["",{"text":"[","color":"dark_gray"},{"text":"FFA","color":"dark_red"},{"text":"]","color":"dark_gray"},{"text":" Hit the ","color":"gray"},{"text":"\"Ready\"","color":"green"},{"text":" NPC to save your changes","color":"gray"}]')
    e.setCanceled(True)