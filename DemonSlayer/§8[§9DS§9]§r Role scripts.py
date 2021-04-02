import random
import math

#API Link :http://www.kodevelopment.nl/customnpcs/api/1.8.9/
#Desc : Demon sllayer UHC PvP script by Natsu91

#===================================#
#_______{ Creating Algorithm }______#
#===================================#



#DEATH STYLE functions :

def InventorySpawn(e) :
	'''Spawn the whole inventory of the bot depending of the Kills amount he had, double armor drops if he was stacked

		EXCEPTION : if OneShot is enabled, stuff dont drop
	'''
	IsEnchanted = True

	if (e.npc.world.getTempdata().get("OneShot") != True) and (e.npc.world.getTempdata().get("TimeBomb") != True):
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
			# Damaging items to make it feeling real
			if (int(e.npc.world.getStoreddata().get("TeamsAlive")) > 20 ):
				Damage = random.randint(10, 250)
			else:
				Damage = random.randint(10, 120)

			MyX = e.npc.getX()			# Attributing coordinates to the item
			MyY = e.npc.getY()
			MyZ = e.npc.getZ()
			SpawnX = int(round(MyX))
			SpawnY = int(round(MyY)) + 1
			SpawnZ = int(round(MyZ))
			
			if (int(Prot[i]) ==0) and (int(Proj[i]) == 0):
				IsEnchanted = False
				e.npc.executeCommand("/summon Item "+str(MyX)+" "+str(MyY)+" "+str(MyZ)+" {Item:{id:"+str(element)+",Damage:"+str(Damage)+",Count:1},Motion:["+str(random.uniform(0.02,0.1)*random.randint(-1,1))+",0.09,"+str(random.uniform(0.02,0.1)*random.randint(-1,1))+"]}") # Looting item
			else:
				e.npc.executeCommand("/summon Item "+str(MyX)+" "+str(MyY)+" "+str(MyZ)+" {Item:{id:"+str(element)+",Damage:"+str(Damage)+",Count:1,tag:{ench:[{id:"+str(EnchID)+",lvl:"+str(EnchLvL)+"}]}},Motion:["+str(random.uniform(0.02,0.1)*random.randint(-1,1))+",0.09,"+str(random.uniform(0.02,0.1)*random.randint(-1,1))+"]}") # Looting item

		# Spawning other items
		if (int(e.npc.world.getStoreddata().get("TeamsAlive")) > 12 ) and (e.npc.world.getTempdata().get("ClearedLoot") != True):
			ItemList = [["minecraft:cobblestone","64"],["minecraft:cobblestone","64"],["minecraft:cobblestone","64"],["minecraft:cobblestone","64"],["minecraft:apple","3"],["minecraft:cooked_beef","64"],["minecraft:cobblestone","64"],["minecraft:cobblestone","64"],["minecraft:cobblestone","64"],["minecraft:cobblestone","64"],["minecraft:cobblestone","64"],["minecraft:log","64"],["minecraft:water_bucket","1"],["minecraft:water_bucket","1"],["minecraft:water_bucket","1"],["minecraft:lava_bucket","1"],["minecraft:fishing_rod","1"],["minecraft:book","2"],["minecraft:flint_and_steel","1"],["minecraft:planks","64"],["minecraft:anvil","1"],["minecraft:enchanting_table","1"],["minecraft:wheat_seeds","12"],["minecraft:string","1"],["minecraft:coal","20"],["minecraft:flint","16"],["minecraft:dirt","64"],["minecraft:leather","11"],["minecraft:reeds","15"],["minecraft:feather","4"],["minecraft:gunpowder","2"],["minecraft:sand","64"],["minecraft:gravel","64"],["minecraft:sapling","16"],["minecraft:red_flower","6"],["minecraft:torch","64"],["minecraft:redstone","64"],["minecraft:bone","3"]]																			
		else:
			ItemList = [["minecraft:cobblestone","64"],["minecraft:cobblestone","64"],["minecraft:cobblestone","64"],["minecraft:log","64"],["minecraft:water_bucket","1"],["minecraft:water_bucket","1"],["minecraft:water_bucket","1"],["minecraft:lava_bucket","1"],["minecraft:fishing_rod","1"],["minecraft:flint_and_steel","1"],["minecraft:planks","64"],["minecraft:anvil","1"],["minecraft:enchanting_table","1"]]																			
		for i in range(0, len(ItemList)-1):	
			Count = random.randint(0,int(ItemList[i][1]))
			
			e.npc.executeCommand("/summon Item "+str(MyX)+" "+str(MyY)+" "+str(MyZ)+" {Item:{id:"+str(ItemList[i][0])+",Count:"+str(Count)+"},Motion:["+str(random.uniform(0.00,0.1)*random.randint(-1,1))+",0.09,"+str(random.uniform(0.02,0.1)*random.randint(-1,1))+"]}") # Looting item
		
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
		if IsEnchanted == True:
			e.npc.executeCommand("/summon Item "+str(MyX)+" "+str(MyY)+" "+str(MyZ)+" {Item:{id:"+str(Item5)+",Damage:"+str(Damage)+",Count:1,tag:"+str(EnchList)+"},Motion:["+str(random.uniform(0.02,0.1)*random.randint(-1,1))+",0.09,"+str(random.uniform(0.02,0.1)*random.randint(-1,1))+"]}") # Looting sword
		else:
			e.npc.executeCommand("/summon Item "+str(MyX)+" "+str(MyY)+" "+str(MyZ)+" {Item:{id:"+str(Item5)+",Damage:"+str(Damage)+",Count:1},Motion:["+str(random.uniform(0.02,0.1)*random.randint(-1,1))+",0.09,"+str(random.uniform(0.02,0.1)*random.randint(-1,1))+"]}") # Looting item
	

		if InventorySpawn.isDone != True :
			GoldenAppleLoot = e.npc.getTempdata().get("GapCount")
			if (GoldenAppleLoot == None) or (GoldenAppleLoot == 0):
				GoldenAppleLoot = 1 + int(round(int(round(e.npc.world.getTempdata().get("GapAtKill")))/2))
			e.npc.executeCommand("/summon Item "+str(MyX)+" "+str(MyY)+" "+str(MyZ)+" {Item:{id:322,Damage:0,Count:"+str(GoldenAppleLoot)+"},Motion:["+str(random.uniform(0.02,0.1)*random.randint(-1,1))+",0.09,"+str(random.uniform(0.02,0.1)*random.randint(-1,1))+"]}") # Looting golden apple based on the amount he had
			if IsEnchanted == True:
				e.npc.executeCommand("/summon Item "+str(MyX)+" "+str(MyY)+" "+str(MyZ)+" {Item:{id:278,Damage:187,Count:1,tag:{ench:[{id:32,lvl:5}]}},Motion:["+str(random.uniform(0.02,0.1)*random.randint(-1,1))+",0.09,"+str(random.uniform(0.02,0.1)*random.randint(-1,1))+"]}")		# Looting a pickaxe
			try:
				e.npc.executeCommand("/xp 20 "+ str(e.source.getName()))		# Looting xp
			except :
				pass

		if e.npc.getStoreddata().get("Kills") >= 4 and (InventorySpawn.isDone != True ):
			InventorySpawn.isDone = True
			InventorySpawn(e)

