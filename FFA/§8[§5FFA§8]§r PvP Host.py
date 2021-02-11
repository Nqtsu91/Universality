import random
import math
import os
#API Link :http://www.kodevelopment.nl/customnpcs/api/1.8.9/
#Credits : Script UHC vs Bots Bot Scattering By Natsu91

#===================================#
#_______{ Creating Algorithm }______#
#===================================#

def SpawningBots(e) :
	e.npc.world.getTempdata().put("BotsToSpawn", 100)
	List = [100, 50, 25, 10, 5, 3, 2]
	e.npc.world.getTempdata().put("TeamToDisplay", List)

	Faction = ""
	if e.npc.world.getTempdata().get("TeamAliveLimit") >= 26 :
		e.npc.world.getTempdata().put("TeamAliveLimit", 25)

	if 0 >= e.npc.world.getTempdata().get("TeamAliveLimit") :
		e.npc.world.getTempdata().put("TeamAliveLimit", 1)

	for i in range(1, int(e.npc.world.getTempdata().get("TeamAliveLimit"))):
		Faction += str("/"+str(i))
	e.npc.world.getStoreddata().put("Factions", str(Faction))				# For the latest scatter method


	TeamMode = e.npc.world.getTempdata().get("TeamSize")
	
	e.npc.executeCommand("/spawnpoint @a 0 196 0")



	e.npc.executeCommand("/scoreboard objectives remove Gravel ")
	e.npc.executeCommand("/scoreboard objectives remove Apple ")
	e.npc.executeCommand("/scoreboard objectives remove Iron ")
	e.npc.executeCommand("/scoreboard objectives remove Gold")
	e.npc.executeCommand("/scoreboard objectives remove Kills")

	e.npc.executeCommand("/scoreboard objectives add Gravel stat.mineBlock.minecraft.gravel")
	e.npc.executeCommand("/scoreboard objectives add Apple stat.mineBlock.minecraft.leaves")
	e.npc.executeCommand("/scoreboard objectives add Iron stat.mineBlock.minecraft.iron_ore")
	e.npc.executeCommand("/scoreboard objectives add Gold stat.mineBlock.minecraft.gold_ore")
	e.npc.executeCommand("/scoreboard objectives remove Arena")
	e.npc.executeCommand("/scoreboard objectives remove Kills")

	for i in range(0,27):					# Initialize team data
		e.npc.world.getStoreddata().put(str(i), TeamMode)
		e.npc.world.getStoreddata().put(str(i)+"Aggro", 0)

	RedditUHCDisplay = e.npc.world.getTempdata().get("RedditUHCDisplay")				# Adding the sidebar scenario
	if RedditUHCDisplay == True :
		e.npc.executeCommand("/scoreboard objectives add Arena dummy "+u'\xa7'+"4"+u'\xa7'+"l Universality Arena")
		e.npc.executeCommand("/scoreboard objectives setdisplay sidebar Arena")



	Spawned = e.npc.getTempdata().get("Spawned")
	e.npc.setPosition(0, 204, 0)
	
	e.npc.executeCommand('/tellraw @p ["",{"text":"[","color":"dark_gray"},{"text":"Arena","color":"dark_red"},{"text":"]","color":"dark_gray"},{"text":" - Loading chuks......","color":"gray"}]')

	e.npc.executeCommand('/playsound note.pling @a')


	e.npc.world.getTempdata().put("StackedList", [])					# To prevent stacked fights

	for i in range (0, 20):
		SpawnerX = random.randint(-120,120)
		SpawnerY = random.randint(-120,120)
		e.npc.world.spawnClone( int(SpawnerX), 150, int(SpawnerY), 3, "Spawner").setFaction(0)			# spawning classic bots
			

	e.npc.setPosition(0, 204, 0)
	e.npc.world.getTempdata().put("GameStarted", 1)
	e.npc.executeCommand('/fill 20 203 0 200 205 0 minecraft:air')
	e.npc.executeCommand('/fill -20 203 0 -200 205 0 minecraft:air')

