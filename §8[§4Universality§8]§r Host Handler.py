import random
import math

#API Link :http://www.kodevelopment.nl/customnpcs/api/1.8.9/
#Credits : Universality Host Handler by Natsu91

#===================================#
#_______{ Creating Algorithm }______#
#===================================#

# Visual things

def FirstSay(e):
	if e.npc.getStoreddata().get('FirstSay') != True :
		e.npc.executeCommand("/gamerule commandBlockOutput false")
		e.npc.executeCommand("/gamerule keepInventory true")
		e.npc.executeCommand('/tellraw @a ["",{"text":"[","color":"dark_gray"},{"text":"Universality","color":"dark_red"},{"text":"]","color":"dark_gray"},{"text":" Thank for downloading the","color":"gray"},{"text":" Universality scripts","color":"dark_red"},{"text":" !"}]')
		e.npc.executeCommand('/tellraw @a ["",{"text":"[","color":"dark_gray"},{"text":"Universality","color":"dark_red"},{"text":"]","color":"dark_gray"},{"text":" You can start a Host on this map by hitting this NPC","color":"gray"}]')
		e.npc.executeCommand('/tellraw @a ["",{"text":"[","color":"dark_gray"},{"text":"Universality","color":"dark_red"},{"text":"]","color":"dark_gray"},{"text":" Right-click the NPC to change the game you host","color":"gray"}]')
		e.npc.executeCommand('/tellraw @a ["",{"text":"[","color":"dark_gray"},{"text":"Universality","color":"dark_red"},{"text":"] ","color":"dark_gray"},{"text":"Need Help ?","color":"gray"},{"text":" Right click the NPC with the helper item!","color":"dark_green"}]')
		e.npc.getStoreddata().put('FirstSay', True)
		e.npc.executeCommand('/give @a compass 1 0 {display:{Name:Help,Lore:[" Hit the NPC with this item to get help"]}}')
		e.npc.executeCommand('/give @a comparator 1 0 {display:{Name:Start,Lore:[" Hit the NPC with this item to start the host"]}}')
		e.npc.executeCommand('/give @a paper 1 0 {display:{Name:Games list,Lore:[" Hit the NPC with this item to get the list of playable games"]}}')
		e.npc.executeCommand('/tellraw @a ["",{"text":"[","color":"dark_gray"},{"text":"Universality","color":"dark_red"},{"text":"]","color":"dark_gray"},{"text":" If the NPC is invisble, but you can still see his name, then a mod may be having problem with NPCs rendering","color":"gray"},{"text":" ( Like OldAnimation )","color":"aqua"}]')

def Help(e):
	try:
		if e.source.getHeldItem().getDisplayName() == "Help":
			e.npc.executeCommand('/tellraw @a ["",{"text":"[","color":"dark_gray"},{"text":"Universality","color":"dark_red"},{"text":"][","color":"dark_gray"},{"text":"Help","color":"dark_green"},{"text":"] ","color":"dark_gray"},{"text":"Hit the NPC to change the game you will host then hit him with the Start item to create the game hub !","color":"gray"}]')
		else :
			Start(e)
	except:
		Start(e)

def Start(e):
	try:
		if e.source.getHeldItem().getDisplayName() == "Start":
			e.npc.executeCommand('/tellraw @a ["",{"text":"[","color":"dark_gray"},{"text":"Universality","color":"dark_red"},{"text":"][","color":"dark_gray"},{"text":"Start","color":"dark_blue"},{"text":"]","color":"dark_gray"},{"text":" Starting your game of '+str(e.npc.getStoreddata().get("GameSelected"))+', please wait.","color":"gray"},{"text":"\n"},{"text":"[","color":"dark_gray"},{"text":"Universality","color":"dark_red"},{"text":"][","color":"dark_gray"},{"text":"HubGenerator","color":"blue"},{"text":"]","color":"dark_gray"},{"text":" Preparing the Hub ....","color":"gray"}]')
			if e.npc.getStoreddata().get("GameSelected") == "UHC" :
				HostUHC(e)
				e.npc.executeCommand("/clear @a")
				e.npc.executeCommand('/tellraw @a ["",{"text":"[","color":"dark_gray"},{"text":"Universality","color":"dark_red"},{"text":"]","color":"dark_gray"},{"text":" Main system switched to ","color":"gray"},{"text":"[","color":"dark_gray"},{"text":"UHC","color":"dark_red"},{"text":"]","color":"dark_gray"}]')
		
			if e.npc.getStoreddata().get("GameSelected") == "Arena FFA" :
				HostFFA(e)
				e.npc.executeCommand("/clear @a")
				e.npc.executeCommand('/tellraw @a ["",{"text":"[","color":"dark_gray"},{"text":"Universality","color":"dark_red"},{"text":"]","color":"dark_gray"},{"text":" Main system switched to ","color":"gray"},{"text":"[","color":"dark_gray"},{"text":"FFA","color":"dark_red"},{"text":"]","color":"dark_gray"}]')
				e.npc.despawn()

		else :
			GameList(e)
	except:
		GameList(e)

