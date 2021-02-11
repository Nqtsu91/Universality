

import random
import math
'''
def interact(e):
	e.npc.executeCommand('/tellraw @a ["",{"text":"[","color":"dark_gray"},{"text":"FFA","color":"dark_red"},{"text":"]","color":"dark_gray"},{"text":" Version : ","color":"gray"},{"text":"'+str(e.npc.getTempdata().get("FFAVersion"))+' ","color":"aqua"},{"text":"!","color":"dark_red"}]')


def interact(e):
	e.npc.say(str(e.npc.world.getStoreddata().get("KillList")))



def interact(e):
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


def kill(e):
	e.npc.say(str(e.entity))


def interact(e):
	e.npc.executeCommand('/tellraw @a ["",{"text":"    \u250c\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2510    \n\u2524\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u251c\n  "},{"text":"Thank you for downloading:","color":"aqua"},{"text":"\n         "},{"text":"Universality","bold":true,"color":"dark_red"},{"text":" !\n    Made by ","color":"gray"},{"text":"Natsu91","color":"gray","hoverEvent":{"action":"show_text","value":"Hey baguette !"}},{"text":" ! ","color":"gray"},{"text":"\u2588","color":"dark_blue"},{"text":"\u2588","color":"white"},{"text":"\u2588","color":"dark_red"},{"text":" \n         "},{"text":"Follow me on :\n      - ","color":"gray"},{"text":"Youtube","color":"red","clickEvent":{"action":"open_url","value":"https://www.youtube.com/channel/UCC11O0EUfQowZVu92RQZK8w"},"hoverEvent":{"action":"show_text","value":"Click here !"}},{"text":" \n      - ","color":"gray"},{"text":"Discord","color":"blue","clickEvent":{"action":"open_url","value":"https://discord.gg/XKhrjqs"},"hoverEvent":{"action":"show_text","value":"Click here"}},{"text":"\n\u2524\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u251c"}]')
	e.setCanceled(True)
	#e.npc.executeCommand("/scoreboard objectives setdisplay sidebar Arena")

def SpecDisplay(e):
	e.npc.getTempdata().put("GapCount", 32)

	e.npc.getStoreddata().put("Sword", '3/0/0/0')
	e.npc.getStoreddata().put("Prot", '2/2/3/2')
	e.npc.getStoreddata().put("Proj", '0/0/0/0')
	e.npc.getStoreddata().put("Armor", '1/1/0/1')
	e.npc.getStoreddata().put("Bow", '3/0/0/0')

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
	else:
		SwordType = "gray"

	if e.player.getGamemode() == 1:
		e.npc.executeCommand('/tellraw @a ["",{"text":"[","color":"dark_gray"},{"text":"Spec","color":"green"},{"text":"] ","color":"dark_gray"},{"text":"Prot '+str(Prot[0])+'","color":"'+str(PartI)+'"},{"text":" / ","color":"dark_gray"},{"text":"Prot '+str(Prot[1])+'","color":"'+str(PartII)+'"},{"text":" / ","color":"dark_gray"},{"text":"Prot '+str(Prot[2])+'","color":"'+str(PartIII)+'"},{"text":" / ","color":"dark_gray"},{"text":"Prot '+str(Prot[3])+'","color":"'+str(PartIV)+'"},{"text":" / ","color":"dark_gray"},{"text":"Sharp '+str(Sword[0])+'","color":"'+str(SwordType)+'"},{"text":" / ","color":"dark_gray"},{"text":"'+str(e.npc.getTempdata().get("GapCount"))+' Golden apple(s)","color":"gold"}]')


def interact(e):
	for i in range(57, 96):						# Terraforming
		e.npc.executeCommand('/fill -120 '+str(i)+' -120 120 '+str(i)+' 0 minecraft:air 0 replace minecraft:planks')
		e.npc.executeCommand('/fill -120 '+str(i)+' -120 120 '+str(i)+' 0 minecraft:air 0 replace minecraft:obsidian')
		e.npc.executeCommand('/fill -120 '+str(i)+' 0 120 '+str(i)+' 120 minecraft:air 0 replace minecraft:planks')
		e.npc.executeCommand('/fill -120 '+str(i)+' 0 120 '+str(i)+' 120 minecraft:air 0 replace minecraft:obsidian')
		e.npc.executeCommand('/fill -120 '+str(i)+' -120 120 '+str(i)+' 0 minecraft:air 0 replace minecraft:tallgrass')
		e.npc.executeCommand('/fill -120 '+str(i)+' 0 120 '+str(i)+' 120 minecraft:air 0 replace minecraft:tallgrass')
		e.npc.executeCommand('/fill -120 '+str(i)+' -120 120 '+str(i)+' 0 minecraft:air 0 replace minecraft:double_plant')
		e.npc.executeCommand('/fill -120 '+str(i)+' 0 120 '+str(i)+' 120 minecraft:air 0 replace minecraft:double_plant')
		e.npc.executeCommand('/fill -120 '+str(i)+' -120 120 '+str(i)+' 0 minecraft:air 0 replace minecraft:red_flower')
		e.npc.executeCommand('/fill -120 '+str(i)+' 0 120 '+str(i)+' 120 minecraft:air 0 replace minecraft:red_flower')		

def SharingArmor(e):
	try:
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
		FactionID = e.npc.getFaction().getId()
		if FactionID == 26 :
			Teaming(e)
			for i in range(0, 3):
				ArmorToGet = ["helmet",'chestplate',"leggings",'boots']
			if (e.player.getHeldItem().getName() == "minecraft:diamond_"+str(ArmorToGet[i])) and (str(Armor[i]) == "0"):
				Armor[i] = "1"
				e.npc.getInventory().setArmor(i,e.npc.world.createItem("minecraft:diamond_""minecraft:diamond_"+str(ArmorToGet[i]),0,1))
				e.npc.executeCommand('/tellraw @a ["",{"text":"[","color":"dark_gray"},{"text":"Team","color":"red"},{"text":"] ","color":"dark_gray"},{"text":"'+str(e.npc.getDisplay().getName())+'","color":"white"},{"text":":","color":"dark_gray"},{"text":" Thank ! ","color":"gray"}]')
				SettingResistance(e)
		else :
			pass
	except:
		pass


def interact(e):
	for i in range(57, 108):						# Terraforming
		e.npc.executeCommand('/fill -120 '+str(i)+' -120 120 '+str(i)+' 0 minecraft:air 0 replace minecraft:tallgrass')
		e.npc.executeCommand('/fill -120 '+str(i)+' -120 120 '+str(i)+' 0 minecraft:air 0 replace minecraft:tallgrass')
		e.npc.executeCommand('/fill -120 '+str(i)+' 0 120 '+str(i)+' 120 minecraft:air 0 replace minecraft:tallgrass')
		e.npc.executeCommand('/fill -120 '+str(i)+' -120 120 '+str(i)+' 0 minecraft:air 0 replace minecraft:double_plant')
		e.npc.executeCommand('/fill -120 '+str(i)+' 0 120 '+str(i)+' 120 minecraft:air 0 replace minecraft:double_plant')
		e.npc.executeCommand('/fill -120 '+str(i)+' -120 120 '+str(i)+' 0 minecraft:air 0 replace minecraft:cobblestone')
		e.npc.executeCommand('/fill -120 '+str(i)+' 0 120 '+str(i)+' 120 minecraft:air 0 replace minecraft:cobblestone')
		e.npc.executeCommand('/fill -120 '+str(i)+' -120 120 '+str(i)+' 0 minecraft:air 0 replace minecraft:obsidian')
		e.npc.executeCommand('/fill -120 '+str(i)+' 0 120 '+str(i)+' 120 minecraft:air 0 replace minecraft:obsidian')
		e.npc.executeCommand('/fill -120 '+str(i)+' -120 120 '+str(i)+' 0 minecraft:air 0 replace minecraft:planks')
		e.npc.executeCommand('/fill -120 '+str(i)+' 0 120 '+str(i)+' 120 minecraft:air 0 replace minecraft:planks')
		e.npc.executeCommand('/fill -120 '+str(i)+' 0 120 '+str(i)+' 120 minecraft:air 0 replace minecraft:planks')
		e.npc.executeCommand('/fill -120 '+str(i)+' -120 120 '+str(i)+' 0 minecraft:air 0 replace minecraft:fence')
		e.npc.executeCommand('/fill -120 '+str(i)+' -120 120 '+str(i)+' 0 minecraft:air 0 replace minecraft:planks')
		e.npc.executeCommand('/fill -120 '+str(i)+' 0 120 '+str(i)+' 120 minecraft:air 0 replace minecraft:fence')
		e.npc.executeCommand('/fill -120 '+str(i)+' -120 120 '+str(i)+' 0 minecraft:air 0 replace minecraft:skull')
		e.npc.executeCommand('/fill -120 '+str(i)+' 0 120 '+str(i)+' 120 minecraft:air 0 replace minecraft:skull')


def interact(e):
	"""
	e.npc.world.getStoreddata().put("Players", e.npc.world.getStoreddata().get("Players")+1)
	e.npc.world.getTempdata().put("PlayerDeads",e.npc.world.getTempdata().get("PlayerDeads")+1)
	A = e.npc.world.getTempdata().get("WinnerList")
    A.append(str(e.player.getName()))
    e.npc.world.getTempdata().put("WinnerList", A)
	"""
	"""
	e.npc.world.getStoreddata().put("TeamsAlive", e.npc.world.getStoreddata().get("TeamsAlive")+2)
	"""

	e.npc.world.getTempdata().put("EnchantProbability", 110)


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


import random
import math
def tick(e):
	try:
		if e.npc.getAttackTarget() != None :
			Target = e.npc.getAttackTarget()
			X = e.npc.getX()
			Z = e.npc.getZ()
			TX = Target.getX()
			TZ = Target.getZ()
			
			a = TX - X
			b = TZ - Z

			Dist = math.sqrt((a)**2 + (b)**2)
			e.npc.world.broadcast(str(Dist))
	except:
		pass



def UseLava(e):
	try:
		if (GetDist(e) <= 5) and (random.randint(0, 16) == 2) and (e.npc.getHealth() >= 10):
			Target = e.npc.getAttackTarget()
			X = int(round(Target.getX()))
			Y = int(round(Target.getY()))
			Z = int(round(Target.getZ()))
			e.npc.world.setBlock(X, Y, Z, "minecraft:lava", 0)
			e.npc.world.setBlock(X, Y, Z+1, "minecraft:lava", 1)
			e.npc.getTempdata().put("LavaTick", 2)
	except:
		pass
		
		





def damaged(e):
	try:
		Size = 20
		X = -30
		Y = 200
		Y2 = 205
		Z = 30
		Name = e.source.getName()
		e.npc.executeCommand('/fill '+str(X+(0.5*Size))+' '+str(Y)+' '+str(Z+(0.5*Size))+' '+str(X-(0.5*Size))+' '+str(Y)+' '+str(Z-(0.5*Size))+' minecraft:stained_glass')

		#e.npc.executeCommand('/fill 40 201 40 -40 205 20 minecraft:air')

		e.npc.executeCommand('/fill '+str(X+(0.5*Size))+' '+str(Y+1)+' '+str(Z+(0.5*Size))+' '+str(X+(0.5*Size))+' '+str(Y2)+' '+str(Z-(0.5*Size))+' minecraft:stained_glass_pane 13')
		e.npc.executeCommand('/fill '+str(X+(0.5*Size))+' '+str(Y+1)+' '+str(Z+(0.5*Size))+' '+str(X-(0.5*Size))+' '+str(Y2)+' '+str(Z+(0.5*Size))+' minecraft:stained_glass_pane 13')
		e.npc.executeCommand('/fill '+str(X-(0.5*Size))+' '+str(Y+1)+' '+str(Z-(0.5*Size))+' '+str(X+(0.5*Size))+' '+str(Y2)+' '+str(Z-(0.5*Size))+' minecraft:stained_glass_pane 13')
		e.npc.executeCommand('/fill '+str(X-(0.5*Size))+' '+str(Y+1)+' '+str(Z-(0.5*Size))+' '+str(X-(0.5*Size))+' '+str(Y2)+' '+str(Z+(0.5*Size))+' minecraft:stained_glass_pane 13')

		
	except Exception as err:
		e.npc.say(str(err))
		e.setCanceled(True)
		pass

def interact(e):
	e.npc.world.getStoreddata().put("TeamsAlive", e.npc.world.getStoreddata().get("TeamsAlive")+1)


def BreakingStuff(e):
	"""
	Making armor loose prot tier every 300 hits
	"""

	if e.npc.getTempdata().get("HitsTaken") == None :
		e.npc.getTempdata().put("HitsTaken", 1)

	elif e.npc.getTempdata().get("HitsTaken") == 250 :
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



def interact(e):
	e.npc.say("say")

def interact(e):
	e.npc.say("say2")


def interact(e):
	e.npc.say(str(e.player.getInventory()[0].getTag('ench')))


def tick(e):
	Players = e.npc.world.getAllPlayers()
	for i in range(0, len(Players)):
		for z in range(0, len(Players[i].getInventory())):
			try:
				if Players[i].getInventory()[z] != None:
					List = ["minecraft:iron_pickaxe","minecraft:iron_axe","minecraft:iron_shovel","minecraft:diamond_pickaxe","minecraft:diamond_axe","minecraft:diamond_shovel","minecraft:gold_pickaxe","minecraft:gold_axe","minecraft:gold_shovel","minecraft:stone_pickaxe","minecraft:stone_axe","minecraft:stone_shovel","minecraft:wooden_pickaxe","minecraft:wooden_axe","minecraft:wooden_shovel"]
					if (Players[i].getInventory()[z].getName() in List) and (Players[i].getInventory()[z].getTag('ench') == None):
						Stack = Players[i].getInventory()[z].getName()
						Players[i].removeAllItems(Players[i].getInventory()[z])
						e.npc.say(str(Stack))
						e.npc.executeCommand("/give "+str(Players[i].getName())+" "+str(Stack)+" 1 0 {ench:[{id:32,lvl:3},{id:34,lvl:2}]}")
			except Exception as ess:
				e.npc.say(str(ess))
				pass


def tick(e):
	e.npc.world.broadcast("YO A TOUS")



def tick(e):
	Players = e.npc.world.getAllPlayers()
	for i in range(0, len(Players)):
		Iron = e.npc.world.getScoreboard().getPlayerScore(str(Players[i].getName()), "HealTrigger", "")
		e.npc.say(str(Iron))



def interact(e):
	e.npc.world.spawnClone(120, 150, -120, 2, "Chunk").getStoreddata().clear()
	#e.npc.world.getStoreddata().clear()

#\xa7
#\u2500



def test():
	npc.executeCommand("/scoreboard objectives add Health health  "+u'\xa7'+"4"+u'\u2764')
	npc.executeCommand('/scoreboard objectives setdisplay belowName Health')
	


test()

import random





def damaged(e):
	pass
	Knocked(e)
	StopCombo(e)

def meleeAttack(e):
	Strafing(e)
	UpdatingReach(e)
	Combo(e)



def interact(e):
	e.npc.world.getTempdata().put("Players", e.npc.world.getTempdata().get("Players")+2)
	e.npc.world.getTempdata().put("TeamsAlive", e.npc.world.getTempdata().get("TeamsAlive")+2)

import random
import math
def Displaying(e):
	if e.npc.getStoreddata().get("OneSecTick") != 1:
		Time = e.npc.world.getTotalTime()
		if e.npc.getStoreddata().get("AllSec") == None:
			e.npc.getStoreddata().put("AllSec", 0)
		else:
			pass
		#OBJLIST = [10*60, None, 8*60]11
		OBJLIST = [10*60, None, None, None, int(e.npc.world.getTempdata().get("PvPTime"))*60, None, None, None, None, None, "Players"]
		e.npc.executeCommand('/scoreboard players set __'+u'\xa7'+'8['+u'\xa7'+'4Players'+u'\xa7'+'8]'+u'\xa7'+'r__ Kills 12')
		e.npc.executeCommand('/scoreboard players set '+u'\xa7'+'1 Kills -1')
		e.npc.executeCommand('/scoreboard players set '+u'\xa7'+'2 Kills 99')
		e.npc.executeCommand('/scoreboard players set '+u'\xa7'+'7BotUHC_by_'+u'\xa7'+'cNatsu91'+u'\xa7'+'r Kills -2')
		e.npc.executeCommand('/scoreboard players set '+u'\xa7'+'c Kills 10')
		e.npc.executeCommand('/scoreboard players set '+u'\xa7'+'5 Kills 6')
		e.npc.executeCommand('/scoreboard players set __'+u'\xa7'+'8['+u'\xa7'+'4FinalHeal'+u'\xa7'+'8]'+u'\xa7'+'r__ Kills 1')
		e.npc.executeCommand('/scoreboard players set '+u'\xa7'+'3 Kills 2')
		e.npc.executeCommand('/scoreboard players set __'+u'\xa7'+'8['+u'\xa7'+'4PvP'+u'\xa7'+'8]'+u'\xa7'+'r__ Kills 5')
		e.npc.executeCommand('/scoreboard players set __'+u'\xa7'+'8['+u'\xa7'+'4Border'+u'\xa7'+'8]'+u'\xa7'+'r__ Kills 9')



		BorderList = ["FirstBorder","SecondBorder","FinalBorder"]
		if int(e.npc.world.getTempdata().get("FirstBorder"))*60 - e.npc.getStoreddata().get("AllSec") <= 0:
			if int(e.npc.world.getTempdata().get("SecondBorder"))*60 - e.npc.getStoreddata().get("AllSec") <= 0:
				if int(e.npc.world.getTempdata().get("FinalBorder"))*60 - e.npc.getStoreddata().get("AllSec") <= 0:
					e.npc.executeCommand('/scoreboard players set '+u'\xa7'+'6Enabled Kills 8')
				else:
					OBJLIST.insert(7, int(e.npc.world.getTempdata().get("FinalBorder"))*60)
			else:
				OBJLIST.insert(7, int(e.npc.world.getTempdata().get("SecondBorder"))*60)
		else:
			OBJLIST.insert(7, int(e.npc.world.getTempdata().get("FirstBorder"))*60)

		if int(e.npc.world.getTempdata().get("PvPTime"))*60 - e.npc.getStoreddata().get("AllSec") <= 0:
			e.npc.executeCommand('/scoreboard players set '+u'\xa7'+'2Enabled Kills 3')

		e.npc.executeCommand('/scoreboard players reset 0:0:0')
		
		if e.npc.getStoreddata().get("AllSec") >= 10*60:
			e.npc.executeCommand('/scoreboard players reset __'+u'\xa7'+'8['+u'\xa7'+'4FinalHeal'+u'\xa7'+'8]'+u'\xa7'+'r__')

		for i in range(0, len(OBJLIST)):
			if OBJLIST[i] != None:
				if OBJLIST[i] == "Players":
					Obj = str(int(e.npc.world.getTempdata().get("Players"))+1)+'/'+str(int(e.npc.world.getTempdata().get("PlayersMax")))
					e.npc.executeCommand('/scoreboard players reset '+str(Obj)+' Kills')
					Obj = str(int(e.npc.world.getTempdata().get("Players")))+'/'+str(int(e.npc.world.getTempdata().get("PlayersMax")))
					e.npc.executeCommand('/scoreboard players set '+str(Obj)+' Kills '+str(i)+'')

				else: 
					if (OBJLIST[i] - e.npc.getStoreddata().get("AllSec") <= 0):
						Value = OBJLIST[i] - e.npc.getStoreddata().get("AllSec")
						Obj = str(int(Value//3600))+':'+str(int(Value//60))+':'+str(int(Value%60))
						e.npc.executeCommand('/scoreboard players reset '+str(Obj)+' Kills')

					else:
						Value = (OBJLIST[i] - e.npc.getStoreddata().get("AllSec"))
						Obj = str(int(Value//3600))+':'+str(int(Value//60))+':'+str(int(Value%60))
						e.npc.executeCommand('/scoreboard players reset '+str(Obj)+' Kills')
						
						Value -= 1
						Obj = str(int(Value//3600))+':'+str(int(Value//60))+':'+str(int(Value%60))
						
						e.npc.executeCommand('/scoreboard players set '+str(Obj)+' Kills '+str(i)+'')

		e.npc.getStoreddata().put("AllSec", e.npc.getStoreddata().get("AllSec")+1)
		e.npc.getStoreddata().put("OneSecTick", 1)
	else:
		e.npc.getStoreddata().put("OneSecTick", 0)

def tick(e):
	try:
		Displaying(e)
	except Exception as err:
		e.npc.say(str(err))
		pass

def interact(e):
	e.npc.executeCommand("/scoreboard objectives add Kills dummy "+u'\xa7'+"4"+u'\xa7'+"l Universality UHC")
	e.npc.executeCommand("/scoreboard objectives setdisplay sidebar Kills")
	e.npc.world.getTempdata().put("PvPTime", 1)
	e.npc.world.getTempdata().put("FirstBorder", 2)
	e.npc.world.getTempdata().put("SecondBorder", 3)
	e.npc.world.getTempdata().put("FinalBorder", 4)
	e.npc.world.getTempdata().put("Players", 15)
	e.npc.world.getTempdata().put("PlayersMax", 15)

def damaged(e):
	e.npc.world.getTempdata().put("Players", e.npc.world.getTempdata().get("Players")-1)
	e.npc.world.getTempdata().put("PlayersMax", 15)


def interact(e):
	e.npc.say(str(e.npc.world.getTempdata().get("AnvilTicks")))




def interact(e):
	#a = "§rTest"
	#e.npc.getDisplay().setName(a)
	Name = e.npc.getDisplay().getName()
	Name = list(Name)
	Name.pop(0)
	Name.pop(0)
	Name = "".join(Name)
	e.npc.getDisplay().setName(str(Name))


def interact(e):
	e.npc.getStats().noFallDamage

'''
a = ["a","a"]
a.remove("a")
print(a)