def DeathTchatMessage(e):
	"""
	Saying death message
	"""
	GoodList = ["Tanjiro",
			"Zenitsu",
			"Inosuke",
			"Kagaya",
			"Tomioka",
			"Shinobu",
			"Kyojuro",
			"Tengen",
			"Muichiro",
			"Mitsuri",
			"Sanemi",
			"Obanai",
			"Gyomei",
			"Urokodaki",
			"Kanae",
			"Sabito",
			"Kanao",
			"Genya",
			"Hotaru",
			"Slayer",
			"Jigoro",
			"Yoriichi",
			"Shinjuro"]
	BadList = ["Muzan",
			"Nakime",
			"Kokushibo",
			"Doma",
			"Akaza",
			"Gyokko",
			"Daki",
			"Gyutaro",
			"Rui",
			"Kaigaku",
			"Sasumaru",
			"Kyogai",
			"Yahaba",
			"Kumo",
			"Furuto",
			"Nezuko",
			"Demon",
			]
	if str(e.npc.getStoreddata().get("Role")) in BadList:
		RoleColor = "red"
	else:
		RoleColor = "green"

	e.npc.executeCommand('/tellraw @a {"text":"                                                                                 ","color":"dark_gray","strikethrough":true}')
	e.npc.executeCommand('/tellraw @a ["",{"text":"'+str(e.npc.getDisplay().getName())+'","color":"yellow"},{"text":" est mort.","color":"gray"}]')
	e.npc.executeCommand('/tellraw @a ["",{"text":"Son role etait : ","color":"gray"},{"text":"'+str(e.npc.getStoreddata().get("Role"))+'","color":"'+str(RoleColor)+'"}]')
	e.npc.executeCommand('/tellraw @a {"text":"                                                                                 ","color":"dark_gray","strikethrough":true}')