def GameList(e):
	try:
		if e.source.getHeldItem().getDisplayName() == "Games list":
			e.npc.executeCommand('/tellraw @a ["",{"text":"[","color":"dark_gray"},{"text":"Universality","color":"dark_red"},{"text":"][","color":"dark_gray"},{"text":"GameList","color":"dark_purple"},{"text":"]","color":"dark_gray"},{"text":" You have ","color":"gray"},{"text":"7 ","color":"white"},{"text":"games installed :","color":"gray"},{"text":" UHC, ","color":"dark_red"},{"text":"LGUHC, ","color":"blue"},{"text":"UHC MeetUp, ","color":"dark_green"},{"text":"Arena FFA, ","color":"dark_blue"},{"text":"Arena 2v2, ","color":"gold"},{"text":"1v1. ","color":"pink"},{"text":"\n"},{"text":"[","color":"dark_gray"},{"text":"Universality","color":"dark_red"},{"text":"][","color":"dark_gray"},{"text":"Info","color":"gold"},{"text":"]","color":"dark_gray"},{"text":" Youre selected game is : ","color":"gray"},{"text":"'+str(e.npc.getStoreddata().get("GameSelected"))+'","color":"dark_red"}]')

		else :
			SwitchGame(e)
	except:
		SwitchGame(e)

def SwitchGame(e):
	GameList = ["UHC","LGUHC","UHC MeetUp","Arena FFA","Arena 2v2","1v1"]			#Playable Games List

	if e.npc.getStoreddata().get("GameTick") == None :				# Initiating List tick data
		e.npc.getStoreddata().put("GameTick", "0")

	if int(e.npc.getStoreddata().get("GameTick")) > len(GameList)-1 :				# Initiating List tick data			+ str(e.npc.getStoreddata().get("GameSelected"))
		e.npc.getStoreddata().put("GameTick", "0")

	if e.npc.getStoreddata().get("GameSelected") == None :				# Initiating List data
		e.npc.getStoreddata().put("GameSelected", GameList[0])


	e.npc.getStoreddata().put("GameSelected", GameList[int(e.npc.getStoreddata().get("GameTick"))])
	e.npc.executeCommand('/tellraw @a ["",{"text":"[","color":"dark_gray"},{"text":"Universality","color":"dark_red"},{"text":"]","color":"dark_gray"},{"text":" The game selected is now :","color":"gray"},{"text":" '+ str(e.npc.getStoreddata().get("GameSelected"))+'","color":"white"}]')

	e.npc.getStoreddata().put("GameTick", str(int(e.npc.getStoreddata().get("GameTick"))+1))


# Games Hosting

def HostUHC(e):
	SpawningHubUHC(e)
	SpawningNPCUHC(e)
	e.npc.despawn()


def HostFFA(e):
	SpawningHubFFA(e)
	SpawningNPCFFA(e)





# Scripts

