import random
import math
import os
#API Link :http://www.kodevelopment.nl/customnpcs/api/1.8.9/
#Credits : Script UHC vs Bots Bot Scattering By Natsu91

#===================================#
#_______{ Creating Algorithm }______#
#===================================#


def LoadAdvanced(e):

    e.npc.world.getTempdata().put("MaxProt", 2)
    e.npc.world.getTempdata().put("MaxSharp", 3)
    e.npc.world.getTempdata().put("MaxGap", 10)


    Path = os.path.dirname(os.path.abspath("__file__"))
    Path += "\\CustomNPC Config\\UHC\\config "+str(e.npc.world.getTempdata().get("ConfigToRead"))+"\\advanced"
    Path = Path.replace("\\", str(os.path.sep))
    with open (str(Path)+".txt", "r") as Config :
        Config = Config.read()
        Config = Config.split(u'\n')
        Name = Config[0]
        del Config[0]
        ToConfigList = ["AnvilTicks","ProtIncreaseTime","SharpIncreaseTime","EnchantIncreaseTime","DiamondIncreaseTime","DiamondIncreaseRate","ClearedLoot","GapIncreaseTime","GapIncreaseRate","GapAtKill","ForcedHelm","ForcedChest","ForcedLegg","ForcedBoots","ForcedSword","HelmProt","ChestProt","LeggProt","BootsProt","HelmProj","ChestProj","LeggProj","BootsProj","SwordSharp","ForcedGap"]


    for i in range (len(Config)-1, -1, -1):
        if Config[i] == "" :
            del Config[i]
        elif Config[i] == " " :
            del Config[i]
        elif Config[i][0] == "#" :
            del Config[i]
        elif Config[i] == u'\r' :
            del Config[i]

    for i in range (0, len(ToConfigList)):
        List = Config[i].split(":")
        try :
            e.npc.world.getTempdata().put(str(ToConfigList[i]), int(List[1]))
        except:
            if List[1] == "True":
                List[1] = True
            else :
                List[1] = False  
            e.npc.world.getTempdata().put(str(ToConfigList[i]), List[1])

    #e.npc.world.getTempdata().put("ListOfTakenNames", [])
    #e.npc.executeCommand('/tellraw @a ["",{"text":"[","color":"dark_gray"},{"text":"UHC","color":"dark_red"},{"text":"]","color":"dark_gray"},{"text":"[","color":"dark_gray"},{"text":"Config","color":"purple"},{"text":"]","color":"dark_gray"},{"text":" Loaded config ","color": green,"bold":true,"italic":false},{"text":"'+str(Name)+'", "color" : dark_green, "underlined" : true} , { "text" :" succesfully", "color" : green, "bold":true}]')


def GiveInventory(e):
    Path = os.path.dirname(os.path.abspath("__file__"))
    Path += "\\CustomNPC Config\\UHC\\config "+str(e.npc.world.getTempdata().get("ConfigToRead"))+"\\inventory"
    Path = Path.replace("\\", str(os.path.sep))
    with open (str(Path)+".txt", "r") as Config :
        e.npc.executeCommand("/clear @a")
        Config = Config.read()
        Config = Config.split('\n')
        for i in range(0, len(e.npc.world.getAllPlayers())):
            Players = e.npc.world.getAllPlayers()
            for z in range (0, len(Config)):                # Getting item + enchant level ( Hardcooooore )
                try:
                    A = Config[z].split("//")
                    if A[3] != 'None' :
                        B = A[3]
                        B = B.replace("s", "")
                        
                        
                        Enchant = ""

                        B = B.replace("]", "")
                        B = B.replace("}", "")
                        B = B.split(",")

                        for b in range(0, len(B)):
                            if (b+1)%2 == 1 :
                                Ench = B[b][-1]
                            else:
                                id = B[b].replace("id:", "")                
                                Enchant += "{id:"+str(id)+",lvl:"+str(Ench)+"},"     
                        
                        #e.npc.say("/give "+str(Players[i].getName())+" "+str(A[0])+" "+str(A[1])+" "+str(A[2])+" {ench:"+str(Enchant)+"}")
                        e.npc.executeCommand("/give "+str(Players[i].getName())+" "+str(A[0])+" "+str(A[1])+" "+str(A[2])+" {ench:["+str(Enchant)+"]}")

                    else:
                        e.npc.executeCommand("/give "+str(Players[i].getName())+" "+str(A[0])+" "+str(A[1])+" "+str(A[2])+"")
                except Exception as err:
                    pass

