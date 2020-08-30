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

		e.npc.executeCommand('/tellraw @a ["",{"text":"[","color":"dark_gray"},{"text":"Universality","color":"dark_red"},{"text":"]","color":"dark_gray"},{"text":" Thanks for downloading the ","color":"dark_green"},{"text":"Universality","color":"dark_red","hoverEvent":{"action":"show_text","value":"Universality by Natsu91"}},{"text":" scripts !","color":"dark_green"}]')
		e.npc.executeCommand('/tellraw @a ["",{"text":"[","color":"dark_gray"},{"text":"Universality","color":"dark_red"},{"text":"]","color":"dark_gray"},{"text":" - Hit the Universality NPC with the items to use them.","color":"gray"}]')
		e.npc.executeCommand('/tellraw @a ["",{"text":"[","color":"dark_gray"},{"text":"Universality","color":"dark_red"},{"text":"]","color":"dark_gray"},{"text":" - Hit the NPC with an empty hand to change the selected game","color":"gray"}]')
		e.npc.executeCommand('/tellraw @a ["",{"text":"[","color":"dark_gray"},{"text":"Universality","color":"dark_red"},{"text":"]","color":"dark_gray"},{"text":" - If you can only see NPCs name, then a mod is interfering with NPCs rendering ","color":"gray"},{"text":"( Like OldAnimation )","underlined":true,"color":"aqua"}]')
		e.npc.executeCommand('/tellraw @a ["",{"text":"[","color":"dark_gray"},{"text":"Universality","color":"dark_red"},{"text":"]","color":"dark_gray"},{"text":" - If you are lost, hit the NPC with the ","color":"gray"},{"text":"help item","underlined":true,"color":"green","insertion":"The compass"},{"text":".","color":"gray"}]')

		e.npc.getStoreddata().put('FirstSay', True)
		e.npc.executeCommand('/give @a compass 1 0 {display:{Name:Help,Lore:[" Hit the NPC with this item to get help"]}}')
		e.npc.executeCommand('/give @a comparator 1 0 {display:{Name:Start,Lore:[" Hit the NPC with this item to start the host"]}}')
		e.npc.executeCommand('/give @a paper 1 0 {display:{Name:Games list,Lore:[" Hit the NPC with this item to get the list of playable games"]}}')
		#e.npc.executeCommand('/tellraw @a ["",{"text":"[","color":"dark_gray"},{"text":"Universality","color":"dark_red"},{"text":"]","color":"dark_gray"},{"text":" If the NPC is invisble, but you can still see his name, then a mod may be having problem with NPCs rendering","color":"gray"},{"text":" ( Like OldAnimation )","color":"aqua"}]')

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
			e.npc.executeCommand('/tellraw @a ["",{"text":"[","color":"dark_gray"},{"text":"Universality","color":"dark_red"},{"text":"][","color":"dark_gray"},{"text":"GameList","color":"dark_purple"},{"text":"]","color":"dark_gray"},{"text":" - For now, ","color":"gray"},{"text":"UHC","color":"dark_blue"},{"text":" is playable, and ","color":"gray"},{"text":"Arena","color":"red"},{"text":" and ","color":"gray"},{"text":"Practice","color":"red"},{"text":" are in developement.","color":"gray"},{"text":"\n "},{"text":"[","color":"dark_gray"},{"text":"Universality","color":"dark_red"},{"text":"][","color":"dark_gray"},{"text":"Info","color":"gold"},{"text":"]","color":"dark_gray"},{"text":" Youre selected game is : ","color":"gray"},{"text":"'+str(e.npc.getStoreddata().get("GameSelected"))+'","color":"dark_red"}]')

		else :
			SwitchGame(e)
	except:
		SwitchGame(e)