#ON KILL ONLY functions :	

def KillingRole(e):
	"""
	Update game datas depending on the role who died
	"""
	if e.entity.getType() == 1:
		KilledRole = str(e.npc.world.getStoreddata().get(str(e.entity.getName())+"Role"))
	else:
		KilledRole = str(e.entity.getStoreddata().get("Role"))
	Role = e.npc.getStoreddata().get("Role")

	if (Role == "Muzan") and (KilledRole == "Nezuko"):
		e.npc.world.getTempdata().put("MuzanKilledNezuko", True)

	if (Role == "Jigoro") and (KilledRole == "Kaigaku"):
		e.npc.world.getTempdata().put("JigoroKilledKaigaku", True)	

	if (Role == "Tanjiro") and (KilledRole == e.npc.world.getTempdata().get("TanjiroTarget")):
		e.npc.world.getTempdata().put("TanjiroKilledTarget", True)

	if KilledRole == "Nezuko":
		e.npc.world.getTempdata().put("NezukoDied", True)

	if KilledRole == "Sabito":
		e.npc.world.getTempdata().put("SabitoDied", True)

	if (KilledRole == "Zenitsu") and (Role == "Kaigaku"):
		e.npc.world.getTempdata().get("KaigakuKilledZenitsu")

	if (Role == "Yahaba") and (KilledRole == e.npc.world.getTempdata().get("YahabaTarget")):
		e.npc.world.getTempdata().put("YahabaKilledTarget", True)
		e.npc.getStats().setMaxHealth(24)

#SCENARIOS functions :				

def BleedingSweets(e):
	'''Drop the configured amount of :
		- diamonds
		- gold
		- iron
	'''
	try:
		BleedingSweets = e.npc.world.getTempdata().get("BleedingSweets")
		if BleedingSweets == True :
			BleedingDiamond = e.npc.world.getTempdata().get("BleedingDiamond")
			BleedingIron = e.npc.world.getTempdata().get("BleedingIron")
			BleedingGold = e.npc.world.getTempdata().get("BleedingGold")
			e.npc.executeCommand("/summon Item ~+0.35 ~ ~+0.35 {Item:{id:264,Damage:0,Count:"+str(BleedingDiamond)+"}}")
			e.npc.executeCommand("/summon Item ~-0.35 ~ ~-0.35 {Item:{id:265,Damage:0,Count:"+str(BleedingIron)+"}}")
			e.npc.executeCommand("/summon Item ~-0.35 ~ ~+0.35 {Item:{id:266,Damage:0,Count:"+str(BleedingGold)+"}}")
	except:
		pass



#INIT GAME functions :

