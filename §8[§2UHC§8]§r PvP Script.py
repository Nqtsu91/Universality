import random
import math
#API Link :http://www.kodevelopment.nl/customnpcs/api/1.8.9/
#Credits : Script UHC vs Bots BotPvPSystem By Natsu91

#===================================#
#_______{ Creating Algorithm }______#
#===================================#



#DEATH STYLE functions :

def InventorySpawn(e) :
	if e.npc.world.getTempdata().get("OneShot") != True :
		import random
		# Spawning enchanted armor
		ItemList = [e.npc.getInventory().getArmor(0).getName(), e.npc.getInventory().getArmor(1).getName() ,e.npc.getInventory().getArmor(2).getName() ,e.npc.getInventory().getArmor(3).getName()]
		for i in range(0, len(ItemList)) :	
			Prot = e.npc.getStoreddata().get("Prot")
			Proj = e.npc.getStoreddata().get("Proj")
			Proj = Proj.split("/")
			Prot = Prot.split("/")

			if int(Prot[i]) == 0 :
				EnchID = 4
				EnchLvL = int(Proj[i])
			else :
				EnchID = 0
				EnchLvL = int(Prot[i])
			element = ItemList[i]
			Damage = random.randint(10, 250)			# Damaging items to make it feeling real
			
			MyX = e.npc.getX()			# Attributing coordinates to the item
			MyY = e.npc.getY()
			MyZ = e.npc.getZ()
			SpawnX = int(MyX) + random.uniform(-1.25, 1.25)
			SpawnY = int(MyY) + 1
			SpawnZ = int(MyZ) + random.uniform(-1.25, 1.25)
		
			e.npc.executeCommand("/summon Item "+str(SpawnX)+" "+str(SpawnY)+" "+str(SpawnZ)+" {Item:{id:"+str(element)+",Damage:"+str(Damage)+",Count:1,tag:{ench:[{id:"+str(EnchID)+",lvl:"+str(EnchLvL)+"}]}}}") # Looting item

		# Spawning other items
		ItemList = [["minecraft:cobblestone","64"],["minecraft:cobblestone","64"],["minecraft:cobblestone","64"],["minecraft:cobblestone","64"],["minecraft:apple","3"],["minecraft:cooked_beef","64"],["minecraft:cobblestone","64"],["minecraft:cobblestone","64"],["minecraft:cobblestone","64"],["minecraft:cobblestone","64"],["minecraft:cobblestone","64"],["minecraft:log","64"],["minecraft:water_bucket","1"],["minecraft:water_bucket","1"],["minecraft:water_bucket","1"],["minecraft:lava_bucket","1"],["minecraft:fishing_rod","1"],["minecraft:book","2"],["minecraft:flint_and_steel","1"],["minecraft:planks","64"],["minecraft:anvil","1"],["minecraft:enchanting_table","1"],["minecraft:wheat_seeds","12"],["minecraft:string","1"],["minecraft:coal","20"],["minecraft:flint","16"],["minecraft:dirt","64"],["minecraft:leather","11"],["minecraft:reeds","15"],["minecraft:feather","4"],["minecraft:gunpowder","2"],["minecraft:sand","64"],["minecraft:gravel","64"],["minecraft:sapling","16"],["minecraft:red_flower","6"],["minecraft:torch","64"],["minecraft:redstone","64"],["minecraft:bone","3"]]																			
		for i in range(0, len(ItemList)-1):	
			MyX = e.npc.getX()			# Attributing coordinates to the item
			MyY = e.npc.getY()
			MyZ = e.npc.getZ()
			SpawnX = int(MyX) + random.uniform(-1.25, 1.25)
			SpawnY = int(MyY) + 1
			SpawnZ = int(MyZ) + random.uniform(-1.25, 1.25)
			Count = random.randint(0,int(ItemList[i][1]))
			
			e.npc.executeCommand("/summon Item "+str(SpawnX)+" "+str(SpawnY)+" "+str(SpawnZ)+" {Item:{id:"+str(ItemList[i][0])+",Count:"+str(Count)+"}}") # Looting item
		
		# Looting other items
		EnchLvL = random.randint(3,4)
		EnchID = 16
		Damage = random.randint(10, 150)
		if e.npc.getInventory().getRightHand().getName() == "minecraft:golden_apple" :
			Item5 = "minecraft:diamond_sword"
		else :
			Item5 = e.npc.getInventory().getRightHand().getName()
		Sword = e.npc.getStoreddata().get("Sword")
		Sword = Sword.split("/")
		EnchList = "{ench:[{id:16,lvl:"+str(Sword[0])+"}"
		for i in range(1, 4):
			if ( i == 1 ) and (int(Sword[i]) != 0):
				EnchID = 20
				EnchLvL = int(Sword[i])
				EnchList += ",{id:20,lvl:"+Sword[1]+"}"
			if (i == 2 ) and (int(Sword[i]) != 0):
				EnchID = 19
				EnchLvL = int(Sword[i])
				EnchList += ",{id:19,lvl:"+Sword[2]+"}"
			if (i == 3) and (int(Sword[i]) != 0) :
				EnchID = 34
				EnchLvL = int(Sword[i])
				EnchList += ",{id:34,lvl:"+Sword[3]+"}"
		
		EnchList += "]}"

		e.npc.executeCommand("/summon Item ~ ~ ~ {Item:{id:"+str(Item5)+",Damage:"+str(Damage)+",Count:1,tag:"+str(EnchList)+"}}") # Looting sword
		if InventorySpawn.isDone != True :
			GoldenAppleLoot = e.npc.getTempdata().get("GapCount")
			if (GoldenAppleLoot == None) or (GoldenAppleLoot == 0):
				GoldenAppleLoot = 1
			e.npc.executeCommand("/summon Item ~ ~ ~ {Item:{id:322,Damage:0,Count:"+str(GoldenAppleLoot)+"}}") # Looting golden apple based on the amount he had
			
			e.npc.executeCommand("/summon Item ~ ~ ~+0.35 {Item:{id:278,Damage:187,Count:1,tag:{ench:[{id:32,lvl:5}]}}}")		# Looting a pickaxe
			try:
				e.npc.executeCommand("/xp 40 "+ str(e.source.getName()))		# Looting xp
			except :
				pass

		if e.npc.getStoreddata().get("Kills") >= 2 and (InventorySpawn.isDone != True ):
			InventorySpawn.isDone = True
			InventorySpawn(e)
			
