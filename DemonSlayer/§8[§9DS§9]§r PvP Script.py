import random
import math

#API Link :http://www.kodevelopment.nl/customnpcs/api/1.8.9/
#Desc : Demon slayer UHC PvP script by Natsu91

#===================================#
#_______{ Creating Algorithm }______#
#===================================#



#DEATH STYLE functions :
											





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

def StuffUpgradeOnKill(e) :
	'''Update armor and sword tier, and enchant levels like if he anvil-ed the stuff he looted on his kill
	'''
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
				ProjList[0] = KillProj[0]
				ProtList[0] = KillProt[0]
				ArmorList = ArmorList.replace("4", "1")
			else :
				ArmorList = ArmorList.replace("4", "0")
		else:
			ArmorList = ArmorList.replace("4", "1")

		if (e.npc.getInventory().getArmor(1).getDisplayName() == "Iron Chestplate"): 
			if (KillStuff[1] == "1"):
				e.npc.getInventory().setArmor(1,e.npc.world.createItem("minecraft:diamond_chestplate",0,1))
				ProjList[1] = KillProj[1]
				ProtList[1] = KillProt[1]
				ArmorList = ArmorList.replace("5", "1")
			else :
				ArmorList = ArmorList.replace("5", "0")
		else:
			ArmorList = ArmorList.replace("5", "1")

		if (e.npc.getInventory().getArmor(2).getDisplayName() == "Iron Leggings"):
			if (KillStuff[2] == "1"):
				e.npc.getInventory().setArmor(2,e.npc.world.createItem("minecraft:diamond_leggings",0,1))
				ProjList[2] = KillProj[2]
				ProtList[2] = KillProt[2]
				ArmorList = ArmorList.replace("6", "1")
			else :
				ArmorList = ArmorList.replace("6", "0")
		else :
			ArmorList = ArmorList.replace("6", "1")

		if (e.npc.getInventory().getArmor(3).getDisplayName() == "Iron Boots"):
			if (KillStuff[3] == "1"):
				e.npc.getInventory().setArmor(3,e.npc.world.createItem("minecraft:diamond_boots",0,1))
				ProjList[3] = KillProj[3]
				ProtList[3] = KillProt[3]
				e.npc.getStoreddata().put("Proj", KillProj[3])
				ArmorList = ArmorList.replace("7", "1")
			else :
				ArmorList = ArmorList.replace("7", "0")
		else:
			ArmorList = ArmorList.replace("7", "1")

		AnvilTicks = e.npc.world.getTempdata().get("AnvilTicks")
		if AnvilTicks == None:
			AnvilTicks = 2
		for j in range (0, AnvilTicks):
			i = random.randint(0, 4)
			if (int(KillProt[i]) == int(MyProt[i])) and (int(MyProt[i]) != 4):				#Anvil stuff
				MyProt.pop(i)
				MyProt.insert(i, str(int(KillProt[i])+1))
			elif int(KillProt[i]) > int(MyProt[i]) :				# Taking better stuff
				MyProt.pop(i)
				MyProt.insert(i, str(KillProt[i]))

		
		if (int(KillSword[0])) > int(Sword[0]) :
			Sword.pop(0)
			Sword.insert(0, str(KillSword[0]))
		
		i = random.randint(0, 2)
		if (i == 2) and (AnvilTicks != 0):
			if (int(KillSword[0]) == int(Sword[0])) and (int(Sword[0]) != 5):
				Sword.pop(0)
				Sword.insert(0, str(int(KillSword[0])+1))

		if int(KillSword[1]) != 0 :
			Sword.pop(1)
			Sword.insert(1, "1")
	
		ArmorList = ArmorList.replace("4", "0")
		ArmorList = ArmorList.replace("5", "0")
		ArmorList = ArmorList.replace("6", "0")
		ArmorList = ArmorList.replace("7", "0")

		
		ProtList = "/".join(MyProt)
		ProjList = "/".join(MyProj)
		SwordList = "/".join(Sword)
		
		e.npc.getStoreddata().put("Prot", ProtList)
		e.npc.getStoreddata().put("Proj", ProjList)
		e.npc.getStoreddata().put("Armor", ArmorList)
		e.npc.getStoreddata().put("Sword", SwordList)
		Gap = e.npc.getTempdata().get("GapCount")
		if Gap != None :
			try:
				Gap += e.entity.getTempdata().get("GapCount")
				if e.entity.getTempdata().get("GapCount") == 0:
					Gap += 1
				Gap += int(round(e.npc.world.getTempdata().get("GapAtKill")))
			except:
				Gap += 6
			if Gap >= 220 :
				Gap = 220
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
		Gap = e.npc.getTempdata().get("GapCount")
		if Gap != None :
			try:
				Gap += e.entity.getTempdata().get("GapCount")
				if e.entity.getTempdata().get("GapCount") == 0:
					Gap += 1
				Gap += int(round(e.npc.world.getTempdata().get("GapAtKill")))
			except:
				Gap += int(round(e.npc.world.getTempdata().get("GapAtKill")))
			if Gap >= 220 :
				Gap = 220
			e.npc.getTempdata().put("GapCount", Gap)
		else :
			e.npc.getTempdata().put("GapCount", 8)

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