def GettingRole(e):
	"""
	Select a role at game starting
	"""
	try:
		if (e.npc.getStoreddata().get("Role") == None) and not (e.npc.getDisplay().getName() in ["Disabled","-"]):		#if no role
			RolesList = e.npc.world.getTempdata().get('RolesList')
			RoleSelected = random.choice(RolesList)
			e.npc.getStoreddata().put("Role", RoleSelected)
			RolesList.remove(RoleSelected)
			e.npc.world.getTempdata().put('RolesList', RolesList)

			GdList = e.npc.world.getTempdata().get("GoodList")
			BdList = e.npc.world.getTempdata().get("BadList")
			MList = e.npc.world.getTempdata().get("MoonList")
			UpMList = e.npc.world.getTempdata().get("UpperMoonList")

			BadList = ["Muzan",
					"Nakime",
					"Kokushibo",
					"Doma",
					"Akaza",
					"Gyokko",
					"Daki",
					"Gyutaro",
					"Rui",
					"Kaigaku",
					"Sasumaru",
					"Kyogai",
					"Yahaba",
					"Kumo",
					"Furuto",
					"Demon"
					]

			GoodList = ["Tanjiro",
					"Zenitsu",
					"Inosuke",
					"Kagaya",
					"Tomioka",
					"Shinobu",
					"Kyojuro",
					"Tengen",
					"Muichiro",
					"Mitsuri",
					"Sanemi",
					"Obanai",
					"Gyomei",
					"Urokodaki",
					"Kanae",
					"Sabito",
					"Kanao",
					"Genya",
					"Hotaru",
					"Slayer",
					"Jigoro",
					"Yoriichi",
					"Shinjuro"]

			UpperMoonList = ["Kokushibo","Doma","Akaza","Gyokko","Daki","Gyutaro"]
			MoonList = ["Rui","Kaigaku","Sasumaru","Kyogai","Yahaba","Kumo","Furuto",'Demon',"Nezuko"]

			if RoleSelected == "Muzan":
				e.npc.world.getTempdata().put("Muzan", str(e.npc.getDisplay().getName()))
			elif RoleSelected == "Daki":
				e.npc.world.getTempdata().put("Daki", str(e.npc.getDisplay().getName()))
			elif RoleSelected == "Gyutaro":
				e.npc.world.getTempdata().put("Gyutaro", str(e.npc.getDisplay().getName()))		
			if RoleSelected in BadList:
				BdList.append(str(e.npc.getDisplay().getName()))
				if RoleSelected in UpperMoonList:
					UpMList.append(str(e.npc.getDisplay().getName()))
				elif RoleSelected in MoonList:
					MList.append(str(e.npc.getDisplay().getName()))
			
			else:
				GdList.append(str(e.npc.getDisplay().getName()))

			e.npc.world.getTempdata().put("GoodList", GdList)
			e.npc.world.getTempdata().put("BadList", BdList)
			e.npc.world.getTempdata().put("MoonList", MList)
			e.npc.world.getTempdata().put("UpperMoonList", UpMList)

			RoleInit(e)	
			JoiningTeam(e)
	except:
		pass

def JoiningTeam(e):
	"""
	Make the bot join a team depending of his role
	"""
	GoodList = ["Tanjiro",
			"Zenitsu",
			"Inosuke",
			"Kagaya",
			"Tomioka",
			"Shinobu",
			"Kyojuro",
			"Tengen",
			"Muichiro",
			"Mitsuri",
			"Sanemi",
			"Obanai",
			"Gyomei",
			"Urokodaki",
			"Kanae",
			"Sabito",
			"Kanao",
			"Genya",
			"Hotaru",
			"Slayer",
			"Jigoro",
			"Yoriichi",
			"Shinjuro"]
	BadList = ["Muzan",
			"Nakime",
			"Kokushibo",
			"Doma",
			"Akaza",
			"Gyokko",
			"Daki",
			"Gyutaro",
			"Rui",
			"Kaigaku",
			"Sasumaru",
			"Kyogai",
			"Yahaba",
			"Kumo",
			"Furuto",
			"Nezuko",
			"Demon"
			]
	

	NearestBots = e.npc.world.getNearbyEntities(int(e.npc.getX()), int(e.npc.getY()), int(e.npc.getZ()), 15, 2).tolist()
	for i in range(0, len(NearestBots)):
		Good = 0
		Bad = 0
		if NearestBots[i].getStoreddata().get("Role") in BadList:
			Bad += 1
		else:
			Good += 1

		if Good < Bad:
			for i in range(0, len(NearestBots)):
				if NearestBots[i].getStoreddata().get("Role") in BadList:
					NearestBots[i].setFaction(42) 

		else:
			NearestBots[i].setFaction(41)


	"""
	Time = e.npc.world.isDay()
	#if e.npc.world.getTempdata().get("GroupList") == None:
	if e.npc.getFaction().getId() == 41:# If faction is safe
		if e.npc.getTempdata().get("MyGroup") == None:			#If not in a group
			NearestBots = e.npc.world.getNearbyEntities(int(e.npc.getX()), int(e.npc.getY()), int(e.npc.getZ()), 20, 2).tolist()
			GroupList = e.npc.world.getTempdata().get("GroupList")
		
			#If no group formed
			if GroupList == None:
				GroupList = {str(e.npc.getDisplay().getName()): []}
				e.npc.world.getTempdata().put("GroupList", GroupList)
				e.npc.getTempdata().put("MyGroup", str(e.npc.getDisplay().getName()))

			#If there is already group formed
			else:
				for i in GroupList.items():					#In the groups created
					if len(GroupList[i[0]]) < 6:
					for j in range(0, len(NearestBots)):			#In the groups near by
						LocalName = NearestBots[j].getName()
						if GroupList[i[0]] == LocalName:				#If group leader is near		
							e.npc.getRole().setFollowing(str(LocalName))			#Following group
							GroupList[i[0]].append(str(e.npc.getDisplay().getName()))				#Updating group list
							e.npc.getTempdata().get("MyGroup", )


	else:	#If already in a group
		NearestBots = e.npc.world.getNearbyEntities(int(e.npc.getX()), int(e.npc.getY()), int(e.npc.getZ()), 20, 2).tolist()
	"""	

