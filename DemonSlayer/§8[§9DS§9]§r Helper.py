def SayingConfig(e):
	Name = e.npc.world.getStoreddata().get("ConfigName")
	if Name == None :
		Name = "Unamed"

	List = ["BotNumber","NoCleanRegen","BleedingDiamonds","BleedingIron","BleedingGold","PvPTime","FinalBorder","SecondBorder","FirstBorder","AppleRate","FlintRate","CutClean","NoCleanUpEnabled","ThunderStrike","WitherSoundI","WitherSoundII","IronGolemSound","WaterAllowed","CatEyes","MasterLevel","SuperHeroes","BookCeption","DoubleHealth","OneShot","BleedingSweets","Rodless","GoldenHeads","ExplodeOnDeath","AbsoLess","ForcedType","BadlionKB","ArcticMeta","LoadTeams"]

	#
	Com = '/tellraw '+str(e.player.getName())+' ["",{"text":"[","color":"dark_gray"},{"text":"DS","color":"dark_red"},{"text":"]","color":"dark_gray"},{"text":" - ","color":"gray"},{"text":"'+str(Name)+'","color":"dark_purple"},{"text":"\n"},{"text":"[","color":"dark_gray"},{"text":"DS","color":"dark_red"},{"text":"] ","color":"dark_gray"},{"text":"----| ","color":"gray"},{"text":"Players","color":"dark_aqua"},{"text":" |----","color":"gray"}]'
	e.npc.executeCommand(Com)

	List = ["BotNumber","TeamSize"]
	for i in range(0, len(List)):
		Com = '/tellraw @a ["",{"text":"[","color":"dark_gray"},{"text":"DS","color":"dark_red"},{"text":"]","color":"dark_gray"},{"text":" - ","color":"gray"},{"text":"'+str(List[i])+'","color":"aqua"},{"text":" : ","color":"gray"},{"text":"'+str(e.npc.world.getTempdata().get(str(List[i])))+'","color":"white"}]'
		e.npc.executeCommand(Com)

	Com = '/tellraw '+str(e.player.getName())+' ["",{"text":"[","color":"dark_gray"},{"text":"DS","color":"dark_red"},{"text":"] ","color":"dark_gray"},{"text":"----| ","color":"gray"},{"text":"Timers","color":"dark_aqua"},{"text":" |----","color":"gray"}]'
	e.npc.executeCommand(Com)

	List = ["PvPTime","FirstBorder","SecondBorder","FinalBorder"]
	for i in range(0, len(List)):
		Com = '/tellraw @a ["",{"text":"[","color":"dark_gray"},{"text":"DS","color":"dark_red"},{"text":"]","color":"dark_gray"},{"text":" - ","color":"gray"},{"text":"'+str(List[i])+'","color":"aqua"},{"text":" : ","color":"gray"},{"text":"'+str(e.npc.world.getTempdata().get(str(List[i])))+'","color":"white"}]'
		e.npc.executeCommand(Com)

	Com = '/tellraw '+str(e.player.getName())+' ["",{"text":"[","color":"dark_gray"},{"text":"DS","color":"dark_red"},{"text":"] ","color":"dark_gray"},{"text":"----| ","color":"gray"},{"text":"Scenarios","color":"dark_aqua"},{"text":" |----","color":"gray"}]'
	e.npc.executeCommand(Com)

	List = ["TimeBomb","TimeBombExplode","TimeBombTime","CutClean","NoCleanUpEnabled","HasteyBoys","CatEyes","MasterLevel","SuperHeroes","DoubleHealth","BleedingSweets","Rodless","Mole"]
	for i in range(0, len(List)):
		Com = '/tellraw @a ["",{"text":"[","color":"dark_gray"},{"text":"DS","color":"dark_red"},{"text":"]","color":"dark_gray"},{"text":" - ","color":"gray"},{"text":"'+str(List[i])+'","color":"aqua"},{"text":" : ","color":"gray"},{"text":"'+str(e.npc.world.getTempdata().get(str(List[i])))+'","color":"white"}]'
		e.npc.executeCommand(Com)

	Com = '/tellraw '+str(e.player.getName())+' ["",{"text":"[","color":"dark_gray"},{"text":"DS","color":"dark_red"},{"text":"] ","color":"dark_gray"},{"text":"----| ","color":"gray"},{"text":"Other infos","color":"dark_aqua"},{"text":" |----","color":"gray"}]'
	e.npc.executeCommand(Com)

	List = ["FireAspectAllowed","GoldenHeads","AbsoLess","AppleRate","FlintRate"]
	for i in range(0, len(List)):
		Com = '/tellraw @a ["",{"text":"[","color":"dark_gray"},{"text":"DS","color":"dark_red"},{"text":"]","color":"dark_gray"},{"text":" - ","color":"gray"},{"text":"'+str(List[i])+'","color":"aqua"},{"text":" : ","color":"gray"},{"text":"'+str(e.npc.world.getTempdata().get(str(List[i])))+'","color":"white"}]'
		e.npc.executeCommand(Com)



def HelperSays(e):
	e.npc.executeCommand('/tellraw '+str(e.player.getName())+' ["",{"text":"[","color":"dark_gray"},{"text":"DS","color":"dark_red"},{"text":"][","color":"dark_gray"},{"text":"Help","color":"dark_green"},{"text":"]","color":"dark_gray"},{"text":" - Just hit the config bots to see their effects.","color":"gray"},{"text":"\n"},{"text":"[","color":"dark_gray"},{"text":"DS","color":"dark_red"},{"text":"][","color":"dark_gray"},{"text":"Help","color":"dark_green"},{"text":"]","color":"dark_gray"},{"text":" - Right click the Config loader to load a config. ","color":"gray"},{"text":"\n"},{"text":"[","color":"dark_gray"},{"text":"DS","color":"dark_red"},{"text":"][","color":"dark_gray"},{"text":"Help","color":"dark_green"},{"text":"]","color":"dark_gray"},{"text":" - Hit him to change the config slot ","color":"gray"},{"text":"\n"},{"text":"[","color":"dark_gray"},{"text":"DS","color":"dark_red"},{"text":"][","color":"dark_gray"},{"text":"Help","color":"dark_green"},{"text":"]","color":"dark_gray"},{"text":" - Right click the Inventory loader to load a config. ","color":"gray"},{"text":"\n"},{"text":"[","color":"dark_gray"},{"text":"DS","color":"dark_red"},{"text":"][","color":"dark_gray"},{"text":"Help","color":"dark_green"},{"text":"]","color":"dark_gray"},{"text":" - Hit him to change the config slot ","color":"gray"},{"text":"\n"},{"text":"[","color":"dark_gray"},{"text":"DS","color":"dark_red"},{"text":"][","color":"dark_gray"},{"text":"Help","color":"dark_green"},{"text":"]","color":"dark_gray"},{"text":" - Right click the Host to change the Team file slot.","color":"gray"},{"text":"\n"},{"text":"[","color":"dark_gray"},{"text":"DS","color":"dark_red"},{"text":"][","color":"dark_gray"},{"text":"Help","color":"dark_green"},{"text":"]","color":"dark_gray"},{"text":" - Hit him to start the game. ","color":"gray"}]')
	
def interact(e):
	if e.npc.getDisplay().getName() == "Helper" :
		HelperSays(e)
	else :
		SayingConfig(e)
		
	e.setCanceled(True)
		
		
def damaged(e):
	e.setCanceled(True)