def BadlionDeathTchatMessage(e):
	if e.npc.world.getTempdata().get("BadlionKillsSystem") == True :
		NameKilled = e.npc.getDisplay().getName()				# Looking for own data
		KilledFaction = e.npc.getFaction().getId()
		KilledKills = e.npc.getStoreddata().get("Kills")
		UnderlinedKilled = "false"
		UnderlinedKiller = "false"
		ItalicKilled = "false"
		ItalicKiller = "false"
		if KilledKills == None :
			KilledKills = 0
			
		FactionArgList = [["green","false","false"],["green","false","false"],["blue","false","false"],["red","false","false"],["yellow","false","false"],["dark_gray","false","false"],["dark_blue","false","false"],["dark_red","false","false"],["dark_green","false","false"],["gold","false","false"],["aqua","false","false"],["light_purple","false","false"],["dark_aqua","false","false"],["dark_purple","false","false"],["green","false","true"],["blue","false","true"],["red","false","true"],["yellow","false","true"],["dark_gray","false","true"],["dark_blue","false","true"],["dark_red","false","true"],["dark_green","false","true"],["gold","false","true"],["aqua","false","true"],["light_purple","false","true"],["dark_aqua","false","true"],["dark_purple","false","true"]]
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
			e.npc.executeCommand('/tellraw @a ["",{"text":"[","color":"dark_gray"},{"text":"UHC","color":"dark_red"},{"text":"] ","color":"dark_gray"},{"text":"'+str(NameKilled)+'","color":"'+str(TeamColorKilled)+'","underlined":"'+str(UnderlinedKilled)+'","italic":"'+str(ItalicKilled)+'"},{"text":"[","color":"white"},{"text":"'+str(int(KilledKills))+'","color":"white"},{"text":"]","color":"white"},{"text":" was slain by ","color":"gray"},{"text":"'+str(NameKiller)+'","color":"'+str(TeamColorKiller)+'","underlined":"'+str(UnderlinedKiller)+'","italic":"'+str(ItalicKiller)+'"},{"text":"[","color":"white"},{"text":"'+str(ActualisedKillerKills) +'","color":"white"},{"text":"]","color":"white"}]')
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
				e.npc.executeCommand('/tellraw @a ["",{"text":"[","color":"dark_gray"},{"text":"UHC","color":"dark_red"},{"text":"] ","color":"dark_gray"},{"text":"'+str(NameKilled)+'","color":"'+str(TeamColorKilled)+'","underlined":"'+str(UnderlinedKilled)+'","italic":"'+str(ItalicKilled)+'"},{"text":"[","color":"white"},{"text":"'+str(int(KilledKills))+'","color":"white"},{"text":"]","color":"white"},{"text":" was slain by ","color":"gray"},{"text":"'+str(NameKiller)+'","color":"'+str(TeamColorKiller)+'","underlined":"'+str(UnderlinedKiller)+'","italic":"'+str(ItalicKiller)+'"},{"text":"[","color":"white"},{"text":"'+str(ActualisedKillerKills) +'","color":"white"},{"text":"]","color":"white"}]')
				InventorySpawn(e)
				BleedingSweets(e)
			except :				# If Killed by PvE
				e.npc.executeCommand('/tellraw @a ["",{"text":"[","color":"dark_gray"},{"text":"UHC","color":"dark_red"},{"text":"] ","color":"dark_gray"},{"text":"'+str(NameKilled)+'","color":"'+str(TeamColorKilled)+'","underlined":"'+str(UnderlinedKilled)+'","italic":"'+str(ItalicKilled)+'"},{"text":"[","color":"white"},{"text":"'+str(int(KilledKills))+'","color":"white"},{"text":"]","color":"white"},{"text":" died in PvE ","color":"gray"}]')
				InventorySpawn(e)
								
def DeathTchatMessage(e):
	if e.npc.world.getTempdata().get("BadlionKillsSystem") == False :
		NameKilled = e.npc.getDisplay().getName()				# Looking for own data
		KilledFaction = e.npc.getFaction().getId()
		UnderlinedKilled = "false"
		UnderlinedKiller = "false"
		ItalicKilled = "false"
		ItalicKiller = "false"

				
		FactionArgList = [["green","false","false"],["green","false","false"],["blue","false","false"],["red","false","false"],["yellow","false","false"],["dark_gray","false","false"],["dark_blue","false","false"],["dark_red","false","false"],["dark_green","false","false"],["gold","false","false"],["aqua","false","false"],["light_purple","false","false"],["dark_aqua","false","false"],["dark_purple","false","false"],["green","false","true"],["blue","false","true"],["red","false","true"],["yellow","false","true"],["dark_gray","false","true"],["dark_blue","false","true"],["dark_red","false","true"],["dark_green","false","true"],["gold","false","true"],["aqua","false","true"],["light_purple","false","true"],["dark_aqua","false","true"],["dark_purple","false","true"]]
		TeamColorKilled = FactionArgList[KilledFaction][0]
		UnderlinedKilled = FactionArgList[KilledFaction][1]
		ItalicKilled = FactionArgList[KilledFaction][2]
			
		try :											# If killed by a bot
			KillerFaction = e.source.getFaction().getId()
			NameKiller = e.source.getDisplay().getName()
			TeamColorKiller = FactionArgList[KillerFaction][0]
			UnderlinedKiller = FactionArgList[KillerFaction][1]
			ItalicKiller = FactionArgList[KillerFaction][2]
				
			e.npc.executeCommand('/tellraw @a ["",{"text":"[","color":"dark_gray"},{"text":"UHC","color":"dark_red"},{"text":"] ","color":"dark_gray"},{"text":"'+str(NameKilled)+'","color":"'+str(TeamColorKilled)+'","underlined":"'+str(UnderlinedKilled)+'","italic":"'+str(ItalicKilled)+'"},{"text":" was slain by ","color":"gray"},{"text":"'+str(NameKiller)+'","color":"'+str(TeamColorKiller)+'","underlined":"'+str(UnderlinedKiller)+'","italic":"'+str(ItalicKiller)+'"}]')
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
				e.npc.executeCommand('/tellraw @a ["",{"text":"[","color":"dark_gray"},{"text":"UHC","color":"dark_red"},{"text":"] ","color":"dark_gray"},{"text":"'+str(NameKilled)+'","color":"'+str(TeamColorKilled)+'","underlined":"'+str(UnderlinedKilled)+'","italic":"'+str(ItalicKilled)+'"},{"text":" was slain by ","color":"gray"},{"text":"'+str(NameKiller)+'","color":"'+str(TeamColorKiller)+'","underlined":"'+str(UnderlinedKiller)+'","italic":"'+str(ItalicKiller)+'"}]')
				InventorySpawn(e)
				BleedingSweets(e)
			except :				# If Killed by PvE
				e.npc.executeCommand('/tellraw @a ["",{"text":"[","color":"dark_gray"},{"text":"UHC","color":"dark_red"},{"text":"] ","color":"dark_gray"},{"text":"'+str(NameKilled)+'","color":"'+str(TeamColorKilled)+'","underlined":"'+str(UnderlinedKilled)+'","italic":"'+str(ItalicKilled)+'"},{"text":" died in PvE ","color":"gray"}]')
				InventorySpawn(e)

def VanillaDeathStyle(e):
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

def HeadPost(e):
	try:
		e.source.getName()
		if e.npc.world.getTempdata().get("GoldenHeads") == True :
			e.npc.executeCommand("/setblock ~ ~ ~ minecraft:fence")	
			e.npc.executeCommand("/setblock ~ ~+1 ~ minecraft:skull 1")
	except:
		pass
def ExplodeOnDeath(e):
	if e.npc.world.getTempdata().get("ExplodeOnDeath") == True :
		e.npc.world.explode(e.npc.getX(),e.npc.getY()+1,e.npc.getZ(),0, False, False)




#ON KILL ONLY functions :	

def IronGolemSound(e):
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
	Name = e.npc.getDisplay().getName()
	Kills = e.npc.getStoreddata().get("Kills")
	if Kills == None :
		Kills = 1
		e.npc.getStoreddata().put("Kills", Kills)
	else :
		Kills += 1
		e.npc.getStoreddata().put("Kills", Kills)

def ScoreBoardUpdateI(e):
	RedditUHCDisplay = e.npc.world.getTempdata().get("RedditUHCDisplay")
	if RedditUHCDisplay == True :
		Name = e.npc.getDisplay().getName()
		e.npc.executeCommand('/scoreboard players add '+str(Name)+' Kills 1')