def RoleInit(e):
	"""
	Enable roles power, but only once
	"""
	Role = e.npc.getStoreddata().get("Role") 
	if Role == "Gyomei":
		e.npc.getStats().setMaxHealth(24)


#TEAMER BOTS ONLY functions :
		


#IN GAME functions :

def TestingDeath(e):
	"""
	Prevent glitched death due to manual damage increase
	"""
	if e.npc.isAlive() == False:
		e.npc.kill()
		died(e)

def DamageIncrease(e):
	"""
	Increase damage depending on the attacker's role
	"""
	try:
		Role = e.npc.getStoreddata().get("Role")
		Time = e.npc.world.isDay()
		if e.source.getType() == 1:
			AtkRole = str(e.npc.world.getStoreddata().get(str(e.source.getName())+"Role"))
			AtkName = e.source.getName()
		else:
			AtkRole = str(e.source.getStoreddata().get("Role"))
			AtkName = e.source.getDisplay().getName()

		#Muzan blood damage increase
		if str(AtkName) == str(e.npc.world.getTempdata().get("MuzanBoost")):
			e.npc.setHealth(e.npc.getHealth()-(e.damage*1.1))

		#Tanjiro damage increase
		if (AtkRole == "Tanjiro") and (e.npc.world.getTempdata().get("TanjiroKilledTarget") == True):
			e.npc.setHealth(e.npc.getHealth()-(e.damage*0.3))

		#Zenitsu damage increase
		elif (AtkRole == "Zenitsu") and (e.source.getHealth() <= 10):
			e.npc.setHealth(e.npc.getHealth()-(e.damage*0.3))

		#Tomioka damage increase
		elif (AtkRole == "Tomioka") and (Time == True) and (e.npc.world.getTempdata().get("TomiokaKilledTanjiroKiller") == True):
			e.npc.setHealth(e.npc.getHealth()-(e.damage*0.3))
		elif (AtkRole == "Tomioka") and (Time == False) and (e.npc.world.getTempdata().get("TomiokaKilledSabitoKiller") == True):
			e.npc.setHealth(e.npc.getHealth()-(e.damage*0.3))

		#Gyomei damage increase
		elif (AtkRole == "Gyomei") and (Time == True):
			e.npc.setHealth(e.npc.getHealth()-(e.damage*0.3))

		#Urokodaki damage increase
		elif (AtkRole == "Urokodaki") and (e.source.inWater() == True):
			e.npc.setHealth(e.npc.getHealth()-(e.damage*0.3))

		#Jigoro damage increase
		elif (AtkRole == "Jigoro") and (e.npc.world.getTempdata().get("JigoroKilledKaigaku") == True):
			e.npc.setHealth(e.npc.getHealth()-(e.damage*0.35))

		#Yoriichi damage increase
		elif (AtkRole == "Yoriichi"):
			e.npc.setHealth(e.npc.getHealth()-(e.damage*0.3))

		#Muzan damage increase
		elif (AtkRole == "Muzan") and (e.npc.world.getTempdata().get("MuzanKilledNezuko") == True):
			e.npc.setHealth(e.npc.getHealth()-(e.damage*0.35))

		#Kokushibo damage increase
		elif (AtkRole == "Kokushibo") and (Time == False):
			e.npc.setHealth(e.npc.getHealth()-(e.damage*0.3))

		#Doma damage increase
		elif (AtkRole == "Doma") and (Time == False):
			e.npc.setHealth(e.npc.getHealth()-(e.damage*0.3))

		#Gyokko damage increase
		elif (AtkRole == "Gyokko") and (Time == False):
			e.npc.setHealth(e.npc.getHealth()-(e.damage*0.3))

		#Akaza damage increase
		elif (AtkRole == "Akaza"):
			e.npc.setHealth(e.npc.getHealth()-(e.damage*0.3))

		#Daki/Gyutaro damage increase
		elif (AtkRole in ["Daki","Gyutaro"]) and (Time == False):
			e.npc.setHealth(e.npc.getHealth()-(e.damage*0.3))

		#Yahaba damage increase
		elif (AtkRole == "Yahaba") and (e.npc.world.getTempdata().get("YahabaKilledTarget") == True):
			e.npc.setHealth(e.npc.getHealth()-(e.damage*0.3))

		#Demon damage increase
		elif (AtkRole == "Demon") and (Time == False):
			Kills = e.npc.getStoreddata().get("Kills")
			if Kills == None:
				Kills = 0
			Damage = 0.3 + (0.03*Kills)
			e.npc.setHealth(e.npc.getHealth()-(e.damage*Damage))

		#Nezuko damage increase
		elif (AtkRole == "Nezuko") and (Time == False):
			e.npc.setHealth(e.npc.getHealth()-(e.damage*0.3))
	except:
		pass

