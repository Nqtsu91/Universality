def SayingConfig(e):
	Name = e.npc.world.getStoreddata().get("ConfigName")
	if Name == None :
		Name = "Unamed"

	List = ["TeamSize","TeamAliveLimit","NoCleanUpEnabled","CatEyes","Rodless","AbsoLess","WaterAllowed","ForcedType","BadlionKB","RedditUHCDisplay","BadlionKillsSystem","ThunderStrike","WitherSoundI","WitherSoundII","IronGolemSound","VanillaDeathStyle","ExplodeOnDeath","ScatterMessageEnabled","NoCleanRegen"]

	e.npc.executeCommand('/tellraw '+str(e.player.getName())+' ["",{"text":"[","color":"dark_gray"},{"text":"Arena","color":"dark_red"},{"text":"][","color":"dark_gray"},{"text":"Config"},{"text":"]","color":"dark_gray"},{"text":" Displaying config ","color":"gray"},{"text":"'+str(Name)+'","color":"dark_purple"},{"text":" :","color":"gray"}]')
	for i in range(0, len(List)):
		Color = "white"
		if str(e.npc.world.getTempdata().get(List[i])) == "True":
			Color = "green"
		elif str(e.npc.world.getTempdata().get(List[i])) == "False":
			Color = "red"
		elif str(e.npc.world.getTempdata().get(List[i])) == "None" :
			Color = "black"
		e.npc.executeCommand('/tellraw '+str(e.player.getName())+' ["",{"text":"[","color":"dark_gray"},{"text":"Arena","color":"dark_red"},{"text":"]","color":"dark_gray"},{"text":" - ","color":"gray"},{"text":"'+str(List[i])+'","color":"light_purple"},{"text":" : ","color":"gray"},{"text":"'+str(e.npc.world.getTempdata().get(List[i]))+'","color":"'+str(Color)+'"}]')


def HelperSays(e):
	e.npc.executeCommand('/tellraw '+str(e.player.getName())+' ["",{"text":"[","color":"dark_gray"},{"text":"Arena","color":"dark_red"},{"text":"][","color":"dark_gray"},{"text":"Help","color":"dark_green"},{"text":"]","color":"dark_gray"},{"text":" - Just hit the config bots to see their effects.","color":"gray"},{"text":"\n"},{"text":"[","color":"dark_gray"},{"text":"Arena","color":"dark_red"},{"text":"][","color":"dark_gray"},{"text":"Help","color":"dark_green"},{"text":"]","color":"dark_gray"},{"text":" - Right click the Config loader to load a config. ","color":"gray"},{"text":"\n"},{"text":"[","color":"dark_gray"},{"text":"Arena","color":"dark_red"},{"text":"][","color":"dark_gray"},{"text":"Help","color":"dark_green"},{"text":"]","color":"dark_gray"},{"text":" - Hit him to change the config slot ","color":"gray"},{"text":"\n"},{"text":"[","color":"dark_gray"},{"text":"Arena","color":"dark_red"},{"text":"][","color":"dark_gray"},{"text":"Help","color":"dark_green"},{"text":"]","color":"dark_gray"},{"text":" - Right click the Inventory loader to load a config. ","color":"gray"},{"text":"\n"},{"text":"[","color":"dark_gray"},{"text":"Arena","color":"dark_red"},{"text":"][","color":"dark_gray"},{"text":"Help","color":"dark_green"},{"text":"]","color":"dark_gray"},{"text":" - Hit him to change the config slot ","color":"gray"},{"text":"\n"},{"text":"[","color":"dark_gray"},{"text":"Arena","color":"dark_red"},{"text":"][","color":"dark_gray"},{"text":"Help","color":"dark_green"},{"text":"]","color":"dark_gray"},{"text":" - Right click the Host to change the Team file slot.","color":"gray"},{"text":"\n"},{"text":"[","color":"dark_gray"},{"text":"Arena","color":"dark_red"},{"text":"][","color":"dark_gray"},{"text":"Help","color":"dark_green"},{"text":"]","color":"dark_gray"},{"text":" - Hit him to start the game. ","color":"gray"}]')
	
def interact(e):
	if e.npc.getDisplay().getName() == "Helper" :
		HelperSays(e)
	else :
		SayingConfig(e)
		
		
		
def damaged(e):
	e.setCanceled(True)