def SuperHeroes(e):
	'''Give a random effect to the bot, choosing between :
		- Resistance II
		- Speed I
		- Strength I
		- Double Health
		- Jump Boost IV
	'''
	SheroesOn = e.npc.world.getTempdata().get("SuperHeroes")
	if e.npc.getStoreddata().get("HasPower") != 1 :
		PowerList = random.randint(1, 5)
		if SheroesOn == True :
			if PowerList == 1 :					# Resistance II
				e.npc.addPotionEffect(11, 100000, 1, True)
			elif PowerList == 2 :					# Speed I
				e.npc.addPotionEffect(1, 100000, 0, True)
			elif PowerList == 3 :					# Stength I
				e.npc.addPotionEffect(5, 100000, 0, True)
			elif PowerList == 4 :					# Health Boost
				e.npc.addPotionEffect(21, 100000, 4, True)
			elif PowerList == 5 :					# Jump Boost
				e.npc.addPotionEffect(8, 100000, 3, True)
				e.npc.addPotionEffect(12, 100000, 0, True)
			e.npc.getStoreddata().put("HasPower", 1)

def DoubleHealth(e):
	'''Add 10 max hearths to the bot
	'''
	DoubleHealth = e.npc.world.getTempdata().get("DoubleHealth")
	if DoubleHealth == True :
		e.npc.getStats().setMaxHealth(40)
		e.npc.setHealth(40)

def OneShot(e):
	'''Set bot HP to 1 with no healing
	'''
	OneShot = e.npc.world.getTempdata().get("OneShot")
	if OneShot == True :
		e.npc.setHealth(1)
		e.npc.getStats().setMaxHealth(1)
		e.npc.getTempdata().put("GapCount", 0)
	
def NoCleanUpActivation(e) :
	'''Instantly give the configured amount of HP to the killer
	'''
	try:
		NoCleanScenario = e.npc.world.getTempdata().get("NoCleanUpEnabled")
		if (NoCleanScenario == True) and (e.source.getHealth() > 0):
			NoCleanConfig = e.npc.world.getTempdata().get("NoCleanRegen")
			KillerHP1 = e.source.getHealth()
			KillerHP = round(KillerHP1)
			NoClean = KillerHP ++ NoCleanConfig
			e.source.setHealth(float(NoClean))
	except:
		pass




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
		if (GameStarted == 1) and ((Name == "Disabled") or (Name == "-") or (Name == "") or (Name == "None") or (Name == " ")):

			ChoosingList = ["NoobTier","CasualTier","CommonTier","CommonTier","GoodTier","GoodTier","GoodTier","ProTier","UHCEliteTier"]

			if len(e.npc.world.getTempdata().get("NameTier"+str("NoobTier"))) == 0 :
				ChoosingList.remove("NoobTier")
			if len(e.npc.world.getTempdata().get("NameTier"+str("CasualTier"))) == 0:
				ChoosingList.remove("CasualTier")
			if len(e.npc.world.getTempdata().get("NameTier"+str("CommonTier"))) == 0:
				ChoosingList.remove("CommonTier")
				ChoosingList.remove("CommonTier")
			if len(e.npc.world.getTempdata().get("NameTier"+str("GoodTier"))) == 0:
				ChoosingList.remove("GoodTier")
				ChoosingList.remove("GoodTier")
				ChoosingList.remove("GoodTier")
			if len(e.npc.world.getTempdata().get("NameTier"+str("ProTier"))) == 0:
				ChoosingList.remove("ProTier")
			if len(e.npc.world.getTempdata().get("NameTier"+str("UHCEliteTier"))) == 0:
				ChoosingList.remove("UHCEliteTier")

			Level = random.choice(ChoosingList)
				
			if (e.npc.world.getTempdata().get("ForcedType") == True) and (len(e.npc.world.getTempdata().get("NameTier"+str("UHCEliteTier"))) != 0 ):
				Level = "UHCEliteTier" 



			e.npc.getTempdata().put("SelectedType", Level)
			SelectedName = random.choice(e.npc.world.getTempdata().get("NameTier"+str(Level)))
			AllowedList = ["_"]
			if not SelectedName in e.npc.world.getTempdata().get("AlreadyTaken") :
				NameList = e.npc.world.getTempdata().get("NameTier"+str(Level))
				NameList.remove(SelectedName)
				e.npc.world.getTempdata().put("NameTier"+str(Level),NameList)

				if Level in ["NoobTier","CasualTier","CommonTier","GoodTier"] :
					Random = random.randint(1, 71)
					SelectedName = list(SelectedName)

					try:
						SelectedName2.split("/")
						e.npc.getDisplay().setCapeTexture('minecraft:textures/cloak/'+str(SelectedName2[1])+'.png')
						SelectedName = SelectedName2[0]
					except:
						pass

					for i in range(0, len(SelectedName)):
						if (SelectedName[i].isalnum() == True) or (SelectedName[i] in AllowedList):
							pass
						else:
							SelectedName.pop(i)

					try:
						SelectedName2 = SelectedName.split("/")
						e.npc.getDisplay().setCapeTexture('minecraft:textures/cloak/'+str(SelectedName2[1])+'.png')
						SelectedName = SelectedName2[0]
					except:
						pass

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
					RandomCape = random.randint(1, 47)
					e.npc.getDisplay().setCapeTexture('minecraft:textures/cloak/'+str(RandomCape)+'.png')

				if e.npc.world.getTempdata().get("ScatterMessageEnabled") == True :
					e.npc.executeCommand('/tellraw @a ["",{"text":"DemonSlayer |","color":"red"},{"text":"Scatter","color":"blue"},{"text":"] ","color":"gold"},{"text":"Scattered ","color":"dark_red"},{"text":"'+str(SelectedName)+'","color":"gray"}]')
				else :
					pass
			else:
				pass
	except Exception as err:
		#e.npc.world.broadcast(str(err))
		e.npc.world.getStoreddata().put("Players", e.npc.world.getStoreddata().get("Players")-1)
		e.npc.despawn()

