import random
import math
#API Link :http://www.kodevelopment.nl/customnpcs/api/1.8.9/
#Credits : Script UHC vs Bots BotPvPSystem By Natsu91

#===================================#
#_______{ Creating Algorithm }______#
#===================================#



#DEATH STYLE functions :

def InventorySpawn(e) :
	'''Spawn the whole inventory of the bot depending of the Kills amount he had, double armor drops if he was stacked

		EXCEPTION : if OneShot is enabled, stuff dont drop
	'''
			

	MyX = e.npc.getX()			# Attributing coordinates to the item
	MyY = e.npc.getY()
	MyZ = e.npc.getZ()
	SpawnX = int(round(MyX))
	SpawnY = int(round(MyY)) + 1
	SpawnZ = int(round(MyZ))
			
	# Spawning other items
	ItemList = [["minecraft:cobblestone","64"],["minecraft:cooked_beef","10"],["minecraft:arrow","64"]]																			
	for i in range(0, len(ItemList)):	
		Count = int(ItemList[i][1])	
		e.npc.executeCommand("/summon Item "+str(SpawnX)+" "+str(SpawnY)+" "+str(SpawnZ)+" {Item:{id:"+str(ItemList[i][0])+",Count:"+str(Count)+"},Motion:["+str(random.uniform(0.00,0.1)*random.randint(-1,1))+",0.05,"+str(random.uniform(0.02,0.1)*random.randint(-1,1))+"]}") # Looting item
		

	if e.npc.world.getTempdata().get("CurrentGame") == "bow":
		GoldenAppleLoot = 1
	else:
		GoldenAppleLoot = e.npc.getTempdata().get("GapCount")
		if (GoldenAppleLoot == None) or (GoldenAppleLoot == 0):
			GoldenAppleLoot = 1
	e.npc.executeCommand("/summon Item "+str(SpawnX)+" "+str(SpawnY)+" "+str(SpawnZ)+" {Item:{id:322,Damage:0,Count:"+str(GoldenAppleLoot)+"},Motion:["+str(random.uniform(0.02,0.1)*random.randint(-1,1))+",0.05,"+str(random.uniform(0.02,0.1)*random.randint(-1,1))+"]}") # Looting golden apple based on the amount he had
						
def BadlionDeathTchatMessage(e):
	'''Display chat message at death with custom colors depending on the killler and killed type and faction
	
		format : Killed["kill amount"] was slain by Killer["kill amount"]

		TRIGGER : InventorySpawn(e)

		EXCEPTION : if no killer is found, "PVE" death message is diplayed instead
	'''
	if e.npc.world.getTempdata().get("BadlionKillsSystem") == True :
		Special = '{"text":"","color":"light_purple"}'
		SpecialKiller = '{"text":"","color":"light_purple"}'
		SpecialList = ["Natsu91","Yvant2000Games","Frizou","iKowz","MASTEEKH","jdegoederen","reb_hi","Strykerss","Etoiles","xGokuuuh","Pikachu","TryHqrd_","_Mik0GODESS","SqndSt0rm","Divinity_Kirito","slooonay","Pxdro","Restump","Nardcoo","Ladak","VERSKUUUH","seltix_x","Pacoima","MarkiLokuras","Boosta","DANTEH","Rzmeur","GrzyLight","Mqyland_hi","Mentally","BiboyQG"]
		NameKilled = e.npc.getDisplay().getName()				# Looking for own data
		KilledFaction = e.npc.getFaction().getId()
		KilledKills = e.npc.getStoreddata().get("Kills")
		UnderlinedKilled = "false"
		UnderlinedKiller = "false"
		ItalicKilled = "false"
		ItalicKiller = "false"
		if KilledKills == None :
			KilledKills = 0
	
		if NameKilled in SpecialList :
			Special = '{"text":"['+u'\u2764'+']","color":"light_purple"}'

		FactionArgList = [["green","false","false"],["green","false","false"],["blue","false","false"],["red","false","false"],["yellow","false","false"],["dark_gray","false","false"],["dark_blue","false","false"],["dark_red","false","false"],["dark_green","false","false"],["gold","false","false"],["aqua","false","false"],["light_purple","false","false"],["dark_aqua","false","false"],["dark_purple","false","false"],["green","false","true"],["blue","false","true"],["red","false","true"],["yellow","false","true"],["dark_gray","false","true"],["dark_blue","false","true"],["dark_red","false","true"],["dark_green","false","true"],["gold","false","true"],["aqua","false","true"],["light_purple","false","true"],["dark_aqua","false","true"],["white","false","false"]]
		TeamColorKilled = FactionArgList[KilledFaction][0]
		UnderlinedKilled = FactionArgList[KilledFaction][1]
		ItalicKilled = FactionArgList[KilledFaction][2]
		
		try :											# If killed by a bot
			KillerFaction = e.source.getFaction().getId()
			NameKiller = e.source.getDisplay().getName()
			KillerKills = e.source.getStoreddata().get("Kills")
			TeamColorKiller = FactionArgList[KillerFaction][0]
			UnderlinedKiller = FactionArgList[KillerFaction][1]
			ItalicKiller = FactionArgList[KillerFaction][2]
			
			if KillerKills == None :
				KillerKills = 0
			ActualisedKillerKills = int(KillerKills) ++ 1

			if NameKiller in SpecialList :
				SpecialKiller = '{"text":"['+u'\u2764'+']","color":"light_purple"}'	

			if e.npc.world.getTempdata().get("TeamSize") == 1 :
				TeamColorKiller = "red"
				UnderlinedKiller = "false"
				ItalicKiller = "false"
				UnderlinedKilled = "false"
				ItalicKilled = "false"
				TeamColorKilled = "green"

			if ((int(KillerKills)+1) % 5 == 0) and (e.npc.world.getTempdata().get("CurrentGame") == "bow"):
				e.npc.executeCommand('/tellraw @a ["",{"text":"[","color":"dark_gray"},{"text":"Arena","color":"dark_red"},{"text":"]","color":"dark_gray"},{"text":"'+str(NameKiller)+'"},{"text":" is now on a ","color":"gray"},{"text":"'+str(int(KillerKills)+1)+'","color":"green"},{"text":" killstreak","color":"gray"}]')

			e.npc.executeCommand('/tellraw @a ["",{"text":"[","color":"dark_gray"},{"text":"Arena","color":"dark_red"},{"text":"] ","color":"dark_gray"},'+Special+',{"text":"'+str(NameKilled)+'","color":"'+str(TeamColorKilled)+'","underlined":"'+str(UnderlinedKilled)+'","italic":"'+str(ItalicKilled)+'"},{"text":"[","color":"white"},{"text":"'+str(int(KilledKills))+'","color":"white"},{"text":"]","color":"white"},{"text":" was slain by ","color":"gray"},'+SpecialKiller+',{"text":"'+str(NameKiller)+'","color":"'+str(TeamColorKiller)+'","underlined":"'+str(UnderlinedKiller)+'","italic":"'+str(ItalicKiller)+'"},{"text":"[","color":"white"},{"text":"'+str(ActualisedKillerKills) +'","color":"white"},{"text":"]","color":"white"}]')
		except :
			try :							 # If killed by a Player
				NameKiller = e.source.getName()
				KillerKills = e.npc.world.getStoreddata().get(str(NameKiller) +"Kills")
				TeamColorKiller = "white"
				UnderlinedKiller = "false"
				ItalicKiller = "false"
				if KillerKills == None :
					KillerKills = 0
				AddingKillsToPlayer = KillerKills + 1
				ActualisedKillerKills = int(KillerKills) ++ 1
				e.npc.world.getStoreddata().put(str(NameKiller)+"Kills", AddingKillsToPlayer)
				if NameKiller in SpecialList :
					SpecialKiller = '{"text":"['+u'\u2764'+']","color":"light_purple"}'	
		
				if e.npc.world.getTempdata().get("TeamSize") == 1 :
					TeamColorKiller = "red"
					UnderlinedKiller = "false"
					ItalicKiller = "false"
					UnderlinedKilled = "false"
					ItalicKilled = "false"
					TeamColorKilled = "green"

				e.npc.executeCommand('/tellraw @a ["",{"text":"[","color":"dark_gray"},{"text":"Arena","color":"dark_red"},{"text":"] ","color":"dark_gray"},'+Special+',{"text":"'+str(NameKilled)+'","color":"'+str(TeamColorKilled)+'","underlined":"'+str(UnderlinedKilled)+'","italic":"'+str(ItalicKilled)+'"},{"text":"[","color":"white"},{"text":"'+str(int(KilledKills))+'","color":"white"},{"text":"]","color":"white"},{"text":" was slain by ","color":"gray"},'+SpecialKiller+',{"text":"'+str(NameKiller)+'","color":"'+str(TeamColorKiller)+'","underlined":"'+str(UnderlinedKiller)+'","italic":"'+str(ItalicKiller)+'"},{"text":"[","color":"white"},{"text":"'+str(ActualisedKillerKills) +'","color":"white"},{"text":"]","color":"white"}]')
				if (int(e.npc.world.getStoreddata().get(str(NameKiller) +"Kills")) % 5 == 0) and (e.npc.world.getTempdata().get("CurrentGame") == "bow"):
					e.npc.executeCommand('/tellraw @a ["",{"text":"[","color":"dark_gray"},{"text":"Arena","color":"dark_red"},{"text":"]","color":"dark_gray"},{"text":"'+str(NameKiller)+'"},{"text":" is now on a ","color":"gray"},{"text":"'+str(int(e.npc.world.getStoreddata().get(str(NameKiller) +"Kills")))+'","color":"green"},{"text":" killstreak","color":"gray"}]')
					if int(e.npc.world.getStoreddata().get(str(NameKiller) +"Kills")) == 5 :
						e.npc.executeCommand('/give '+str(NameKiller)+' minecraft:diamond_helmet 1 0 {Unbreakable:1,ench:[{id:4,lvl:2}]}')
					elif int(e.npc.world.getStoreddata().get(str(NameKiller) +"Kills")) == 15 :
						e.npc.executeCommand('/give '+str(NameKiller)+' minecraft:diamond_leggings 1 0 {Unbreakable:1,ench:[{id:4,lvl:2}]}')
					elif int(e.npc.world.getStoreddata().get(str(NameKiller) +"Kills")) == 30 :
						e.npc.executeCommand('/give @a minecraft:diamond_chestplate 1 0 {Unbreakable:1,ench:[{id:0,lvl:2}]}')
				
				InventorySpawn(e)
			except :				# If Killed by PvE
				e.npc.executeCommand('/tellraw @a ["",{"text":"[","color":"dark_gray"},{"text":"Arena","color":"dark_red"},{"text":"] ","color":"dark_gray"},'+Special+',{"text":"'+str(NameKilled)+'","color":"'+str(TeamColorKilled)+'","underlined":"'+str(UnderlinedKilled)+'","italic":"'+str(ItalicKilled)+'"},{"text":"[","color":"white"},{"text":"'+str(int(KilledKills))+'","color":"white"},{"text":"]","color":"white"},'+SpecialKiller+',{"text":" died in PvE ","color":"gray"}]')
				InventorySpawn(e)
								