def StuffUpgradeOnKill(e) :
	try :
		KillProt = e.entity.getStoreddata().get("Prot")
		KillProj = e.entity.getStoreddata().get("Proj")
		KillSword = e.entity.getStoreddata().get("Sword")
		MyProt = e.npc.getStoreddata().get("Prot")
		MyProj = e.npc.getStoreddata().get("Proj")
		Sword = e.npc.getStoreddata().get("Sword")
		KillStuff = e.entity.getStoreddata().get('Armor')

		KillStuff = KillStuff.split("/")
		KillProj = KillProj.split("/")
		KillProt = KillProt.split("/")
		KillSword = KillSword.split("/")

		MyProj = MyProj.split("/")
		MyProt = MyProt.split("/")
		Sword = Sword.split("/")

		ArmorList = "4/5/6/7"

		if (e.npc.getInventory().getArmor(0).getDisplayName() == "Iron Helmet"): 
			if (KillStuff[0] == "1"):
				e.npc.getInventory().setArmor(0,e.npc.world.createItem("minecraft:diamond_helmet",0,1))
				e.npc.getStoreddata().put("Prot", KillProt[0])
				e.npc.getStoreddata().put("Proj", KillProj[0])
				ArmorList.replace("4", "1")
			else :
				ArmorList.replace("6", "0")

		if (e.npc.getInventory().getArmor(1).getDisplayName() == "Iron Chestplate"): 
			if (KillStuff[1] == "1"):
				e.npc.getInventory().setArmor(1,e.npc.world.createItem("minecraft:diamond_chestplate",0,1))
				e.npc.getStoreddata().put("Prot", KillProt[1])
				e.npc.getStoreddata().put("Proj", KillProj[1])
				ArmorList.replace("5", "1")
			else :
				ArmorList.replace("6", "0")

		if (e.npc.getInventory().getArmor(2).getDisplayName() == "Iron Leggings"):
			if (KillStuff[2] == "1"):
				e.npc.getInventory().setArmor(2,e.npc.world.createItem("minecraft:diamond_leggings",0,1))
				e.npc.getStoreddata().put("Prot", KillProt[2])
				e.npc.getStoreddata().put("Proj", KillProj[2])
				ArmorList.replace("6", "1")
			else :
				ArmorList.replace("6", "0")

		if (e.npc.getInventory().getArmor(3).getDisplayName() == "Iron Boots"):
			if (KillStuff[3] == "1"):
				e.npc.getInventory().setArmor(3,e.npc.world.createItem("minecraft:diamond_boots",0,1))
				e.npc.getStoreddata().put("Prot", KillProt[3])
				e.npc.getStoreddata().put("Proj", KillProj[3])
				ArmorList.replace("7", "1")
			else :
				ArmorList.replace("7", "0")

		if (e.npc.getStoreddata().get("TickForUpgrade") == None) or (e.npc.getStoreddata().get("TickForUpgrade") == "0"):
			e.npc.getStoreddata().put("TickForUpgrade", "1") 
			for i in range (0, 4):
				if (int(KillProt[i]) == int(MyProt[i])) and (int(MyProt[i]) != 4):				#Anvil stuff
					MyProt.pop(i)
					MyProt.insert(i, str(int(KillProt[i])+1))
				elif int(KillProt[i]) > int(MyProt[i]) :				# Taking better stuff
					MyProt.pop(i)
					MyProt.insert(i, str(KillProt[i]))

		else :
			e.npc.getStoreddata().put("TickForUpgrade", str(int(e.npc.getStoreddata().get("TickForUpgrade"))+1))

		if e.npc.getStoreddata().get("TickForUpgrade") == "3" :
			e.npc.getStoreddata().put("TickForUpgrade", "0")

		if (int(KillSword[0])) > int(Sword[0]) :
			Sword.pop(0)
			Sword.insert(0, str(KillSword[0]))
		

		elif (int(KillSword[0]) == int(Sword[0])) and (int(Sword[0]) != 5):
			Sword.pop(0)
			Sword.insert(0, str(int(KillSword[0])+1))

		if int(KillSword[1]) != 0 :
			Sword.pop(1)
			Sword.insert(1, "1")

		
		
		ProtList = "/".join(MyProt)
		ProjList = "/".join(MyProj)
		SwordList = "/".join(Sword)
		
		e.npc.getStoreddata().put("Prot", ProtList)
		e.npc.getStoreddata().put("Proj", ProjList)
		e.npc.getStoreddata().put("Armor", ArmorList)
		e.npc.getStoreddata().put("Sword", SwordList)
		Gap = e.npc.getTempdata().get("GapCount")
		if Gap != None :
			Gap += 10
			try:
				Gap += e.entity.getTempdata().get("Gap")
			except:
				Gap += 5
			e.npc.getTempdata().put("GapCount", Gap)
		else :
			e.npc.getTempdata().put("GapCount", 8)

		WaterRemainig = e.npc.getTempdata().get("WaterRemaining")
		if WaterRemainig != None :
			WaterRemainig == 3
			e.npc.getTempdata().put("WaterRemaining", WaterRemainig)
		else :
			e.npc.getTempdata().put("WaterRemaining", 3)
	except:
		pass

def ThunderStrike(e):
	ThunderActivated = e.npc.world.getTempdata().get("ThunderStrike")
	if ThunderActivated == True :
		X = e.npc.getX()
		Y = e.npc.getY()
		Z = e.npc.getZ()
		e.npc.world.thunderStrike(X, Y+5, Z)

def UpdateAggro(e):
	e.npc.world.getStoreddata().put(str(e.npc.getFaction().getId())+"Aggro", str(int(e.npc.world.getStoreddata().get(str(e.npc.getFaction().getId())+"Aggro"))+1))



#SCENARIOS functions :				

def AbsoLess(e):
	if e .npc.world.getTempdata().get("AbsoLess") == True :
		e.npc.executeCommand("/effect @a minecraft:absorption 0")

def MasterLevel(e):
	MasterLevelOn = e.npc.world.getTempdata().get("MasterLevel")
	if MasterLevelOn == True:
		e.npc.executeCommand("/xp 1000l @a")

def CatEyes(e):
	CatEyesOn = e.npc.world.getTempdata().get("CatEyes")
	if CatEyesOn == True :
		e.npc.executeCommand('/effect @a minecraft:night_vision 1000000 0 true')

def SuperHeroes(e):
	SheroesOn = e.npc.world.getTempdata().get("SuperHeroes")
	PowerList = random.randint(1, 6)
	if SheroesOn == True :
		if PowerList == 1 :
			e.npc.addPotionEffect(11, 100000, 1, True)
		elif PowerList == 2 :
			e.npc.addPotionEffect(1, 100000, 0, True)
		elif PowerList == 3 :
			e.npc.addPotionEffect(5, 100000, 0, True)
		elif PowerList == 4 :
			e.npc.addPotionEffect(21, 100000, 4, True)
		elif PowerList == 5 :
			e.npc.addPotionEffect(10, 100000, 0, True)
		elif PowerList == 6 :
			e.npc.addPotionEffect(21, 100000, 0, True)
			e.npc.addPotionEffect(11, 100000, 0, True)
			e.npc.addPotionEffect(1, 100000, 0, True)

def DoubleHealth(e):
	DoubleHealth = e.npc.world.getTempdata().get("DoubleHealth")
	if DoubleHealth == True :
		e.npc.getStats().setMaxHealth(40)
		e.npc.setHealth(40)

def BookCeption(e):
	BookCeption = e.npc.world.getTempdata().get("BookCeption")
	if BookCeption == True :
		Tier4 = ["16","0","1","17","3","32","48","2","4","18"]
		Tier3 = ["34","61","62","8"]
		Tier2 = ["49","19","20","5","7"]
		Tier1 = ["6","50","51","33"]
		randomTier = random.randint(1, 4)
		if randomTier == 1 :
			randomBook = random.choice(Tier1)
			e.npc.executeCommand("/summon Item ~ ~ ~+0.35 {Item:{id:403,Count:1,tag:{StoredEnchantments:[{id:"+str(randomBook)+",lvl:1}]}}}")
		elif randomTier == 2 :
			randomBook = random.choice(Tier2)
			randomLevel = random.randint(1,2)
			e.npc.executeCommand("/summon Item ~ ~ ~+0.35 {Item:{id:403,Count:1,tag:{StoredEnchantments:[{id:"+str(randomBook)+",lvl:"+str(randomLevel)+"}]}}}")
		elif randomTier == 3 :
			randomBook = random.choice(Tier3)
			randomLevel = random.randint(1,3)
			e.npc.executeCommand("/summon Item ~ ~ ~+0.35 {Item:{id:403,Count:1,tag:{StoredEnchantments:[{id:"+str(randomBook)+",lvl:"+str(randomLevel)+"}]}}}")
		elif randomTier == 4 :
			randomBook = random.choice(Tier4)
			randomLevel = random.randint(1,4)
			e.npc.executeCommand("/summon Item ~ ~ ~+0.35 {Item:{id:403,Count:1,tag:{StoredEnchantments:[{id:"+str(randomBook)+",lvl:"+str(randomLevel)+"}]}}}")

def OneShot(e):
	OneShot = e.npc.world.getTempdata().get("OneShot")
	if OneShot == True :
		e.npc.setHealth(1)
		e.npc.getStats().setMaxHealth(1)
		e.npc.getTempdata().put("GapCount", 0)
	
