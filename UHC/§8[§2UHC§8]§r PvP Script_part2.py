import random
import math
#API Link :http://www.kodevelopment.nl/customnpcs/api/1.8.9/
#Credits : Script UHC vs Bots BotPvPSystem By Natsu91

#===================================#
#_______{ Creating Algorithm }______#
#===================================#


#SCENARIOS

def MasterLevel(e):
	'''Give everyone 1000 levels every bot spawn
	'''
	MasterLevelOn = e.npc.world.getTempdata().get("MasterLevel")
	if MasterLevelOn == True:
		e.npc.executeCommand("/xp 1000l @a")

def TimeBomb(e):
	"""
	Summons a chest filled with NPC's inventory

	- Chest not exploding for now
	"""
	IsEnchanted = True
	if e.npc.world.getTempdata().get("TimeBomb") == True:
		e.npc.executeCommand("/fill ~ ~+1 ~+1 ~ ~+1 ~ minecraft:air")			# Spawning a chest at death coordinates
		e.npc.executeCommand("/fill ~ ~ ~+1 ~ ~ ~ minecraft:chest")
		e.npc.executeCommand("/playsound random.levelup @a ~ ~ ~")			# Just a sound
		e.npc.executeCommand("/xp 40 "+ str(e.source.getName()))		# Looting xp
		TimeBombList = e.npc.world.getTempdata().get("TimeBombList")
		X = e.npc.getX()												# Saving coordinates
		Y = e.npc.getY()
		Z = e.npc.getZ()
		SwitchedCoord = False
		TimeBombTimer = int(round(e.npc.world.getTempdata().get("TimeBombTime")))
		TimeBombList.append([int(round(X)),int(round(Y)),int(round(Z)),TimeBombTimer])
		e.npc.world.getTempdata().put("TimeBombList", TimeBombList)
		SlotCounter = 0
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

			Item = ItemList[i]
			# Damaging items to make it feeling real
			if (int(e.npc.world.getStoreddata().get("TeamsAlive")) > 20 ):
				Damage = random.randint(10, 250)
			else:
				Damage = random.randint(10, 120)

			if (int(Prot[i]) == 0) and (int(Proj[i]) == 0):
				IsEnchanted = False
			
			Count = 1
			Tag = '{ench:[{id:'+str(EnchID)+',lvl:'+str(EnchLvL)+'}]}'		# Compilating everithing into a tag, then into a command

			if IsEnchanted != True:
				Tag = ""

			Com = '/replaceitem block '+str(X)+' '+str(Y)+' '+str(Z)+' slot.container.'+str(SlotCounter)+' '+str(Item)+' '+str(Count)+' '+str(Damage)+' '+str(Tag)+''
			SlotCounter += 1
			e.npc.executeCommand(str(Com))

		# Adding Sword
		Damage = random.randint(10, 150)
		Count = 1
		if e.npc.getInventory().getRightHand().getName() == "minecraft:golden_apple" :
			Item = "minecraft:diamond_sword"
		else :
			Item = e.npc.getInventory().getRightHand().getName()

		Sword = e.npc.getStoreddata().get("Sword")
		Sword = Sword.split("/")
		Tag = "{ench:[{id:16,lvl:"+str(Sword[0])+"}"
		for i in range(1, 4):
			if ( i == 1 ) and (int(Sword[i]) != 0):
				EnchID = 20
				EnchLvL = int(Sword[i])
				Tag += ",{id:20,lvl:"+Sword[1]+"}"
			if (i == 2 ) and (int(Sword[i]) != 0):
				EnchID = 19
				EnchLvL = int(Sword[i])
				Tag += ",{id:19,lvl:"+Sword[2]+"}"
			if (i == 3) and (int(Sword[i]) != 0) :
				EnchID = 34
				EnchLvL = int(Sword[i])
				Tag += ",{id:34,lvl:"+Sword[3]+"}"

		
		Tag += "]}"
		if IsEnchanted != True:
			Tag = ""

		Com = '/replaceitem block '+str(X)+' '+str(Y)+' '+str(Z)+' slot.container.'+str(SlotCounter)+' '+str(Item)+' '+str(Count)+' '+str(Damage)+' '+str(Tag)+''
		SlotCounter += 1
		e.npc.executeCommand(str(Com))

		# Adding the golden apples
		GoldenAppleLoot = e.npc.getTempdata().get("GapCount")
		if (GoldenAppleLoot == None) or (0 >= GoldenAppleLoot):
			GoldenAppleLoot = 1 + int(round(e.npc.world.getTempdata().get("GapAtKill")))
		if GoldenAppleLoot >= 64:
			while GoldenAppleLoot > 64:
				GoldenAppleLoot -= 64
			
				Item = "minecraft:golden_apple"
				Damage = 0
				Count = 64
				Tag = ""
				Com = '/replaceitem block '+str(X)+' '+str(Y)+' '+str(Z)+' slot.container.'+str(SlotCounter)+' '+str(Item)+' '+str(Count)+' '+str(Damage)+' '+str(Tag)+''
				SlotCounter += 1
				e.npc.executeCommand(str(Com))
			
			Item = "minecraft:golden_apple"
			Damage = 0
			Count = GoldenAppleLoot
			Tag = ""
			Com = '/replaceitem block '+str(X)+' '+str(Y)+' '+str(Z)+' slot.container.'+str(SlotCounter)+' '+str(Item)+' '+str(Count)+' '+str(Damage)+' '+str(Tag)+''
			SlotCounter += 1
			e.npc.executeCommand(str(Com))

		else:
			Item = "minecraft:golden_apple"
			Damage = 0
			Count = GoldenAppleLoot
			Tag = ""
			Com = '/replaceitem block '+str(X)+' '+str(Y)+' '+str(Z)+' slot.container.'+str(SlotCounter)+' '+str(Item)+' '+str(Count)+' '+str(Damage)+' '+str(Tag)+''
			SlotCounter += 1
			e.npc.executeCommand(str(Com))

		# Adding the golden head, to prevent conflict with the golden head scenario
		if e.npc.world.getTempdata().get("GoldenHeads") == True:
			Count = 1
			Item = "minecraft:skull"
			Damage = 0
			Tag = '' 
			Com = '/replaceitem block '+str(X)+' '+str(Y)+' '+str(Z+1)+' slot.container.0 '+str(Item)+' '+str(Count)+' '+str(Damage)+' '+str(Tag)+''
			e.npc.executeCommand(str(Com))


		# Adding some blocks and other stuff
		if (int(e.npc.world.getStoreddata().get("TeamsAlive")) > 12 ) and (e.npc.world.getTempdata().get("ClearedLoot") != True):
			ItemList = [["minecraft:cobblestone","64"],["minecraft:cobblestone","64"],["minecraft:cobblestone","64"],["minecraft:cobblestone","64"],["minecraft:apple","3"],["minecraft:cooked_beef","64"],["minecraft:cobblestone","64"],["minecraft:cobblestone","64"],["minecraft:cobblestone","64"],["minecraft:cobblestone","64"],["minecraft:cobblestone","64"],["minecraft:log","64"],["minecraft:water_bucket","1"],["minecraft:water_bucket","1"],["minecraft:water_bucket","1"],["minecraft:lava_bucket","1"],["minecraft:fishing_rod","1"],["minecraft:book","2"],["minecraft:flint_and_steel","1"],["minecraft:planks","64"],["minecraft:anvil","1"],["minecraft:enchanting_table","1"],["minecraft:wheat_seeds","12"],["minecraft:string","1"],["minecraft:coal","20"],["minecraft:flint","16"],["minecraft:dirt","64"],["minecraft:leather","11"],["minecraft:reeds","15"],["minecraft:feather","4"],["minecraft:gunpowder","2"],["minecraft:sand","64"],["minecraft:gravel","64"],["minecraft:sapling","16"],["minecraft:red_flower","6"],["minecraft:torch","64"],["minecraft:redstone","64"],["minecraft:bone","3"]]																			
		else:
			ItemList = [["minecraft:cobblestone","64"],["minecraft:cobblestone","64"],["minecraft:cobblestone","64"],["minecraft:log","64"],["minecraft:water_bucket","1"],["minecraft:water_bucket","1"],["minecraft:water_bucket","1"],["minecraft:lava_bucket","1"],["minecraft:fishing_rod","1"],["minecraft:flint_and_steel","1"],["minecraft:planks","64"],["minecraft:anvil","1"],["minecraft:enchanting_table","1"]]																			

		for i in range(0, len(ItemList)-1):	
			Count = random.randint(0,int(ItemList[i][1]))
			if Count != 0:
				if (SlotCounter == 27) and (SwitchedCoord == False):
					SlotCounter = 1
					SwitchedCoord = True
					Z += 1
				Item = ItemList[i][0]
				Damage = 0
				Tag = ''
				Com = '/replaceitem block '+str(X)+' '+str(Y)+' '+str(Z)+' slot.container.'+str(SlotCounter)+' '+str(Item)+' '+str(Count)+' '+str(Damage)+' '+str(Tag)+''
				SlotCounter += 1
				e.npc.executeCommand(str(Com))


		#Adding the pickaxe
		if IsEnchanted == True:
			Tag = '{ench:[{id:32,lvl:3}]}'
			Item = "minecraft:diamond_pickaxe"
			Count = 1
			Damage = random.randint(127, 325)

			Com = '/replaceitem block '+str(X)+' '+str(Y)+' '+str(Z)+' slot.container.'+str(SlotCounter)+' '+str(Item)+' '+str(Count)+' '+str(Damage)+' '+str(Tag)+''
			SlotCounter += 1
			e.npc.executeCommand(str(Com))