def DeathTchatMessage(e):
	'''Display chat message at death with custom colors depending on the killler and killed type and faction
	
		format : Killed was slain by Killer

		TRIGGER : InventorySpawn(e)
		
		EXCEPTION : if no killer is found, "PVE" death message is diplayed instead
	'''
	if e.npc.world.getTempdata().get("BadlionKillsSystem") == False :
		Special = '{"text":"","color":"light_purple"}'
		SpecialKiller = '{"text":"","color":"light_purple"}'
		SpecialList = ["Natsu91","Yvant2000Games","Frizou","iKowz","MASTEEKH","jdegoederen","reb_hi","Strykerss","Etoiles","xGokuuuh","Pikachu","TryHqrd_","_Mik0GODESS","SqndSt0rm","Divinity_Kirito","slooonay","Pxdro","Restump","Nardcoo","Ladak","VERSKUUUH","seltix_x","Pacoima","MarkiLokuras","Boosta","DANTEH","Rzmeur","GrzyLight","Mqyland_hi","Mentally","BiboyQG"]
		NameKilled = e.npc.getDisplay().getName()				# Looking for own data
		KilledFaction = e.npc.getFaction().getId()
		UnderlinedKilled = "false"
		UnderlinedKiller = "false"
		ItalicKilled = "false"
		ItalicKiller = "false"
		if NameKilled in SpecialList :
			Special = '{"text":"['+u'\u2764'+']","color":"light_purple"}'
				
		FactionArgList = [["green","false","false"],["green","false","false"],["blue","false","false"],["red","false","false"],["yellow","false","false"],["dark_gray","false","false"],["dark_blue","false","false"],["dark_red","false","false"],["dark_green","false","false"],["gold","false","false"],["aqua","false","false"],["light_purple","false","false"],["dark_aqua","false","false"],["dark_purple","false","false"],["green","false","true"],["blue","false","true"],["red","false","true"],["yellow","false","true"],["dark_gray","false","true"],["dark_blue","false","true"],["dark_red","false","true"],["dark_green","false","true"],["gold","false","true"],["aqua","false","true"],["light_purple","false","true"],["dark_aqua","false","true"],["white","false","false"]]
		TeamColorKilled = FactionArgList[KilledFaction][0]
		UnderlinedKilled = FactionArgList[KilledFaction][1]
		ItalicKilled = FactionArgList[KilledFaction][2]

		try :											# If killed by a bot
			KillerFaction = e.source.getFaction().getId()
			NameKiller = e.source.getDisplay().getName()
			KillerKills = e.source.getStoreddata().get("Kills")
			TeamColorKiller = FactionArgList[KillerFaction][0]
			UnderlinedKiller = FactionArgList[KillerFaction][1]
			ItalicKiller = FactionArgList[KillerFaction][2]

			if NameKiller in SpecialList :
				SpecialKiller = '{"text":"['+u'\u2764'+']","color":"light_purple"}'	

			if e.npc.world.getTempdata().get("TeamSize") == 1 :
				TeamColorKiller = "white"
				UnderlinedKiller = "false"
				ItalicKiller = "false"
				UnderlinedKilled = "false"
				ItalicKilled = "false"
				TeamColorKilled = "white"

			if KillerKills == None :
				KillerKills = 0

			if ((int(KillerKills)+1) % 5 == 0) and (e.npc.world.getTempdata().get("CurrentGame") == "bow"):
				e.npc.executeCommand('/tellraw @a ["",{"text":"[","color":"dark_gray"},{"text":"Arena","color":"dark_red"},{"text":"]","color":"dark_gray"},{"text":"'+str(NameKiller)+'"},{"text":" is now on a ","color":"gray"},{"text":"'+str(int(KillerKills)+1)+'","color":"green"},{"text":" killstreak","color":"gray"}]')

			e.npc.executeCommand('/tellraw @a ["",{"text":"[","color":"dark_gray"},{"text":"Arena","color":"dark_red"},{"text":"] ","color":"dark_gray"},'+Special+',{"text":"'+str(NameKilled)+'","color":"'+str(TeamColorKilled)+'","underlined":"'+str(UnderlinedKilled)+'","italic":"'+str(ItalicKilled)+'"},{"text":" was slain by ","color":"gray"},'+SpecialKiller+',{"text":"'+str(NameKiller)+'","color":"'+str(TeamColorKiller)+'","underlined":"'+str(UnderlinedKiller)+'","italic":"'+str(ItalicKiller)+'"}]')
		except :
			try :							 # If killed by a Player
				NameKiller = e.source.getName()
				KillerKills = e.npc.world.getStoreddata().get(str(NameKiller) +"Kills")
				TeamColorKiller = "white"
				UnderlinedKiller = "false"
				ItalicKiller = "false"
				if KillerKills == None :
					KillerKills = 0
				AddingKillsToPlayer = KillerKills + 1
				ActualisedKillerKills = int(KillerKills) ++ 1
				e.npc.world.getStoreddata().put(str(NameKiller)+"Kills", AddingKillsToPlayer)

				if NameKiller in SpecialList :
					SpecialKiller = '{"text":"['+u'\u2764'+']","color":"light_purple"}'	

				if e.npc.world.getTempdata().get("TeamSize") == 1 :
					TeamColorKiller = "white"
					UnderlinedKiller = "false"
					ItalicKiller = "false"
					UnderlinedKilled = "false"
					ItalicKilled = "false"
					TeamColorKilled = "white"

				e.npc.executeCommand('/tellraw @a ["",{"text":"[","color":"dark_gray"},{"text":"Arena","color":"dark_red"},{"text":"] ","color":"dark_gray"},'+Special+',{"text":"'+str(NameKilled)+'","color":"'+str(TeamColorKilled)+'","underlined":"'+str(UnderlinedKilled)+'","italic":"'+str(ItalicKilled)+'"},{"text":" was slain by ","color":"gray"},'+SpecialKiller+',{"text":"'+str(NameKiller)+'","color":"'+str(TeamColorKiller)+'","underlined":"'+str(UnderlinedKiller)+'","italic":"'+str(ItalicKiller)+'"}]')
				if (int(e.npc.world.getStoreddata().get(str(NameKiller) +"Kills")) % 5 == 0) and (e.npc.world.getTempdata().get("CurrentGame") == "bow"):
					e.npc.executeCommand('/tellraw @a ["",{"text":"[","color":"dark_gray"},{"text":"Arena","color":"dark_red"},{"text":"]","color":"dark_gray"},{"text":"'+str(NameKiller)+'"},{"text":" is now on a ","color":"gray"},{"text":"'+str(int(e.npc.world.getStoreddata().get(str(NameKiller) +"Kills")))+'","color":"green"},{"text":" killstreak","color":"gray"}]')
					if int(e.npc.world.getStoreddata().get(str(NameKiller) +"Kills")) == 5 :
						e.npc.executeCommand('/give '+str(NameKiller)+' minecraft:diamond_helmet 1 0 {Unbreakable:1,ench:[{id:4,lvl:2}]}')
					elif int(e.npc.world.getStoreddata().get(str(NameKiller) +"Kills")) == 15 :
						e.npc.executeCommand('/give '+str(NameKiller)+' minecraft:diamond_leggings 1 0 {Unbreakable:1,ench:[{id:4,lvl:2}]}')
					elif int(e.npc.world.getStoreddata().get(str(NameKiller) +"Kills")) == 30 :
						e.npc.executeCommand('/give @a minecraft:diamond_chestplate 1 0 {Unbreakable:1,ench:[{id:0,lvl:2}]}')
						
				
				InventorySpawn(e)
			except :				# If Killed by PvE
				e.npc.executeCommand('/tellraw @a ["",{"text":"[","color":"dark_gray"},{"text":"Arena","color":"dark_red"},{"text":"] ","color":"dark_gray"},'+Special+',{"text":"'+str(NameKilled)+'","color":"'+str(TeamColorKilled)+'","underlined":"'+str(UnderlinedKilled)+'","italic":"'+str(ItalicKilled)+'"},{"text":" died in PvE ","color":"gray"}]')
				InventorySpawn(e)

def VanillaDeathStyle(e):
	'''Cancel the display of bot's armor if he die, to make it looks like player, or despawn it instantly, depending on the UHC rules
	'''
	if e.npc.world.getTempdata().get("VanillaDeathStyle") == True :	# Clearing Npc's armor before he die to show only his skin
		e.npc.getInventory().setArmor(0, None)
		e.npc.getInventory().setArmor(1, None)
		e.npc.getInventory().setArmor(2, None)
		e.npc.getInventory().setArmor(3, None)
		e.npc.getInventory().setRightHand(None)
		e.npc.getStats().setResistance(2, -1)
	else :
		e.npc.despawn()
		pass

def ExplodeOnDeath(e):
	'''Display an explosion at the location of the death of the bot
	'''
	if e.npc.world.getTempdata().get("ExplodeOnDeath") == True :
		e.npc.world.explode(e.npc.getX(),e.npc.getY()+1,e.npc.getZ(),0, False, False)




#ON KILL ONLY functions :	

def IronGolemSound(e):
	'''Play the IronGolem death sound to the killer of the bot
	'''
	try :
		IronGolemSound = e.npc.world.getTempdata().get("IronGolemSound")
		NameKiller = e.source.getName()
		X = e.source.getX()
		Y = e.source.getY()
		Z = e.source.getZ()
		if IronGolemSound == True :
			e.npc.executeCommand('/playsound mob.irongolem.death '+str(NameKiller)+' '+str(X)+' '+str(Y)+' '+str(Z)+'')
	except :
		pass

def WitherSoundI(e):
	'''Play the Wither death sound to the killer of the bot
	'''
	try :
		IronGolemSound = e.npc.world.getTempdata().get("WitherSoundI")
		NameKiller = e.source.getName()
		X = e.source.getX()
		Y = e.source.getY()
		Z = e.source.getZ()
		if IronGolemSound == True :
			e.npc.executeCommand('/playsound mob.wither.death '+str(NameKiller)+' '+str(X)+' '+str(Y)+' '+str(Z)+'')
	except :
		pass	

def WitherSoundII(e):
	'''Play the Wither spawn sound to the killer of the bot
	'''
	try :
		IronGolemSound = e.npc.world.getTempdata().get("WitherSoundII")
		NameKiller = e.source.getName()
		X = e.source.getX()
		Y = e.source.getY()
		Z = e.source.getZ()
		if IronGolemSound == True :
			e.npc.executeCommand('/playsound mob.wither.spawn '+str(NameKiller)+' '+str(X)+' '+str(Y)+' '+str(Z)+'')
	except :
		pass	

def BadlionKillsSystem(e):
	'''Count every kills the bot make to be displayed in the BadlionDeathMessage(e)
	'''
	Name = e.npc.getDisplay().getName()
	Kills = e.npc.getStoreddata().get("Kills")
	if Kills == None :
		Kills = 1
		e.npc.getStoreddata().put("Kills", Kills)
	else :
		Kills += 1
		e.npc.getStoreddata().put("Kills", Kills)

def ScoreBoardUpdateI(e):
	'''Count kills of the bot in the sidebar
		- must have RedditUHCDisplay to True
	'''
	RedditUHCDisplay = e.npc.world.getTempdata().get("RedditUHCDisplay")
	if RedditUHCDisplay == True :
		Name = e.npc.getDisplay().getName()
		e.npc.executeCommand('/scoreboard players add '+str(Name)+' Arena 1')

def StuffUpgradeOnKill(e) :
	'''Update armor and sword tier, and enchant levels like if he anvil-ed the stuff he looted on his kill
	'''
	try :
		if (e.npc.world.getTempdata().get("CurrentGame") == "bow"):
			MyProt = e.npc.getStoreddata().get("Prot")
			MyProj = e.npc.getStoreddata().get("Proj")
			Sword = e.npc.getStoreddata().get("Sword")

			MyProj = MyProj.split("/")
			MyProt = MyProt.split("/")
			Sword = Sword.split("/")

			ArmorList = "4/5/6/7"

			if int(e.npc.getStoreddata().get("Kills")) == 5:
				e.npc.getInventory().setArmor(0,e.npc.world.createItem("minecraft:diamond_helmet",0,1))
				ArmorList.replace("4", "1") 

			elif int(e.npc.getStoreddata().get("Kills")) == 15:
				e.npc.getInventory().setArmor(2,e.npc.world.createItem("minecraft:diamond_leggings",0,1))
				ArmorList.replace("6", "1")

			elif int(e.npc.getStoreddata().get("Kills")) == 30:
				e.npc.getInventory().setArmor(1,e.npc.world.createItem("minecraft:diamond_chestplate",0,1))
				ArmorList.replace("5", "1")

			elif int(e.npc.getStoreddata().get("Kills")) == 40:
				e.npc.getInventory().setRightHand(e.npc.world.createItem("minecraft:diamond_sword",0,1))



			ProtList = "/".join(MyProt)
			ProjList = "/".join(MyProj)
			SwordList = "/".join(Sword)
			
			e.npc.getStoreddata().put("Prot", ProtList)
			e.npc.getStoreddata().put("Proj", ProjList)
			e.npc.getStoreddata().put("Armor", ArmorList)
			e.npc.getStoreddata().put("Sword", SwordList)
			e.npc.getTempdata().put("GapCount", e.npc.getTempdata().get("GapCount")+2)

			WaterRemainig = e.npc.getTempdata().get("WaterRemaining")
			if WaterRemainig != None :
				WaterRemainig == 3
				e.npc.getTempdata().put("WaterRemaining", WaterRemainig)
			else :
				e.npc.getTempdata().put("WaterRemaining", 3)

		if (e.npc.world.getTempdata().get("CurrentGame") == "melee"):
			e.npc.getTempdata().put("GapCount", e.npc.getTempdata().get("GapCount")+10)
	except Exception as err:
		e.npc.say(str(err))