def BleedingSweets(e):
	BleedingSweets = e.npc.world.getTempdata().get("BleedingSweets")
	if BleedingSweets == True :
		BleedingDiamond = e.npc.world.getTempdata().get("BleedingDiamond")
		BleedingIron = e.npc.world.getTempdata().get("BleedingIron")
		BleedingGold = e.npc.world.getTempdata().get("BleedingGold")
		e.npc.executeCommand("/summon Item ~+0.35 ~ ~+0.35 {Item:{id:264,Damage:0,Count:"+str(BleedingDiamond)+"}}")
		e.npc.executeCommand("/summon Item ~-0.35 ~ ~-0.35 {Item:{id:265,Damage:0,Count:"+str(BleedingIron)+"}}")
		e.npc.executeCommand("/summon Item ~-0.35 ~ ~+0.35 {Item:{id:266,Damage:0,Count:"+str(BleedingGold)+"}}")
		
def MoleReveal(e):
	Mole = e.npc.world.getTempdata().get("Mole")
	if Mole == True :
		TimeLimit = e.npc.getStoreddata().get("TimeLimit")
		MoleAlreadySet = e.npc.world.getStoreddata().get(str(e.npc.getFaction().getId())+"Mole")
		MolePerTeam = e.npc.world.getTempdata().get("MolePerTeam")
		ImMole = e.npc.getStoreddata().get("ImMole")
		Reveal = e.npc.getStoreddata().get("Revealed")

		if MoleAlreadySet == None :
			MoleAlreadySet = 0
			e.npc.world.getStoreddata().put(str(e.npc.getFaction().getId())+"Mole", 0)

		elif (MoleAlreadySet <= int(MolePerTeam)) and (ImMole != 1):
			e.npc.world.getStoreddata().put(str(e.npc.getFaction().getId())+"Mole", int(MoleAlreadySet)+1)
			e.npc.getStoreddata().put("ImMole", 1)
			ImMole = e.npc.getStoreddata().get("ImMole")

		if  (e.npc.getStoreddata().get("ImMole") == 1 ) and ( TimeLimit == None ) :
			TimeLimit = [0, 1500, 8000, 1000]
			TimeLimit = random.choice(TimeLimit)
			e.npc.getStoreddata().put("TimeLimit", TimeLimit)

		if (e.npc.getStoreddata().get("ImMole") == 1) and (TimeLimit-100 <= e.npc.world.getTime() <= TimeLimit+100) and (e.npc.getStoreddata().get("Revealed") != 1):
			e.npc.getStoreddata().put("Revealed", 1)
			e.npc.executeCommand('/tellraw @a ["",{"text":"[","color":"dark_gray"},{"text":"UHC","color":"dark_red"},{"text":"] ","color":"dark_gray"},{"text":"[","color":"gold"},{"text":"Mole","color":"pink"},{"text":"] ","color":"gold"},{"text":"'+str(e.npc.getDisplay().getName())+'","color":"red"},{"text":" is a mole ! ","color":"gray"}]')
			e.npc.setFaction(23)

def NoCleanUpActivation(e) :
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
	import random
	Name = e.npc.getDisplay().getName()
	GameStarted = e.npc.world.getTempdata().get("GameStarted")
	tick = 0
	try :
		if (GameStarted == 1) and (Name == "Disabled") :

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

			a = random.choice(ChoosingList)
				
			if (e.npc.world.getTempdata().get("ForcedType") == True) and (len(e.npc.world.getTempdata().get("NameTier"+str("UHCEliteTier"))) != 0 ):
				a = "UHCEliteTier" 



			e.npc.getTempdata().put("SelectedType", a)
			SelectedName = random.choice(e.npc.world.getTempdata().get("NameTier"+str(a)))
			NameList = e.npc.world.getTempdata().get("NameTier"+str(a))
			NameList.remove(SelectedName)
			e.npc.world.getTempdata().put("NameTier"+str(a),NameList)

			if a in ["NoobTier","CasualTier","CommonTier","GoodTier"] :
				Random = random.randint(1, 71)
				e.npc.getDisplay().setName(str(SelectedName))
				e.npc.getDisplay().setSkinTexture('minecraft:textures/entity/Random'+str(Random)+'.png')

			else :
				e.npc.getDisplay().setSkinTexture('minecraft:textures/entity/'+SelectedName+'.png')
				e.npc.getDisplay().setName(str(SelectedName))

			RandomForCape = random.randint(1, 3)
			if RandomForCape == 3:
				RandomCape = random.randint(1, 25)
				e.npc.getDisplay().setCapeTexture('minecraft:textures/cloak/'+str(RandomCape)+'.png')

			if e.npc.world.getTempdata().get("ScatterMessageEnabled") == True :
				e.npc.executeCommand('/tellraw @a ["",{"text":"[","color":"dark_gray"},{"text":"UHC","color":"dark_red"},{"text":"] ","color":"dark_gray"},{"text":"[","color":"gold"},{"text":"Scatter","color":"blue"},{"text":"] ","color":"gold"},{"text":"Scattered ","color":"dark_red"},{"text":"'+str(SelectedName)+'","color":"gray"}]')
			else :
				pass
	except:
		e.npc.world.getStoreddata().put("Players", e.npc.world.getStoreddata().get("Players")-1)
		e.npc.world.broadcast("Deleting because of NoName " + str(e.npc.world.getStoreddata().get("Players")))
		TeamReduction(e)
		e.npc.despawn()

def SettingArmor(e) :
	if e.npc.getInventory().getArmor(0) == None :
		DiamondProbability = e.npc.world.getTempdata().get("DiamondProbability")
		PartList = ["_helmet","_chestplate","_leggings","_boots"]
		FireAspectAllowed = e.npc.world.getTempdata().get("FireAspectAllowed")
		ArcticMeta = e.npc.world.getTempdata().get("ArcticMeta")
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
				if random.randint(1, int(DiamondProbability)) == 1 :										# Random between 1 - Max to know if it is a diamond piece or a iron piece
					e.npc.getInventory().setArmor(i,e.npc.world.createItem("minecraft:iron"+str(PartList[i]),0,1))
					ArmorList.append("0")
				else :
					e.npc.getInventory().setArmor(i,e.npc.world.createItem("minecraft:diamond"+str(PartList[i]),0,1))
					ArmorList.append("1")
				if ArcticMeta == True :
					if random.randint(0, 5) == 5 :
						ProjList.append(str(random.randint(1,2)))									# Enchanting it randomly
				else :
					ProtList.append(str(random.randint(1,2)))
					ProjList.append("0")

		if e.npc.getInventory().getRightHand() == None :
			if random.randint(1, int(DiamondProbability)) == 1 :
				e.npc.getInventory().setRightHand(e.npc.world.createItem("minecraft:iron_sword",0,1))
			else :
				e.npc.getInventory().setRightHand(e.npc.world.createItem("minecraft:diamond_sword",0,1))
			SwordList.append(str(random.randint(3,4)))						# Giving a sharpness enchant
			if FireAspectAllowed == True :									# And a fire one if allowed
				if random.randint(0,10) == 10 :
					SwordList.append("1")
				else :
					SwordList.append("0")
			else :
				SwordList.append("0")

			SwordList.append(str(random.choice(KbList)))	# Giving a knockback one as well
			SwordList.append(str(random.choice(UnbreakList)))	# Giving a unbreaking
			
		if e.npc.getTempdata().get("Bow") == None :
			if ArcticMeta == True :
				BowList.append(str(random.choice(PowerArcticList)))		# Setting a power bow ( powerful bow if its on a reddit meta )
			else :
				BowList.append(str(random.choice(PowerList)))
			
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
			ProtEffect = int(Prot[0]) * 0.012
			ProjEffect = int(Proj[0]) * 0.02
			MeleeResToSet += 0.13 + ProtEffect
			ProjToSet += 0.15 + ProjEffect
		else :
			ProtEffect = int(Prot[0]) * 0.012
			ProjEffect = int(Proj[0]) * 0.02
			MeleeResToSet += 0.1 + ProtEffect
			ProjToSet += 0.1 + ProjEffect
		

		if int(Armor[1]) == 1 :							# Diamond Chestplate
			ProtEffect = int(Prot[1]) * 0.012
			ProjEffect = int(Proj[1]) * 0.02
			MeleeResToSet += 0.33 + ProtEffect
			ProjToSet += 0.3 + ProjEffect
		else :
			ProtEffect = int(Prot[1]) * 0.012
			ProjEffect = int(Proj[1]) * 0.02
			MeleeResToSet += 0.3 + ProtEffect
			ProjToSet += 0.2 + ProjEffect


		if int(Armor[2]) == 1 :							# Diamond Leggings
			ProtEffect = int(Prot[2]) * 0.012
			ProjEffect = int(Proj[2]) * 0.02
			MeleeResToSet += 0.22 + ProtEffect
			ProjToSet += 0.15 + ProjEffect
		else :
			ProtEffect = int(Prot[2]) * 0.012
			ProjEffect = int(Proj[2]) * 0.02
			MeleeResToSet += 0.19 + ProtEffect
			ProjToSet += 0.2 + ProjEffect


		if int(Armor[3]) == 1 :							# Diamond Boots
			ProtEffect = int(Prot[3]) * 0.012
			ProjEffect = int(Proj[3]) * 0.02
			MeleeResToSet += 0.13 + ProtEffect
			ProjToSet += 0.15 + ProjEffect
		else :
			ProtEffect = int(Prot[3]) * 0.012
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