def SpawningBots(e) :
	if e.npc.world.getTempdata().get("FirstBorder") == 0:
		e.npc.world.getTempdata().put("Radius", 110)
	elif e.npc.world.getTempdata().get("SecondBorder") == 0:
		e.npc.world.getTempdata().put("Radius", 70)
	elif e.npc.world.getTempdata().get("LastBorder") == 0:
		e.npc.world.getTempdata().put("Radius", 40)
	else:
		e.npc.world.getTempdata().put("Radius", 220)
	List = [100, 50, 25, 10, 5, 3, 2]
	e.npc.world.getTempdata().put("TeamToDisplay", List)
	BotsToSpawn = e.npc.world.getTempdata().get("BotNumber")
	e.npc.world.getTempdata().put("TimeBombList", [])

	Faction = ""
	if e.npc.world.getTempdata().get("TeamAliveLimit") >= 40 :
		e.npc.world.getTempdata().put("TeamAliveLimit", 40)

	if 0 >= e.npc.world.getTempdata().get("TeamAliveLimit") :
		e.npc.world.getTempdata().put("TeamAliveLimit", 1)

	for i in range(1, int(e.npc.world.getTempdata().get("TeamAliveLimit"))+1):
		if i != 26:
			Faction += str("/"+str(i))
	e.npc.world.getStoreddata().put("Factions", str(Faction))				# For the latest scatter method

	e.npc.world.getTempdata().put("ListOfTakenNames", [])

	BotsToSpawn = e.npc.world.getTempdata().get("BotNumber")
	TeamMode = e.npc.world.getTempdata().get("TeamSize")
	
	e.npc.executeCommand("/spawnpoint @a 0 196 0")

		
	if BotsToSpawn%TeamMode == 1 :
		BotsToSpawn = TeamMode * round(BotsToSpawn/TeamMode)

	e.npc.executeCommand("/scoreboard objectives remove Gravel ")
	e.npc.executeCommand("/scoreboard objectives remove Apple ")
	e.npc.executeCommand("/scoreboard objectives remove Iron ")
	e.npc.executeCommand("/scoreboard objectives remove Gold")

	e.npc.executeCommand("/scoreboard objectives add Gravel stat.mineBlock.minecraft.gravel")
	e.npc.executeCommand("/scoreboard objectives add Apple stat.mineBlock.minecraft.leaves")
	e.npc.executeCommand("/scoreboard objectives add Iron stat.mineBlock.minecraft.iron_ore")
	e.npc.executeCommand("/scoreboard objectives add Gold stat.mineBlock.minecraft.gold_ore")
	e.npc.executeCommand("/scoreboard objectives add GHead stat.useItem.minecraft.golden_apple")

	TeamsAlive = (BotsToSpawn/TeamMode) + 1
	e.npc.world.getStoreddata().put("TeamsAlive", TeamsAlive)

	e.npc.world.getStoreddata().put("BotsToSpawn", BotsToSpawn)				# For the latest scatter method

	for i in range(0,41):					# Initialize team data
		e.npc.world.getStoreddata().put(str(i), TeamMode)
		e.npc.world.getStoreddata().put(str(i)+"Aggro", 0)

	PlayerList = len(e.npc.world.getAllPlayers())
	e.npc.world.getStoreddata().put("Players", BotsToSpawn + PlayerList)			# Getting data for bots spawn
	e.npc.world.getStoreddata().put("PlayersMax", BotsToSpawn + PlayerList)

	RedditUHCDisplay = e.npc.world.getTempdata().get("RedditUHCDisplay")				# Adding the sidebar scenario
	if RedditUHCDisplay == True :
		e.npc.executeCommand("/scoreboard objectives setdisplay sidebar Kills")
		e.npc.executeCommand("/scoreboard players set "+u'\xa7'+"c"+u'\xa7'+"oPlayers Kills "+str(int(e.npc.world.getStoreddata().get("Players")))+"")

	Spawned = e.npc.getTempdata().get("Spawned")
	TeamID = -1
	SpecialsOn = e.npc.world.getTempdata().get("SpecialsOn")
	Specials = 0
	Specials =["_Mik0_","SandSt0rm","Y0z0Ra_","_FeuilleChan_","Kine_Sama"]		# Specials bots list x)
	SpecialsNumber = 0

	i = 0      # Tick for spawning specials bot
	
	e.npc.executeCommand('/tellraw @p ["",{"text":"[","color":"dark_gray"},{"text":"UHC","color":"dark_red"},{"text":"]","color":"dark_gray"},{"text":" - Loading chunks......","color":"gray"}]')

	e.npc.executeCommand('/playsound note.pling @a')


	e.npc.world.getTempdata().put("StackedList", [])					# To prevent stacked fights

	for i in range (0, 20):
		SpawnerX = random.randint(-220,220)
		SpawnerY = random.randint(-220,220)
		e.npc.world.spawnClone( int(SpawnerX), 150, int(SpawnerY), 2, "Spawner").setFaction(0)			# spawning classic bots
			

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

	e.npc.executeCommand("/scoreboard teams empty deads")
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
	e.npc.executeCommand("/scoreboard objectives remove Arena")

	e.npc.executeCommand("/scoreboard objectives remove Kills")

	e.npc.executeCommand("/scoreboard objectives add Kills dummy "+u'\xa7'+"4"+u'\xa7'+"l Universality UHC")
	e.npc.executeCommand("/scoreboard objectives add Kills dummy "+u'\xa7'+"4"+u'\xa7'+"l Universality UHC")
	e.npc.executeCommand("/scoreboard objectives setdisplay sidebar Kills")

	e.npc.executeCommand("/scoreboard objectives add Spawn trigger")

	e.npc.executeCommand("/gamerule doFireTick false")								# Few gamerules to avoid game lags and to add more game stability
	e.npc.executeCommand("/gamerule naturalRegeneration false")
	e.npc.executeCommand("/gamerule commandBlockOutput false")

	e.npc.world.getTempdata().put("KillList", [])								# Clearing the Kill list, to not clone kill leaderboard


	e.npc.executeCommand('/scoreboard objectives add HealTrigger trigger')
	e.npc.executeCommand('/scoreboard objectives add 1BorderTrigger trigger')
	e.npc.executeCommand('/scoreboard objectives add 2BorderTrigger trigger')
	e.npc.executeCommand('/scoreboard objectives add 3BorderTrigger trigger')
	e.npc.executeCommand('/scoreboard objectives add PvPTrigger trigger')


	# Sending potential name in the cloud data

	Path = os.path.dirname(os.path.abspath("__file__"))
	Path += "\\CustomNPC Config\\UHC\\config "+str(e.npc.world.getTempdata().get("ConfigToRead"))+"\\Teams"
	Path = Path.replace("\\", str(os.path.sep))
	with open (str(Path)+".txt", "r") as TierList :
		TierList = TierList.read()
		TierList = TierList.split(\n)
		e.npc.world.getTempdata().put("TeamNameList", TierList)
		Variable = e.npc.world.getTempdata().get("NameTier"+str("UHCEliteTier"))
		Variable_2 = e.npc.world.getTempdata().get("NameTier"+str("ProTier"))
		NewList = e.npc.world.getTempdata().get("AlreadyTaken")
		if NewList == None :
			e.npc.world.getTempdata().put("AlreadyTaken", [])

		for j in range(0, len(TierList)):
			ToDelete = TierList[j].split("//")
			for i in range(0, len(ToDelete)):
				NewList = e.npc.world.getTempdata().get("AlreadyTaken")
				NewList.append(ToDelete[i])
				try:
					e.npc.world.getTempdata().put("AlreadyTaken", NewList)
				except Exception as err:
					#e.npc.world.broadcast(str(err)+" "+str(ToDelete))
					pass

	e.npc.world.getStoreddata().put("KillList", "")

	e.npc.executeCommand("/worldborder center 0 0")
	e.npc.executeCommand("/worldborder set 40000")