def ThunderStrike(e):
	'''Display a thunder ABOVE the kill to avoid item burning or insta-killing killer
	'''
	ThunderActivated = e.npc.world.getTempdata().get("ThunderStrike")
	if ThunderActivated == True :
		X = e.npc.getX()
		Y = e.npc.getY()
		Z = e.npc.getZ()
		e.npc.world.thunderStrike(X, Y+5, Z)



#SCENARIOS functions :				

def AbsoLess(e):
	'''Remove absorption effect every tick to everyone
	'''
	if e .npc.world.getTempdata().get("AbsoLess") == True :
		e.npc.executeCommand("/effect @a minecraft:absorption 0")

def NoCleanUpActivation(e) :
	'''Instantly give the configured amount of HP to the killer
	'''
	try:
		NoCleanScenario = e.npc.world.getTempdata().get("NoCleanUpEnabled")
		if NoCleanScenario == True :
			NoCleanConfig = e.npc.world.getTempdata().get("NoCleanRegen")
			KillerHP1 = e.source.getHealth()
			KillerHP = round(KillerHP1)
			NoClean = KillerHP ++ NoCleanConfig
			e.source.setHealth(float(NoClean))
	except:
		pass

def RodlessActivation(e):
	'''Different reach attribution if RodLess is enabled
	'''
	if e.npc.getStoreddata().get("IsEating") != True :
		SelectedType = e.npc.getTempdata().get("SelectedType")
		Rodless = e.npc.world.getTempdata().get("Rodless")
		if Rodless == True :
			if SelectedType == "CasualTier" :
				ReachList = [1, 2, 2, 2, 2, 2, 2, 2, 2, 2]
				NewReach = random.choice(ReachList)
				e.npc.getStats().getMelee().setRange(NewReach)

			if SelectedType == "CommonTier" :
				ReachList = [1, 2, 2, 2, 2, 2, 2, 3, 3, 3]
				NewReach = random.choice(ReachList)
				e.npc.getStats().getMelee().setRange(NewReach)

			if SelectedType == "GoodTier" :
				ReachList = [1, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3]
				NewReach = random.choice(ReachList)
				e.npc.getStats().getMelee().setRange(NewReach)

			if SelectedType == "ProTier" :
				ReachList = [1, 2, 2, 2, 2, 2, 3, 3, 3, 3]
				NewReach = random.choice(ReachList)
				e.npc.getStats().getMelee().setRange(NewReach)

			if SelectedType == "UHCEliteTier" :
				ReachList = [1, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3]
				NewReach = random.choice(ReachList)
				e.npc.getStats().getMelee().setRange(NewReach)

			if SelectedType == "NoobTier" :
				ReachList = [2, 2, 1, 1, 1, 1, 1, 1, 1, 1]
				NewReach = random.choice(ReachList)
				e.npc.getStats().getMelee().setRange(NewReach)
	else :
		e.npc.getStats().getMelee().setRange(0)



#INIT GAME functions :

def SettingEntity(e):
	"""
	Generate a bot with a tier, a skin, a cape, and a name depending of the lists and the config
	"""
	import random
	Name = e.npc.getDisplay().getName()
	GameStarted = e.npc.world.getTempdata().get("GameStarted")
	tick = 0
	try :
		if (GameStarted == 1) and ((Name == "Disabled") or (Name == "-") or (Name == "")):

			ChoosingList = ["NoobTier","CasualTier","CommonTier","GoodTier","ProTier","UHCEliteTier"]

			if len(e.npc.world.getTempdata().get("NameTier"+str("NoobTier"))) == 0 :
				ChoosingList.remove("NoobTier")
			if len(e.npc.world.getTempdata().get("NameTier"+str("CasualTier"))) == 0:
				ChoosingList.remove("CasualTier")
			if len(e.npc.world.getTempdata().get("NameTier"+str("CommonTier"))) == 0:
				ChoosingList.remove("CommonTier")
			if len(e.npc.world.getTempdata().get("NameTier"+str("GoodTier"))) == 0:
				ChoosingList.remove("GoodTier")
			if len(e.npc.world.getTempdata().get("NameTier"+str("ProTier"))) == 0:
				ChoosingList.remove("ProTier")
			if len(e.npc.world.getTempdata().get("NameTier"+str("UHCEliteTier"))) == 0:
				ChoosingList.remove("UHCEliteTier")

			Level = random.choice(ChoosingList)
				
			if (e.npc.world.getTempdata().get("ForcedType") == True) and (len(e.npc.world.getTempdata().get("NameTier"+str("UHCEliteTier"))) != 0 ):
				Level = "UHCEliteTier" 


			AllowedList = ["_"]
			e.npc.getTempdata().put("SelectedType", Level)
			SelectedName = random.choice(e.npc.world.getTempdata().get("NameTier"+str(Level)))

			if Level in ["NoobTier","CasualTier","CommonTier","GoodTier"] :
				Random = random.randint(1, 71)
				SelectedName = list(SelectedName)
				for i in range(0, len(SelectedName)):
					if (SelectedName[i].isalnum() == True) or (SelectedName[i] in AllowedList):
						pass
					else:
						SelectedName.pop(i)
				SelectedName = "".join(SelectedName)
				e.npc.getDisplay().setName(str(SelectedName))
				e.npc.getDisplay().setSkinTexture('minecraft:textures/entity/Random'+str(Random)+'.png')

			else :
				e.npc.getDisplay().setSkinTexture('minecraft:textures/entity/'+SelectedName+'.png')
				SelectedName = list(SelectedName)
				for i in range(0, len(SelectedName)):
					if (SelectedName[i].isalnum() == True) or (SelectedName[i] in AllowedList):
						pass
					else:
						SelectedName.pop(i)
				SelectedName = "".join(SelectedName)
				e.npc.getDisplay().setName(str(SelectedName))

			RandomForCape = random.randint(1, 3)
			if RandomForCape == 3:
				RandomCape = random.randint(1, 35)
				e.npc.getDisplay().setCapeTexture('minecraft:textures/cloak/'+str(RandomCape)+'.png')

			if e.npc.world.getTempdata().get("ScatterMessageEnabled") == True :
				e.npc.executeCommand('/tellraw @a ["",{"text":"[","color":"dark_gray"},{"text":"Arena","color":"dark_red"},{"text":"] ","color":"dark_gray"},{"text":"[","color":"gold"},{"text":"Scatter","color":"blue"},{"text":"] ","color":"gold"},{"text":"Scattered ","color":"dark_red"},{"text":"'+str(SelectedName)+'","color":"gray"}]')
			else :
				pass
		else:
			pass
	except Exception as err:
		e.npc.world.broadcast(str(err))
		e.npc.world.broadcast("Deleting because of NoName " + str(e.npc.world.getStoreddata().get("Players")))
		e.npc.despawn()

def SettingArmor(e) :
	"""
	Initialize the bot armor display + enchants
	"""
	if e.npc.getInventory().getArmor(0) == None :
		if e.npc.world.getTempdata().get("CurrentGame") == "melee":
			PartList = ["_helmet","_chestplate","_leggings","_boots"]
			ProtList = []			# The protection enchant list
			ProjList = []			# The projectile protection enchant list
			ArmorList = []			# The Armor material list
			BowList = []			# The bow enchant list
			SwordList = []			# The sword enchant list

			KbList = [0]  # Because its way too annoying
			UnbreakList = [0,0,0,0,0,0,0,0,0,1,2,1,1,2]
			PowerList = [1,1,2,2,2,2,2,2,3,3]
			PowerArcticList = [1,1,2,2,2,3,3,3,3,4,4,5]

			for i in range(0,4):
				if e.npc.getInventory().getArmor(i) == None :
					e.npc.getInventory().setArmor(i,e.npc.world.createItem("minecraft:diamond"+str(PartList[i]),0,1))
					ArmorList.append("1")
				if (i == 0) or (i == 3):
					ProtList.append("0")
					ProjList.append("1")
				else:
					ProtList.append("1")
					ProjList.append("0")


			e.npc.getInventory().setRightHand(e.npc.world.createItem("minecraft:diamond_sword",0,1))
			SwordList.append("3")
			SwordList.append("0")
			SwordList.append("0")
			SwordList.append("0")
			BowList.append("2")
			e.npc.getTempdata().put("GapCount", 10)
		else:
			PartList = ["_helmet","_chestplate","_leggings","_boots"]
			ProtList = []			# The protection enchant list
			ProjList = []			# The projectile protection enchant list
			ArmorList = []			# The Armor material list
			BowList = []			# The bow enchant list
			SwordList = []			# The sword enchant list

			KbList = [0]  # Because its way too annoying
			UnbreakList = [0,0,0,0,0,0,0,0,0,1,2,1,1,2]
			PowerList = [1,1,2,2,2,2,2,2,3,3]
			PowerArcticList = [1,1,2,2,2,3,3,3,3,4,4,5]

			for i in range(0,3):
				if e.npc.getInventory().getArmor(i) == None :
					e.npc.getInventory().setArmor(i,e.npc.world.createItem("minecraft:iron"+str(PartList[i]),0,1))
					ArmorList.append("0")
				if (i == 0) or (i == 2):
					ProtList.append("0")
					ProjList.append("2")
				else:
					ProtList.append("1")
					ProjList.append("0")

			e.npc.getInventory().setArmor(3,e.npc.world.createItem("minecraft:diamond_boots",0,1))
			ArmorList.append("1")
			ProtList.append("2")
			ProjList.append("0")

			e.npc.getInventory().setRightHand(e.npc.world.createItem("minecraft:iron_sword",0,1))
			SwordList.append("1")
			SwordList.append("0")
			SwordList.append("0")
			SwordList.append("0")
			BowList.append("4")
			e.npc.getTempdata().put("GapCount", 1)
			
			
		ProtList = "/".join(ProtList)
		ProjList = "/".join(ProjList)
		SwordList = "/".join(SwordList)
		ArmorList = "/".join(ArmorList)
		BowList = "/".join(BowList)
		
		e.npc.getStoreddata().put("Prot", ProtList)
		e.npc.getStoreddata().put("Proj", ProjList)
		e.npc.getStoreddata().put("Armor", ArmorList)
		e.npc.getStoreddata().put("Bow", BowList)
		e.npc.getStoreddata().put("Sword", SwordList)
		e.npc.getTempdata().put("WaterRemaining", random.randint(1, 3))