def SpawningHubUHC(e):

	e.npc.world.getTempdata().put("GameMode", "UHC")

	e.npc.executeCommand('/tp @a 0 202 0')
	e.npc.executeCommand('/fill 120 58 120 -120 58 0 minecraft:dirt')
	e.npc.executeCommand('/fill 120 58 0 -120 58 -120 minecraft:dirt')

	e.npc.executeCommand('/fill -15 200 -15 15 200 15 minecraft:stained_glass')
	e.npc.executeCommand('/fill -15 201 -15 -15 205 15 minecraft:stained_glass_pane 11')
	e.npc.executeCommand('/fill -15 201 -15 15 205 -15 minecraft:stained_glass_pane 11')
	e.npc.executeCommand('/fill 15 201 15 -15 205 15 minecraft:stained_glass_pane 11')
	e.npc.executeCommand('/fill 15 201 15 15 205 -15 minecraft:stained_glass_pane 11')
	e.npc.executeCommand('/fill -1 200 -1 1 200 1 minecraft:bedrock')
	
	e.npc.executeCommand('/setblock -13 201 0 minecraft:stone') # For the settings NPCs
	e.npc.executeCommand("/fill -12 201 7 -14 201 -7 minecraft:stone_slab")
	e.npc.executeCommand('/setblock -13 201 -2 minecraft:stone')
	e.npc.executeCommand('/setblock -13 201 -4 minecraft:stone')
	e.npc.executeCommand('/setblock -13 201 -6 minecraft:stone')
	
	e.npc.executeCommand('/setblock -13 201 2 minecraft:stone')
	e.npc.executeCommand('/setblock -13 201 4 minecraft:stone')
	e.npc.executeCommand('/setblock -13 201 6 minecraft:stone')
	
	
	e.npc.executeCommand('/setblock 13 201 0 minecraft:stone') # For the settings choosers NPCs
	e.npc.executeCommand('/setblock 13 201 4 minecraft:stone')
	e.npc.executeCommand('/setblock 13 201 -4 minecraft:stone')
	
	e.npc.executeCommand('/setblock 0 201 -13 minecraft:stone') # For the helper NPC
	e.npc.executeCommand('/setblock 2 201 -13 minecraft:stone')

	e.npc.executeCommand('/setblock 13 201 12 minecraft:stone') # for the config loader NPC

	e.npc.executeCommand("/fill 1 200 19 -1 200 21 minecraft:bedrock")		# For the "Fate" zone

	e.npc.executeCommand("/fill 2 200 18 -2 200 22 minecraft:stained_glass")
	e.npc.executeCommand("/fill 1 201 22 -1 201 22 minecraft:fence")
	e.npc.executeCommand("/fill 1 201 18 -1 201 18 minecraft:fence")
	e.npc.executeCommand("/fill 2 201 19 2 201 21 minecraft:fence")
	e.npc.executeCommand("/fill -2 201 19 -2 201 21 minecraft:fence")

	e.npc.executeCommand("/setblock 13 201 -13 minecraft:stone")

	e.npc.executeCommand('/tp @a 0 202 0')
	e.npc.executeCommand("/title @a UHC")
	
def SpawningNPCUHC(e):
	e.npc.world.spawnClone(-13, 203, 0, 2, "Host Settings UHC").getDisplay().setName("Hit me to change variable")
	e.npc.world.spawnClone(-13, 203, 2, 2, "Host Settings UHC").getDisplay().setName("+1")
	e.npc.world.spawnClone(-13, 203, 4, 2, "Host Settings UHC").getDisplay().setName("+5")
	e.npc.world.spawnClone(-13, 203, 6, 2, "Host Settings UHC").getDisplay().setName("+10")
	e.npc.world.spawnClone(-13, 203, -2, 2, "Host Settings UHC").getDisplay().setName("-1")
	e.npc.world.spawnClone(-13, 203, -4, 2, "Host Settings UHC").getDisplay().setName("-5")
	e.npc.world.spawnClone(-13, 203, -6, 2, "Host Settings UHC").getDisplay().setName("-10")
	e.npc.world.spawnClone(13, 203, -4, 2, "Host Settings UHC").getDisplay().setName("Config Bots")
	e.npc.world.spawnClone(13, 203, 0, 2, "Host UHC")
	e.npc.world.spawnClone(13, 203, 4, 2, "Host Settings UHC").getDisplay().setName("Config Scenarios")
	e.npc.world.spawnClone(13, 203, 12, 2, "Config loader").getDisplay()
	e.npc.world.spawnClone(0, 203, -13, 2, "Helper")
	e.npc.world.spawnClone(2, 203, -13, 2, "Helper").getDisplay().setName("Whats my current Config ?")
	e.npc.world.spawnClone(1, 203, 19, 2, "Accept Fate").getDisplay().setName("Respawn")
	e.npc.world.spawnClone(-1, 203, 21, 2, "Accept Fate")
	e.npc.world.spawnClone(13, 203, -13, 2, "Inventory loader")