def VisualEffects(e):
	if e.npc.world.getTempdata().get("GameStarted") == 1 :
		if e.npc.getTempdata().get("Tick") == None :
			e.npc.executeCommand("/xp -10000l @a")
			e.npc.executeCommand('/tellraw @a ["",{"text":"[","color":"dark_gray"},{"text":"UHC","color":"dark_red"},{"text":"]","color":"dark_gray"},{"text":" \u22d9 ","bold":true,"color":"gray"},{"text":"Chunks loaded","color":"gray"}]')
			e.npc.executeCommand("/clear @a")
			e.npc.executeCommand("/gamemode 2 @a")
			e.npc.executeCommand('/playsound note.bass @a')
			Host = e.npc.getTempdata().get("Host")
			e.npc.executeCommand('/title @a times 20 120 20')
			e.npc.executeCommand('/title @a subtitle ["",{"text":"Hosted by : ","color":"gray"},{"text":"'+str(Host)+'","color":"red"}]')
			e.npc.executeCommand('/title @a title ["",{"text":"The ","color":"gray"},{"text":"UHC","color":"dark_red"},{"text":" Started !","color":"gray"}]')

		if e.npc.getTempdata().get("Tick") == 2 :
			e.npc.executeCommand('/tellraw @a ["",{"text":"[","color":"dark_gray"},{"text":"UHC","color":"dark_red"},{"text":"]","color":"dark_gray"},{"text":" \u22d9 ","bold":true,"color":"gray"},{"text":"Preparing Bots data....","color":"gray"}]')
			e.npc.executeCommand('/playsound note.hat @a')

			

		if e.npc.getTempdata().get("Tick") == 4 :
			e.npc.executeCommand('/tellraw @a ["",{"text":"[","color":"dark_gray"},{"text":"UHC","color":"dark_red"},{"text":"]","color":"dark_gray"},{"text":" \u22d9 ","bold":true,"color":"gray"},{"text":"Preparing border data....","color":"gray"}]')
			e.npc.executeCommand('/playsound note.pling @a')
			

		if e.npc.getTempdata().get("Tick") == 6 :
			e.npc.executeCommand('/tellraw @p ["",{"text":"[","color":"dark_gray"},{"text":"UHC","color":"dark_red"},{"text":"]","color":"dark_gray"},{"text":" \u22d9 ","bold":true,"color":"gray"},{"text":"Preparing CutClean.....","color":"gray"}]')
			e.npc.executeCommand('/playsound note.pling @p')
			

		if e.npc.getTempdata().get("Tick") == 8 :
			e.npc.executeCommand('/tellraw @a ["",{"text":"[","color":"dark_gray"},{"text":"UHC","color":"dark_red"},{"text":"]","color":"dark_gray"},{"text":" \u22d9 ","bold":true,"color":"gray"},{"text":"Saving scenarios.....","color":"gray"}]')
			e.npc.executeCommand('/playsound note.pling @a')
			

		if e.npc.getTempdata().get("Tick") == 10 :
			e.npc.executeCommand('/tellraw @a ["",{"text":"[","color":"dark_gray"},{"text":"UHC","color":"dark_red"},{"text":"]","color":"dark_gray"},{"text":" \u22d9 ","bold":true,"color":"gray"},{"text":"Scattering players.....","color":"gray"}]')
			e.npc.executeCommand("/tp @a 0 72 0")
			e.npc.executeCommand("/effect @a minecraft:resistance 7 45 true")
			e.npc.executeCommand("/effect @a minecraft:slowness 7 45 true")
			e.npc.executeCommand("/effect @a minecraft:blindness 7 45 true")
			e.npc.executeCommand('/playsound note.pling @p')
			GiveInventory(e)
			
		if e.npc.getTempdata().get("Tick") == 20 :
			e.npc.executeCommand('/tellraw @a ["",{"text":">>> ","color": gray},{"text":"Game started ", "color" : white}]')
			e.npc.executeCommand('/effect @a minecraft:instant_health 1 45 true')
			e.npc.executeCommand("/gamemode 0 @a")
			for i in range (0, len(e.npc.world.getAllPlayers())):
				e.npc.executeCommand('/tellraw '+str(e.npc.world.getAllPlayers()[i].getName())+' ["",{"text":"[","color":"dark_gray"},{"text":"UHC","color":"dark_red"},{"text":"]","color":"dark_gray"},{"text":" (Reminder) - Players CrossTeaming is allowed","color":"gray"},{"text":"\n"},{"text":"[","color":"dark_gray"},{"text":"UHC","color":"dark_red"},{"text":"]","color":"dark_gray"},{"text":" (Reminder) - Final Heal in 10 minutes !","color":"gray"},{"text":"\n"},{"text":"[","color":"dark_gray"},{"text":"UHC","color":"dark_red"},{"text":"]","color":"dark_gray"},{"text":" (Reminder) - Good luck have fun ","color":"gray"},{"text":"'+str(e.npc.world.getAllPlayers()[i].getName())+'","color":"red"},{"text":" !","color":"gray"}]')


			e.npc.executeCommand('/playsound note.pling @p')

			e.npc.world.spawnClone(1, 195, 3, 2, "Accept Fate")
			e.npc.world.spawnClone(1, 195, -3, 2, "Accept Fate").getDisplay().setName("Respawn")


			PvPTime = int(e.npc.world.getTempdata().get("PvPTime")) * 1200
			MeetUp = e.npc.world.getStoreddata().put("MeetUp", e.npc.world.getTotalTime() + PvPTime)

			PvPTime = int(e.npc.world.getTempdata().get("FirstBorder")) * 1200
			MeetUp = e.npc.world.getStoreddata().put("FirstBorder", e.npc.world.getTotalTime() + PvPTime)

			PvPTime = int(e.npc.world.getTempdata().get("SecondBorder")) * 1200
			MeetUp = e.npc.world.getStoreddata().put("SecondBorder", e.npc.world.getTotalTime() + PvPTime)

			PvPTime = int(e.npc.world.getTempdata().get("FinalBorder")) * 1200
			MeetUp = e.npc.world.getStoreddata().put("FinalBorder", e.npc.world.getTotalTime() + PvPTime)
			LoadAdvanced(e)

			e.npc.world.spawnClone( 0, 250, 0, 2, "Border").getStoreddata().clear()
			
			e.npc.despawn()




