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
    Special = '{"text":"","color":"light_purple"}'
    SpecialKiller = '{"text":"","color":"light_purple"}'
    SpecialList = ["Natsu91","Yvant2000Games","Frizou","iKowz","MASTEEKH","jdegoederen","reb_hi","Strykerss","Etoiles","xGokuuuh","Pikachu","TryHqrd_","_Mik0GODESS","SqndSt0rm","Divinity_Kirito","slooonay","Pxdro","Restump","Nardcoo","Ladak","VERSKUUUH","seltix_x","Pacoima","MarkiLokuras","Boosta","DANTEH","Rzmeur","GrzyLight","Mqyland_hi","Mentally","BiboyQG"]
    try :
        int(KilledKills)
    except:
        KilledKills = 0

    e.npc.world.getStoreddata().put("Players", e.npc.world.getStoreddata().get("Players")-1)

    if e.npc.world.getTempdata().get("PlayerDeads") == None :
        e.npc.world.getTempdata().put("PlayerDeads", len(e.npc.world.getAllPlayers())-1)
    else :
        e.npc.world.getTempdata().put("PlayerDeads", e.npc.world.getTempdata().get("PlayerDeads")-1)

    e.npc.executeCommand("/gamemode 3 @p")

    NameKiller = Killer[0]
    KillerFaction = int(Killer[1])
    KillerKills = Killer[2].split(".")
    KillerKills = KillerKills[0]
    FactionArgList = [["green","false","false"],["green","false","false"],["blue","false","false"],["red","false","false"],["yellow","false","false"],["dark_gray","false","false"],["dark_blue","false","false"],["dark_red","false","false"],["dark_green","false","false"],["gold","false","false"],["aqua","false","false"],["light_purple","false","false"],["dark_aqua","false","false"],["dark_purple","false","false"],["green","false","true"],["blue","false","true"],["red","false","true"],["yellow","false","true"],["dark_gray","false","true"],["dark_blue","false","true"],["dark_red","false","true"],["dark_green","false","true"],["gold","false","true"],["aqua","false","true"],["light_purple","false","true"],["dark_aqua","false","true"],["white","false","false"]]
    TeamColorKiller = FactionArgList[KillerFaction][0]
    UnderlinedKiller = FactionArgList[KillerFaction][1]
    ItalicKiller = FactionArgList[KillerFaction][2]
    
    if NameKiller in SpecialList :
        SpecialKiller = '{"text":"['+u'\u2764'+']","color":"light_purple"}'    

    if Source in SpecialList :
        Special = '{"text":"['+u'\u2764'+']","color":"light_purple"}'

    if e.npc.world.getTempdata().get("BadlionKillsSystem") == True :
        e.npc.executeCommand('/tellraw @a ["",{"text":"[","color":"dark_gray"},{"text":"Arena","color":"dark_red"},{"text":"] ","color":"dark_gray"},'+Special+',{"text":"'+str(Source)+'"},{"text":"[","color":"white"},{"text":"'+str(int(KilledKills))+'","color":"white"},{"text":"]","color":"white"},{"text":" was slain by ","color":"gray"},'+SpecialKiller+',{"text":"'+str(NameKiller)+'","color":"'+str(TeamColorKiller)+'","underlined":"'+str(UnderlinedKiller)+'","italic":"'+str(ItalicKiller)+'"},{"text":"[","color":"white"},{"text":"'+str(int(KillerKills)) +'","color":"white"},{"text":"]","color":"white"}]')
    else:
        e.npc.executeCommand('/tellraw @a ["",{"text":"[","color":"dark_gray"},{"text":"Arena","color":"dark_red"},{"text":"] ","color":"dark_gray"},'+Special+',{"text":"'+str(Source)+'"},{"text":" was slain by ","color":"gray"},'+SpecialKiller+',{"text":"'+str(NameKiller)+'","color":"'+str(TeamColorKiller)+'","underlined":"'+str(UnderlinedKiller)+'","italic":"'+str(ItalicKiller)+'"}]')
  


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
            except Exception as err:
                e.npc.executeCommand('/tellraw @p ["",{"text":"[","color":"dark_gray"},{"text":"UHC","color":"dark_red"},{"text":"] ","color":"dark_gray"},{"text":"We ran into a problem, sorry !","color":"gray"}]')
                e.npc.world.broadcast(str(err))
        else :
            NeverDie(e)


def damaged(e):
    e.setCanceled(True)