def SettingResistance(e):
	"""
	Calculation of resistance melee/arrow depending of the armor and enchants the bot have.
	Also set the melee damage
	"""
	if e.npc.world.getTempdata().get("OneShot") != True :
		# resistance melee du fer : 10 30 20 10 // Arrow : 5 20 20 5  // Degat : 9
		# resistance melee du diamant : 12.5 40 25 12.5 // Arrow : 5  30 20 5 // Degat : 11
		MeleeResToSet = 0
		ProjToSet = 0
		DamageToSet = 0
		DiamondPart = 0
		Sword = e.npc.getStoreddata().get("Sword")
		Prot = e.npc.getStoreddata().get("Prot")
		Proj = e.npc.getStoreddata().get("Proj")
		Armor = e.npc.getStoreddata().get("Armor")
		Bow = e.npc.getStoreddata().get("Bow")


		Sword = Sword.split("/")
		Prot = Prot.split("/")
		Armor = Armor.split("/")
		Proj = Proj.split("/")
		Bow = Bow.split("/")

		e.npc.getStats().getMelee().setKnockback(int(Sword[2]))
		if int(Sword[1]) == 1 :
			e.npc.getStats().getMelee().setEffect(1,1,5)


		if int(Armor[0]) == 1 :							# Diamond Helmet
			ProtEffect = int(Prot[0]) * 0.008
			ProjEffect = int(Proj[0]) * 0.02
			MeleeResToSet += 0.13 + ProtEffect
			ProjToSet += 0.15 + ProjEffect
		else :
			ProtEffect = int(Prot[0]) * 0.008
			ProjEffect = int(Proj[0]) * 0.02
			MeleeResToSet += 0.1 + ProtEffect
			ProjToSet += 0.1 + ProjEffect
		

		if int(Armor[1]) == 1 :							# Diamond Chestplate
			ProtEffect = int(Prot[1]) * 0.008
			ProjEffect = int(Proj[1]) * 0.02
			MeleeResToSet += 0.33 + ProtEffect
			ProjToSet += 0.3 + ProjEffect
		else :
			ProtEffect = int(Prot[1]) * 0.012
			ProjEffect = int(Proj[1]) * 0.02
			MeleeResToSet += 0.3 + ProtEffect
			ProjToSet += 0.2 + ProjEffect


		if int(Armor[2]) == 1 :							# Diamond Leggings
			ProtEffect = int(Prot[2]) * 0.008
			ProjEffect = int(Proj[2]) * 0.02
			MeleeResToSet += 0.22 + ProtEffect
			ProjToSet += 0.15 + ProjEffect
		else :
			ProtEffect = int(Prot[2]) * 0.008
			ProjEffect = int(Proj[2]) * 0.02
			MeleeResToSet += 0.19 + ProtEffect
			ProjToSet += 0.2 + ProjEffect


		if int(Armor[3]) == 1 :							# Diamond Boots
			ProtEffect = int(Prot[3]) * 0.008
			ProjEffect = int(Proj[3]) * 0.02
			MeleeResToSet += 0.13 + ProtEffect
			ProjToSet += 0.15 + ProjEffect
		else :
			ProtEffect = int(Prot[3]) * 0.008
			ProjEffect = int(Proj[3]) * 0.02
			MeleeResToSet += 0.1 + ProtEffect
			ProjToSet += 0.1 + ProjEffect


		MeleeResToSet += 1
		ProjToSet += 1

		if MeleeResToSet >= 2 :
			MeleeResToSet = 1.96

		e.npc.getStats().setResistance(0, (MeleeResToSet))
		e.npc.getStats().setResistance(1, (ProjToSet))
		try :
			e.npc.getInventory().getRightHand().getName()
		except:
			e.npc.getInventory().setRightHand(e.npc.world.createItem("minecraft:diamond_sword",0,1))
			
		if e.npc.getInventory().getRightHand().getName() == "minecraft:diamond_sword" :	# Diamond sword
			SwordEffect = int(Sword[0]) * 1.25
			DamageToSet = 7 + int(SwordEffect)
		else :													# iron Sword
			SwordEffect = int(Sword[0]) * 1.25
			DamageToSet = 6 + int(SwordEffect)

		e.npc.getStats().getMelee().setStrength(DamageToSet)
	else :
		e.npc.getStats().setResistance(0, -1)
		e.npc.getStats().setResistance(1, -1)
		e.npc.getStats().getMelee().setStrength(100)

def ActualisingTeamMembers(e):
	"""
	Send team members of every teams in the global list 
	"""
	GameRunning = e.npc.world.getTempdata().get("GameRunning")
	if GameRunning == 1 :
		Name = e.npc.getDisplay().getName()
		if Name != "Disabled" :
			Posted = e.npc.getStoreddata().get("IDPosted")
			TeamID = e.npc.getFaction().getId()
			PlayerList = e.npc.world.getStoreddata().get("PlayerList")
			if PlayerList == None and Posted == None :
				e.npc.world.getStoreddata().put("PlayerList", str(Name)+"/"+str(TeamID))
				e.npc.getStoreddata().put("IDPosted", 1)
			elif PlayerList != None and Posted == None :
				try :
					PlayerList = PlayerList.split("//")
				except:
					PlayerList = list(PlayerList)
				PlayerList.append(str(Name)+"/"+str(TeamID))
				PlayerList = "//".join(PlayerList)
				e.npc.world.getStoreddata().put("PlayerList", PlayerList)
				e.npc.getStoreddata().put("IDPosted", 1)

def ScoreBoardUpdateIII(e):
	"""
	Make every bot join the right scoreboard team depending of his faction
	Used to add color to sidebar when RedditUHCDisplay is true 
	"""
	pass

def SettingInitialKills(e):
	"""
	Initialize kills to 0 
	"""
	Kills = e.npc.getStoreddata().get("Kills")
	if Kills == None :
		e.npc.getStoreddata().put("Kills", 0)

def MayStopArena(e):
	NeedStop = e.npc.world.getTempdata().get("NeedStop")
	if NeedStop == None :
		e.npc.despawn()


#TEAMER BOTS ONLY functions :

def GappleSharing(e):
	"""
	Giving a golden_apple to the bot when you right click him, if he is in your team, and if you have a gap to give.
	Display back the number of gap the bot have
	"""
	try:
		FactionID = e.npc.getFaction().getId()
		if FactionID == 26 :
			Teaming(e)
			if e.player.getHeldItem().getName() == "minecraft:golden_apple":
				e.npc.getTempdata().put("GapCount", e.npc.getTempdata().get("GapCount")+1)
				e.player.getHeldItem().setStackSize(e.player.getHeldItem().getStackSize()-1)
				e.npc.executeCommand('/tellraw @a ["",{"text":"[","color":"dark_gray"},{"text":"Team","color":"red"},{"text":"] ","color":"dark_gray"},{"text":"'+str(e.npc.getDisplay().getName())+'","color":"white"},{"text":":","color":"dark_gray"},{"text":" I have ","color":"gray"},{"text":"'+str(e.npc.getTempdata().get("GapCount"))+'","color":"dark_gray"},{"text":" golden apple","color":"gray"}]')
		else :
			pass
	except:
		pass
		
def KillingPlayer(e):
	"""
	Sending data to the Server bots to display player elimination message
	"""
	try :
		e.npc.world.getTempdata().put(str(e.entity.getName()+"Killer"), [str(e.npc.getDisplay().getName()),str(e.npc.getFaction().getId()),str(e.npc.getStoreddata().get("Kills"))])
	except:
		pass
		
def Teaming(e):
	"""
	Making bots with faction ID = 26 follow the player that interacted with them
	"""
	if e.npc.getFaction().getId() == 26 :
		Source = e.player.getMCEntity()
		e.npc.getRole().setInfinite(1)
		e.npc.getRole().setGuiDisabled(1)
		e.npc.getRole().setOwner(Source)

def AllyResistance(e):		#Not needed but just to prevent ez kill ally bot 
	"""
	Give Resistance II to Ally bots, to prevent them from dying easily
	"""
	if e.npc.getFaction().getId() == 26 :
		e.npc.addPotionEffect(11, 100000, 1, False)



#IN GAME functions :

def EnableFallDamage(e):
	e.npc.getStats().noFallDamage = False

def NoStackedFights(e):                      # If target stacked avoid fight if stacked too
	"""
	Avoid fighting another stacked target, stacked = 4 Kills or more
	"""
	if (int(e.npc.world.getStoreddata().get("TeamsAlive")) > 12 ) and (e.npc.world.getTempdata().get("TeamSize") == 1):
		try:
			if [str(e.npc.getAttackTarget().getDisplay().getName()), str(int(e.npc.getAttackTarget().getStoreddata().get("Kills")))] in e.npc.world.getTempdata().get("StackedList"):
				e.npc.setAttackTarget(None)
				ChooseZone(e)
		except:
			pass

def ActualisingHealth(e):
	'''Calculate the health of the bot with Absorption
	'''
	if e.npc.getStoreddata().get("AbsoDisplay") <= 0 :
		e.npc.getStoreddata().put("AbsoDisplay", 0)
	else:
		e.npc.getStoreddata().put("AbsoDisplay", e.npc.getStoreddata().get("AbsoDisplay")-e.damage)

def WeatherClear(e):
	'''Clear weather
	'''
	e.npc.executeCommand("/weather clear")

def WantToRod(e):
	'''Regulate the use of the rod
	'''
	try:
		if e.npc.world.getTempdata().get("Rodless") != True :
			if e.npc.getStoreddata().get("IsEating") != True :
				Hp = e.npc.getHealth()
				TX = e.npc.getAttackTarget().getX()
				TZ = e.npc.getAttackTarget().getZ()
				X = e.npc.getX()
				Z = e.npc.getZ()
				Target = e.npc.getAttackTarget()

				FX = (X - TX)**2
				FZ = (Z - TZ)**2
				Dist = math.sqrt(FX + FZ)


				if (7 <= Hp <= 12) and (random.randint(0, 5) == 0) and (e.npc.getTempdata().get("GapCount") != 0):
					e.npc.getTempdata().put("NeedRod", e.npc.getTempdata().get("NeedRod")+1)

				if (6 <= Dist <= 9) and (random.randint(0, 5) == 0):
					e.npc.getTempdata().put("NeedRod", e.npc.getTempdata().get("NeedRod")+1)
			
				if random.randint(0, 20) == 0 :
					e.npc.getTempdata().put("NeedRod", e.npc.getTempdata().get("NeedRod")+1)
	except:		
		pass

def Rod(e):
	'''Throw a snowball as a rod every tick
	'''
	if e.npc.world.getTempdata().get("Rodless") != True :
		if e.npc.world.getTempdata().get("OneShot") != True :
			if e.npc.getTempdata().get("NeedRod") == None :
				e.npc.getTempdata().put("NeedRod", 0)

			if e.npc.getTempdata().get("NeedRod") != 0 :
				try:
					Rotate = e.npc.getRotation()
					if (e.npc.getTempdata().get("SelectedType") != "UHCEliteTier") or (e.npc.getTempdata().get("SelectedType") != "ProTier"):
						Int = 100
					else:
						Int = 85
					e.npc.shootItem(e.npc.getAttackTarget(),e.npc.world.createItem("minecraft:snowball",0,1), Int)
					e.npc.getTempdata().put("NeedRod", (e.npc.getTempdata().get("NeedRod")-1))
				except:
					pass
		else :
			try:
				Rotate = e.npc.getRotation()
				e.npc.getStats().getRanged().setStrength(150)
				if e.npc.getTempdata().get("TickOneShot") == 1 :
					e.npc.shootItem(e.npc.getAttackTarget(),e.npc.world.createItem("minecraft:arrow",0,1), 65)
					e.npc.getTempdata().put("NeedRod", (e.npc.getTempdata().get("NeedRod")-1))
					e.npc.getTempdata().put("TickOneShot", 0)
				else :
					e.npc.getTempdata().put("TickOneShot", 1)
			except:
				pass

def AntiFreeDeath(e):
	'''Cancel lava-death
	'''
	Source = str(e.mcDamageSource)
	Source = Source.split("@")
	if (Source[0] == "net.minecraft.util.DamageSource") and (e.npc.getHealth() <= 8):
		e.setCanceled(True)       

def SwordDebug(e):
	'''Prevent bots from loosing their sword
	'''
	if e.npc.getInventory().getRightHand() == None :
		e.npc.getInventory().setRightHand(e.npc.world.createItem("minecraft:diamond_sword",0,1))
		SettingResistance(e)