def TimeBomb(e):
	"""
	Summons a chest filled with NPC's inventory

	- Chest not exploding for now
	"""
	IsEnchanted = True
	if e.npc.world.getTempdata().get("TimeBomb") == True:
		e.npc.executeCommand("/fill ~ ~+1 ~+1 ~ ~+1 ~ minecraft:air")			# Spawning a chest at death coordinates
		e.npc.executeCommand("/fill ~ ~ ~+1 ~ ~ ~ minecraft:chest")
		X = e.npc.getX()												# Saving coordinates
		Y = e.npc.getY()
		Z = e.npc.getZ()
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

			if (int(Prot[i]) ==0) and (int(Proj[i]) == 0):
				IsEnchanted = False
			
			Count = 1
			Tag = '{ench:[{id:'+str(EnchID)+',lvl:'+str(EnchLvL)+'}]}'		# Compilating everithing into a tag, then into a command

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
		if (GoldenAppleLoot == None) or (GoldenAppleLoot == 0):
			GoldenAppleLoot = 1

		Item = "minecraft:golden_apple"
		Damage = 0
		Count = GoldenAppleLoot
		Tag = ""
		Com = '/replaceitem block '+str(X)+' '+str(Y)+' '+str(Z)+' slot.container.'+str(SlotCounter)+' '+str(Item)+' '+str(Count)+' '+str(Damage)+' '+str(Tag)+''
		SlotCounter += 1
		e.npc.executeCommand(str(Com))



		# Adding some blocks and other stuff
		if (int(e.npc.world.getStoreddata().get("TeamsAlive")) > 12 ) and (e.npc.world.getTempdata().get("ClearedLoot") != True):
			ItemList = [["minecraft:cobblestone","64"],["minecraft:cobblestone","64"],["minecraft:cobblestone","64"],["minecraft:cobblestone","64"],["minecraft:apple","3"],["minecraft:cooked_beef","64"],["minecraft:cobblestone","64"],["minecraft:cobblestone","64"],["minecraft:cobblestone","64"],["minecraft:cobblestone","64"],["minecraft:cobblestone","64"],["minecraft:log","64"],["minecraft:water_bucket","1"],["minecraft:water_bucket","1"],["minecraft:water_bucket","1"],["minecraft:lava_bucket","1"],["minecraft:fishing_rod","1"],["minecraft:book","2"],["minecraft:flint_and_steel","1"],["minecraft:planks","64"],["minecraft:anvil","1"],["minecraft:enchanting_table","1"],["minecraft:wheat_seeds","12"],["minecraft:string","1"],["minecraft:coal","20"],["minecraft:flint","16"],["minecraft:dirt","64"],["minecraft:leather","11"],["minecraft:reeds","15"],["minecraft:feather","4"],["minecraft:gunpowder","2"],["minecraft:sand","64"],["minecraft:gravel","64"],["minecraft:sapling","16"],["minecraft:red_flower","6"],["minecraft:torch","64"],["minecraft:redstone","64"],["minecraft:bone","3"]]																			
		else:
			ItemList = [["minecraft:cobblestone","64"],["minecraft:cobblestone","64"],["minecraft:cobblestone","64"],["minecraft:log","64"],["minecraft:water_bucket","1"],["minecraft:water_bucket","1"],["minecraft:water_bucket","1"],["minecraft:lava_bucket","1"],["minecraft:fishing_rod","1"],["minecraft:flint_and_steel","1"],["minecraft:planks","64"],["minecraft:anvil","1"],["minecraft:enchanting_table","1"]]																			

		for i in range(0, len(ItemList)-1):	
			Count = random.randint(1,int(ItemList[i][1]))
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