#DEATH STYLE functions :

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

#ON KILL ONLY functions :	


#SCENARIOS functions :				

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



#TEAMER BOTS ONLY functions :

def SharingArmor(e):
	"""
	Giving a diamond armor piece to the bot when you right click him, if he is in your team, and if you have a piece to give.
	"""
	try:
		Sword = e.npc.getStoreddata().get("Sword")
		Armor = e.npc.getStoreddata().get("Armor")
		Armor = Armor.split("/")

		FactionID = e.npc.getFaction().getId()
		if FactionID == 26 :
			Teaming(e)
			for i in range(0, 4):
				ArmorToGet = ["helmet",'chestplate',"leggings",'boots']
				if (e.player.getHeldItem().getName() == "minecraft:diamond_"+str(ArmorToGet[i])) and (str(Armor[i]) == "0"):
					Armor[i] = "1"
					e.npc.getInventory().setArmor(i,e.npc.world.createItem("minecraft:diamond_"+str(ArmorToGet[i]),0,1))
					e.npc.executeCommand('/tellraw @a ["",{"text":"[","color":"dark_gray"},{"text":"Team","color":"red"},{"text":"] ","color":"dark_gray"},{"text":"'+str(e.npc.getDisplay().getName())+'","color":"white"},{"text":":","color":"dark_gray"},{"text":" Thank ! ","color":"gray"}]')
					Armor = "/".join(Armor)
					e.npc.getStoreddata().put("Armor", Armor)
					SettingResistance(e)
		else :
			pass
	except:
		pass

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
	except Exception as err:
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
		e.npc.addPotionEffect(11, 100000, 0, False)