def LifeMessageBow(e):
	'''Send message to the shooter when he hit his target + play sound
	'''
	try:
		Health = str(e.npc.getHealth() - e.damage)
		Type = str(e.mcDamageSource)
		Type = list(Type)
		Name = e.npc.getDisplay().getName()
		X = e.source.getX()
		Y = e.source.getY()
		Z = e.source.getZ()
		if float(Health) < 0 :
			Health = str(0)
		Health = round(float(Health))
		try :
			Source = e.source.getName()
			if Type[37] == "I" :
				e.npc.executeCommand('/tellraw '+str(Source)+' ["",{"text":"[","color":"dark_gray"},{"text":"Arena","color":"dark_red"},{"text":"] ","color":"dark_gray"},{"text":"[","color":"gold"},{"text":"Bow","color":"aqua"},{"text":"] ","color":"gold"},{"text":"'+str(Name)+'","color":"red"},{"text":" is now at ","color":"white"},{"text":"'+str(int(round(e.npc.getHealth()))+int(round(e.npc.getStoreddata().get("AbsoDisplay"))))+" "+u'\u2764'+'","color":"dark_red"}]')
				e.npc.executeCommand('/playsound random.successful_hit '+str(Source)+' '+str(X)+' '+str(Y)+' '+str(Z)+' 1 0.5')
		except:
			pass
	except:
		pass

def Strafing(e):
	'''Make the bot strafe ( need a fix )
	'''
	try :
		Level = e.npc.getTempdata().get("SelectedType") # Making the Npc strafe left or right with a timer and a side choosing script
		if Level != "NoobTier" : 							# Only NoobTier doesnt strafe
			TargetX = e.npc.getAttackTarget().getX()
			TargetZ = e.npc.getAttackTarget().getX()
			MyX = e.npc.getX()
			MyY = e.npc.getY()
			MyZ = e.npc.getZ()
			BaseStrafe = "left"

			try:
				StrafeTick += 1					# Creating a 'StrafeTick' variable if it doesnt exist
			except:
				StrafeTick = 0

			if StrafeTick == 4 and BaseStrafe == "left":
				BaseStrafe = "right"
			elif StrafeTick == 4 :
				BaseStrafe = "left"

			if (TargetX-1 <= MyX <= TargetX+1) and (TargetZ > MyZ):
				if BaseStrafe == "left" :
					e.npc.navigateTo(TargetX-2, MyY, TargetZ, 2) 		# Strafing left
				elif BaseStrafe == "right" :
					e.npc.navigateTo(TargetX+2, MyY, TargetZ, 2) 		# Strafing right

			elif (TargetX-1 <= MyX <= TargetX+1) and (TargetZ < MyZ):
				if BaseStrafe == "left" :
					e.npc.navigateTo(TargetX+2, MyY, TargetZ, 2) 		# ~
				elif BaseStrafe == "right" :
					e.npc.navigateTo(TargetX-2, MyY, TargetZ,2) 		# ~

			elif (TargetX > MyX) and (TargetZ-1 <= MyZ <= TargetZ+1):
				if BaseStrafe == "left" :
					e.npc.navigateTo(TargetX, MyY, TargetZ-2, 2) 		# ~
				elif BaseStrafe == "right" :
					e.npc.navigateTo(TargetX, MyY, TargetZ+2, 2) 		# ~

			elif (TargetX < MyX) and (TargetZ-1 <= MyZ <= TargetZ+1):
				if BaseStrafe == "left" :
					e.npc.navigateTo(TargetX, MyY, TargetZ+2, 2) 		# ~
				elif BaseStrafe == "right" :
					e.npc.navigateTo(TargetX, MyY, TargetZ-2, 2) 		# ~
	except :
		pass
	"""
	elif (TargetX < MyX) and (TargetZ < MyZ ) and (StrafeTick == 5):
		if BaseStrafe == "left" :
			e.npc.navigateTo(TargetX, MyY, TargetZ-1, 0) # Decal Gauche
		elif BaseStrafe == "right" :
			e.npc.navigateTo(TargetX-1, MyY, TargetZ, 0) # Decal Droite
	elif (TargetX > MyX) and (TargetZ > MyZ ) and (StrafeTick == 5):
		if BaseStrafe == "left" :
			e.npc.navigateTo(TargetX, MyY, TargetZ+1, 0) # Decal Gauche
		elif BaseStrafe == "right" :
			e.npc.navigateTo(TargetX+1, MyY, TargetZ, 0) # Decal Droite
	elif (TargetX > MyX) and (TargetZ < MyZ ) and (StrafeTick == 5):
		if BaseStrafe == "left" :
			e.npc.navigateTo(TargetX+1, MyY, TargetZ, 0) # Decal Gauche
		elif BaseStrafe == "right" :
			e.npc.navigateTo(TargetX, MyY, TargetZ-1, 0) # Decal Droite
	elif (TargetX < MyX) and (TargetZ > MyZ ) and (StrafeTick == 5):
		if BaseStrafe == "left" :
			e.npc.navigateTo(TargetX-1, MyY, TargetZ, 0) # Decal Gauche
		elif BaseStrafe == "right" :
			e.npc.navigateTo(TargetX, MyY, TargetZ+1, 0) # Decal Droite
	"""		
	
def Missing(e):
	'''Make the bot fail a hit sometime depending on his tier
	'''
	SelectedType = e.npc.getTempdata().get("SelectedType")							# Just cancelling the damage event if the Npc fail his hit to simulate an human AIM, better the Npc is, lower his miss chances are.
	if SelectedType == "CasualTier" :
		ReachList = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 3, 3, 3, 3]
		MissChance = random.choice(ReachList)
		if MissChance == 3 :
			e.setCanceled(True)

	if SelectedType == "CommonTier" :
		ReachList = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 3, 3, 3]
		MissChance = random.choice(ReachList)
		if MissChance == 3 :
			e.setCanceled(True)

	if SelectedType == "GoodTier" :
		ReachList = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 3]
		MissChance = random.choice(ReachList)
		if MissChance == 3 :
			e.setCanceled(True)

	if SelectedType == "ProTier" :
		ReachList = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 3]
		MissChance = random.choice(ReachList)
		if MissChance == 3 :
			e.setCanceled(True)

	if SelectedType == "UHCEliteTier" :
		ReachList = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 3, 1, 1, 1, 1, 3]
		MissChance = random.choice(ReachList)
		if MissChance == 3 :
			e.setCanceled(True)

	if SelectedType == "NoobTier" :
		ReachList = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 3, 3, 3, 3, 3, 3]
		MissChance = random.choice(ReachList)
		if MissChance == 3 :
			e.setCanceled(True)

def Targeting(e):
	'''Make the bot stop the chase if he is too far away
	'''
	if e.npc.getAttackTarget() != None :
		
		try:
			Target = e.entity
			if (abs(Target.getX() - e.npc.getX()) <= 20 )and (abs(Target.getZ() - e.npc.getZ()) <= 20):
				pass
			else:
				e.npc.setAttackTarget(None)
		except:
			pass
	"""
	TeamID = e.npc.getFaction().getId()
	TeamList = e.npc.world.getStoreddata().get(str(TeamID))
	TeamMode = e.npc.world.getTempdata().get("TeamSize")
	GapCount = e.npc.getTempdata().get("GapCount")
	PlayersLeft = e.npc.world.getStoreddata().get("Players")
	MyX = e.npc.getX()
	MyY = e.npc.getY()
	MyZ = e.npc.getZ()
	NearestPlayers = e.npc.world.getNearbyEntities(int(MyX), int(MyY), int(MyZ), 25, 2).tolist()
	TeamPresence = []
	Max = 0
	try :
		if e.npc.getAttackTarget().getDisplay().getName() == e.npc.getDisplay().getName() :
			e.npc.setAttackTarget(None)
		if e.npc.getAttackTarget().getFaction().getId() == TeamID :
			e.npc.setAttackTarget(None)
		if e.npc.getAttackTarget().getFaction().getId() == 0 :
			e.npc.setAttackTarget(None)
	except:
		pass

	if e.npc.getAttackTarget() == None :
		for i in range(len(NearestPlayers)-1, 0, -1):
			if NearestPlayers[i].getFaction().getId() == TeamID :
				NearestPlayers.pop(i)
					
		if (len(NearestPlayers) <= 10) and (len(NearestPlayers) > 1): # Targeting by largest team size
			for i in range (0, len(NearestPlayers)-1):
				TeamPresence.append(NearestPlayers[i].getFaction().getId())
			
			for i in range (0, len(TeamPresence)-1):
				if Max  (TeamPresence.count(TeamPresence[i])):
					Max = TeamPresence[i]

			for i in range (0, len(NearestPlayers)-1):
				if NearestPlayers[i].getFaction().getId() == Max :
					e.npc.setAttackTarget(NearestPlayers[i])
	else :
		pass
	"""

def UsingWater(e):
	'''Make the bot place water buckets
	'''
	WaterAllowed = e.npc.world.getTempdata().get("WaterAllowed")
	if (WaterAllowed == True) and (e.npc.getTempdata().get("WaterUsed") == None):			# Checking if the npc didnt spawned a water bucket already to avoid spamming water and create lags and annoying fights

		WaterRemaining = e.npc.getTempdata().get("WaterRemaining")

		PosList = [e.npc.getX(), e.npc.getY(), e.npc.getZ()]
		if ( WaterRemaining > 1) and (random.randint(0, 3) == 0):
			e.npc.executeCommand('/setblock ~ ~ ~ minecraft:water')					# Creating 2 water blocks to update the first and make the water flow
			e.npc.executeCommand('/setblock ~ ~ ~+1 minecraft:water 1')
			#WaterRemaining -= 1 Canceled right now
			e.npc.getTempdata().put("WaterRemaining", WaterRemaining)
			e.npc.getTempdata().put("WaterUsed", PosList)						# Saving the coordinates of the water in a Tempdata to clear it later
			DeletingWater.TickerMax = 2

def CancelFire(e):
	'''Make the bot extinguish himself when on fire
	'''
	if e.npc.isBurning() == True :
		if (random.randint(0, 3) == 0) and (e.npc.getTempdata().get("WaterUsed") == None):
			e.npc.executeCommand('/setblock ~ ~ ~ minecraft:water')					# Creating 2 water blocks to update the first and make the water flow
			e.npc.executeCommand('/setblock ~ ~ ~+1 minecraft:water 1')
			PosList = [e.npc.getX(),e.npc.getY(),e.npc.getZ()]
			e.npc.getTempdata().put("WaterUsed", PosList)
			DeletingWater.TickerMax = 1

def HealthDisplay(e):
	'''Display the health of the bot with absorption
	'''
	Health = e.npc.getHealth()
	if e.npc.getStoreddata().get("AbsoDisplay") == None :
		LifeToDisplay = 0
		e.npc.getStoreddata().put("AbsoDisplay", 0)

	e.npc.getDisplay().setTitle("  "+str(int(round(e.npc.getHealth()))+int(round(e.npc.getStoreddata().get("AbsoDisplay"))))+" "+u'\u2764'+"  ")