def MeetUpArmor(e):
	"""
	Initialize the bot armor display + enchants in meetups
	"""
	if (e.npc.getInventory().getArmor(0) == None) and (e.npc.world.getTempdata().get("MeetUpMode") == True):
		Sword = e.npc.world.getTempdata().get("ForcedSword")
		Helm = e.npc.world.getTempdata().get("ForcedHelm")
		Chest = e.npc.world.getTempdata().get("ForcedChest")
		Legg = e.npc.world.getTempdata().get("ForcedLegg")
		Boots = e.npc.world.getTempdata().get("ForcedBoots")

		HelmProt = e.npc.world.getTempdata().get("HelmProt")
		ChestProt = e.npc.world.getTempdata().get("ChestProt")
		LeggProt = e.npc.world.getTempdata().get("LeggProt")
		BootsProt = e.npc.world.getTempdata().get("BootsProt")

		HelmProj = e.npc.world.getTempdata().get("HelmProj")
		ChestProj = e.npc.world.getTempdata().get("ChestProj")
		LeggProj = e.npc.world.getTempdata().get("LeggProj")
		BootsProj = e.npc.world.getTempdata().get("BootsProj")

		SwordSharp = e.npc.world.getTempdata().get("SwordSharp")
		StartGap = e.npc.world.getTempdata().get("ForcedGap")

		ProtList = []			# The protection enchant list
		ProjList = []			# The projectile protection enchant list
		ArmorList = []			# The Armor material list
		BowList = ["0","0","0","0"]			# The bow enchant list
		SwordList = []			# The sword enchant list

		List = [Helm, Chest, Legg, Boots]
		EnchProtList = [HelmProt, ChestProt, LeggProt, BootsProt]
		EnchProjList = [HelmProj, ChestProj, LeggProj, BootsProj]
		PartList = ["_helmet","_chestplate","_leggings","_boots"]
		for i in range(0,4):
			if e.npc.getInventory().getArmor(i) == None :
				if List[i] == True :										# Random between 1 - 100 to know if it is a diamond piece or a iron piece
					e.npc.getInventory().setArmor(i,e.npc.world.createItem("minecraft:diamond"+str(PartList[i]),0,1))
					ArmorList.append("1")
				else :
					e.npc.getInventory().setArmor(i,e.npc.world.createItem("minecraft:iron"+str(PartList[i]),0,1))
					ArmorList.append("0")

				if EnchProtList[i] != 0 :
					ProtList.append(str(int(round(EnchProtList[i]))))
				else:
					ProtList.append("0")

				if EnchProjList[i] != 0 :
					ProjList.append(str(int(round(EnchProjList[i]))))
				else :
					ProjList.append("0")

		if Sword == True:
			e.npc.getInventory().setRightHand(e.npc.world.createItem("minecraft:diamond_sword",0,1))
		else:
			e.npc.getInventory().setRightHand(e.npc.world.createItem("minecraft:iron_sword",0,1))

		SwordList.append(str(int(round(SwordSharp))))
		SwordList.append("0")
		SwordList.append("0")
		SwordList.append("0")


		if e.npc.getTempdata().get("GapCount") == None:
			e.npc.getTempdata().put("GapCount", int(round(StartGap)))


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
		e.npc.getTempdata().put("DeathTimer", None)

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
			ProjEffect = int(Proj[0]) * 0.02
			MeleeResToSet += 0.12
			ProjToSet += 0.15 + ProjEffect
		else :
			ProjEffect = int(Proj[0]) * 0.02
			MeleeResToSet += 0.08 
			ProjToSet += 0.1 + ProjEffect
		

		if int(Armor[1]) == 1 :							# Diamond Chestplate
			ProjEffect = int(Proj[1]) * 0.02
			MeleeResToSet += 0.32 
			ProjToSet += 0.3 + ProjEffect
		else :
			ProjEffect = int(Proj[1]) * 0.01
			MeleeResToSet += 0.24
			ProjToSet += 0.2 + ProjEffect


		if int(Armor[2]) == 1 :							# Diamond Leggings
			ProjEffect = int(Proj[2]) * 0.02
			MeleeResToSet += 0.24
			ProjToSet += 0.15 + ProjEffect
		else :
			ProjEffect = int(Proj[2]) * 0.01
			MeleeResToSet += 0.20
			ProjToSet += 0.2 + ProjEffect


		if int(Armor[3]) == 1 :							# Diamond Boots
			ProjEffect = int(Proj[3]) * 0.02
			MeleeResToSet += 0.12
			ProjToSet += 0.15 + ProjEffect
		else :
			ProjEffect = int(Proj[3]) * 0.01
			MeleeResToSet += 0.08
			ProjToSet += 0.1 + ProjEffect


		#Now affecting the protection enchantment
		PercentLeft = 1-MeleeResToSet
		if e.npc.getTempdata().get("SelectedType") == "UHCEliteTier" :
			MeleeResToSet += (PercentLeft*((int(Prot[0])+int(Prot[1])+int(Prot[2])+int(Prot[3]))*5))/100
		else:
			MeleeResToSet += (PercentLeft*((int(Prot[0])+int(Prot[1])+int(Prot[2])+int(Prot[3]))*4))/100


		MeleeResToSet += 1
		ProjToSet += 1

		if MeleeResToSet >= 1.96 :
			MeleeResToSet = 1.96

		e.npc.getStats().setResistance(0, (MeleeResToSet))
		e.npc.getStats().setResistance(1, (ProjToSet))
		try :
			e.npc.getInventory().getRightHand().getName()
		except:
			e.npc.getInventory().setRightHand(e.npc.world.createItem("minecraft:diamond_sword",0,1))
			
		if e.npc.getInventory().getRightHand().getName() == "minecraft:diamond_sword" :	# Diamond sword
			SwordEffect = int(Sword[0]) * 1.5
			DamageToSet = 7 + int(SwordEffect)
		else :													# iron Sword
			SwordEffect = int(Sword[0]) * 1.5
			DamageToSet = 6 + int(SwordEffect)

		e.npc.getStats().getMelee().setStrength(DamageToSet)
		
	else :
		e.npc.getStats().setResistance(0, -1)
		e.npc.getStats().setResistance(1, -1)
		e.npc.getStats().setResistance(2, 1.8)
		e.npc.getStats().getMelee().setStrength(100)