def HasteyBoys(e):
    if True:
        Players = e.npc.world.getAllPlayers()
        for i in range(0, len(Players)):
            for z in range(0, len(Players[i].getInventory())):
                try:
                    if Players[i].getInventory()[z] != None:
                        e.npc.say(str(Players[i].getInventory()[z].getTag('ench')))
                        List = ["minecraft:iron_pickaxe","minecraft:iron_axe","minecraft:iron_shovel","minecraft:diamond_pickaxe","minecraft:diamond_axe","minecraft:diamond_shovel","minecraft:gold_pickaxe","minecraft:gold_axe","minecraft:gold_shovel","minecraft:stone_pickaxe","minecraft:stone_axe","minecraft:stone_shovel","minecraft:wooden_pickaxe","minecraft:wooden_axe","minecraft:wooden_shovel"]
                        if (Players[i].getInventory()[z].getName() in List) and (Players[i].getInventory()[z].getTag('ench') == None):
                            Ench = '{ench:[{id:32,lvl:3},{id:34,lvl:2}]}'
                            e.npc.executeCommand('/replaceitem entity '+str(Players[i].getName())+' slot.container.'+str(int(round(z)))+' '+str(Players[i].getInventory()[z].getName())+' 1 0 '+str(Ench)+'')
                            #e.npc.executeCommand("/give "+str(Players[i].getName())+" "+str(Stack)+" 1 0 {ench:[{id:32,lvl:3},{id:34,lvl:2}]}")
                except Exception as ess:
                    e.npc.say(str(ess))
                    pass