def UsingGap(e):
	'''Make the bot use a golden_apple
	'''
	#e.npc.getTempdata().put("IsEating", False)
	IsUsingGap = e.npc.getTempdata().get("IsUsingGap")
	GapCount = e.npc.getTempdata().get("GapCount")
	Health = e.npc.getHealth()
	HealthNerfed = round(Health)
	Timer = e.npc.getTempdata().get("Timer")

	if GapCount == None :
		GapCount = random.randint(8, 16)
		e.npc.getTempdata().put("GapCount", GapCount)

	if Timer == None :
		Timer = 0

	IsSlowed = e.npc.getPotionEffect(2)

	if (IsUsingGap == 1) and (IsSlowed == -1) and (GapCount > 0) and (HealthNerfed < 17) and (0 < HealthNerfed):   # Applying slowness to npc and making his reach go to 0 to simulate eating 		( UpdatingReach(e) )
		e.npc.addPotionEffect(2, 2, 2, True)
		e.npc.getStoreddata().put("IsEating", True)
		e.npc.getTempdata().put("SwordItem",e.npc.getInventory().getRightHand())					# Saving his sword before replacing it with a golden apple
		e.npc.getInventory().setRightHand(e.npc.world.createItem("minecraft:golden_apple",0,1))			# Put a golden apple in his hand
		Timer = 0																					# Creating a 2sec timer for the eating
		e.npc.executeCommand("/playsound customnpcs:gun.pistol.shot @a")				# Playing eating sound ( only if you have the right texture/sound pack )

	elif IsSlowed != -1 :										# Testing if he finished eating
		if Timer == 3 :
			e.npc.getStoreddata().put("IsEating", False)						# Allow his reach to change from 0 		( UpdatingReach(e) )
			e.npc.addPotionEffect(10, 4, 1, False)						# Adding the 2 regeneration and absorption effects
			e.npc.getStoreddata().put("AbsoDisplay", 4)												# Adding abso to display
			

			if e.npc.world.getTempdata().get('AbsoLess') != True :
				e.npc.addPotionEffect(22, 120, 0, False)
			e.npc.getInventory().setRightHand(e.npc.getTempdata().get("SwordItem"))				# Respawning his sword in his hand
			GapCount -= 1																# Clearing one of his golden apple
			GapCount = e.npc.getTempdata().put("GapCount", GapCount)
			IsUsingGap = e.npc.getTempdata().put("IsUsingGap", 0)
			IsRunning = 0														# Making him stop running to avoid being annoying
			e.npc.getTempdata().put("IsRunning", IsRunning)
			e.npc.getAi().setRetaliateType(0)							# Making him fight
			e.npc.getAi().setWalkingSpeed(6)

	Timer += 1
	e.npc.getTempdata().put("Timer", Timer)
	TryStack(e)

def WantToGap(e):
    '''Regulate the use of golden_apple 
    '''
    List = ["NoobTier","CasualTier","CommonTier","GoodTier"]            # List of non-strat golden_apple
    if not e.npc.getTempdata().get("SelectedType") in List :        # If player is good
        Target = e.npc.getAttackTarget()
        if Target != None:                                      # Prevent crashes  
            Regen = e.npc.getPotionEffect(10)                       # Regen effect currently running ?
            TargetDist = GetDist(e)                             # Target distance
            Health = e.npc.getHealth()                          # My health
            TargetHealth = Target.getHealth()                       # Target health

            if ((Regen != 1) and (TargetDist >= 6) and (Health <= 18)) or ((Regen != 1) and (TargetHealth+5 >= Health) and (Health <= 11)) :								# Using Gap classic
                Health = e.npc.getHealth()
                HealthNerfed = round(Health)
                LifeLimit = [1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0]
                LimitChoice = random.choice(LifeLimit)
                GapCount = e.npc.getTempdata().get("GapCount")
                if GapCount == None :
                    e.npc.getTempdata().put("GapCount", 1)

                if (LimitChoice == 1) and (HealthNerfed < 17):
                    IsUsingGap = e.npc.getTempdata().put("IsUsingGap", 1)

            elif (e.npc.getTempdata().get("IsUsingGap") != 1) or (random.randint(0, 3) == 0):
                Health = e.npc.getHealth()
                HealthNerfed = round(Health)
                LifeLimit = [1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0]
                LimitChoice = random.choice(LifeLimit)
                if (LimitChoice == 1) and (HealthNerfed <= 13) and (e.npc.getPotionEffect(2) != 1):								# Using Gap chug
                    e.npc.getTempdata().put("IsUsingGap", 1)
                    e.npc.getStats().setResistance(3, 1.2)
                    if e.npc.getTempdata().get("GapTickRod") == 1 :
                        e.npc.getTempdata().put("NeedRod", e.npc.getTempdata().get("NeedRod")+1)
                        e.npc.getTempdata().put("GapTickRod", 0)
                    else:
                        if e.npc.getTempdata().get("GapTickRod") == None :
                            e.npc.getTempdata().put("GapTickRod", 0)
                        e.npc.getTempdata().put("GapTickRod", 1)
                    UsingWater(e)

    else:
        Health = e.npc.getHealth()
        HealthNerfed = round(Health)
        LifeLimit = [1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0]
        LimitChoice = random.choice(LifeLimit)
        GapCount = e.npc.getTempdata().get("GapCount")
        if GapCount == None :
            e.npc.getTempdata().put("GapCount", 1)

        if (LimitChoice == 1) and (HealthNerfed < 17):
            IsUsingGap = e.npc.getTempdata().put("IsUsingGap", 1)

def UpdatingReach(e):
	'''Handle reach changes
	'''
	IsSlowed = e.npc.getPotionEffect(2)
	if IsSlowed != 1 :
		if e.npc.getStoreddata().get("IsEating") != True :
			Rodless = e.npc.world.getTempdata().get("Rodless")
			if Rodless != True :	
				SelectedType = e.npc.getTempdata().get("SelectedType")
				if SelectedType == "CasualTier" :
					ReachList = [1, 2, 2, 2, 2, 2, 2, 3, 3, 3]
					NewReach = random.choice(ReachList)
					e.npc.getStats().getMelee().setRange(NewReach)

				if SelectedType == "CommonTier" :
					ReachList = [1, 2, 2, 2, 3, 3, 3, 3, 3, 3]
					NewReach = random.choice(ReachList)
					e.npc.getStats().getMelee().setRange(NewReach)

				if SelectedType == "GoodTier" :
					ReachList = [2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 4]
					NewReach = random.choice(ReachList)
					e.npc.getStats().getMelee().setRange(NewReach)

				if SelectedType == "ProTier" :
					ReachList = [2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 4, 4]
					NewReach = random.choice(ReachList)
					e.npc.getStats().getMelee().setRange(NewReach)

				if SelectedType == "UHCEliteTier" :
					ReachList = [2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4]
					NewReach = random.choice(ReachList)
					e.npc.getStats().getMelee().setRange(NewReach)

				if SelectedType == "NoobTier" :
					ReachList = [2, 2, 2, 2, 1, 1, 1, 1, 1, 1]
					NewReach = random.choice(ReachList)
					e.npc.getStats().getMelee().setRange(NewReach)
	else :
		e.npc.getStats().getMelee().setRange(0)

def MeetUpChecking(e):	
	'''Force bots to go to 0 ; 0 
	'''			
	MeetUp = e.npc.world.getStoreddata().get("MeetUp")
	if e.npc.getFaction().getId() != 26 :
		try:
			if (e.npc.world.getTotalTime() >= MeetUp) and (e.npc.getAttackTarget() == None):		# Navigating to 0 0 when Meet Up start
				X = 0
				Z = 0

				if e.npc.getX() >= 0 :
					X -= 5
				else:
					X += 5

				if e.npc.getZ() >= 0 :
					Z -= 5
				else :
					Z += 5

				e.npc.navigateTo(e.npc.getX()+X, e.npc.getY(), e.npc.getZ()+Z, 3)
		except:
			pass

def DeletingWater(e):
	'''Delete water on certain time
	'''
	try:
		if (e.npc.getTempdata().get("WaterUsed") != None) and (DeletingWater.Ticker == DeletingWater.TickerMax) :
			e.npc.executeCommand("/fill "+str(e.npc.getTempdata().get("WaterUsed")[0])+" "+str(e.npc.getTempdata().get("WaterUsed")[1])+" "+str(e.npc.getTempdata().get("WaterUsed")[2])+" "+str(e.npc.getTempdata().get("WaterUsed")[0])+" "+str(e.npc.getTempdata().get("WaterUsed")[1]+1)+" "+str(e.npc.getTempdata().get("WaterUsed")[2])+" minecraft:air")
			e.npc.extinguish()
			e.npc.getTempdata().put("WaterRemaining", 3)
			e.npc.getTempdata().put("WaterUsed", None)					# Saving that there is a water bucket usable

		if (e.npc.getTempdata().get("WaterUsed") != None):
			if DeletingWater.Ticker == 5 :
				DeletingWater.Ticker = 0
			else :
				DeletingWater.Ticker += 1
	except :
		DeletingWater.Ticker = 0
		DeletingWater.TickerMax = 2

def BadlionKB(e):
	'''Reduce knockbcak to force melee
	'''
	if e.npc.world.getTempdata().get("BadlionKB") == True :
		e.npc.getStats().setResistance(3, (random.uniform(1.4, 1.8)))



#ON DEATH ONLY functions :

def CountingPlayers(e):
	if e.npc.getFaction().getId() != 26 :
		e.npc.world.getStoreddata().put("Players", e.npc.world.getStoreddata().get("Players")-1)

def CountingKills(e):
	MyKills = e.npc.getStoreddata().get("Kills")
	if MyKills == None:
		MyKills = 0

	KillList = e.npc.world.getStoreddata().get("KillList")
	NewList = ("//" + e.npc.getDisplay().getName())+ '|' +(str(int(MyKills)))
	if KillList == None :
		e.npc.world.getStoreddata().put("KillList", NewList)

	else:
		KillList = e.npc.world.getStoreddata().get("KillList")
		NewList = ("//" + e.npc.getDisplay().getName())+ '|' +(str(int(MyKills)))
		OldList = ("//" + e.npc.getDisplay().getName())+ '|' +(str(int(MyKills-1)))
		if OldList in KillList :
			KillList = KillList.replace(str("//" + e.npc.getDisplay().getName())+ '|' +(str(int(MyKills-1))), str(NewList))
			e.npc.world.getStoreddata().put("KillList", KillList)
		else:
			NewList = ("//" + e.npc.getDisplay().getName())+ '|' +(str(int(MyKills)))
			e.npc.world.getStoreddata().put("KillList", KillList+NewList)

def CountingPlayersLeft(e):
	try:
		List = [200, 150, 100, 50, 25, 10, 5, 3]
		if int(e.npc.world.getStoreddata().get("TeamsAlive")) in List :
			e.npc.executeCommand('/tellraw @a ["",{"text":"[","color":"dark_gray"},{"text":"UHC","color":"dark_red"},{"text":"] ","color":"dark_gray"},{"text":"[","color": dark_gray,"bold":false},{"text":"Players","color" : dark_green},{"text":"] ","color": dark_gray,"bold":false},{"text":" - There is ","color": gray,"bold":false},{"text":"'+str(int(e.npc.world.getStoreddata().get("TeamsAlive")))+'","color": light_purple,"bold":false},{"text":" teams alive. ","color": gray,"bold":false},{"text":" (With","color":"white"},{"text":" '+str(int(e.npc.world.getStoreddata().get("Players")))+'","color":"aqua"},{"text":" players)","color":"white"}]')
	except:
		pass

def TeamReduction(e):
	try :
		TeamID = e.npc.getFaction().getId()
		e.npc.world.getStoreddata().put(str(TeamID), e.npc.world.getStoreddata().get(str(TeamID))-1)
		if (e.npc.world.getStoreddata().get(str(TeamID))) <= 0 :
			Factions = e.npc.world.getStoreddata().get("Factions")
			Factions = Factions.split("/")
			Factions.append(str(TeamID))
			Factions = "/".join(Factions)
			e.npc.world.getStoreddata().put("Factions", Factions)
			e.npc.world.getTempdata().put(str(TeamID)+"Team", None)						# For the LoadTeam thingy

	except:
		pass

def WinnerStats(e):
	try:
		if e.npc.getHealth() > 0 :
			if (int(e.npc.world.getStoreddata().get("TeamsAlive")) <= 5) and (e.npc.getStoreddata().get("SentWin") != 1) and (e.npc.getDisplay().getName() != "-") and (e.npc.getDisplay().getName() != "Disabled"):
				if e.npc.world.getTempdata().get("WinnerList") == None :
					e.npc.world.getTempdata().put("WinnerList", [str(e.npc.getDisplay().getName())])
				else :
					A = e.npc.world.getTempdata().get("WinnerList")
					A.append(str(e.npc.getDisplay().getName()))
					e.npc.world.getTempdata().put("WinnerList", A)
				e.npc.getStoreddata().put("SentWin", 1)
	except Exception as err:
		#e.npc.world.broadcast(str(err))
		pass

def DelWinnerStats(e):
	try:
		if e.npc.world.getTempdata().get("WinnerList") != None :
			A = e.npc.world.getTempdata().get("WinnerList")
			A.remove(str(e.npc.getDisplay().getName()))
			e.npc.world.getTempdata().put("WinnerList", A)
	except Exception as err:
		#e.npc.world.broadcast(str(err))
		pass	