def StartingGame(e) :						# Initiating in-game objectives for the sidebar display 
	try:
		e.npc.getTimers().start(2, 0, True)			# The Rod block timer
	except:
		pass

	#Adding player to potential winner list
	List = []
	for i in range(0, len(e.npc.world.getAllPlayers())):
		List.append(e.npc.world.getAllPlayers()[i].getName())

	e.npc.world.getTempdata().put("WinnerList", List)

	e.npc.executeCommand("/scoreboard teams add green")
	e.npc.executeCommand("/scoreboard teams option green color green")
	e.npc.executeCommand("/scoreboard teams add blue")
	e.npc.executeCommand("/scoreboard teams option blue color blue")
	e.npc.executeCommand("/scoreboard teams add red")
	e.npc.executeCommand("/scoreboard teams option red color red")
	e.npc.executeCommand("/scoreboard teams add gold")
	e.npc.executeCommand("/scoreboard teams option gold color gold")
	e.npc.executeCommand("/scoreboard teams add dark_green")
	e.npc.executeCommand("/scoreboard teams option dark_green color dark_green")
	e.npc.executeCommand("/scoreboard teams add aqua")
	e.npc.executeCommand("/scoreboard teams option aqua color aqua")
	e.npc.executeCommand("/scoreboard teams add purple")
	e.npc.executeCommand("/scoreboard teams option purple color purple")
	e.npc.executeCommand("/scoreboard teams add yellow")
	e.npc.executeCommand("/scoreboard teams option yellow color yellow")
	e.npc.executeCommand("/scoreboard teams add deads")
	e.npc.executeCommand("/scoreboard teams option deads color black")
	e.npc.executeCommand("/scoreboard teams add Players")
	e.npc.executeCommand("/scoreboard teams option Players color dark_aqua")
	e.npc.executeCommand("/scoreboard teams join Players Players")


	e.npc.executeCommand("/scoreboard objectives add border trigger")
	e.npc.executeCommand("/scoreboard objectives add PvP trigger")

	e.npc.executeCommand("/gamerule doFireTick false")								# Few gamerules to avoid game lags and to add more game stability
	e.npc.executeCommand("/gamerule naturalRegeneration false")
	e.npc.executeCommand("/gamerule commandBlockOutput false")

	e.npc.world.getTempdata().put("KillList", [])								# Clearing the Kill list, to not clone kill leaderboard


	e.npc.world.getStoreddata().put("KillList", "")

	e.npc.executeCommand("/worldborder center 0 0")
	e.npc.executeCommand("/worldborder set 40000")

def VisualEffects(e):
	if e.npc.world.getTempdata().get("GameStarted") == 1 :
		if e.npc.getTempdata().get("Tick") == None :
			e.npc.executeCommand('/tellraw @a ["",{"text":"[","color":"dark_gray"},{"text":"Arena","color":"dark_red"},{"text":"]","color":"dark_gray"},{"text":" \u22d9 Bots are spawning...","color":"gray"}]')
			e.npc.executeCommand("/clear @a")
			e.npc.executeCommand("/gamemode 2 @a")
			e.npc.executeCommand('/playsound note.bass @a')
			Host = e.npc.getTempdata().get("Host")
			e.npc.executeCommand('/title @a times 20 60 20')
			e.npc.executeCommand('/title @a subtitle ["",{"text":"'+str(Host)+'","color":"white"},{"text":" mode !","color":"gray"}]')
			e.npc.executeCommand('/title @a title ["",{"text":"Welcome to ","color":"gray"},{"text":"Arena","color":"red"},{"text":" !","color":"gray"}]')

		if e.npc.getTempdata().get("Tick") == 2 :
			e.npc.executeCommand('/tellraw @a ["",{"text":"[","color":"dark_gray"},{"text":"Arena","color":"dark_red"},{"text":"]","color":"dark_gray"},{"text":" \u22d9 Scattering players...","color":"gray"}]')
			e.npc.executeCommand('/playsound note.pling @a')
			

		if e.npc.getTempdata().get("Tick") == 4 :
			e.npc.executeCommand('/tellraw @a ["",{"text":"[","color":"dark_gray"},{"text":"Arena","color":"dark_red"},{"text":"]","color":"dark_gray"},{"text":" Arena ready !","color":"gray"}]')
			e.npc.executeCommand("/tp @a 0 72 0")
			e.npc.executeCommand("/effect @a minecraft:resistance 7 45 true")
			e.npc.executeCommand("/effect @a minecraft:slowness 7 45 true")
			e.npc.executeCommand('/playsound note.pling @p')
			
		if e.npc.getTempdata().get("Tick") == 6 :
			e.npc.executeCommand('/effect @a minecraft:instant_health 1 45 true')
			e.npc.executeCommand("/effect @a minecraft:slowness 0 0 true")
			e.npc.executeCommand("/gamemode 0 @a")
			for i in range (0, len(e.npc.world.getAllPlayers())):
				e.npc.executeCommand('/tellraw @a ["",{"text":"[","color":"dark_gray"},{"text":"Arena","color":"dark_red"},{"text":"]","color":"dark_gray"},{"text":" - ","color":"gray"},{"text":"'+str(e.npc.world.getAllPlayers()[i].getName())+'","color":"red"},{"text":" joined the arena !","color":"gray"}]')

			e.npc.executeCommand('/playsound note.pling @p')

			#e.npc.world.spawnClone(1, 195, 3, 2, "Accept Fate")
			e.npc.world.spawnClone(1, 195, -3, 3, "Accept Fate").getDisplay().setName("Respawn")
			GiveInventory(e)
			
			e.npc.despawn()