def SettingEntityForced(e):
	"""
	Same as SettingEntity(e) but with a already choosen name, contained in the teams.txt file
	"""
	try:
		GameStarted = e.npc.world.getTempdata().get("GameStarted")
		Name = e.npc.getDisplay().getName()		
		if ((GameStarted == 1) and ((Name == "Disabled"))) or ((e.npc.getDisplay().getName() == "Disabled") and (e.npc.world.getTempdata().get("26Team")) != str("None") and (e.npc.getFaction().getId() == 26)):
			TeamListHere = e.npc.getTempdata().get("NewName")
			NameNow = str(TeamListHere)
			NameHere = [e.npc.world.getTempdata().get(str(int(e.npc.getFaction().getId()))+"Team")]

			try:
				SelectedName2 = NameNow.split("/")
				e.npc.getDisplay().setCapeTexture('minecraft:textures/cloak/'+str(SelectedName2[1])+'.png')
				NameNow = SelectedName2[0]
			except:
				pass


			if (NameNow == '') and (e.npc.getFaction().getId() == 26):
				e.npc.despawn()
			if ((NameNow != "Disabled") and (NameNow != "-")):
				e.npc.getDisplay().setName(str(NameNow))

				GlobalNamesList = e.npc.world.getTempdata().get("ListOfTakenNames")						#Prevent duplicated players
				if GlobalNamesList != None:
					GlobalNamesList.append(str(NameNow))
				else:
					GlobalNamesList = [str(NameNow),""]

				e.npc.world.getTempdata().put("ListOfTakenNames", GlobalNamesList)

				if NameNow in e.npc.world.getTempdata().get("NameTier"+str("NoobTier")):
					Level = "NoobTier"
				elif NameNow in e.npc.world.getTempdata().get("NameTier"+str("CasualTier")):
					Level = "CasualTier"
				elif NameNow in e.npc.world.getTempdata().get("NameTier"+str("CommonTier")):
					Level = "CommonTier"
				elif NameNow in e.npc.world.getTempdata().get("NameTier"+str("GoodTier")):
					Level = "GoodTier"
				elif NameNow in e.npc.world.getTempdata().get("NameTier"+str("ProTier")):
					Level = "ProTier"
				elif NameNow in e.npc.world.getTempdata().get("NameTier"+str("UHCEliteTier")):
					Level = "UHCEliteTier"

				else:
					Level = "CommonTier"

				NameList = e.npc.world.getTempdata().get("NameTier"+str(Level))
				try:
					NameList.remove(NameNow)
				except:
					pass
				e.npc.world.getTempdata().put("NameTier"+str(Level),NameList)

				e.npc.getTempdata().put("SelectedType", Level)

				if Level in ["NoobTier","CasualTier","CommonTier","GoodTier"] :
					Random = random.randint(1, 71)
					e.npc.getDisplay().setSkinTexture('minecraft:textures/entity/Random'+str(Random)+'.png')

				else :
					e.npc.getDisplay().setSkinTexture('minecraft:textures/entity/'+NameNow+'.png')

				RandomForCape = random.randint(1, 3)
				if RandomForCape == 3:
					RandomCape = random.randint(1, 25)
					e.npc.getDisplay().setCapeTexture('minecraft:textures/cloak/'+str(RandomCape)+'.png')

				if e.npc.world.getTempdata().get("ScatterMessageEnabled") == True :
					e.npc.executeCommand('/tellraw @a ["",{"text":"DemonSlayer |","color":"red"},{"text":"Scatter","color":"blue"},{"text":"] ","color":"gold"},{"text":"Scattered ","color":"dark_red"},{"text":"'+str(SelectedName)+'","color":"gray"}]')
				else :
					pass	
			else:
				SettingEntity(e)
		elif (Name == "-"):
			SettingEntity(e)	
	
	except Exception as err:
		e.npc.say(str(err))
		pass

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