def RoleEffects(e):
	"""
	Applying role effects
	"""
	Role = e.npc.getStoreddata().get("Role")
	Time = e.npc.world.isDay()
	if (Role == "Tanjiro") and (e.npc.world.getTempdata().get("TanjiroKilledTarget") == True):
		e.npc.say("Tanjiro killed his target")
		pass
	if (Role == "Tanjiro") and (e.npc.world.getTempdata().get("NezukoDied") == True):
		e.npc.addPotionEffect(18, 100000, 0, True)

	elif (Role == "Zenitsu"):
		if (e.npc.getHealth() >= 10):
			e.npc.addPotionEffect(18, 10, 0, True)
		else:
			e.npc.addPotionEffect(1, 10, 1, True)	

	elif (Role == "Inosuke") and (Time == False):
		e.npc.addPotionEffect(11, 10, 0, True)

	elif (Role == "Tomioka"):
		e.npc.addPotionEffect(1, 10, 1, True)
		if e.npc.world.getTempdata().get("SabitoDied") == True:
			e.npc.addPotionEffect(11, 10000, 0, True)

	elif (Role == "Shinobu"):
		e.npc.addPotionEffect(18, 10000, 0, True)

	elif (Role == "Kyojuro") or (Role == "Shinjuro"):
		e.npc.addPotionEffect(12, 10000, 0, True)
		e.npc.getStats().getMelee().setEffect(1,1,5)

	elif (Role == "Tengen"):
		e.npc.addPotionEffect(3, 10000, 0, True)
		e.npc.addPotionEffect(1, 10000, 0, True)

	elif (Role == "Sanemi"):
		if (Time == False):
			e.npc.addPotionEffect(1, 10, 1, True)
		else:
			e.npc.addPotionEffect(1, 10, 0, True)
	
	elif (Role == "Gyomei"):
		if (Time == False):
			e.npc.addPotionEffect(11, 10, 0, True)

	elif (Role == "Urokodaki"):
		if (Time == True):
			e.npc.addPotionEffect(1, 10, 0, True)

	elif (Role == "Sabito"):
		if (Time == False):
			e.npc.addPotionEffect(1, 10, 0, True)

	elif (Role == "Jigoro"):
		e.npc.addPotionEffect(1, 1000, 0, True)

	elif (Role == "Yoriichi"):
		e.npc.addPotionEffect(1, 1000, 0, True)
		if Time == True:
			e.npc.addPotionEffect(11, 10, 0, True)

	elif (Role == "Muzan"):
		e.npc.addPotionEffect(11, 1000, 0, True)
		if Time == True:
			e.npc.addPotionEffect(1, 10, 0, True)
		if e.npc.world.getTempdata().get("MuzanKilledNezuko") == True:
			e.npc.addPotionEffect(11, 1000, 1, True)

	elif (Role == "Nakime"):
		e.npc.addPotionEffect(18, 1000, 0, True)

	elif (Role == "Kokushibo"):
		e.npc.addPotionEffect(1, 1000, 0, True)

	elif (Role == "Daki") and (Time == True):
		e.npc.addPotionEffect(18, 10, 0, True)

	elif (Role == "Rui") and (Time == True):
		e.npc.addPotionEffect(18, 10, 0, True)		

	elif (Role == "Kaigaku"):
		e.npc.addPotionEffect(1, 10000, 0, True)
		if (Time == True) and (e.npc.world.getTempdata().get("KaigakuKilledZenitsu") == False):
			e.npc.addPotionEffect(18, 10, 0, True)

	elif (Role == "Furuto") and (Time == True):
		e.npc.addPotionEffect(18, 10, 0, True)

	elif (Role == "Demon") and (Time == True):
		e.npc.addPotionEffect(18, 10, 0, True)

