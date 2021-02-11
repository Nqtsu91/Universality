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


#DEATH STYLE functions :


#ON KILL ONLY functions :	


#SCENARIOS functions :				


#TEAMER BOTS ONLY functions :


#IN GAME functions :

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
			ProtEffect = int(Prot[0]) * 0.01
			ProjEffect = int(Proj[0]) * 0.02
			MeleeResToSet += 0.1 + ProtEffect
			ProjToSet += 0.15 + ProjEffect
		else :
			ProtEffect = int(Prot[0]) * 0.01
			ProjEffect = int(Proj[0]) * 0.01
			MeleeResToSet += 0.08 + ProtEffect
			ProjToSet += 0.1 + ProjEffect
		

		if int(Armor[1]) == 1 :							# Diamond Chestplate
			ProtEffect = int(Prot[1]) * 0.01
			ProjEffect = int(Proj[1]) * 0.02
			MeleeResToSet += 0.4 + ProtEffect
			ProjToSet += 0.3 + ProjEffect
		else :
			ProtEffect = int(Prot[1]) * 0.01
			ProjEffect = int(Proj[1]) * 0.01
			MeleeResToSet += 0.3 + ProtEffect
			ProjToSet += 0.2 + ProjEffect


		if int(Armor[2]) == 1 :							# Diamond Leggings
			ProtEffect = int(Prot[2]) * 0.005
			ProjEffect = int(Proj[2]) * 0.02
			MeleeResToSet += 0.2 + ProtEffect
			ProjToSet += 0.15 + ProjEffect
		else :
			ProtEffect = int(Prot[2]) * 0.01
			ProjEffect = int(Proj[2]) * 0.01
			MeleeResToSet += 0.17 + ProtEffect
			ProjToSet += 0.2 + ProjEffect


		if int(Armor[3]) == 1 :							# Diamond Boots
			ProtEffect = int(Prot[3]) * 0.01
			ProjEffect = int(Proj[3]) * 0.02
			MeleeResToSet += 0.1 + ProtEffect
			ProjToSet += 0.15 + ProjEffect
		else :
			ProtEffect = int(Prot[3]) * 0.01
			ProjEffect = int(Proj[3]) * 0.01
			MeleeResToSet += 0.08 + ProtEffect
			ProjToSet += 0.1 + ProjEffect


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
		List = ["NoobTier","CasualTier","CommonTier","GoodTier"]            # List of non lava user
		if not e.npc.getTempdata().get("SelectedType") in List :  
			if (Dist <= 7) and (random.randint(0, 20) == 2) and (e.npc.getHealth() >= 10) and (e.npc.getTempdata().get("LavaTick") == 0):
				Target = e.npc.getAttackTarget()
				X = int(round(Target.getX()))
				Y = int(round(Target.getY()))
				Z = int(round(Target.getZ()))
				for i in range(0, 15):
					if e.npc.world.getBlock(X, Y-i, Z).getName() != "minecraft:air":
						i = 15
						e.npc.world.setBlock(X, Y-i, Z, "minecraft:lava", 0)
						e.npc.world.setBlock(X, Y-i, Z+1, "minecraft:lava", 1)
						e.npc.getTempdata().put("LavaTick", 2)
						e.npc.getTempdata().put("LavaCoord", [X, Y-i, Z])

	except Exception as err:
		pass

def RemoveLava(e):
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
		
		
def damaged(e):
	BreakingStuff(e)

def meleeAttack(e):
	pass

def kill(e):
	pass

def died(e):
	pass

def tick(e):
	if (e.npc.world.getTempdata().get("GameStarted") != 1) and (e.npc.getFaction().getId() != 26):
		e.npc.despawn()
		pass
	if (e.npc.world.getTempdata().get("GameStarted") == 1):
		UseLava(e)
		RemoveLava(e)


def interact(e):
	SpecDisplay(e)
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