def SwitchGame(e):
	GameList = ["UHC"]			#Playable Games List

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

	e.npc.executeCommand('/tp @a 0 196 0')
	e.npc.executeCommand('/gamemode 2 @a')
	e.npc.executeCommand('/tp '+str(e.source.getName())+' 0 202 0')
	e.npc.executeCommand('/fill 120 58 120 -120 58 0 minecraft:dirt')
	e.npc.executeCommand('/fill 120 58 0 -120 58 -120 minecraft:dirt')

	e.npc.executeCommand('/fill -15 200 -15 15 200 15 minecraft:stained_glass')					# Hub
	e.npc.executeCommand('/fill -15 201 -15 -15 205 15 minecraft:stained_glass_pane 11')
	e.npc.executeCommand('/fill -15 201 -15 15 205 -15 minecraft:stained_glass_pane 11')
	e.npc.executeCommand('/fill 15 201 15 -15 205 15 minecraft:stained_glass_pane 11')
	e.npc.executeCommand('/fill 15 201 15 15 205 -15 minecraft:stained_glass_pane 11')


	e.npc.executeCommand('/fill -15 194 -15 15 194 15 minecraft:stained_glass')					# Hub
	e.npc.executeCommand('/fill -15 195 -15 -15 199 15 minecraft:stained_glass_pane 11')
	e.npc.executeCommand('/fill -15 195 -15 15 199 -15 minecraft:stained_glass_pane 11')
	e.npc.executeCommand('/fill 15 195 15 -15 199 15 minecraft:stained_glass_pane 11')
	e.npc.executeCommand('/fill 15 195 15 15 199 -15 minecraft:stained_glass_pane 11')


	e.npc.executeCommand('/fill -1 200 -1 1 200 1 minecraft:bedrock')

	e.npc.executeCommand("/fill 0 200 13 0 201 13 minecraft:bedrock")		# Config
	e.npc.executeCommand("/setblock -1 201 13 minecraft:stone_slab")
	e.npc.executeCommand("/setblock 1 201 13 minecraft:stone_slab")
	e.npc.executeCommand("/setblock 0 201 12 minecraft:stone_slab")
	e.npc.executeCommand("/setblock 0 201 14 minecraft:stone_slab")
	
	e.npc.executeCommand('/setblock -13 200 0 minecraft:bedrock') 		# Start

	e.npc.executeCommand("/fill 0 200 -13 0 201 -13 minecraft:bedrock")		# Inventories
	e.npc.executeCommand("/setblock -1 201 -13 minecraft:stone_slab")
	e.npc.executeCommand("/setblock 1 201 -13 minecraft:stone_slab")
	e.npc.executeCommand("/setblock 0 201 -12 minecraft:stone_slab")
	e.npc.executeCommand("/setblock 0 201 -14 minecraft:stone_slab")

	
	# Helper + Credits

	e.npc.executeCommand("/fill -12 201 7 -14 201 -7 minecraft:stone_slab")

	e.npc.executeCommand('/setblock -13 201 -3 minecraft:stone')

	e.npc.executeCommand('/setblock -13 201 3 minecraft:stone')

	e.npc.executeCommand("/setblock 13 201 0 minecraft:stone")
	e.npc.executeCommand("/setblock 13 200 0 minecraft:stone")
	e.npc.executeCommand("/setblock 13 201 -1 minecraft:stone_slab")
	e.npc.executeCommand("/setblock 13 201 1 minecraft:stone_slab")
	e.npc.executeCommand("/setblock 14 201 0 minecraft:stone_slab")
	e.npc.executeCommand("/setblock 12 201 0 minecraft:stone_slab")

	e.npc.executeCommand('/tp '+str(e.source.getName())+' 0 202 0')
	
def SpawningNPCUHC(e):

	e.npc.world.spawnClone(13, 203, 0, 2, "Host UHC")

	e.npc.world.spawnClone(0, 203, -13, 2, "Handler").getDisplay().setName("Config")
	e.npc.world.spawnClone(0, 203, 13, 2, "Handler").getDisplay().setName("Inventories")
	e.npc.world.spawnClone(14, 195, 0, 2, "Helper").getDisplay().setName("Display Config")
	e.npc.world.spawnClone(13, 202, -13, 2, "Helper").getDisplay().setName("Display Config")

	e.npc.world.spawnClone(-13, 202, 0, 2, "Dev")
	e.npc.world.spawnClone(13, 202, 13, 2, "Helper")
	e.npc.world.spawnClone(-13, 202, -3, 2, "Dev").getDisplay().setName("Discord")
	e.npc.world.spawnClone(-13, 202, 3, 2, "Dev").getDisplay().setName("Youtube")

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