def GiveInventory(e):
	"""Give Arena inventory to player"""
	if e.npc.world.getTempdata().get("CurrentGame") == "bow":
		e.npc.executeCommand('/give @a minecraft:iron_helmet 1 0 {Unbreakable:1,ench:[{id:4,lvl:1}]}')
		e.npc.executeCommand('/give @a minecraft:iron_chestplate 1 0 {Unbreakable:1,ench:[{id:0,lvl:1}]}')
		e.npc.executeCommand('/give @a minecraft:iron_leggings 1 0 {Unbreakable:1,ench:[{id:4,lvl:1}]}')
		e.npc.executeCommand('/give @a minecraft:diamond_boots 1 0 {Unbreakable:1,ench:[{id:0,lvl:2}]}')

		e.npc.executeCommand('/give @a minecraft:iron_sword 1 0 {Unbreakable:1,ench:[{id:16,lvl:1}]}')
		e.npc.executeCommand('/give @a minecraft:bow 1 0 {Unbreakable:1,ench:[{id:48,lvl:2}]}')

		e.npc.executeCommand('/give @a minecraft:cobblestone 64')
		e.npc.executeCommand('/give @a minecraft:cooked_beef 10')
		e.npc.executeCommand('/give @a minecraft:arrow 64')
		e.npc.executeCommand('/give @a minecraft:water_bucket 1')
		e.npc.executeCommand('/give @a minecraft:golden_apple 1')
		e.npc.executeCommand('/give @a minecraft:fishing_rod 1 0 {Unbreakable:1}')

	else:
		e.npc.executeCommand('/give @a minecraft:diamond_helmet 1 0 {Unbreakable:1,ench:[{id:4,lvl:2}]}')
		e.npc.executeCommand('/give @a minecraft:diamond_chestplate 1 0 {Unbreakable:1,ench:[{id:0,lvl:2}]}')
		e.npc.executeCommand('/give @a minecraft:diamond_leggings 1 0 {Unbreakable:1,ench:[{id:0,lvl:2}]}')
		e.npc.executeCommand('/give @a minecraft:diamond_boots 1 0 {Unbreakable:1,ench:[{id:4,lvl:2}]}')

		e.npc.executeCommand('/give @a minecraft:diamond_sword 1 0 {Unbreakable:1,ench:[{id:16,lvl:3}]}')
		e.npc.executeCommand('/give @a minecraft:bow 1 0 {Unbreakable:1,ench:[{id:48,lvl:2}]}')

		e.npc.executeCommand('/give @a minecraft:cobblestone 64')
		e.npc.executeCommand('/give @a minecraft:cooked_beef 10')
		e.npc.executeCommand('/give @a minecraft:arrow 64')
		e.npc.executeCommand('/give @a minecraft:water_bucket 1')
		e.npc.executeCommand('/give @a minecraft:lava_bucket 1')
		e.npc.executeCommand('/give @a minecraft:golden_apple 8')
		e.npc.executeCommand('/give @a minecraft:fishing_rod 1 0 {Unbreakable:1}')

def damaged(e):
	if e.npc.getTempdata().get("Confirmed") == True :
		try:
			if e.npc.world.getTempdata().get("CurrentGame") == "bow":
				e.npc.getTempdata().put("Host", "ArcticMC")
			else:
				e.npc.getTempdata().put("Host", "Nontia")
		except:
			pass
		try :
			e.source.getName()
			NeedStop = e.npc.world.getTempdata().put("NeedStop", 1)
			StartingGame(e)
			SpawningBots(e)
		except Exception as err :
			e.npc.world.broadcast(str(err))
			e.npc.executeCommand('/tellraw @p ["",{"text":"[","color":"dark_gray"},{"text":"Arena","color":"dark_red"},{"text":"]","color":"dark_gray"},{"text":" - Cannot start your game, errored config.","color":"gray"}]')
		e.npc.getTempdata().put("Confirmed", False)
	else :
		e.npc.getTempdata().put("Confirmed", True)
		e.npc.executeCommand('/tellraw @p ["",{"text":"[","color":"dark_gray"},{"text":"Arena","color":"dark_red"},{"text":"][","color":"dark_gray"},{"text":"Reminder","color":"dark_aqua"},{"text":"]","color":"dark_gray"},{"text":" - Click again to start but please ensure you loaded the right team file by right clicking this NPC.","color":"gray"}]')

def tick(e):
	VisualEffects(e)
	if e.npc.world.getTempdata().get("GameStarted") == 1 :
		if 	e.npc.getTempdata().get("Tick") == None :
			e.npc.getTempdata().put("Tick", 1)
		else :
			e.npc.getTempdata().put("Tick", e.npc.getTempdata().get("Tick")+1)
			

def interact(e):
	e.npc.executeCommand('/tellraw @p ["",{"text":"[","color":"dark_gray"},{"text":"Arena","color":"dark_red"},{"text":"][","color":"dark_gray"},{"text":"Teams","color":"red"},{"text":"]","color":"dark_gray"},{"text":" Ready to load team slot ","color":"gray"},{"text":"' +str(e.npc.getTempdata().get("TeamsToRead"))+'","color":"aqua"}]')
	e.setCanceled(True)