def SettingInitialKills(e):
	"""
	Initialize kills to 0 
	"""
	Kills = e.npc.getStoreddata().get("Kills")
	if Kills == None :
		e.npc.getStoreddata().put("Kills", 0)




#TEAMER BOTS ONLY functions :
		
def KillingPlayer(e):
	"""
	Sending data to the Server bots to display player elimination message
	"""
	try :
		e.npc.world.getTempdata().put(str(e.entity.getName()+"Killer"), [str(e.npc.getDisplay().getName()),str(e.npc.getFaction().getId()),str(e.npc.getStoreddata().get("Kills"))])
	except:
		pass
		


#IN GAME functions :

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


				if (5 <= Hp <= 20) and (random.randint(0, 5) == 0) and (e.npc.getTempdata().get("GapCount") != 0):
					e.npc.getTempdata().put("NeedRod", e.npc.getTempdata().get("NeedRod")+1)

				if (6 <= Dist <= 9) and (random.randint(0, 5) == 0):
					e.npc.getTempdata().put("NeedRod", e.npc.getTempdata().get("NeedRod")+1)

				if (Hp < 7) and (0 <= Dist <= 7) and (random.randint(0, 5) == 0) and (e.npc.getTempdata().get("SelectedType") == "UHCEliteTier"):
					e.npc.getTempdata().put("NeedRod", e.npc.getTempdata().get("NeedRod")+1)

				if (e.npc.getTempdata().get("SelectedType") != "UHCEliteTier") or (e.npc.getTempdata().get("SelectedType") != "ProTier"):
					RodTick = 20
				elif (e.npc.getTempdata().get("SelectedType") == "ProTier"):
					RodTick = 16
				else:
					RodTick = 12
				if random.randint(0, RodTick) == 0 :
					e.npc.getTempdata().put("NeedRod", e.npc.getTempdata().get("NeedRod")+1)
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
				e.npc.executeCommand('/tellraw '+str(Source)+' ["",{"text":"DemonSlayer |","color":"red"},{"text":"Bow","color":"aqua"},{"text":"] ","color":"gold"},{"text":"'+str(Name)+'","color":"red"},{"text":" is now at ","color":"white"},{"text":"'+str(int(round(e.npc.getHealth()))+int(round(e.npc.getStoreddata().get("AbsoDisplay"))))+" "+u'\u2764'+'","color":"dark_red"}]')
				e.npc.executeCommand('/playsound random.successful_hit '+str(Source)+' '+str(X)+' '+str(Y)+' '+str(Z)+' 1 0.5')
		except:
			pass
	except:
		pass
	
def Missing(e):
	'''Make the bot fail a hit sometime depending on his tier
	'''
	SelectedType = e.npc.getTempdata().get("SelectedType")							# Just cancelling the damage event if the Npc fail his hit to simulate an human AIM, better the Npc is, lower his miss chances are.
	if SelectedType == "CasualTier" :
		ReachList = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 3, 3, 3, 3, 1, 1, 1, 1]
		MissChance = random.choice(ReachList)
		if MissChance == 3 :
			e.setCanceled(True)

	if SelectedType == "CommonTier" :
		ReachList = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 3, 3, 3, 1, 1, 1, 1]
		MissChance = random.choice(ReachList)
		if MissChance == 3 :
			e.setCanceled(True)

	if SelectedType == "GoodTier" :
		ReachList = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 3, 3, 1, 1, 1, 1]
		MissChance = random.choice(ReachList)
		if MissChance == 3 :
			e.setCanceled(True)

	if SelectedType == "ProTier" :
		ReachList = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 3, 3, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
		MissChance = random.choice(ReachList)
		if MissChance == 3 :
			e.setCanceled(True)

	if SelectedType == "UHCEliteTier" :
		ReachList = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 3]
		MissChance = random.choice(ReachList)
		if MissChance == 3 :
			e.setCanceled(True)

	if SelectedType == "NoobTier" :
		ReachList = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 3, 3, 3, 3, 3, 1, 1, 1, 1]
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
	if (WaterAllowed == True) and (e.npc.getTempdata().get("WaterUsed") == None) and (1 < e.npc.getHealth()):			# Checking if the npc didnt spawned a water bucket already to avoid spamming water and create lags and annoying fights

		WaterRemaining = e.npc.getTempdata().get("WaterRemaining")

		PosList = [e.npc.getX(), e.npc.getY(), e.npc.getZ()]
		if ( WaterRemaining > 1) and (random.randint(0, 3) == 0):
			e.npc.executeCommand('/setblock ~ ~ ~ minecraft:water')					# Creating 2 water blocks to update the first and make the water flow
			e.npc.executeCommand('/setblock ~ ~ ~+1 minecraft:water 1')
			#WaterRemaining -= 1 Canceled right now
			e.npc.getTempdata().put("WaterRemaining", WaterRemaining)
			e.npc.getTempdata().put("WaterUsed", PosList)						# Saving the coordinates of the water in a Tempdata to clear it later
			DeletingWater.TickerMax = 1