def damaged(e):
	HasteyBoys(e)


def InventorySpawn(e) :
	'''Spawn the whole inventory of the bot depending of the Kills amount he had, double armor drops if he was stacked

		EXCEPTION : if OneShot is enabled, stuff dont drop
	'''
	IsEnchanted = True
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
				GoldenAppleLoot = 1
			e.npc.executeCommand("/summon Item "+str(MyX)+" "+str(MyY)+" "+str(MyZ)+" {Item:{id:322,Damage:0,Count:"+str(GoldenAppleLoot)+"},Motion:["+str(random.uniform(0.02,0.1)*random.randint(-1,1))+",0.09,"+str(random.uniform(0.02,0.1)*random.randint(-1,1))+"]}") # Looting golden apple based on the amount he had
			if IsEnchanted == True:
				e.npc.executeCommand("/summon Item "+str(MyX)+" "+str(MyY)+" "+str(MyZ)+" {Item:{id:278,Damage:187,Count:1,tag:{ench:[{id:32,lvl:5}]}},Motion:["+str(random.uniform(0.02,0.1)*random.randint(-1,1))+",0.09,"+str(random.uniform(0.02,0.1)*random.randint(-1,1))+"]}")		# Looting a pickaxe
			try:
				e.npc.executeCommand("/xp 40 "+ str(e.source.getName()))		# Looting xp
			except :
				pass

		if e.npc.getStoreddata().get("Kills") >= 4 and (InventorySpawn.isDone != True ):
			InventorySpawn.isDone = True
			InventorySpawn(e)