def damaged(e):
	if e.npc.getTempdata().get("Confirmed") == True :
		e.npc.getTempdata().put("SpecialsOn", True)
		e.npc.getTempdata().put("Spawned", 0)
		try:
			e.npc.getTempdata().put("Host", e.source.getName())
		except:
			pass
		try :
			e.source.getName()
			StartingGame(e)
			SpawningBots(e)
		except Exception as err :
			#e.npc.world.broadcast(str(err))
			e.npc.executeCommand('/tellraw @p ["",{"text":"[","color":"dark_gray"},{"text":"UHC","color":"dark_red"},{"text":"]","color":"dark_gray"},{"text":" - Cannot start your game, errored config.","color":"gray"}]')
			e.npc.getTempdata().put("Confirmed", False)
	else :
		e.npc.getTempdata().put("Confirmed", True)
		e.npc.executeCommand('/tellraw @a ["",{"text":"[","color":"dark_gray"},{"text":"UHC","color":"dark_red"},{"text":"]","color":"dark_gray"},{"text":" Click again to start !","color":"red"}]')

def tick(e):
	VisualEffects(e)
	if e.npc.world.getTempdata().get("GameStarted") == 1 :
		if 	e.npc.getTempdata().get("Tick") == None :
			e.npc.getTempdata().put("Tick", 1)
		else :
			e.npc.getTempdata().put("Tick", e.npc.getTempdata().get("Tick")+1)
			

def interact(e):
	pass