def ScoreBoardUpdateII(e):
	try :
		RedditUHCDisplay = e.npc.world.getTempdata().get("RedditUHCDisplay")
		if RedditUHCDisplay == True :
			e.npc.executeCommand('/scoreboard players add '+str(e.source.getName())+' Arena 1')
	except:
		pass	

def ScoreBoardUpdateV(e):
	try :
		RedditUHCDisplay = e.npc.world.getTempdata().get("RedditUHCDisplay")
		if RedditUHCDisplay == True :
			Name = e.npc.getDisplay().getName()
			e.npc.executeCommand('/scoreboard players reset '+str(Name)+' Arena')
	except:
		pass

def NoRespawn(e):
	if e.npc.getTempdata().get("Respawn") == 2 :
		e.npc.despawn()
	elif (e.npc.getTempdata().get("Respawn") == 1) or (e.npc.getTempdata().get("Respawn") == 0) :
		e.npc.getTempdata().put("Respawn", e.npc.getTempdata().get("Respawn")+1)

def UnStack(e):
    Kills = e.npc.getStoreddata().get("Kills")
    List = e.npc.world.getTempdata().get("StackedList")          
    try:
        List.remove([str(e.npc.getDisplay().getName()), str(int(Kills))])
    except:
        pass
		

#POST GAME functions :

def EndGame(e):
	try :
		PlayerList = e.npc.world.getAllPlayers()
		for i in range (0, len(PlayerList)):
			NewList = (("//" + PlayerList[i].getName())+ '|' +str(e.npc.world.getStoreddata().get(str(int(PlayerList[i].getName()) +"Kills"))))
			e.npc.world.getStoreddata().put("KillList", e.npc.world.getStoreddata().get("KillList") + NewList)
	except:
		pass
	KillList = e.npc.world.getStoreddata().get("KillList")
	Max = 0
	i = 0
	SortedList = []
	KillList = KillList.split("//")
	for i in range (0, len(KillList)):
		KillList[i] = KillList[i].split("|")


	IntList = []
	Max =["", 0]
	Count = 0
	MaxDisplay = 10
	if MaxDisplay >= len(KillList):
 	   MaxDisplay = len(KillList)-1

	FinalList = []
	MaxForWhile = len(KillList)

		

	for i in range(len(KillList)-1, 0, -1):
		ToInt = KillList[i][1].split(".")
		KillList[i][1] = ToInt[0]

	while len(FinalList) != MaxDisplay:
 		for i in range(len(KillList)-1, 0, -1):
			if (KillList[i][1] == None) or (KillList[i][1] == "None"):
				KillList[i][1] = 0
 			if int(KillList[i][1]) >= int(Max[1]):
				Max = KillList[i]
				Integrer = i
		FinalList.insert(Count, Max)
		try:
			KillList.pop(Integrer)
		except :
				KillList.pop(Integrer-1)
		Count += 1
		Max = ['', 0]

	ColorList = ["red","gold","yellow","aqua","aqua","white","white","white","white","white"]

	for i in range (0, 10):
		e.npc.executeCommand('/tellraw @a ["",{"text":"[","color":"dark_gray"},{"text":"UHC","color":"dark_red"},{"text":"] ","color":"dark_gray"},{"text":"[","color": gray,"bold":true},{"text":"Kills","color" : blue},{"text":"] ","color": gray,"bold":true},{ "text" :"'+str(i+1)+' : ","bold":flase},{ "text" :"'+str(FinalList[i][0])+' --- ","color": '+str(ColorList[i])+',"bold":false},{ "text" :"'+str(FinalList[i][1])+' Kills ","bold":false}]')

	e.npc.world.getTempdata().put("GameStarted", 0)
	e.npc.world.spawnClone(13, 203, 0, 3, "Host FFA")



#Misc

def GoToZone(e, Zone, Side):
    CurrentZone = GettingZone(e)             # Getting the current Zone
    ZoneList = [[-15, 15],[-35, 35],[-65, 65],[-105, 105],[-200, 200]]

    ZoneListName = ["Middle","NoMansLand","StackZone","NearBorder","RandomZone"] 
    WantedZoneName = ZoneListName[Zone]

    WantedZone = ZoneList[Zone]   
    a = (WantedZone[1]-2 <= abs(int(e.npc.getX())) <= WantedZone[1]+2)
    b = (WantedZone[1]-2 <= abs(int(e.npc.getZ())) <= WantedZone[1]+2)
    if ((WantedZone[1]-3 <= abs(int(e.npc.getX())) <= WantedZone[1]+3) != True) or ((WantedZone[1]-3 <= abs(int(e.npc.getZ())) <= WantedZone[1]+3) != True):
        X = e.npc.getX()
        Y = e.npc.getY()
        Z = e.npc.getZ()
        
        e.npc.getTempdata().put("IsMovingFromZone", True)

        if (X < 0) and (WantedZone[0] < X):                      # Nearest X coordinates for Next Zone
            X -= 2
        elif (0 <= X) and (X <= WantedZone[1]):
            X += 2
        if (Z < 0) and (WantedZone[0] < Z):                      # Nearest Z coordinates for Next Zone
            Z -= 2
        elif (0 <= Z) and (Z <= WantedZone[1]):
            Z += 2


        if (X < 0) and (X <= WantedZone[0]):                      # Nearest X coordinates for Previous Zone
            X += 2
        elif (0 <= X) and (WantedZone[1] <= X):
            X -= 2
        if (Z < 0) and (Z <= WantedZone[0]):                      # Nearest Z coordinates for Previous Zone
            Z += 2
        elif (0 <= Z) and (WantedZone[1] <= Z):
            Z -= 2


        e.npc.navigateTo(X, Y, Z, 2)

    else:
        e.npc.getAi().setRetaliateType(0)

def GettingZone(e):
    x = e.npc.getX()
    z = e.npc.getZ()
    Zone = None

    if (-26 <= x <= 26) and (-26 <= z <= 26):
        Zone = "Middle"

    elif (-46 <= x <= 46) and (-46 <= z <= 46):
        Zone = "NoMansLand"
    
    elif (-81 <= x <= 81) and (-81 <= z <= 81):
        Zone = "StackZone"

    elif (-121 <= x <= 121) and (-121 <= z <= 121):
        Zone = "NearBorder"

    else:
        Zone = "RandomZone"

    return(str(Zone))

def TryStack(e):
	try:
		Around = e.npc.world.getNearbyEntities(int(e.npc.getX()), int(e.npc.getY()), int(e.npc.getZ()), 8, 2).tolist()
		if int(e.npc.world.getTempdata().get("TeamSize"))*3 <= len(Around) :
			List = []
			for i in range(0, len(Around)):
				if not ([Around[i].getFaction().getId(), e.npc.world.getStoreddata().get(str(Around[i].getFaction().getId())+"Aggro")]) in List :
					List.append([Around[i].getFaction().getId(), e.npc.world.getStoreddata().get(str(Around[i].getFaction().getId())+"Aggro")])

			Min = 99999999
			Int = None
			NewList = []
			for i in range (len(List)-1, -1, -1):
				if int(List[i][1]) <= Min :
					Min = int(List[i][1])
					Int = List[i][0]
			

			if int(e.npc.getFaction().getId()) == Int :
				ChooseZone(e)
				
		else:
			pass
	except:
		pass

def ChooseZone(e):
    CurrentZone = GettingZone(e)
    if CurrentZone == "Middle" :
        e.npc.getStoreddata().put("GoTozone","1")
        e.npc.getAi().setRetaliateType(3)
        GoToZone(e, 1, "Ext")

    elif (CurrentZone == "NoMansLand"):
        if (e.npc.world.getTempdata().get("FinalBorder") >= e.npc.world.getTotalTime()):
            e.npc.getStoreddata().put("GoTozone", "2")
            e.npc.getAi().setRetaliateType(3)
            GoToZone(e, 2, "Ext")
        else:
            e.npc.getStoreddata().put("GoTozone", "0")
            e.npc.getAi().setRetaliateType(3)
            GoToZone(e, 0, "Ext")

    elif (CurrentZone == "StackZone"):
        if (e.npc.world.getTempdata().get("SecondBorder") >= e.npc.world.getTotalTime()):
            e.npc.getStoreddata().put("GoTozone", "3")
            e.npc.getAi().setRetaliateType(3)
            GoToZone(e, 3, "Ext")
        else:
            e.npc.getStoreddata().put("GoTozone", "1")
            e.npc.getAi().setRetaliateType(3)
            GoToZone(e, 1, "Ext")
    
    elif (CurrentZone == "NearBorder"):
        if (e.npc.world.getTempdata().get("FirstBorder") >= e.npc.world.getTotalTime()):
            e.npc.getStoreddata().put("GoTozone", "1")
            e.npc.getAi().setRetaliateType(3)
            GoToZone(e, 1, "Ext")
        else:
            pass
    else:
        pass

def BorderShrink(e):

    if (e.npc.world.getStoreddata().get("FinalBorder") <= e.npc.world.getTotalTime()):
        if e.npc.getStoreddata().get("HasShrunkFinal") == None :
            X = e.npc.getX()
            Z = e.npc.getZ()
            Y = e.npc.getY()
            if (e.npc.getX() >= 45) :
                X = 40
                Y = 75
            elif (-45 >= e.npc.getX()):
                X = -40
                Y = 75

            if (e.npc.getZ() >= 45) :
                Z = 40
                Y = 75
            elif (-45 >= e.npc.getZ()):
                Z = -40
                Y = 75
            
            e.npc.setPosition(X, Y, Z)
            e.npc.getStoreddata().put("HasShrunkFinal", "Done")

    elif (e.npc.world.getStoreddata().get("SecondBorder") <= e.npc.world.getTotalTime()):
        if e.npc.getStoreddata().get("HasShrunkSecond") == None :
            X = e.npc.getX()
            Z = e.npc.getZ()
            Y = e.npc.getY()
            if (e.npc.getX() >= 80) :
                X = 75
                Y = 75
            elif (-80 >= e.npc.getX()):
                X = -75
                Y = 75

            if (e.npc.getZ() >= 80) :
                Z = 75
                Y = 75
            elif (-80 >= e.npc.getZ()):
                Z = -75
                Y = 75
            
            e.npc.setPosition(X, Y, Z)
            e.npc.getStoreddata().put("HasShrunkSecond", "Done")


    elif (e.npc.world.getStoreddata().get("FirstBorder") <= e.npc.world.getTotalTime()):
        if e.npc.getStoreddata().get("HasShrunkFirst") == None :
            X = e.npc.getX()
            Z = e.npc.getZ()
            Y = e.npc.getY()
            if (e.npc.getX() >= 120) :
                X = 115
                Y = 75
            elif (-120 >= e.npc.getX()):
                X = -115
                Y = 75

            if (e.npc.getZ() >= 120) :
                Z = 115
                Y = 75
            elif (-120 >= e.npc.getZ()):
                Z = -115
                Y = 75
            
            e.npc.setPosition(X, Y, Z)
            e.npc.getStoreddata().put("HasShrunkFirst", "Done")

def Crit(e):
	List = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1]
	if random.choice(List) == 1 :
		e.npc.getStats().getMelee().setStrength(e.npc.getStats().getMelee().getStrength()+3)

def AntiGapHit(e):
	try:
		if e.npc.getInventory().getRightHand().getName() == "minecraft:golden_apple" :
			e.setCanceled(True)
	except:
		pass
	
def GetDist(e):
    if e.npc.getAttackTarget() != None :
        Target = e.npc.getAttackTarget()
        X = e.npc.getX()
        Z = e.npc.getZ()
        TX = Target.getX()
        TZ = Target.getZ()
        
        a = TX - X
        b = TZ - Z

        Dist = math.sqrt((a)**2 + (b)**2)
        return(Dist)

def Clicks(e):
    if e.npc.getAttackTarget() != None :
        if GetDist(e) <= 4 :
            e.npc.swingHand()