import random
def died(e):
	TimeBomb(e)



def AutoAssign(e):
	"""Automatically assign the last teams alive
	"""
	if e.npc.world.getStoreddata().get(str(e.npc.getFaction().getId())+"AssignedTeam") == None:
		NearBots = e.npc.world.getNearbyEntities(int(e.npc.getX()), int(e.npc.getY()), int(e.npc.getZ()), 8, 2).tolist()
		NearPlayers = e.npc.world.getNearbyEntities(int(e.npc.getX()), int(e.npc.getY()), int(e.npc.getZ()), 8, 1).tolist()
		if e.npc.world.getTempdata().get("PlayersAssignedTeam") == None:
			e.npc.world.getTempdata().put("PlayersAssignedTeam", int(round(e.npc.getFaction().getId())))
			e.npc.world.getStoreddata().put(str(e.npc.getFaction().getId())+"AssignedTeam", -1)
		else:
			for i in range(len(NearBots)-1, -1, -1):
				if (NearBots[i].getFaction().getId() == e.npc.getFaction().getId()) or (e.npc.world.getStoreddata().get(str(NearBots[i].getFaction().getId())+"AssignedTeam") != None):
					NearBots.pop(i)
				else:
					pass
			e.npc.world.getTempdata().put(str(e.npc.getFaction().getId())+"AssignedTeam", int(round(NearBots[0].getFaction().getId())))
			e.npc.world.getStoreddata().put(str(NearBots[i].getFaction().getId())+"AssignedTeam", int(round(e.npc.getFaction().getId())))
		


