import random
import math
#API Link :http://www.kodevelopment.nl/customnpcs/api/1.8.9/
#Credits : Script UHC vs Bots Bot Scattering By Natsu91

#===================================#
#_______{ Creating Algorithm }______#
#===================================#
def SpawningBots(e) :
	BotsToSpawn = e.npc.world.getTempdata().get("BotNumber")

	e.npc.world.getStoreddata().put("Factions", "1/2/3/4/5/6/7/8/9/10/11/12/13/14/15/16/17/18/19/20/21/22/23/24/25")				# For the latest scatter method

	BotsToSpawn = e.npc.world.getTempdata().get("BotNumber")
	TeamMode = e.npc.world.getTempdata().get("TeamSize")
	
	if BotsToSpawn%TeamMode == 1 :
		BotsToSpawn = TeamMode * round(BotsToSpawn/TeamMode)



	TeamsAlive = BotsToSpawn/TeamMode + 1
	e.npc.world.getStoreddata().put("TeamsAlive", TeamsAlive)

	e.npc.world.getStoreddata().put("BotsToSpawn", BotsToSpawn)				# For the latest scatter method

	for i in range(0,26):					# Initialize team data
		e.npc.world.getStoreddata().put(str(i), TeamMode)

	PlayerList = len(e.npc.world.getAllPlayers())
	e.npc.world.getStoreddata().put("Players", BotsToSpawn + PlayerList)			# Getting data for bots spawn

	RedditUHCDisplay = e.npc.world.getTempdata().get("RedditUHCDisplay")				# Adding the sidebar scenario
	if RedditUHCDisplay == True :
		e.npc.executeCommand("/scoreboard objectives add Kills dummy")
		e.npc.executeCommand("/scoreboard objectives setdisplay sidebar Kills")
		e.npc.executeCommand("/scoreboard players set Players Kills "+str(int(e.npc.world.getStoreddata().get("Players")))+"")

	Spawned = e.npc.getTempdata().get("Spawned")
	e.npc.setPosition(0, 204, 0)
	TeamID = -1
	SpecialsOn = e.npc.world.getTempdata().get("SpecialsOn")
	Specials = 0
	Specials =["_Mik0_","SandSt0rm","Y0z0Ra_","_FeuilleChan_","Kine_Sama"]		# Specials bots list x)
	SpecialsNumber = 0

	i = 0      # Tick for spawning specials bot
	
	e.npc.executeCommand('/tellraw @a ["",{"text":"----------------------------------------------","color": gray,"bold":true}]')						# Because i like arctic UHC style :D
	e.npc.executeCommand('/tellraw @a ["",{"text":">>> ","color": gray},{"text":"Waiting for scatter to finish...", "color" : dark_red}]')
	e.npc.executeCommand('/tellraw @a ["",{"text":"----------------------------------------------","color": gray,"bold":true}]')
	e.npc.executeCommand('/playsound note.pling @a')

	for i in range (0, 20):
		SpawnerX = random.randint(-120,120)
		SpawnerY = random.randint(-120,120)
		e.npc.world.spawnClone( int(SpawnerX), 150, int(SpawnerY), 2, "Spawner").setFaction(0)			# spawning classic bots
			

	e.npc.setPosition(0, 204, 0)
	e.npc.world.getTempdata().put("GameStarted", 1)
	e.npc.executeCommand('/fill 20 203 0 200 205 0 minecraft:air')
	e.npc.executeCommand('/fill -20 203 0 -200 205 0 minecraft:air')