def CancelFire(e):
	'''Make the bot extinguish himself when on fire
	'''
	if e.npc.isBurning() == True :
		if (random.randint(0, 3) == 0) and (e.npc.getTempdata().get("WaterUsed") == None) and (1 < e.npc.getHealth()):
			e.npc.executeCommand('/setblock ~ ~ ~ minecraft:water')					# Creating 2 water blocks to update the first and make the water flow
			e.npc.executeCommand('/setblock ~ ~ ~+1 minecraft:water 1')
			PosList = [e.npc.getX(),e.npc.getY(),e.npc.getZ()]
			e.npc.getTempdata().put("WaterUsed", PosList)
			DeletingWater.TickerMax = 1

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
		if Timer == 2 :
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

	Timer += 1
	e.npc.getTempdata().put("Timer", Timer)

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
                    e.npc.getTempdata().put("GapCount", random.randint(8, 17))

                if (LimitChoice == 1) and (HealthNerfed < 17):
                    IsUsingGap = e.npc.getTempdata().put("IsUsingGap", 1)

            elif (e.npc.getTempdata().get("IsUsingGap") != 1) or (random.randint(0, 3) == 0):
                Health = e.npc.getHealth()
                HealthNerfed = round(Health)
                LifeLimit = [1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0]
                LimitChoice = random.choice(LifeLimit)
                if (LimitChoice == 1) and (HealthNerfed <= 13) and (e.npc.getPotionEffect(2) != 1):								# Using Gap chug
                    e.npc.getTempdata().put("IsUsingGap", 1)
                    e.npc.getStats().setResistance(3, 1.4)
                    if e.npc.getTempdata().get("GapTickRod") == 1 :
                        try:
                            e.npc.getTempdata().put("NeedRod", e.npc.getTempdata().get("NeedRod")+1)
                        except:
                            e.npc.getTempdata().put("NeedRod", 1)
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
	'''Handle reach changes
	'''
	Rodless = e.npc.world.getTempdata().get("Rodless")
	if Rodless != True :	
		SelectedType = e.npc.getTempdata().get("SelectedType")
		if SelectedType == "CasualTier" :
			ReachList = [2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3]
			NewReach = random.choice(ReachList)
			e.npc.getStats().getMelee().setRange(NewReach)

		if SelectedType == "CommonTier" :
			ReachList = [2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 4]
			NewReach = random.choice(ReachList)
			e.npc.getStats().getMelee().setRange(NewReach)

		if SelectedType == "GoodTier" :
			ReachList = [2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 4]
			NewReach = random.choice(ReachList)
			e.npc.getStats().getMelee().setRange(NewReach)

		if SelectedType == "ProTier" :
			ReachList = [2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 4, 4]
			NewReach = random.choice(ReachList)
			e.npc.getStats().getMelee().setRange(NewReach)

		if SelectedType == "UHCEliteTier" :
			ReachList = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 4, 4, 4, 4]
			NewReach = random.choice(ReachList)
			e.npc.getStats().getMelee().setRange(NewReach)

		if SelectedType == "NoobTier" :
			ReachList = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 22]
			NewReach = random.choice(ReachList)
			e.npc.getStats().getMelee().setRange(NewReach)
		
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
		DeletingWater.TickerMax = 1

def BadlionKB(e):
	'''Reduce knockbcak to force melee
	'''
	try:
		e.npc.getStats().setResistance(3, (1 + (abs(int(e.npc.world.getTempdata().get("KBValue")))*0.01)))
	except:
		e.npc.getStats().setResistance(3, 1.18)


#ON DEATH ONLY functions :

def CountingPlayers(e):
	try:
		if e.npc.getFaction().getId() != 26 :
			e.npc.world.getStoreddata().put("Players", int(e.npc.world.getStoreddata().get("Players"))-1)
	except:
		e.npc.world.broadcast("Game already ended !")
		pass

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

#POST GAME functions :


#Misc

def GoToZone(e, Zone, Side):
	if e.npc.world.getTempdata().get("DeathMatchTP") != True :
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

def ChooseZone(e):
	if e.npc.world.getTempdata().get("DeathMatchTP") != True :
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
	else:
		e.npc.getAi().setRetaliateType(0)

def BorderShrink(e):

    if (e.npc.world.getStoreddata().get("FinalBorder") <= e.npc.world.getTotalTime()):
        if e.npc.getStoreddata().get("HasShrunkFinal") == None :
            X = e.npc.getX()
            Z = e.npc.getZ()
            Y = e.npc.getY()
            if (e.npc.getX() >= 45) :
                X = 40
                Y = 95
            elif (-45 >= e.npc.getX()):
                X = -40
                Y = 95

            if (e.npc.getZ() >= 45) :
                Z = 40
                Y = 95
            elif (-45 >= e.npc.getZ()):
                Z = -40
                Y = 95
            
            e.npc.setPosition(X, Y, Z)
            e.npc.getStoreddata().put("HasShrunkFinal", "Done")

    elif (e.npc.world.getStoreddata().get("SecondBorder") <= e.npc.world.getTotalTime()):
        if e.npc.getStoreddata().get("HasShrunkSecond") == None :
            X = e.npc.getX()
            Z = e.npc.getZ()
            Y = e.npc.getY()
            if (e.npc.getX() >= 80) :
                X = 75
                Y = 95
            elif (-80 >= e.npc.getX()):
                X = -75
                Y = 95

            if (e.npc.getZ() >= 80) :
                Z = 75
                Y = 95
            elif (-80 >= e.npc.getZ()):
                Z = -75
                Y = 95
            
            e.npc.setPosition(X, Y, Z)
            e.npc.getStoreddata().put("HasShrunkSecond", "Done")


    elif (e.npc.world.getStoreddata().get("FirstBorder") <= e.npc.world.getTotalTime()):
        if e.npc.getStoreddata().get("HasShrunkFirst") == None :
            X = e.npc.getX()
            Z = e.npc.getZ()
            Y = e.npc.getY()
            if (e.npc.getX() >= 120) :
                X = 115
                Y = 95
            elif (-120 >= e.npc.getX()):
                X = -115
                Y = 95

            if (e.npc.getZ() >= 120) :
                Z = 115
                Y = 95
            elif (-120 >= e.npc.getZ()):
                Z = -115
                Y = 95
            
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