def YoriichiAbso(e):
	"""
	Clearing abso on hit
	"""
	if e.npc.getStoreddata().get("Role") == "Yoriichi":
		if e.target.getType() == 1:
			e.npc.executeCommand("/effect "+str(e.target.getName())+" minecraft:absorption 0")
		else:
			e.target.addPotionEffect(22, 0, 0, True)

def YoriichiAbsoPlayer(e):
	"""
	Clearing abso when hit
	"""
	try:
		if e.source.getType() == 1:
			if e.npc.world.getStoreddata().get(str(e.source.getName())+"Role") == "Yoriichi":
				e.npc.addPotionEffect(22, 0, 0, True)
	except:
		pass


#ON DEATH ONLY functions :

def EnableDeathTimer(e):
	"""
	Start the death timer to show death after a period of time
	"""
	try:
		if (e.source.getType() == 1) or (e.source == None) or (e.npc.getStoreddata().get("Role") in ["Daki",'Gyutaro']):				#Only if killed by player
			e.npc.getTempdata().put("DeathTimer", 0)
		else:										#Else just count as dead and looted already
			DeathTchatMessage(e)
			e.npc.despawn()
	except:
		DeathTchatMessage(e)
		e.npc.despawn()

def DeathTimer(e):
	"""
	Tick the death timer after death
	"""
	try:			#To avoid error when not dead
		if (e.npc.getStoreddata().get("Role") == "Daki") and (e.npc.world.getTempdata().get("GyutaroDead") != True) and (e.npc.getTempdata().get("DeathTimer") == 60) and (e.npc.isAlive() == False):
			e.npc.setHealth(20)
			e.npc.getStats().setMaxHealth(e.npc.getStats().getMaxHealth()-2)
			e.npc.world.getTempdata().put("DakiDead", False)
			e.npc.getTempdata().put("DeathTimer", 0)
			e.npc.reset()

		elif (e.npc.getStoreddata().get("Role") == "Gyutaro") and (e.npc.world.getTempdata().get("DakiDead") != True) and (e.npc.getTempdata().get("DeathTimer") == 60) and (e.npc.isAlive() == False):
			e.npc.setHealth(20)
			e.npc.getStats().setMaxHealth(e.npc.getStats().getMaxHealth()-1)
			e.npc.world.getTempdata().put("GyutaroDead", False)
			e.npc.getTempdata().put("DeathTimer", 0)
			e.npc.reset()

		elif (e.npc.getStoreddata().get("Role") in ["Daki","Gyutaro"]) and ((e.npc.world.getTempdata().get("GyutaroDead") == True) and (e.npc.world.getTempdata().get("DakiDead") == True)):
			DeathTchatMessage(e)
			InventorySpawn(e)
			e.npc.despawn()

		elif (e.npc.getTempdata().get("DeathTimer") >= 10) and not (e.npc.getStoreddata().get("Role") in ["Daki","Gyutaro"]):				#Showing death message
			DeathTchatMessage(e)
			try:
				InventorySpawn(e)
			except Exception as err:
				e.npc.say(str(err))
			BleedingSweets(e)
			e.npc.despawn()
		else:
			e.npc.getTempdata().put("DeathTimer", e.npc.getTempdata().get("DeathTimer")+1)
	except Exception as err:
		pass