def SettingEntityForced(e):
	try:
		GameStarted = e.npc.world.getTempdata().get("GameStarted")
		if (GameStarted == 1) and (e.npc.getDisplay().getName() == "Disabled") and (e.npc.world.getTempdata().get(str(int(e.npc.getFaction().getId()))+"Team")) != str("None"):
			TeamListHere = e.npc.world.getTempdata().get(str(int(e.npc.getFaction().getId()))+"Team")
			try:
				NameHere = TeamListHere.split("//")
			except:
				pass
			NameNow = str(NameHere[0])
			e.npc.getDisplay().setName(str(NameHere[0]))
			NameHere.pop(0)
			NameHere = "//".join(NameHere)
			e.npc.world.getTempdata().put(str(int(e.npc.getFaction().getId()))+"Team", NameHere)

			if NameNow in e.npc.world.getTempdata().get("NameTier"+str("NoobTier")):
				a = "NoobTier"
			elif NameNow in e.npc.world.getTempdata().get("NameTier"+str("CasualTier")):
				a = "CasualTier"
			elif NameNow in e.npc.world.getTempdata().get("NameTier"+str("CommonTier")):
				a = "CommonTier"
			elif NameNow in e.npc.world.getTempdata().get("NameTier"+str("GoodTier")):
				a = "GoodTier"
			elif NameNow in e.npc.world.getTempdata().get("NameTier"+str("ProTier")):
				a = "ProTier"
			elif NameNow in e.npc.world.getTempdata().get("NameTier"+str("UHCEliteTier")):
				a = "UHCEliteTier"

			else:
				a = "CommonTier"

			if a == "UHCEliteTier" or a == "ProTier" :
				if e.npc.world.getStoreddata().get(str(e.npc.getFaction().getId())+"Aggro") == None :
					e.npc.world.getStoreddata().put(str(e.npc.getFaction().getId())+"Aggro", 1)
			else:
				e.npc.world.getStoreddata().put(str(e.npc.getFaction().getId())+"Aggro", e.npc.world.getStoreddata().get(str(e.npc.getFaction().getId())+"Aggro")+1)

			NameList = e.npc.world.getTempdata().get("NameTier"+str(a))
			NameList.remove(NameNow)
			e.npc.world.getTempdata().put("NameTier"+str(a),NameList)

			e.npc.getTempdata().put("SelectedType", a)

			if a in ["NoobTier","CasualTier","CommonTier","GoodTier"] :
				Random = random.randint(1, 71)
				e.npc.getDisplay().setSkinTexture('minecraft:textures/entity/Random'+str(Random)+'.png')

			else :
				e.npc.getDisplay().setSkinTexture('minecraft:textures/entity/'+NameNow+'.png')

			RandomForCape = random.randint(1, 3)
			if RandomForCape == 3:
				RandomCape = random.randint(1, 25)
				e.npc.getDisplay().setCapeTexture('minecraft:textures/cloak/'+str(RandomCape)+'.png')

			if e.npc.world.getTempdata().get("ScatterMessageEnabled") == True :
				e.npc.executeCommand('/tellraw @a ["",{"text":"[","color":"dark_gray"},{"text":"UHC","color":"dark_red"},{"text":"] ","color":"dark_gray"},{"text":"[","color":"gold"},{"text":"Scatter","color":"blue"},{"text":"] ","color":"gold"},{"text":"Scattered ","color":"dark_red"},{"text":"'+str(SelectedName)+'","color":"gray"}]')
			else :
				pass	
		else:
			SettingEntity(e)	
		
	except:
		pass



def ActualisingTeamMembers(e):
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

	FactionID = e.npc.getFaction().getId()
	Name = e.npc.getDisplay().getName()
	if FactionID == 0 or FactionID == 1 :
		e.npc.executeCommand('/scoreboard teams join green '+str(Name)+'')
	if FactionID == 2 or FactionID == 3 :
		e.npc.executeCommand('/scoreboard teams join blue '+str(Name)+'')
	if FactionID == 4 or FactionID == 5 :
		e.npc.executeCommand('/scoreboard teams join red '+str(Name)+'')
	if FactionID == 6 or FactionID == 7 :
		e.npc.executeCommand('/scoreboard teams join gold '+str(Name)+'')
	if FactionID == 8 or FactionID == 9 :
		e.npc.executeCommand('/scoreboard teams join aqua '+str(Name)+'')
	if FactionID == 10 or FactionID == 11 :
		e.npc.executeCommand('/scoreboard teams join dark_green '+str(Name)+'')
	if FactionID == 12 or FactionID == 13 :
		e.npc.executeCommand('/scoreboard teams join purple '+str(Name)+'')
	if FactionID == 14 or FactionID == 15 :
		e.npc.executeCommand('/scoreboard teams join yellow '+str(Name)+'')

def SettingInitialKills(e):
	Kills = e.npc.getStoreddata().get("Kills")
	if Kills == None :
		e.npc.getStoreddata().put("Kills", 0)




#TEAMER BOTS ONLY functions :

def GappleSharing(e):
	try:
		FactionID = e.npc.getFaction().getId()
		if FactionID == 26 :
			Teaming(e)
			if e.player.getHeldItem().getName() == "minecraft:golden_apple":
				e.npc.getTempdata().put("GapCount", e.npc.getTempdata().get("GapCount")+1)
				e.player.getHeldItem().setStackSize(e.player.getHeldItem().getStackSize()-1)
		else :
			pass
	except:
		pass
		
def KillingPlayer(e):
	try :
		e.npc.world.getTempdata().put(str(e.entity.getName()+"Killer"), [str(e.npc.getDisplay().getName()),str(e.npc.getFaction().getId()),str(e.npc.getStoreddata().get("Kills"))])
	except:
		pass
		
def Teaming(e):
	Source = e.player.getMCEntity()
	e.npc.getRole().setInfinite(1)
	e.npc.getRole().setGuiDisabled(1)
	e.npc.getRole().setOwner(Source)



#IN GAME functions :

def WeatherClear(e):
	e.npc.executeCommand("/weather clear")

def WantToRod(e):
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
			
				if random.randint(0, 16) == 0 :
					e.npc.getTempdata().put("NeedRod", e.npc.getTempdata().get("NeedRod")+1)
	except:		
		pass

def Rod(e):
	if e.npc.world.getTempdata().get("OneShot") != True :
		if e.npc.getTempdata().get("NeedRod") == None :
			e.npc.getTempdata().put("NeedRod", 0)

		if e.npc.getTempdata().get("NeedRod") != 0 :
			try:
				Rotate = e.npc.getRotation()
				e.npc.shootItem(e.npc.getAttackTarget(),e.npc.world.createItem("minecraft:snowball",0,1), 100)
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
	Source = str(e.mcDamageSource)
	Source = Source.split("@")
	if (Source[0] == "net.minecraft.util.DamageSource") and (e.npc.getHealth() <= 5):
		e.setCanceled(True)       

