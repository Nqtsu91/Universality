import random
import math
#API Link :http://www.kodevelopment.nl/customnpcs/api/1.8.9/
#Credits : Script UHC vs Bots Settings By Natsu91

#===================================#
#_______{ Creating Algorithm }______#
#===================================#

def GettingVarToMod(e):
    CurrentVarToMod = e.npc.world.getTempdata().get("CurrentVarToMod")
    return CurrentVarToMod


def ModifingVar(e):
    Name = e.npc.getDisplay().getName()
    VarToMod = GettingVarToMod(e)
    VarToAdd = ["BotNumber","TeamSize","TeamAliveLimit","PvPTime","MinTimeSpread","MaxTimeSpread","FinalBorder","SecondBorder","FirstBorder","DiamondProbability","EnchantProbability","XpMultiplicator","AppleRate","FlintRate","NoCleanRegen","BleedingDiamond","BleedingIron","BleedingGold","MolePerTeam","TimeBombTime","KBValue","StartDeathmatchAt"]
    VarToReWrite = ['MeetUpMode',"ClearedLoot","TimeBomb","CutClean","HasteyBoys","NoCleanUpEnabled","CatEyes","MasterLevel","SuperHeroes","BookCeption","DoubleHealth","BleedingSweets","Rodless","Mole","OneShot","GoldenHeads","FireAspectAllowed","AbsoLess","WaterAllowed","ForcedType","ArcticMeta","LoadTeams","RedditUHCDisplay","BadlionKillsSystem","ThunderStrike","WitherSoundI","WitherSoundII","IronGolemSound","VanillaDeathStyle","ExplodeOnDeath","ScatterMessageEnabled","TimeBombExplode"]
    if VarToMod in VarToAdd :
		VarValue = e.npc.world.getTempdata().get(VarToMod)
		if VarValue == None :
			VarValue = 0
		NameToInt = int(Name)
		VarModed = ( VarValue + NameToInt )
		e.npc.world.getTempdata().put(str(VarToMod), VarModed)
		VarValue = e.npc.world.getTempdata().get(VarToMod)
		e.npc.executeCommand('/tellraw @a ["",{"text":"[","color":"dark_gray"},{"text":"UHC","color":"dark_red"},{"text":"][","color":"dark_gray"},{"text":"Config"},{"text":"]","color":"dark_gray"},{"text":" Added ","color":"gray"},{"text":"'+str(Name)+'","color":"dark_red"},{"text":" to ","color":"gray"},{"text":"'+str(VarToMod)+'","color":"green"},{"text":" (Now","color":"white"},{"text":" '+str(VarValue)+'","color":"aqua"},{"text":")","color":"white"}]')

		
    elif VarToMod in VarToReWrite :
        VarValue = e.npc.world.getTempdata().get(str(VarToMod))
        if VarValue == None:
            VarValue = False
        if VarValue == True :
            e.npc.world.getTempdata().put(str(VarToMod), False)
            e.npc.executeCommand('/tellraw @a ["",{"text":"[","color":"dark_gray"},{"text":"UHC","color":"dark_red"},{"text":"][","color":"dark_gray"},{"text":"Config"},{"text":"]","color":"dark_gray"},{"text":" Set","color":"gray"},{"text":" '+str(VarToMod)+'","color":"blue"},{"text":" to","color":"gray"},{"text":" False","color":"red"}]')
        elif VarValue == False :
            e.npc.world.getTempdata().put(str(VarToMod), True)
            e.npc.executeCommand('/tellraw @a ["",{"text":"[","color":"dark_gray"},{"text":"UHC","color":"dark_red"},{"text":"][","color":"dark_gray"},{"text":"Config"},{"text":"]","color":"dark_gray"},{"text":" Set","color":"gray"},{"text":" '+str(VarToMod)+'","color":"blue"},{"text":" to","color":"gray"},{"text":" True","color":"green"}]')	
	else:
		e.npc.say("Error")
		e.npc.say(str(VarValue))
		