def RodBlock(e):
	List = e.npc.world.getAllPlayers()
	for i in range (0, len(List)):
		try:
			List[i].getMCEntity().field_71104_cf.field_146043_c = None
		except Exception as err:
			pass

def ClearingName(e):
	"""Clear name weird letters"""
	if e.npc.world.getTempdata().get("TeamSize") == 1:
		Name = e.npc.getDisplay().getName()
		Name = list(Name)
		Name.pop(0)
		Name.pop(0)
		Name.pop(-1)
		Name.pop(-1)
		Name = "".join(Name)
		e.npc.getDisplay().setName(str(Name))

def UseLava(e):
	try:
		if (e.npc.world.getTempdata().get("DeathMatchTP") == True):
			Cond1 = True
			Cond2 = (int(e.npc.world.getTempdata().get("Assign"+str(e.npc.getFaction().getId()))) == int(e.npc.getAttackTarget().getFaction().getId()))
		else:
			Cond1 = True
			Cond2 = True

		if (e.npc.getAi().getRetaliateType() == 0) and ((Cond1 == True) and (Cond2 == True)):
			Dist = GetDist(e)
			List = ["NoobTier","CasualTier","GoodTier","CommonTier"]            # List of non lava user
			if not e.npc.getTempdata().get("SelectedType") in List :  
				Target = e.npc.getAttackTarget()
				Y = int(round(Target.getY()))
				MyY = int(round(e.npc.getY()))
				if (Dist <= 5) and (random.randint(0,8) == 2) and (e.npc.getHealth() >= 8) and (e.npc.getTempdata().get("LavaTick") == 0) and (Y-3 <= MyY <= Y+3):
					Target = e.npc.getAttackTarget()
					X = int(round(Target.getX()))
					Y = int(round(Target.getY()))
					Z = int(round(Target.getZ()))
					if (e.npc.world.getBlock(X, Y-1, Z).getName() == "minecraft:air"):
						Y -= 1
					e.npc.world.setBlock(X, Y, Z, "minecraft:lava", 0)
					e.npc.world.setBlock(X, Y, Z+1, "minecraft:lava", 1)
					e.npc.getTempdata().put("LavaTick", 2)
					e.npc.getTempdata().put("LavaCoord", [X, Y, Z])
							

	except Exception as err:
		pass

def RemoveLava(e):
	try:
		if (e.npc.getTempdata().get("LavaTick") == None):
			e.npc.getTempdata().put("LavaTick", 0)

		if (e.npc.getTempdata().get("LavaTick") != 0) and (e.npc.getTempdata().get("LavaTick") != None):
			e.npc.getTempdata().put("LavaTick", e.npc.getTempdata().get("LavaTick")-1)

		elif (e.npc.getTempdata().get("LavaTick") == 0) and (e.npc.getTempdata().get("LavaCoord") != None):
			X = int(e.npc.getTempdata().get("LavaCoord")[0])
			Y = int(e.npc.getTempdata().get("LavaCoord")[1])
			Z = int(e.npc.getTempdata().get("LavaCoord")[2])
			e.npc.world.setBlock(X, Y, Z, "minecraft:air", 0)
			e.npc.world.setBlock(X, Y, Z+1, "minecraft:air", 0)
			e.npc.getTempdata().put("LavaCoord", None)
	except:
		pass

def StopCombo(e):
	try:
		if e.damage >= 1 :
			e.npc.getTempdata().put("ComboTick", 0)
	except:
		pass

def Knocked(e):
	"""
	Prevent reach from being too far if damaged, to make rod tricks possible
	"""
	try:
		if e.npc.getTempdata().get("ReachTick") == None:
			e.npc.getTempdata().put("ReachTick", 0)

		elif e.npc.getTempdata().get("ReachTick") == 4:
			e.npc.getTempdata().put("ReachTick", 0) 

			IsSlowed = e.npc.getPotionEffect(2)
			if IsSlowed != 1 :	
				SelectedType = e.npc.getTempdata().get("SelectedType")

				if SelectedType == "UHCEliteTier" :
					ReachList = [2,3,3,3,3,3,4,4]
					NewReach = random.choice(ReachList)
					e.npc.getStats().getMelee().setRange(NewReach)

				elif SelectedType == "ProTier" :
					ReachList = [2,2,3,3,3,3,3,3]
					NewReach = random.choice(ReachList)
					e.npc.getStats().getMelee().setRange(NewReach)

				elif SelectedType == "GoodTier" :
					ReachList = [2,2,2,2,2,2,3,3]
					NewReach = random.choice(ReachList)
					e.npc.getStats().getMelee().setRange(NewReach)

				else:
					e.npc.getStats().getMelee().setRange(2)
			else :
				e.npc.getStats().getMelee().setRange(0)
		
		else:
			e.npc.getTempdata().put("ReachTick", e.npc.getTempdata().get("ReachTick")+1) 
	except:
		pass