def SwordDebug(e):
	if e.npc.getInventory().getRightHand() == None :
		e.npc.getInventory().setRightHand(e.npc.world.createItem("minecraft:diamond_sword",0,1))
		SettingResistance(e)

def LifeMessageBow(e):
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
				e.npc.executeCommand('/tellraw '+str(Source)+' ["",{"text":"[","color":"dark_gray"},{"text":"UHC","color":"dark_red"},{"text":"] ","color":"dark_gray"},{"text":"[","color":"gold"},{"text":"Bow","color":"aqua"},{"text":"] ","color":"gold"},{"text":"'+str(Name)+'","color":"red"},{"text":" is now at ","color":"white"},{"text":"'+str(Health)+'","color":"dark_red"}]')
				e.npc.executeCommand('/playsound random.successful_hit '+str(Source)+' '+str(X)+' '+str(Y)+' '+str(Z)+' 1 0.5')
		except:
			pass
	except:
		pass

def Strafing(e):
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
		ReachList = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 3, 3]
		MissChance = random.choice(ReachList)
		if MissChance == 3 :
			e.setCanceled(True)

	if SelectedType == "ProTier" :
		ReachList = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 3]
		MissChance = random.choice(ReachList)
		if MissChance == 3 :
			e.setCanceled(True)

	if SelectedType == "UHCEliteTier" :
		ReachList = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 3]
		MissChance = random.choice(ReachList)
		if MissChance == 3 :
			e.setCanceled(True)

	if SelectedType == "NoobTier" :
		ReachList = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 3, 3, 3, 3, 3, 3, 3, 3]
		MissChance = random.choice(ReachList)
		if MissChance == 3 :
			e.setCanceled(True)

def Targeting(e):
	if e.npc.getAttackTarget() != None :
		
		try:
			Target = e.entity
			if (abs(Target.getX() - e.npc.getX()) <= 20 )and (abs(Target.getZ() - e.npc.getZ()) <= 20):
				pass
			else:
				e.npc.setAttackTarget(None)
		except:
			pass
		
		#try:
		Target = e.entity
		Aggro = 0 
		TargetAggro = 0	
		MyId = e.npc.getFaction().getId()
		RunOn = e.npc.getTempdata().get("RunOn")
		if Target.getType() == 2 : 
			TheirId = Target.getFaction().getId()
		elif Target.getType() == 1:
			TargetAggro = int(e.npc.world.getStoreddata().get(str(Target.getName()) +"Kills"))	
			TheirId = None	
				

		Ennemy = e.npc.world.getNearbyEntities(int(e.npc.getX()), int(e.npc.getY()), int(e.npc.getZ()), 8, 2).tolist()

		for i in range (0, len(Ennemy)):
			if Ennemy[i].getFaction().getId() == TheirId :
				TargetAggro += Ennemy[i].getStoreddata().get("Aggro")
			if Ennemy[i].getFaction().getId() == MyId :
				Aggro += Ennemy[i].getStoreddata().get("Aggro")		

		if Aggro+2 < TargetAggro :
			e.npc.getAi().setRetaliateType(3)
			e.npc.getTempdata().put("RunOn", 30)

				


		elif RunOn <= 0:
			e.npc.getAi().setRetaliateType(0) 

		#except:
			#pass

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
	WaterAllowed = e.npc.world.getTempdata().get("WaterAllowed")
	if WaterAllowed == True and e.npc.getTempdata().get("WaterUsed") == None:			# Checking if the npc didnt spawned a water bucket already to avoid spamming water and create lags and annoying fights

		WaterRemaining = e.npc.getTempdata().get("WaterRemaining")

		PosList = [e.npc.getX(),e.npc.getY(),e.npc.getZ()]
		if ( WaterRemaining > 1):
			e.npc.executeCommand('/setblock ~ ~ ~ minecraft:water')					# Creating 2 water blocks to update the first and make the water flow
			e.npc.executeCommand('/setblock ~ ~ ~+1 minecraft:water 1')
			WaterRemaining -= 1
			e.npc.getTempdata().put("WaterRemaining", WaterRemaining)
			e.npc.getTempdata().put("WaterUsed", PosList)						# Saving the coordinates of the water in a Tempdata to clear it later


def CancelFire(e):
	if e.npc.isBurning() == True :
		if (random.randint(0, 8) == 0) and (e.npc.getTempdata().get("WaterUsed") == None):
			e.npc.executeCommand('/setblock ~ ~ ~ minecraft:water')					# Creating 2 water blocks to update the first and make the water flow
			e.npc.executeCommand('/setblock ~ ~ ~+1 minecraft:water 1')
			PosList = [e.npc.getX(),e.npc.getY(),e.npc.getZ()]
			e.npc.getTempdata().put("WaterUsed", PosList)


def HealthDisplay(e):
	Health = e.npc.getHealth()
	LifeToDisplay = int(round(Health))
	e.npc.getDisplay().setTitle(' ' + (str(LifeToDisplay) + " HP "))

def UsingGap(e):
	#e.npc.getTempdata().put("IsEating", False)
	IsUsingGap = e.npc.getTempdata().get("IsUsingGap")
	GapCount = e.npc.getTempdata().get("GapCount")
	Health = e.npc.getHealth()
	HealthNerfed = round(Health)
	Timer = e.npc.getTempdata().get("Timer")

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

	if IsSlowed != -1 :										# Testing if he finished eating
		if Timer == 2 :
			e.npc.getStoreddata().put("IsEating", False)						# Allow his reach to change from 0 		( UpdatingReach(e) )
			e.npc.addPotionEffect(10, 4, 1, False)						# Adding the 2 regeneration and absorption effects
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
	List = ["NoobTier","CasualTier","CommonTier","GoodTier"]
	if not e.npc.getTempdata().get("SelectedType") in List :
		IsEating = e.npc.getPotionEffect(10)
		if IsEating != 1 :								# Using Gap classic
			Health = e.npc.getHealth()
			HealthNerfed = round(Health)
			LifeLimit = [1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0]
			LimitChoice = random.choice(LifeLimit)
			GapCount = e.npc.getTempdata().get("GapCount")
			if GapCount == None :
				e.npc.getTempdata().put("GapCount", random.randint(8, 17))

			if (LimitChoice == 1) and (HealthNerfed < 17):
				IsUsingGap = e.npc.getTempdata().put("IsUsingGap", 1)

		Health = e.npc.getHealth()
		HealthNerfed = round(Health)
		LifeLimit = [1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0]
		LimitChoice = random.choice(LifeLimit)
		if (LimitChoice == 1) and (HealthNerfed <= 13) and (e.npc.getPotionEffect(2) != 1):								# Using Gap chug
			IsUsingGap = e.npc.getTempdata().put("IsUsingGap", 1)
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
			e.npc.getTempdata().put("GapCount", random.randint(8, 17))

		if (LimitChoice == 1) and (HealthNerfed < 17):
			IsUsingGap = e.npc.getTempdata().put("IsUsingGap", 1)

def UpdatingReach(e):
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
					ReachList = [2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3]
					NewReach = random.choice(ReachList)
					e.npc.getStats().getMelee().setRange(NewReach)

				if SelectedType == "ProTier" :
					ReachList = [2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 4]
					NewReach = random.choice(ReachList)
					e.npc.getStats().getMelee().setRange(NewReach)

				if SelectedType == "UHCEliteTier" :
					ReachList = [2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 4]
					NewReach = random.choice(ReachList)
					e.npc.getStats().getMelee().setRange(NewReach)

				if SelectedType == "NoobTier" :
					ReachList = [2, 2, 2, 2, 1, 1, 1, 1, 1, 1]
					NewReach = random.choice(ReachList)
					e.npc.getStats().getMelee().setRange(NewReach)
	else :
		e.npc.getStats().getMelee().setRange(0)