#IN GAME functions :

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
					ReachList = [2,2,2,2,3,3,3,4]
					NewReach = random.choice(ReachList)
					e.npc.getStats().getMelee().setRange(NewReach)

				elif SelectedType == "ProTier" :
					ReachList = [2,2,2,2,3,3,3,3]
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

			if e.npc.getStats().getMelee().getRange() == 3:
				e.npc.getStats().getMelee().setKnockback(1)
				e.npc.getStats().getMelee().setRange(3)
			else:
				pass

		else:
			e.npc.getTempdata().put("ComboTick", e.npc.getTempdata().get("ComboTick")+1)
			e.npc.getStats().getMelee().setKnockback(0) 
	except:
		pass

def Strafing(e):
	'''Make the bot strafe ( need a fix )
	'''
	try :
		Level = e.npc.getTempdata().get("SelectedType")			# Making the Npc strafe left or right with a timer and a side choosing script
		if Level != "NoobTier" : 							# Only NoobTier doesnt strafe
			IsStrafing = e.npc.getTempdata().get("IsStrafing")
			TargetX = e.npc.getAttackTarget().getX()
			TargetZ = e.npc.getAttackTarget().getX()
			MyX = e.npc.getX()
			MyY = e.npc.getY()
			MyZ = e.npc.getZ()
			BaseStrafe = "left"

			if e.npc.getTempdata().get("StrafeTick") == None:
				e.npc.getTempdata().put("StrafeTick", 0)
			elif e.npc.getTempdata().get("StrafeTick") == 5:
				e.npc.getTempdata().put("IsStrafing", False)   
				e.npc.getTempdata().put("StrafeTick", 0)
				


			StrafeTick = e.npc.getTempdata().get("StrafeTick")

			if StrafeTick == 4 and BaseStrafe == "left":
				BaseStrafe = "right"
			elif StrafeTick == 4 :
				BaseStrafe = "left"

			if (TargetX-3 <= MyX <= TargetX+3) and (IsStrafing != True):
				if BaseStrafe == "left" :
					e.npc.navigateTo(TargetX-4, MyY, int(round((TargetZ+MyZ)//2)), 2) 		# Strafing left
					
					e.npc.getTempdata().put("IsStrafing", True)
				elif BaseStrafe == "right" :
					e.npc.navigateTo(TargetX+4, MyY, int(round((TargetZ+MyZ)//2)), 2) 		# Strafing left
					e.npc.getTempdata().put("IsStrafing", True)


			e.npc.getTempdata().put("StrafeTick", e.npc.getTempdata().get("StrafeTick")+1)
			
			
	except Exception as err:
		pass
	
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

def BreakingStuff(e):
	"""
	Making armor loose prot tier every 300 hits
	"""


	if (e.npc.world.getStoreddata().get("TeamsAlive") >= 15):
		BreakVar = 300
	else:
		BreakVar = 220


	if e.npc.getTempdata().get("HitsTaken") == None :
		e.npc.getTempdata().put("HitsTaken", 1)

	elif e.npc.getTempdata().get("HitsTaken") >= BreakVar :
		List = [0,0,0,1,1,2,2,3,3]
		Piece = int(random.choice(List))
		MyProt = str(e.npc.getStoreddata().get("Prot"))
		MyProt = MyProt.split("/")

		if (int(MyProt[Piece])-1) >= 1:
			MyProt[Piece] = str(int(MyProt[Piece])-1)
			ProtList = "/".join(MyProt)
			e.npc.executeCommand('/playsound random.break @a')
			e.npc.getStoreddata().put("Prot", ProtList)
			e.npc.getTempdata().put("HitsTaken", 0)
		
		SettingResistance(e)
	else:
		e.npc.getTempdata().put("HitsTaken", e.npc.getTempdata().get("HitsTaken")+1)

def SpecDisplay(e):

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

	if str(Armor[0]) == "1":
		PartI = "aqua"
	else:
		PartI = "gray"

	if str(Armor[1]) == "1":
		PartII = "aqua"
	else:
		PartII = "gray"

	if str(Armor[2]) == "1":
		PartIII = "aqua"
	else:
		PartIII = "gray"

	if str(Armor[3]) == "1":
		PartIV = "aqua"
	else:
		PartIV = "gray"

	if e.npc.getInventory().getRightHand().getName() == "minecraft:diamond_sword":
		SwordType = "aqua"
	elif str(Sword[1]) == "1":
		SwordType = 'red'
	else:
		SwordType = "gray"

	if e.player.getGamemode() == 1:
		e.npc.executeCommand('/tellraw @a ["",{"text":"[","color":"dark_gray"},{"text":"Spec","color":"green"},{"text":"]","color":"dark_gray"},{"text":"Prot '+str(Prot[0])+'","color":"'+str(PartI)+'"},{"text":" / ","color":"dark_gray"},{"text":"Prot '+str(Prot[1])+'","color":"'+str(PartII)+'"},{"text":" / ","color":"dark_gray"},{"text":"Prot '+str(Prot[2])+'","color":"'+str(PartIII)+'"},{"text":" / ","color":"dark_gray"},{"text":"Prot '+str(Prot[3])+'","color":"'+str(PartIV)+'"},{"text":" / ","color":"dark_gray"},{"text":"Sharp '+str(Sword[0])+'","color":"'+str(SwordType)+'"},{"text":" / ","color":"dark_gray"},{"text":"'+str(e.npc.getTempdata().get("GapCount"))+' Gapple(s)","color":"gold"}]')

def UseLava(e):
	try:
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

def MeetUpChecking(e):	
	'''Force bots to go to 0 ; 0 
	'''			
	MeetUp = e.npc.world.getStoreddata().get("MeetUp")
	if (e.npc.getFaction().getId() != 26) and (e.npc.getAttackTarget() == None):
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

				e.npc.navigateTo(e.npc.getX()+X, e.npc.getY(), e.npc.getZ()+Z, 2)
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

#POST GAME functions :



#Misc

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

def Banning(e):
	if e.npc.getStats().getMelee().getRange() >= 5 :
		e.npc.executeCommand('/tellraw @a ["",{"text":"[","color":"dark_red"},{"text":"FAC","color":"dark_purple"},{"text":"] ","color":"dark_red"},{"text":"========================","color":"red"}]')
		e.npc.executeCommand('/tellraw @a ["",{"text":"[","color":"dark_red"},{"text":"FAC","color":"dark_purple"},{"text":"]","color":"dark_red"},{"text":" '+str(e.npc.getDisplay().getName())+'","color":"red"},{"text":" has been banned for :","color":"gold"},{"text":" Hacked Client/G-Cheat","color":"red"}]')
		e.npc.executeCommand('/tellraw @a ["",{"text":"[","color":"dark_red"},{"text":"FAC","color":"dark_purple"},{"text":"] ","color":"dark_red"},{"text":"========================","color":"red"}]')		
		e.npc.getStats().getMelee().setStrength(0)
		e.npc.getStats().setAggroRange(0)
		e.npc.getAi().setWalkingSpeed(0)
		e.npc.getDisplay().setSkinTexture('minecraft:textures/entity/zombie/zombie.png')


	#Classes :

def LastFight(e):
	"""
	Teleport the NPC on the final fight zone (deathmatch)
	"""
	if (e.npc.world.getStoreddata().get("TeamsAlive") == e.npc.world.getTempdata().get("StartDeathmatchAt")) and (e.npc.getTempdata().get("IsDeathMatch") == None):
		e.npc.setPosition(0, 155, 0)
		e.npc.getTempdata().put("IsDeathMatch", "True")

def SpecMessageDeath(e):
	"""
	Display some message to make the game feel real
	"""
	if e.npc.world.getTempdata().get("StartDeathmatchAt") > e.npc.world.getStoreddata().get("TeamsAlive"):
		MessageList = ["gg","holly","Gg","ty4p",'ez lol',"GG",'GG !',"He's crack :o",":O !","wp","Pvp god be like","gg !","gg","gg","gg"]
		SpecList = ["Gonzaloo","dedreviil","Davuki","Fukano","Etoiles","Pickachu","Mentally"]
		a = '/tellraw @a ["",{"text":"[","color":"gray"},{"text":"Host","color":"dark_aqua"},{"text":"] ","color":"gray"},{"text":"[","color":"gray"},{"text":"Spec","color":"aqua"},{"text":"] ","color":"gray"},{"text":"'+str(random.choice(SpecList))+'","color":"gold"},{"text":" : ","color":"white"},{"text":"'+str(random.choice(MessageList))+'","color":"white"}]'
		e.npc.executeCommand(a)


#Classes :
# nah joking im too bad



#================================#
#_______{ Calling Events }_______#
#================================#


def init(e):
	try:
		e.npc.getTimers().start(2, 0, True)			# The Rod block timer
		e.npc.getTempdata().put("NeedRod", 0)
	except:
		pass
	MasterLevel(e)
	RodlessActivation(e)
	AllyResistance(e)
		
		
def damaged(e):
	if not (e.npc.world.getTempdata().get("MeetUpMode") == True):
		BreakingStuff(e)
	RodlessActivation(e)
	Knocked(e)
	StopCombo(e)
	Rod(e)

def meleeAttack(e):
	RodlessActivation(e)
	Banning(e)
	Strafing(e)
	Combo(e)

def kill(e):
	pass

def died(e):
	try :			# Only if Killed by player
		e.source.getName()
		TimeBomb(e)
	except Exception as err:
		#e.npc.say(str(err))
		pass
	SpecMessageDeath(e)
	VanillaDeathStyle(e)

def tick(e):
	if (e.npc.world.getTempdata().get("GameStarted") != 1) and (e.npc.getFaction().getId() != 26) and (e.npc.getFaction().getId() != 0):
		#e.npc.say(str(e.npc.getFaction().getId()))
		e.npc.despawn()
		pass
	if (e.npc.world.getTempdata().get("GameStarted") == 1):
		UseLava(e)
		RemoveLava(e)
		MeetUpChecking(e)
		Rod(e)
		LastFight(e)


def interact(e):
	SpecDisplay(e)
	GappleSharing(e)
	SharingArmor(e)
	e.setCanceled(True)
	
def target(e):

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