def RoleActualisation(e):
	"""
	Some utils for Daki and Gyutaro
	"""
	try:
		if e.source.getType() == 1:
			KillerRole = str(e.npc.world.getStoreddata().get(str(e.source.getName())+"Role"))
		else:
			KillerRole = str(e.source.getStoreddata().get("Role"))
	except:
		KillerRole = None
	Role = e.npc.getStoreddata().get("Role")

	if e.npc.getStoreddata().get("Role") == "Daki":
		e.npc.world.getTempdata().put("DakiDead", True)
	elif e.npc.getStoreddata().get("Role") == "Gyutaro":
		e.npc.world.getTempdata().put("GyutaroDead", True)
	elif (e.npc.getStoreddata().get("Role") == "Nezuko") and (KillerRole == 'Muzan'):
		e.npc.world.getTempdata().put("MuzanKilledNezuko", True)

def TeamsCounting(e):
	"""
	Know if team demon or village is eliminated
	"""
	GoodList = ["Tanjiro",
			"Zenitsu",
			"Inosuke",
			"Kagaya",
			"Tomioka",
			"Shinobu",
			"Kyojuro",
			"Tengen",
			"Muichiro",
			"Mitsuri",
			"Sanemi",
			"Obanai",
			"Gyomei",
			"Urokodaki",
			"Kanae",
			"Sabito",
			"Kanao",
			"Genya",
			"Hotaru",
			"Slayer",
			"Jigoro",
			"Yoriichi",
			"Shinjuro"]
	BadList = ["Muzan",
			"Nakime",
			"Kokushibo",
			"Doma",
			"Akaza",
			"Gyokko",
			"Daki",
			"Gyutaro",
			"Rui",
			"Kaigaku",
			"Sasumaru",
			"Kyogai",
			"Yahaba",
			"Kumo",
			"Furuto",
			"Nezuko",
			"Demon",
			]
	if (str(e.npc.getStoreddata().get("Role")) in BadList) or (e.npc.getTempdata().get("IsInfected") == True):
		e.npc.world.getTempdata().put("BadGroup", e.npc.world.getTempdata().get("BadGroup")-1)
		if e.npc.world.getTempdata().get("BadGroup") == 0:
			e.npc.world.getTempdata().put("TotalGroup", e.npc.world.getTempdata().get("TotalGroup")-1)
	else:
		e.npc.world.getTempdata().put("GoodGroup", e.npc.world.getTempdata().get("GoodGroup")-1)
		if e.npc.world.getTempdata().get("GoodGroup") == 0:
			e.npc.world.getTempdata().put("TotalGroup", e.npc.world.getTempdata().get("TotalGroup")-1)
#POST GAME functions :


#Misc


#================================#
#_______{ Calling Events }_______#
#================================#

def init(e):
	GameStarted = e.npc.world.getTempdata().get("GameStarted")
	if GameStarted == 1:
		GettingRole(e)

def damaged(e):
	DamageIncrease(e)
	YoriichiAbsoPlayer(e)
	TestingDeath(e)

def meleeAttack(e):
	YoriichiAbso(e)

def kill(e):
	KillingRole(e)

def died(e):
	InventorySpawn.isDone = False
	RoleActualisation(e)
	EnableDeathTimer(e)

def tick(e):
	GettingRole(e)
	DeathTimer(e)
	RoleEffects(e)

def interact(e):
	if e.player.getGamemode() == 1:
		e.npc.say(str(e.npc.getStoreddata().get("Role")))
	e.setCanceled(True)
	
def target(e):
	pass

def timer(e):			# Rod Block
	pass


    #============================#
    #___{ Credits and thanks }___#
    #============================#

#   Thanks to noppes for creating the CustomNPC mod
#   and to every people of the CustomNPC discord server
#   for helping me with commands and creating scripts

# /tellraw @a ["",{"text":"[","color":"dark_gray"},{"text":"Spec","color":"green"},{"text":"]","color":"dark_gray"},{"text":" ====","color":"dark_purple"},{"text":" / ","color":"dark_gray"},{"text":"====","color":"dark_purple"},{"text":" / ","color":"dark_gray"},{"text":"====","color":"dark_purple"},{"text":" /","color":"dark_gray"},{"text":" ====","color":"dark_purple"},{"text":" / ","color":"dark_gray"},{"text":"=======","color":"light_purple"},{"text":" /","color":"dark_gray"},{"text":" =======","color":"gold"}]