def PlayerDeath(e):
	try:
		Source = e.entity.getName()
		e.npc.executeCommand('/clear '+str(e.entity.getName()))
		Killer = e.npc.world.getTempdata().get(str(Source)+"Killer")
		KilledKills = e.npc.world.getStoreddata().get(str(Source) +"Kills")
		Special = '{"text":"","color":"light_purple"}'
		SpecialKiller = '{"text":"","color":"light_purple"}'
		SpecialList = ["Natsu91","Yvant2000Games","Frizou","iKowz","MASTEEKH","jdegoederen","reb_hi","Strykerss","Etoiles","xGokuuuh","Pikachu","TryHqrd_","_Mik0GODESS","SqndSt0rm","Divinity_Kirito","slooonay","Pxdro","Restump","Nardcoo","Ladak","VERSKUUUH","seltix_x","Pacoima","MarkiLokuras","Boosta","DANTEH","Rzmeur","GrzyLight","Mqyland_hi","Mentally","BiboyQG"]
		try :
			int(KilledKills)
		except:
			KilledKills = 0

		e.npc.executeCommand("/gamemode 3 @p")

		NameKiller = Killer[0]
		KillerFaction = int(Killer[1])
		KillerKills = Killer[2].split(".")
		KillerKills = KillerKills[0]
		FactionArgList = [["green","false","false"],["green","false","false"],["blue","false","false"],["red","false","false"],["yellow","false","false"],["dark_gray","false","false"],["dark_blue","false","false"],["dark_red","false","false"],["dark_green","false","false"],["gold","false","false"],["aqua","false","false"],["light_purple","false","false"],["dark_aqua","false","false"],["dark_purple","false","false"],["green","false","true"],["blue","false","true"],["red","false","true"],["yellow","false","true"],["dark_gray","false","true"],["dark_blue","false","true"],["dark_red","false","true"],["dark_green","false","true"],["gold","false","true"],["aqua","false","true"],["light_purple","false","true"],["dark_aqua","false","true"],["white","false","false"]]
		TeamColorKiller = FactionArgList[KillerFaction][0]
		UnderlinedKiller = FactionArgList[KillerFaction][1]
		ItalicKiller = FactionArgList[KillerFaction][2]

		e.npc.executeCommand('/scoreboard players reset '+str(NameKiller)+' Arena')
		
		if NameKiller in SpecialList :
			SpecialKiller = '{"text":"['+u'\u2764'+']","color":"light_purple"}'    

		if Source in SpecialList :
			Special = '{"text":"['+u'\u2764'+']","color":"light_purple"}'

		if e.npc.world.getTempdata().get("BadlionKillsSystem") == True :
			e.npc.executeCommand('/tellraw @a ["",{"text":"[","color":"dark_gray"},{"text":"Arena","color":"dark_red"},{"text":"] ","color":"dark_gray"},'+Special+',{"text":"'+str(Source)+'"},{"text":"[","color":"white"},{"text":"'+str(int(KilledKills))+'","color":"white"},{"text":"]","color":"white"},{"text":" was slain by ","color":"gray"},'+SpecialKiller+',{"text":"'+str(NameKiller)+'","color":"'+str(TeamColorKiller)+'","underlined":"'+str(UnderlinedKiller)+'","italic":"'+str(ItalicKiller)+'"},{"text":"[","color":"white"},{"text":"'+str(int(KillerKills)) +'","color":"white"},{"text":"]","color":"white"}]')
		else:
			e.npc.executeCommand('/tellraw @a ["",{"text":"[","color":"dark_gray"},{"text":"Arena","color":"dark_red"},{"text":"] ","color":"dark_gray"},'+Special+',{"text":"'+str(Source)+'"},{"text":" was slain by ","color":"gray"},'+SpecialKiller+',{"text":"'+str(NameKiller)+'","color":"'+str(TeamColorKiller)+'","underlined":"'+str(UnderlinedKiller)+'","italic":"'+str(ItalicKiller)+'"}]')
		GiveInventory(e)
		e.npc.world.getStoreddata().put(str(Source) +"Kills", 0)
		e.npc.executeCommand("/scoreboard players reset "+str(Source)+" Arena")
		e.npc.executeCommand("/scoreboard players reset "+str(Source)+" Kills")
	except:
		pass

def GiveInventory(e):
	"""Give Arena inventory to player"""
	if e.npc.world.getTempdata().get("CurrentGame") == "bow":
		e.npc.executeCommand('/give '+str(e.entity.getName())+' minecraft:iron_helmet 1 0 {Unbreakable:1,ench:[{id:4,lvl:1}]}')
		e.npc.executeCommand('/give '+str(e.entity.getName())+' minecraft:iron_chestplate 1 0 {Unbreakable:1,ench:[{id:0,lvl:1}]}')
		e.npc.executeCommand('/give '+str(e.entity.getName())+' minecraft:iron_leggings 1 0 {Unbreakable:1,ench:[{id:4,lvl:1}]}')
		e.npc.executeCommand('/give '+str(e.entity.getName())+' minecraft:diamond_boots 1 0 {Unbreakable:1,ench:[{id:0,lvl:2}]}')

		e.npc.executeCommand('/give '+str(e.entity.getName())+' minecraft:iron_sword 1 0 {Unbreakable:1,ench:[{id:16,lvl:1}]}')
		e.npc.executeCommand('/give '+str(e.entity.getName())+' minecraft:bow 1 0 {Unbreakable:1,ench:[{id:48,lvl:2}]}')

		e.npc.executeCommand('/give '+str(e.entity.getName())+' minecraft:cobblestone 64')
		e.npc.executeCommand('/give '+str(e.entity.getName())+' minecraft:cooked_beef 10')
		e.npc.executeCommand('/give '+str(e.entity.getName())+' minecraft:arrow 64')
		e.npc.executeCommand('/give '+str(e.entity.getName())+' minecraft:water_bucket 1')
		e.npc.executeCommand('/give '+str(e.entity.getName())+' minecraft:golden_apple 1')
		e.npc.executeCommand('/give '+str(e.entity.getName())+' minecraft:fishing_rod 1 0 {Unbreakable:1}')
	else:
		e.npc.executeCommand('/give '+str(e.entity.getName())+' minecraft:diamond_helmet 1 0 {Unbreakable:1,ench:[{id:4,lvl:2}]}')
		e.npc.executeCommand('/give '+str(e.entity.getName())+' minecraft:diamond_chestplate 1 0 {Unbreakable:1,ench:[{id:0,lvl:2}]}')
		e.npc.executeCommand('/give '+str(e.entity.getName())+' minecraft:diamond_leggings 1 0 {Unbreakable:1,ench:[{id:0,lvl:2}]}')
		e.npc.executeCommand('/give '+str(e.entity.getName())+' minecraft:diamond_boots 1 0 {Unbreakable:1,ench:[{id:4,lvl:2}]}')

		e.npc.executeCommand('/give '+str(e.entity.getName())+' minecraft:diamond_sword 1 0 {Unbreakable:1,ench:[{id:16,lvl:3}]}')
		e.npc.executeCommand('/give '+str(e.entity.getName())+' minecraft:bow 1 0 {Unbreakable:1,ench:[{id:48,lvl:2}]}')

		e.npc.executeCommand('/give '+str(e.entity.getName())+' minecraft:cobblestone 64')
		e.npc.executeCommand('/give '+str(e.entity.getName())+' minecraft:cooked_beef 10')
		e.npc.executeCommand('/give '+str(e.entity.getName())+' minecraft:arrow 64')
		e.npc.executeCommand('/give '+str(e.entity.getName())+' minecraft:water_bucket 1')
		e.npc.executeCommand('/give '+str(e.entity.getName())+' minecraft:lava_bucket 1')
		e.npc.executeCommand('/give '+str(e.entity.getName())+' minecraft:golden_apple 8')
		e.npc.executeCommand('/give '+str(e.entity.getName())+' minecraft:fishing_rod 1 0 {Unbreakable:1}')


#Classes :
# nah joking im too bad



#================================#
#_______{ Calling Events }_______#
#================================#


def init(e):
	GameStarted = e.npc.world.getTempdata().get("GameStarted")
	try:
		e.npc.getTimers().start(2, 0, True)			# The Rod block timer
	except:
		pass
	if GameStarted == 1:
		SettingEntity(e)
		SettingArmor(e)
		SettingResistance(e)
		SettingInitialKills(e)
		RodlessActivation(e)
		UpdatingReach(e)
		AllyResistance(e)
		
		
def damaged(e):
	SettingEntity(e)
	Clicks(e)
	EnableFallDamage(e)
	e.npc.world.getTempdata().put("GameRunning", 1)
	SwordDebug(e)
	SettingResistance(e)
	LifeMessageBow(e)
	UpdatingReach(e)
	BadlionKB(e)
	AntiFreeDeath(e)
	AbsoLess(e)
	ActualisingHealth(e)

def meleeAttack(e):
	Clicks(e)
	AntiGapHit(e)
	Crit(e)
	UpdatingReach(e)
	Strafing(e)
	Missing(e)
	BadlionKB(e)
	AbsoLess(e)

def kill(e):
	ScoreBoardUpdateIII(e)
	BadlionKillsSystem(e)
	ScoreBoardUpdateI(e)
	SettingResistance(e)
	StuffUpgradeOnKill(e)
	CountingKills(e)
	KillingPlayer(e)
	PlayerDeath(e)

def died(e):
	e.npc.getTempdata().put("Respawn", 0) 			# To avoid glitched respawn, which will make the player counter false
	TeamReduction(e)
	ThunderStrike(e)
	ScoreBoardUpdateII(e)
	BadlionDeathTchatMessage(e)
	DeathTchatMessage(e)
	IronGolemSound(e)
	WitherSoundI(e)
	WitherSoundII(e)
	NoCleanUpActivation(e)
	ScoreBoardUpdateV(e)
	VanillaDeathStyle(e)
	ExplodeOnDeath(e)

def tick(e):
	GameStarted = e.npc.world.getTempdata().get("GameStarted")
	if GameStarted == 1:
		if e.npc.getAi().getRetaliateType() == 3:
			GoToZone(e, int(e.npc.getStoreddata().get("GoTozone")),"Ext")
		BorderShrink(e)
		CancelFire(e)
		NoRespawn(e)
		ActualisingTeamMembers(e)
		HealthDisplay(e)
		WantToGap(e)
		UsingGap(e)
		Strafing(e)
		DeletingWater(e)
		WeatherClear(e)
		WantToRod(e)
		Rod(e)
		Clicks(e)
		#LastSending(e)
		try:
			e.npc.getTempdata().put("RunOn", e.npc.getTempdata().get("RunOn")-1 )
		except:
			e.npc.getTempdata().put("RunOn", 0)
	MayStopArena(e)

def interact(e):
	GappleSharing(e)
	#e.npc.getTempdata().put("SelectedType", "UHCEliteTier")
	#e.npc.world.getStoreddata().put("Players", e.npc.world.getStoreddata().get("Players")+1)
	e.setCanceled(True)
	
def target(e):
	Clicks(e)
	SettingEntity(e)
	pass

def timer(e):			# Rod Block
	List = e.npc.world.getAllPlayers()
	for i in range (0, len(List)):
		try:
			List[i].getMCEntity().field_71104_cf.field_146043_c = None
		except Exception as err:
			pass


    #============================#
    #___{ Credits and thanks }___#
    #============================#

#   Thanks to noppes for creating the CustomNPC mod
#   and to every people of the CustomNPC discord server
#   for helping me with commands and creating scripts



# /tellraw @a ["",{"text":"[","color":"dark_gray"},{"text":"Spec","color":"green"},{"text":"]","color":"dark_gray"},{"text":" ====","color":"dark_purple"},{"text":" / ","color":"dark_gray"},{"text":"====","color":"dark_purple"},{"text":" / ","color":"dark_gray"},{"text":"====","color":"dark_purple"},{"text":" /","color":"dark_gray"},{"text":" ====","color":"dark_purple"},{"text":" / ","color":"dark_gray"},{"text":"=======","color":"light_purple"},{"text":" /","color":"dark_gray"},{"text":" =======","color":"gold"}]