def StartingGame(e) :						# Initiating in-game objectives for the sidebar display 
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


	e.npc.executeCommand("/gamerule doFireTick false")								# Few gamerules to avoid game lags and to add more game stability
	e.npc.executeCommand("/gamerule naturalRegeneration false")
	e.npc.executeCommand("/gamerule commandBlockOutput false")

	e.npc.world.getTempdata().put("KillList", [])								# Clearing the Kill list, to not clone kill leaderboard

	# Sending potential name in the cloud data
	Total = 0
	TierToList = ["NoobTier","CasualTier","CommonTier","GoodTier","ProTier","UHCEliteTier"]
	ToSend = ["NameTierNoobTier","NameTierCasualTier","NameTierCommonTier","NameTierGoodTier","NameTierProTier","NameTierUHCEliteTier"]
	for i in range (0, len(TierToList)):
		with open ("C:\\Program Files (x86)\\CustomNPC Config\\UHC\\Pseudos\\"+str(TierToList[i])+".txt", "r") as TierList :
			TierList = TierList.read()
			TierList = TierList.split(",")
			e.npc.world.getTempdata().put(str(ToSend[i]), TierList)
			Total += len(TierList)

	with open ("C:\\Program Files (x86)\\CustomNPC Config\\UHC\\Teams\\Teams.txt", "r") as TierList :
		TierList = TierList.read()
		TierList = TierList.split(\n)
		e.npc.world.getTempdata().put("TeamNameList", TierList)


	if e.npc.world.getTempdata().get("CreateBorder") == True :
		e.npc.executeCommand("/worldborder center 0 0")
		e.npc.executeCommand("/worldborder set 400")


def VisualEffects(e):
	if e.npc.world.getTempdata().get("GameStarted") == 1 :
		if e.npc.getTempdata().get("Tick") == None :
			e.npc.executeCommand('/tellraw @a ["",{"text":">>> ","color": gray},{"text":"All Chunks loaded, ready !", "color" : dark_red}]')
			e.npc.executeCommand('/playsound note.bass @a')

		if e.npc.getTempdata().get("Tick") == 2 :
			e.npc.executeCommand('/tellraw @a ["",{"text":">>> ","color": gray},{"text":"Scatter finished !", "color" : dark_red},{"text":" Now starting in 5 seconds... ","color": gray}]')
			e.npc.executeCommand('/playsound note.hat @a')


		if e.npc.getTempdata().get("Tick") == 4 :
			e.npc.executeCommand('/tellraw @a ["",{"text":">>> ","color": gray},{"text":"Game starts in ", "color" : dark_red},{"text":"4","color": white}]')
			e.npc.executeCommand('/playsound note.pling @a')
			

		if e.npc.getTempdata().get("Tick") == 6 :
			e.npc.executeCommand('/tellraw @a ["",{"text":">>> ","color": gray},{"text":"Game starts in ", "color" : dark_red},{"text":"3","color": white}]')
			e.npc.executeCommand('/playsound note.pling @a')
			

		if e.npc.getTempdata().get("Tick") == 8 :
			e.npc.executeCommand('/tellraw @a ["",{"text":">>> ","color": gray},{"text":"Game starts in ", "color" : dark_red},{"text":"2","color": white}]')
			e.npc.executeCommand('/playsound note.pling @a')
			

		if e.npc.getTempdata().get("Tick") == 10 :
			e.npc.executeCommand('/tellraw @a ["",{"text":">>> ","color": gray},{"text":"Game starts in ", "color" : dark_red},{"text":"1","color": white}]')
			e.npc.executeCommand('/playsound note.pling @a')
			
		if e.npc.getTempdata().get("Tick") == 12 :
			e.npc.executeCommand('/tellraw @a ["",{"text":">>> ","color": gray},{"text":"Game started ", "color" : white}]')
			e.npc.executeCommand('/playsound note.pling @a')


			PvPTime = int(e.npc.world.getTempdata().get("PvPTime")) * 1200
			MeetUp = e.npc.world.getStoreddata().put("MeetUp", e.npc.world.getTotalTime() + PvPTime)
			e.npc.despawn()


def damaged(e):
	e.npc.getTempdata().put("SpecialsOn", True)
	e.npc.getTempdata().put("Spawned", 0)
	#try :
	e.source.getName()
	StartingGame(e)
	SpawningBots(e)
	#except :
		#pass
	

def tick(e):
	VisualEffects(e)
	if e.npc.world.getTempdata().get("GameStarted") == 1 :
		if 	e.npc.getTempdata().get("Tick") == None :
			e.npc.getTempdata().put("Tick", 1)
		else :
			e.npc.getTempdata().put("Tick", e.npc.getTempdata().get("Tick")+1)

