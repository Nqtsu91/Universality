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
    VarToAdd = ["BotNumber","TeamSize","DiamondProbability","NoCleanRegen","BleedingDiamonds","BleedingIron","BleedingGold","PvPTime","MinTimeSpread","MaxTimeSpread","MolePerTeam"]
    VarToReWrite = ["BadlionKillsSystem","NoCleanUpEnabled","ThunderStrike","WitherSoundI","WitherSoundII","IronGolemSound","WaterAllowed","CatEyes","MasterLevel","SuperHeroes","BookCeption","DoubleHealth","OneShot","BleedingSweets","Rodless","Mole","RedditUHCDisplay","GoldenHeads","ExplodeOnDeath","FireAspectAllowed","AbsoLess","ForcedType","BadlionKB","ArcticMeta","ScatterMessageEnabled","CreateBorder"]
    if VarToMod in VarToAdd :
		VarValue = e.npc.world.getTempdata().get(VarToMod)
		if VarValue == None :
			VarValue = 0
		NameToInt = int(Name)
		VarModed = ( VarValue + NameToInt )
		e.npc.world.getTempdata().put(str(VarToMod), VarModed)
		VarValue = e.npc.world.getTempdata().get(VarToMod)
		e.npc.executeCommand('/tellraw @a ["",{"text":"[","color": green,"bold":true},{"text":"UHCHandler","color" : dark_green},{"text":"] ","color": green,"bold":true},{ "text" :"Added ","color" : green},{ "text" :"'+str(Name)+'","color" : aqua,"bold":true},{"text":" to the value","color": aqua},{"text" :"'+str(VarToMod)+'","color" : aqua,"bold":true},{"text":" which is now at ","color": green},{ "text" :"'+str(VarValue)+'","color" : red,"bold":true}]')

		
    elif VarToMod in VarToReWrite :
        VarValue = e.npc.world.getTempdata().get(str(VarToMod))
        if VarValue == None:
            VarValue = False
        if VarValue == True :
            e.npc.world.getTempdata().put(str(VarToMod), False)
            e.npc.executeCommand('/tellraw @a ["",{"text":"[","color": green,"bold":true},{"text":"UHCHandler","color" : dark_green},{"text":"] ","color": green,"bold":true},{ "text" :"'+str(VarToMod)+'","color" : aqua,"bold":true},{"text":" is now set to ","color": aqua},{"text":" False","color": red,"bold":true}]')
        elif VarValue == False :
            e.npc.world.getTempdata().put(str(VarToMod), True)
            e.npc.executeCommand('/tellraw @a ["",{"text":"[","color": green,"bold":true},{"text":"UHCHandler","color" : dark_green},{"text":"] ","color": green,"bold":true},{ "text" :"'+str(VarToMod)+'","color" : aqua,"bold":true},{"text":" is now set to ","color": aqua},{"text":" True","color": red,"bold":true}]')
	else:
		e.npc.say("Error")
		e.npc.say(str(VarValue))
		
def Switching(e):
	CurrentConfig = e.npc.world.getTempdata().get("CurrentConfig")
	Tick = e.npc.world.getTempdata().get("Tick")
	Tick -= 1
	if CurrentConfig == "Scenarios" :
		ListOfVar = ["BadlionKillsSystem","NoCleanUpEnabled","ThunderStrike","WitherSoundI","WitherSoundII","IronGolemSound","WaterAllowed","CatEyes","MasterLevel","SuperHeroes","BookCeption","DoubleHealth","OneShot","BleedingSweets","Rodless","Mole","RedditUHCDisplay","GoldenHeads","ExplodeOnDeath","FireAspectAllowed","AbsoLess","ForcedType","BadlionKB","ArcticMeta","ScatterMessageEnabled","CreateBorder"]
		e.npc.world.getTempdata().put("CurrentVarToMod" , ListOfVar[Tick])
		e.npc.executeCommand('/tellraw @a ["",{"text":"[","color": green,"bold":true},{"text":"UHCHandler","color" : dark_green},{"text":"] ","color": green,"bold":true},{ "text" :"You will now modify the scenario : ","color" : aqua,"bold":true},{"text":"'+ListOfVar[Tick]+'","color": red,"bold":true}]')
	
	elif CurrentConfig == "Bots" :
		ListOfVar = ["BotNumber","TeamSize","DiamondProbability","NoCleanRegen","BleedingDiamonds","BleedingIron","BleedingGold","PvPTime","MinTimeSpread","MaxTimeSpread","MolePerTeam"]
		e.npc.world.getTempdata().put("CurrentVarToMod" , ListOfVar[Tick])
		e.npc.executeCommand('/tellraw @a ["",{"text":"[","color": green,"bold":true},{"text":"UHCHandler","color" : dark_green},{"text":"] ","color": green,"bold":true},{ "text" :"You will now modify the value : ","color" : aqua,"bold":true},{"text":"'+ListOfVar[Tick]+'","color": red,"bold":true}]')



def damaged(e):
	try:
		if e.npc.getDisplay().getName() == "Hit me to change variable" :
			Tick = e.npc.world.getTempdata().get("Tick")
			CurrentConfig = e.npc.world.getTempdata().get("CurrentConfig")
			if CurrentConfig == "Scenarios" :
				if (Tick == 26):
					Tick = 0
					e.npc.world.getTempdata().put("Tick", 0)
			if CurrentConfig == "Bots" and (Tick == 10):
				Tick = 0
				e.npc.world.getTempdata().put("Tick", 0)
			else :
				Tick += 1
				e.npc.world.getTempdata().put("Tick", Tick)
			Switching(e)	
		elif e.npc.getDisplay().getName() == "Config Bots" :
			e.npc.world.getTempdata().put("CurrentConfig", "Bots")
			e.npc.world.getTempdata().put("Tick", 0)
			e.npc.executeCommand('/tellraw @a ["",{"text":"[","color": green,"bold":true},{"text":"UHCHandler","color" : dark_green},{"text":"] ","color": green,"bold":true},{ "text" :"You will now modify the in-game ","color" : aqua,"bold":true},{"text":" bots settings and team size","color": red,"bold":true}]')
		elif e.npc.getDisplay().getName() == "Config Scenarios" :
			e.npc.world.getTempdata().put("CurrentConfig", "Scenarios")
			e.npc.world.getTempdata().put("Tick", 0)
			e.npc.executeCommand('/tellraw @a ["",{"text":"[","color": green,"bold":true},{"text":"UHCHandler","color" : dark_green},{"text":"] ","color": green,"bold":true},{ "text" :"You will now modify the in-game ","color" : aqua,"bold":true},{"text":" scenarios","color": red,"bold":true}]')
		else :
			ModifingVar(e)
		e.setCanceled(True)
	except:
		e.setCanceled(True)