def MeetUpChecking(e):				
	MeetUp = e.npc.world.getStoreddata().get("MeetUp")
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
	try:
		if ( e.npc.getTempdata().get("WaterUsed") != None ) and (DeletingWater.Ticker == 5) :
			e.npc.executeCommand("/fill "+str(e.npc.getTempdata().get("WaterUsed")[0])+" "+str(e.npc.getTempdata().get("WaterUsed")[1])+" "+str(e.npc.getTempdata().get("WaterUsed")[2])+" "+str(e.npc.getTempdata().get("WaterUsed")[0])+" "+str(e.npc.getTempdata().get("WaterUsed")[1]+1)+" "+str(e.npc.getTempdata().get("WaterUsed")[2])+" minecraft:air")
			e.npc.getTempdata().put("WaterRemaining", e.npc.getTempdata().get("WaterRemaining")+1)
		elif DeletingWater.Ticker == 5 :
			DeletingWater.Ticker = 0
		else :
			DeletingWater.Ticker += 1
	except :
		DeletingWater.Ticker = 0

def BadlionKB(e):
	if e.npc.world.getTempdata().get("BadlionKB") == True :
		e.npc.getStats().setResistance(3, (random.uniform(1.4, 1.8)))


#ON DEATH ONLY functions :

def CountingPlayers(e):
	e.npc.world.getStoreddata().put("Players", e.npc.world.getStoreddata().get("Players")-1)
	if e.npc.world.getStoreddata().get("Players") == 50 :
		e.npc.executeCommand('/tellraw @a ["",{"text":"[","color":"dark_gray"},{"text":"UHC","color":"dark_red"},{"text":"] ","color":"dark_gray"},{"text":"[","color": gray,"bold":true},{"text":"Players","color" : dark_green},{"text":"] ","color": gray,"bold":true},{ "text" :"There is 50 players alive !","color" : aqua,"bold":true}]')
	if e.npc.world.getStoreddata().get("Players") == 25 :
		e.npc.executeCommand('/tellraw @a ["",{"text":"[","color":"dark_gray"},{"text":"UHC","color":"dark_red"},{"text":"] ","color":"dark_gray"},{"text":"[","color": gray,"bold":true},{"text":"Players","color" : dark_green},{"text":"] ","color": gray,"bold":true},{ "text" :"There is 25 players alive !","color" : aqua,"bold":true}]')
	if e.npc.world.getStoreddata().get("Players") == 10 :
		e.npc.executeCommand('/tellraw @a ["",{"text":"[","color":"dark_gray"},{"text":"UHC","color":"dark_red"},{"text":"] ","color":"dark_gray"},{"text":"[","color": gray,"bold":true},{"text":"Players","color" : dark_green},{"text":"] ","color": gray,"bold":true},{ "text" :"There is 10 players alive !","color" : aqua,"bold":true}]')
	if e.npc.world.getStoreddata().get("Players") == 3 :
		e.npc.executeCommand('/tellraw @a ["",{"text":"[","color":"dark_gray"},{"text":"UHC","color":"dark_red"},{"text":"] ","color":"dark_gray"},{"text":"[","color": gray,"bold":true},{"text":"Players","color" : dark_green},{"text":"] ","color": gray,"bold":true},{ "text" :"There is 3 last players alive !","color" : aqua,"bold":true}]')
	if e.npc.world.getStoreddata().get("Players") == 1 or e.npc.world.getStoreddata().get("TeamsAlive") == 0.0 :
		e.npc.executeCommand('/tellraw @a ["",{"text":"[","color":"dark_gray"},{"text":"UHC","color":"dark_red"},{"text":"] ","color":"dark_gray"},{"text":"[","color": gray,"bold":true},{"text":"Players","color" : dark_green},{"text":"] ","color": gray,"bold":true},{ "text" :"We now have a winner ! Congratulation !","color" : aqua,"bold":true}]')


def ScoreBoardUpdateVI(e):
	try :
		RedditUHCDisplay = e.npc.world.getTempdata().get("RedditUHCDisplay")
		if RedditUHCDisplay == True :
			e.npc.executeCommand('/scoreboard players remove Players Kills 1')
	except:
		pass

def CountingKills(e):
	MyKills = e.npc.getStoreddata().get("Kills")
	if MyKills == None:
		MyKills = 0

	KillList = e.npc.world.getStoreddata().get("KillList")
	NewList = ("//" + e.npc.getDisplay().getName())+ '|' +(str(MyKills))
	if KillList == None :
		e.npc.world.getStoreddata().put("KillList", NewList)

	else:
		KillList = e.npc.world.getStoreddata().get("KillList")
		NewList = ("//" + e.npc.getDisplay().getName())+ '|' +(str(MyKills))
		OldList = ("//" + e.npc.getDisplay().getName())+ '|' +(str(MyKills-1))
		if OldList in KillList :
			KillList = KillList.replace(str("//" + e.npc.getDisplay().getName())+ '|' +(str(MyKills-1)), str(NewList))
			e.npc.world.getStoreddata().put("KillList", KillList)
		else:
			NewList = ("//" + e.npc.getDisplay().getName())+ '|' +(str(MyKills))
			e.npc.world.getStoreddata().put("KillList", KillList+NewList)

	
def CountingPlayersOnKill(e):
	if e.npc.world.getStoreddata().get("TeamsAlive") == 1 :
		e.npc.executeCommand('/tellraw @a ["",{"text":"[","color":"dark_gray"},{"text":"UHC","color":"dark_red"},{"text":"] ","color":"dark_gray"},{"text":"[","color": gray,"bold":true},{"text":"Players","color" : dark_green},{"text":"] ","color": gray,"bold":true},{ "text" :"We now have a winner ! Congratulation !","color" : aqua,"bold":true}]')

	

def TeamReduction(e):
	try :
		TeamID = e.npc.getFaction().getId()
		e.npc.world.getStoreddata().put(str(TeamID), e.npc.world.getStoreddata().get(str(TeamID))-1)
		if (e.npc.world.getStoreddata().get(str(TeamID))) <= 0 :
			e.npc.executeCommand('/tellraw @a ["",{"text":"[","color":"dark_gray"},{"text":"UHC","color":"dark_red"},{"text":"] ","color":"dark_gray"},{"text":" Team ","color":"gray"},{"text":"'+str(TeamID)+', is now eliminated","color":"red"}]')
			Factions = e.npc.world.getStoreddata().get("Factions")
			Factions = Factions.split("/")
			Factions.append(str(TeamID))
			Factions = "/".join(Factions)
			e.npc.world.getStoreddata().put("Factions", Factions)
			e.npc.world.getStoreddata().put("TeamsAlive", e.npc.world.getStoreddata().get("TeamsAlive")-1)
			e.npc.world.getTempdata().put(str(TeamID)+"Team", None)						# For the LoadTeam thingy
	except:
		pass

def ScoreBoardUpdateII(e):
	Name = e.npc.getDisplay().getName()
	e.npc.executeCommand('/scoreboard players reset '+str(Name)+'')

def ScoreBoardUpdateIV(e):
	Name = e.npc.getDisplay().getName()
	e.npc.executeCommand('/scoreboard teams leave')

def ScoreBoardUpdateV(e):
	try :
		RedditUHCDisplay = e.npc.world.getTempdata().get("RedditUHCDisplay")
		if RedditUHCDisplay == True :
			Name = e.source.getName()
			e.npc.executeCommand('/scoreboard players add '+str(Name)+' Kills 1')
	except:
		pass

def NoRespawn(e):
	if e.npc.getTempdata().get("Respawn") == 2 :
		e.npc.despawn()
	elif (e.npc.getTempdata().get("Respawn") == 1) or (e.npc.getTempdata().get("Respawn") == 0) :
		e.npc.getTempdata().put("Respawn", e.npc.getTempdata().get("Respawn")+1)


		

#POST GAME functions :

def EndGame(e):
	try :
		PlayerList = e.npc.world.getAllPlayers()
		for i in range (0, len(PlayerList)):
			NewList = (("//" + PlayerList[i].getName())+ '|' +str(e.npc.world.getStoreddata().get(str(PlayerList[i].getName()) +"Kills")))
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
	e.npc.world.spawnClone(13, 203, 0, 2, "Host UHC")


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
    Around = e.npc.world.getNearbyEntities(int(e.npc.getX()), int(e.npc.getY()), int(e.npc.getZ()), 8, 2).tolist()
    if 2*3 <= len(Around) :
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
	List = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1]
	if random.choice(List) == 1 :
		e.npc.getStats().getMelee().setStrength(e.npc.getStats().getMelee().getStrength()+3)


