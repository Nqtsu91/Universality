import random
import math
#API Link :http://www.kodevelopment.nl/customnpcs/api/1.8.9/
#Credits : Script UHC vs Bots BotScatteringV4 By Natsu91

#===================================#
#_______{ Creating Algorithm }______#
#===================================#

def AcceptFate(e):
    Source = e.player.getName()
    Killer = e.npc.world.getTempdata().get(str(Source)+"Killer")
    KilledKills = e.npc.world.getStoreddata().get(str(Source) +"Kills")

    e.npc.world.getStoreddata().put("Players", e.npc.world.getStoreddata().get("Players")-1)

    if e.npc.world.getTempdata().get("PlayerDeads") == None :
        e.npc.world.getTempdata().put("PlayerDeads", len(e.npc.world.getAllPlayers())-1)
    else :
        e.npc.world.getTempdata().put("PlayerDeads", e.npc.world.getTempdata().get("PlayerDeads")-1)

    e.npc.executeCommand("/gamemode 3 @p")

    NameKiller = Killer[0]
    KillerFaction = int(Killer[1])
    KillerKills = Killer[2]
    FactionArgList = [["green","false","false"],["green","false","false"],["blue","false","false"],["red","false","false"],["yellow","false","false"],["dark_gray","false","false"],["dark_blue","false","false"],["dark_red","false","false"],["dark_green","false","false"],["gold","false","false"],["aqua","false","false"],["light_purple","false","false"],["dark_aqua","false","false"],["dark_purple","false","false"],["green","false","true"],["blue","false","true"],["red","false","true"],["yellow","false","true"],["dark_gray","false","true"],["dark_blue","false","true"],["dark_red","false","true"],["dark_green","false","true"],["gold","false","true"],["aqua","false","true"],["light_purple","false","true"],["dark_aqua","false","true"],["dark_purple","false","true"]]
    TeamColorKiller = FactionArgList[KillerFaction][0]
    UnderlinedKiller = FactionArgList[KillerFaction][1]
    ItalicKiller = FactionArgList[KillerFaction][2]


    if e.npc.world.getTempdata().get("BadlionKillsSystem") == True :
        e.npc.executeCommand('/tellraw @a ["",{"text":"[","color":"dark_gray"},{"text":"UHC","color":"dark_red"},{"text":"] ","color":"dark_gray"},{"text":"'+str(Source)+'"},{"text":"[","color":"white"},{"text":"'+str(int(KilledKills))+'","color":"white"},{"text":"]","color":"white"},{"text":" was slain by ","color":"gray"},{"text":"'+str(NameKiller)+'","color":"'+str(TeamColorKiller)+'","underlined":"'+str(UnderlinedKiller)+'","italic":"'+str(ItalicKiller)+'"},{"text":"[","color":"white"},{"text":"'+str(KillerKills) +'","color":"white"},{"text":"]","color":"white"}]')
    else:
        e.npc.executeCommand('/tellraw @a ["",{"text":"[","color":"dark_gray"},{"text":"UHC","color":"dark_red"},{"text":"] ","color":"dark_gray"},{"text":"'+str(Source)+'"},{"text":" was slain by ","color":"gray"},{"text":"'+str(NameKiller)+'","color":"'+str(TeamColorKiller)+'","underlined":"'+str(UnderlinedKiller)+'","italic":"'+str(ItalicKiller)+'"}]')
  
    if e.npc.world.getTempdata().get("PlayerDeads") == 0 or e.npc.world.getTempdata().get("PlayerDeads") == 0.0 :
        e.npc.executeCommand('/tellraw @a ["",{"text":"[","color":"dark_gray"},{"text":"UHC","color":"dark_red"},{"text":"] ","color":"dark_gray"},{"text":"Team ","color":"gray"},{"text":"Players, is now eliminated","color":"red"}]')


def NeverDie(e):
    e.npc.executeCommand("/tp @p 0 85 0")

#===============================#
#_______{ Calling Events }______#
#===============================#

def interact(e):
    GameStarted = e.npc.world.getTempdata().get("GameStarted")
    if GameStarted == 1:
        if e.npc.getDisplay().getName() == "Accept Fate" :
            try:
                AcceptFate(e)
            except:
                e.npc.executeCommand('/tellraw @p ["",{"text":"[","color":"dark_gray"},{"text":"UHC","color":"dark_red"},{"text":"] ","color":"dark_gray"},{"text":"We ran into a problem, sorry !","color":"gray"}]')
        else :
            NeverDie(e)