def Switching(e):
	CurrentConfig = e.npc.world.getTempdata().get("CurrentConfig")
	Tick = e.npc.world.getTempdata().get("Tick")
	Tick -= 1
	if CurrentConfig == "Scenarios" :
		ListOfVar = ["HasteyBoys","TimeBomb","CutClean","BadlionKillsSystem","NoCleanUpEnabled","ThunderStrike","WitherSoundI","WitherSoundII","IronGolemSound","WaterAllowed","CatEyes","MasterLevel","SuperHeroes","BookCeption","DoubleHealth","OneShot","BleedingSweets","Rodless","Mole","RedditUHCDisplay","GoldenHeads","ExplodeOnDeath","FireAspectAllowed","AbsoLess","ForcedType","ArcticMeta","ScatterMessageEnabled","FinalBorder","SecondBorder","FirstBorder","AppleRate","FlintRate","TimeBombExplode","TimeBombTime","StartDeathmatchAt"]
		e.npc.world.getTempdata().put("CurrentVarToMod" , ListOfVar[Tick])
		e.npc.executeCommand('/tellraw @a ["",{"text":"[","color":"dark_gray"},{"text":"UHC","color":"dark_red"},{"text":"][","color":"dark_gray"},{"text":"Config"},{"text":"]","color":"dark_gray"},{"text":" Now editing :","color":"gray"},{"text":" '+ListOfVar[Tick]+'","color":"blue"}]')
	
	elif CurrentConfig == "Bots" :
		ListOfVar = ["BotNumber","TeamSize","TeamAliveLimit","DiamondProbability","KBValue","NoCleanRegen","BleedingDiamonds","BleedingIron","BleedingGold","PvPTime","MinTimeSpread","MaxTimeSpread","MolePerTeam"]
		e.npc.world.getTempdata().put("CurrentVarToMod" , ListOfVar[Tick])
		e.npc.executeCommand('/tellraw @a ["",{"text":"[","color":"dark_gray"},{"text":"UHC","color":"dark_red"},{"text":"][","color":"dark_gray"},{"text":"Config"},{"text":"]","color":"dark_gray"},{"text":" Now editing :","color":"gray"},{"text":" '+ListOfVar[Tick]+'","color":"blue"}]')



def damaged(e):
	try:
		if e.npc.getDisplay().getName() == "Change Variable" :
			Tick = e.npc.world.getTempdata().get("Tick")
			CurrentConfig = e.npc.world.getTempdata().get("CurrentConfig")
			if CurrentConfig == "Scenarios" :
				if (Tick == 35):
					Tick = 0
					e.npc.world.getTempdata().put("Tick", 0)
			if CurrentConfig == "Bots" and (Tick == 12):
				Tick = 0
				e.npc.world.getTempdata().put("Tick", 0)
			else :
				Tick += 1
				e.npc.world.getTempdata().put("Tick", Tick)
			Switching(e)	
		elif e.npc.getDisplay().getName() == "Config Bots" :
			e.npc.world.getTempdata().put("CurrentConfig", "Bots")
			e.npc.world.getTempdata().put("Tick", 0)
			e.npc.executeCommand('/tellraw @a ["",{"text":"[","color":"dark_gray"},{"text":"UHC","color":"dark_red"},{"text":"][","color":"dark_gray"},{"text":"Config"},{"text":"]","color":"dark_gray"},{"text":" You can now edit : ","color":"gray"},{"text":"Bots settings","color":"dark_green"}]')
		elif e.npc.getDisplay().getName() == "Config Scenarios" :
			e.npc.world.getTempdata().put("CurrentConfig", "Scenarios")
			e.npc.world.getTempdata().put("Tick", 0)
			e.npc.executeCommand('/tellraw @a ["",{"text":"[","color":"dark_gray"},{"text":"UHC","color":"dark_red"},{"text":"][","color":"dark_gray"},{"text":"Config"},{"text":"]","color":"dark_gray"},{"text":" You can now edit : ","color":"gray"},{"text":"Scenarios","color":"dark_blue"}]')
		else :
			ModifingVar(e)
		e.setCanceled(True)
	except:
		e.setCanceled(True)


def Despawn(e):
    if e.npc.world.getTempdata().get("ConfigMode") != True:
        e.npc.despawn()


def tick(e):
    Despawn(e)