def interact(e):
	A = ["Aulioh","Natsu91","Nardcoo","AtReaLity","jdegoederen","ZMCNikolai","Blocksssssss","HeyGh0st"]
	e.npc.world.getTempdata().put("WinnerList", A)
	e.npc.world.getTempdata().put("AssignDone", None)
	e.npc.world.getTempdata().put("AssignEnabled", None)

def tick(e):
	AutoAssign(e)

def interact(e):
	e.npc.say(str(A))
	e.npc.say(str(B))

def interact(e):
	e.npc.say(str(e.npc.getStoreddata().put("Proj")))

def IsObsitraped(e):
	try:
		X = e.npc.getX()
		Y = e.npc.getY()
		Z = e.npc.getZ()
		if e.npc.world.getBlock(int(round(X)), int(round(Y)+1), int(round(Z))).getName() == "minecraft:obsidian":
			e.npc.say("Yo a tous")
	except Exception as err:
		e.npc.say(str(err))
		pass

def AntiLock(e):
	try:
		X = e.npc.getX()
		Y = e.npc.getY()
		Z = e.npc.getZ()
		VoidList = ["minecraft:tallgrass","minecraft:red_flower",None]
		#e.npc.say(str(e.npc.world.getBlock(int(round(X)), int(round(Y)), int(round(Z))).getName()))
		if e.npc.world.getBlock(int(round(X)), int(round(Y)), int(round(Z))).getName() in VoidList:
			e.npc.say("Yo a tous")
	except Exception as err:
		e.npc.say(str(err))
		pass

def tick(e):
	IsObsitraped(e)
	AntiLock(e)

def BadlionKB(e):
	'''Reduce knockbcak to force melee
	'''
	e.npc.getStats().setResistance(3, (1 + (abs(int(e.npc.world.getTempdata().get("KBValue")))/100)))

import random
def interact(e):
	for i in range(-240, 250, 10):
		for j in range(-240, 250, 10):
			e.npc.executeCommand('/setblock '+str(i)+' 250 '+str(j)+' simplechunkloader:tile.simplechunkloader')