def AntiGapHit(e):
	if e.npc.getPotionEffect(2) == 0 :
		e.setCanceled(True)


#Classes :

class N91data() :
    def getPlayers(self, e):
        PlayersLeft = e.npc.world.getStoreddata().get("Players")
        return PlayersLeft
    def getKills(self, e):
        Kills = e.npc.getStoreddata().get("Kills")
        return Kills
    def getTeam(self, e):
		try :
			TeamID = e.npc.getFaction().getId()
			PlayerList = e.npc.world.getStoreddata().get("PlayerList")
			PlayerList = PlayerList.split("//")
			CutedList = []
			TeamList = []
			for i in range (0, len(PlayerList)-1):
				CutedList.append(PlayerList[i].split("/"))
			for i in range (0, len(CutedList)-1):
				if CutedList[i][1] == str(TeamID) :
					TeamList.append(CutedList[i][0])
			#color, underlined, italic
			FactionArgList = [["green","false","false"],["green","true","false"],["green","true","true"],["red","false","false"],["red","true","false"],["red","true","true"],["blue","false","false"],["blue","true","false"],["blue","true","true"],["yellow","false","false"],["yellow","true","false"],["yellow","true","true"],["gold","false","false"],["gold","true","false"],["gold","true","true"]]
			#ID, members, color
			return TeamList
		except :
			pass
    def getLevel(self, e):
		Name = e.npc.getDisplay().getName()
		NoobTier = ["MaxEstLa","Ply1","SiSenioritasse","youngplayerz855","goldogrin556","Puncture_","Galtarr","MATISSE","xKyukoAlt","selfdestruction999","EauDeDakin","LesBotsDeN91","Farmerman","CustomNPCIsProcessing","xX_PvpIziNoHack_Xx","sunBurst","SomeEterionsShots","Powered__","m__y__t__h_IsBack"]
		RandomTier = ["Maksyme","WoXys","KitaraL","Holy_Mister","BiscuitGames29","ISpiderManI","KeriiX","Skyippy","MrVince28","_Slyder73_","xdeoss","Luzord12","Freyxhan","P_Y_R_E_W","pvnx","Scolaris_87X","xX_EndeuhrIsBac_Xx","talentedGinger17","RBRBRBRRRBR","BoltTheMan","AILLErox","BearGrunt","Yoxhni","LPF_SkyZoX","LPF_Talented","LPF_GetingOverMe","ImBackToHack","m___y___t___h","UnaltDePro","UnNainDomptable","Genius_","Enobaria","Gaipo","Guil","lxgende_","ImGOD","EkS_Dragon","EkS_Remontada","EkS_YqhnGOD","EkS_FreeKill","ZZikray","UnLavabo"]
		GoodTier = ["NNeko","Gamur","ThozFR","Bichard","Restrict_","Thunder_","ZauSFR","M4NTIC","Dieu_Ekoo","80Alpha","Jerfox_Airlines","Skymarinette","Azahelia","LovinCofee","DarknessAngel","MEE6","anzil","EvoRay","SkyZen","Jhinou","Elfy","Biche_","Oraclette","Mizuki_Okami","Dwino_Onii","PecSon","TitBiscuit","Banano","KidiZoom","MathoX","Skilldus","PromisjTryHard","Aykinz","FAKOMA","Frodo_","Bayko13","Mercuroh","ItsHxppy","Mqwed","iKowz","Baker_r","bisharp_p","Rev_an","Xygna","iSwey","Luministe","Captureee","doyouevenbanter","Niware","Adhes","RoiMars","nemenems","Daiko","ItsIno","Sheyk_","KazyIsBack","Astrotro","AuRon011","Wispexe"]
		ProTier = ["Guep","TheGuill84","Libe_","Restump","jdgoederen","Etoiles","xNestorio","Bea4st","SuperBxllamy","gogos_111","GRQ_","Nannoxx","Strykerss","BYSLIDE","MASTEEKH","iT0uch","D4anteh","Jaguar_EL","GrayLight","GregMasterFlash","CedGhoss","Nardcoo"]
		if Name in NoobTier :
			Level = Noob
		elif Name in RandomTier :
			Level = Random
		elif Name in GoodTier :
			Level = Good
		elif Name in Protier :
			Level = Pro
		return Level
    def getHeal(self):
        GapCount = e.npc.getTempdata().get("GapCount")
        return int(GapCount)
    def getFireAspect(self):
        IsFire = e.npc.getInventory().getRightHand().hasEnchant(20)
        if IsFire == True:
            return True
        else :
            return False


#================================#
#_______{ Calling Events }_______#
#================================#


def init(e):
	GameStarted = e.npc.world.getTempdata().get("GameStarted")
	if GameStarted == 1:
		if e.npc.world.getTempdata().get("LoadTeams") != True :
			SettingEntity(e)
		else:
			SettingEntityForced(e)
		SettingArmor(e)
		SettingResistance(e)
		SettingInitialKills(e)
		SuperHeroes(e)
		MasterLevel(e)
		DoubleHealth(e)
		CatEyes(e)
		OneShot(e)
		RodlessActivation(e)
		MoleReveal(e)
		UpdatingReach(e)
		
		
def damaged(e):
	AntiGapHit(e)
	e.npc.world.getTempdata().put("GameRunning", 1)
	SwordDebug(e)
	SettingResistance(e)
	LifeMessageBow(e)
	UpdatingReach(e)
	MoleReveal(e)
	BadlionKB(e)
	AntiFreeDeath(e)
	AbsoLess(e)

def meleeAttack(e):
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
	#CountingPlayersOnKill(e)
	KillingPlayer(e)
	UpdateAggro(e)

def died(e):
	CountingPlayers(e)
	InventorySpawn.isDone = False		# To spawn a full inv if he had kills ( more armor and blocks)
	e.npc.getTempdata().put("Respawn", 0) 			# To avoid glitched respawn, which will make the player counter false
	ThunderStrike(e)
	ScoreBoardUpdateII(e)
	BadlionDeathTchatMessage(e)
	DeathTchatMessage(e)
	ScoreBoardUpdateIV(e)
	IronGolemSound(e)
	WitherSoundI(e)
	WitherSoundII(e)
	NoCleanUpActivation(e)
	BookCeption(e)
	ScoreBoardUpdateV(e)
	HeadPost(e)
	VanillaDeathStyle(e)
	TeamReduction(e)
	ExplodeOnDeath(e)
	ScoreBoardUpdateVI(e)
	
def tick(e):
	GameStarted = e.npc.world.getTempdata().get("GameStarted")
	if GameStarted == 1:
		if e.npc.getAi().getRetaliateType() == 3:
			GoToZone(e, int(e.npc.getStoreddata().get("GoTozone")),"Ext")
		BorderShrink(e)
		SettingEntityForced(e)
		CancelFire(e)
		NoRespawn(e)
		MoleReveal(e)
		ActualisingTeamMembers(e)
		MeetUpChecking(e)
		HealthDisplay(e)
		BadlionKB(e)
		WantToGap(e)
		UsingGap(e)
		Strafing(e)
		DeletingWater(e)
		WeatherClear(e)
		WantToRod(e)
		Rod(e)
		#LastSending(e)
		try:
			e.npc.getTempdata().put("RunOn", e.npc.getTempdata().get("RunOn")-1 )
		except:
			e.npc.getTempdata().put("RunOn", 0)


def interact(e):
	GappleSharing(e)
	#e.npc.getTempdata().put("SelectedType", "UHCEliteTier")
	#e.npc.world.getStoreddata().put("Players", e.npc.world.getStoreddata().get("Players")+1)
	e.setCanceled(True)
	
def target(e):
	#Targeting(e)
	pass



    #============================#
    #___{ Credits and thanks }___#
    #============================#

#   Thanks to noppes for creating the CustomNPC mod
#   and to every people of the CustomNPC discord server
#   for helping me with commands and creating scripts