def SpawningHubFFA(e):
	e.npc.executeCommand('/tp @a 0 202 0')
	e.npc.executeCommand('/fill 120 58 120 -120 58 0 minecraft:dirt')
	e.npc.executeCommand('/fill 120 58 0 -120 58 -120 minecraft:dirt')

	e.npc.executeCommand('/fill -15 200 -15 15 200 15 minecraft:stained_glass')
	e.npc.executeCommand('/fill -15 201 -15 -15 205 15 minecraft:stained_glass_pane 9')
	e.npc.executeCommand('/fill -15 201 -15 15 205 -15 minecraft:stained_glass_pane 9')
	e.npc.executeCommand('/fill 15 201 15 -15 205 15 minecraft:stained_glass_pane 9')
	e.npc.executeCommand('/fill 15 201 15 15 205 -15 minecraft:stained_glass_pane 9')
	e.npc.executeCommand('/fill -1 200 -1 1 200 1 minecraft:bedrock')
	
	e.npc.executeCommand('/setblock -13 201 0 minecraft:stone') # For the settings NPCs
	e.npc.executeCommand("/fill -12 201 7 -14 201 -7 minecraft:stone_slab")
	e.npc.executeCommand('/setblock -13 201 -2 minecraft:stone')
	e.npc.executeCommand('/setblock -13 201 -4 minecraft:stone')
	e.npc.executeCommand('/setblock -13 201 -6 minecraft:stone')
	
	e.npc.executeCommand('/setblock -13 201 2 minecraft:stone')
	e.npc.executeCommand('/setblock -13 201 4 minecraft:stone')
	e.npc.executeCommand('/setblock -13 201 6 minecraft:stone')
	
	
	e.npc.executeCommand('/setblock 13 201 0 minecraft:stone') # For the settings choosers NPCs
	e.npc.executeCommand('/setblock 13 201 4 minecraft:stone')
	e.npc.executeCommand('/setblock 13 201 -4 minecraft:stone')
	
	e.npc.executeCommand('/setblock 0 201 -13 minecraft:stone') # For the helper NPC
	e.npc.executeCommand('/setblock 2 201 -13 minecraft:stone')

	e.npc.executeCommand('/setblock 13 201 12 minecraft:stone') # for the config loader NPC


	e.npc.executeCommand("/setblock 13 201 -13 minecraft:stone")

	e.npc.executeCommand('/tp @a 0 202 0')
	e.npc.executeCommand("/title @a UHC")


	
def SpawningNPCFFA(e):
    List = ["-1", "+1", "Config_loader", "Inventory_loader", "+5", "-5", "+10", "+10", "Helper", "Whats_my_current_Config_?", "Hit_me_to_change_variable", "Config_Bots", "Config_Scenarios", "Respawn", "Accept_Fate", "Host UHC"]
    for i in range(0, len(List)):
        e.npc.executeCommand("/noppes npc "+str(List[i])+" delete")

    e.npc.world.getTempdata().put("GameMode", "FFA")

    e.npc.executeCommand("/worldborder center 0 0")
    e.npc.executeCommand("/worldborder set 160")
    e.npc.world.spawnClone(13, 203, 0, 3, "Join FFA")



#======================#
#_______{ Hooks }______#
#======================#

def interact(e):
	e.npc.say(str(e.npc.getStoreddata().get("GameSelected")))
	e.npc.say(str(e.npc.getStoreddata().get("GameTick")))

def damaged(e):
	Help(e)
	e.setCanceled(True)


def died(e):
    pass


def init(e):
	FirstSay(e)