def Combo(e):
	try:
		if e.npc.getTempdata().get("ComboTick") == None:
			e.npc.getTempdata().put("ComboTick", 0)

		elif e.npc.getTempdata().get("ComboTick") == 2:
			e.npc.getTempdata().put("ComboTick", 0) 

			if e.npc.getStats().getMelee().getRange() == 4:
				e.npc.getStats().getMelee().setKnockback(1)
				e.npc.getStats().getMelee().setRange(3)
			else:
				pass

		else:
			e.npc.getTempdata().put("ComboTick", e.npc.getTempdata().get("ComboTick")+1)
			e.npc.getStats().getMelee().setKnockback(0) 
	except:
		pass

def Rod(e):
	'''Throw a snowball as a rod every tick
	'''
	try:
		if (e.npc.world.getTempdata().get("Rodless") != True) and (e.npc.getInventory().getRightHand().getName() != "minecraft:golden_apple"):
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
	except:
		pass

#================================#
#_______{ Calling Events }_______#
#================================#

def init(e):
	GameStarted = e.npc.world.getTempdata().get("GameStarted")
	try:
		e.npc.getTimers().start(2, 0, True)			# The Rod block timer
		e.npc.getTempdata().put("NeedRod", 0)
	except:
		pass

	if GameStarted == 1:
		if e.npc.world.getTempdata().get("LoadTeams") != True :
			SettingEntity(e)
		else:
			SettingEntityForced(e)

		MeetUpArmor(e)
		SettingResistance(e)
		SettingInitialKills(e)
		SuperHeroes(e)
		DoubleHealth(e)
		OneShot(e)
		UpdatingReach(e)		
		
def damaged(e):
	RodBlock(e)
	SettingEntityForced(e)
	SettingEntity(e)
	Clicks(e)
	SwordDebug(e)
	try:
		SettingResistance(e)
	except Exception as err:
		e.npc.world.broadcast(str(err))
	LifeMessageBow(e)
	BadlionKB(e)
	AntiFreeDeath(e)
	AbsoLess(e)
	ActualisingHealth(e)
	Knocked(e)
	StopCombo(e)
	Rod(e)

def meleeAttack(e):
	Combo(e)
	RodBlock(e)
	Clicks(e)
	AntiGapHit(e)
	Crit(e)
	UpdatingReach(e)
	Missing(e)
	BadlionKB(e)
	AbsoLess(e)

def kill(e):
	RodBlock(e)
	BadlionKillsSystem(e)
	try:
		SettingResistance(e)
	except Exception as err:
		e.npc.world.broadcast(str(err))
	StuffUpgradeOnKill(e)
	CountingKills(e)
	KillingPlayer(e)

def died(e):
	try:
		InventorySpawn.isDone = False		# To spawn a full inv if he had kills ( more armor and blocks)
		e.npc.getTempdata().put("Respawn", 0) 			# To avoid glitched respawn, which will make the player counter false
	except:
		pass
	try:
		RodBlock(e)
		CountingPlayers(e)
		ThunderStrike(e)
		IronGolemSound(e)
		WitherSoundI(e)
		WitherSoundII(e)
		NoCleanUpActivation(e)
	except Exception as err:
		e.npc.world.broadcast("Errored at death : "+str(err))

def tick(e):
	GameStarted = e.npc.world.getTempdata().get("GameStarted")
	SettingEntityForced(e)
	if GameStarted == 1:
		if (e.npc.getAi().getRetaliateType() == 3) and (e.npc.world.getTempdata().get("DeathMatchTP") != True):
			GoToZone(e, int(e.npc.getStoreddata().get("GoTozone")),"Ext")
		BorderShrink(e)
		CancelFire(e)
		ActualisingTeamMembers(e)
		WantToGap(e)
		UsingGap(e)
		DeletingWater(e)
		WeatherClear(e)
		WantToRod(e)
		Targeting(e)
		Clicks(e)
		RodBlock(e)
		Rod(e)
		RemoveLava(e)
		UseLava(e)
		try:
			e.npc.getTempdata().put("RunOn", e.npc.getTempdata().get("RunOn")-1 )
		except:
			e.npc.getTempdata().put("RunOn", 0)
	else:
		e.npc.despawn()
		pass

def interact(e):
	e.setCanceled(True)
	
def target(e):
	RodBlock(e)
	UpdatingReach(e)
	Clicks(e)
	SettingEntityForced(e)
	SettingEntity(e)
	Targeting(e)
	pass

def timer(e):			# Rod Block
	RodBlock(e)


    #============================#
    #___{ Credits and thanks }___#
    #============================#

#   Thanks to noppes for creating the CustomNPC mod
#   and to every people of the CustomNPC discord server
#   for helping me with commands and creating scripts

# /tellraw @a ["",{"text":"[","color":"dark_gray"},{"text":"Spec","color":"green"},{"text":"]","color":"dark_gray"},{"text":" ====","color":"dark_purple"},{"text":" / ","color":"dark_gray"},{"text":"====","color":"dark_purple"},{"text":" / ","color":"dark_gray"},{"text":"====","color":"dark_purple"},{"text":" /","color":"dark_gray"},{"text":" ====","color":"dark_purple"},{"text":" / ","color":"dark_gray"},{"text":"=======","color":"light_purple"},{"text":" /","color":"dark_gray"},{"text":" =======","color":"gold"}]
