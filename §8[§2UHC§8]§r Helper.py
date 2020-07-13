def SayingConfig(e):
	Name = e.npc.world.getStoreddata().get("ConfigName")
	if Name == None :
		Name = "Unamed"

	List = ["BotNumber","TeamSize","DiamondProbability","NoCleanRegen","BleedingDiamonds","BleedingIron","BleedingGold","PvPTime","MinTimeSpread","MaxTimeSpread","MolePerTeam","FinalBorder","SecondBorder","FirstBorder","AppleRate","FlintRate","CutClean","BadlionKillsSystem","NoCleanUpEnabled","ThunderStrike","WitherSoundI","WitherSoundII","IronGolemSound","WaterAllowed","CatEyes","MasterLevel","SuperHeroes","BookCeption","DoubleHealth","OneShot","BleedingSweets","Rodless","Mole","RedditUHCDisplay","GoldenHeads","ExplodeOnDeath","FireAspectAllowed","AbsoLess","ForcedType","BadlionKB","ArcticMeta","ScatterMessageEnabled"]

	e.npc.executeCommand('/tellraw @a ["",{"text":"[","color":"dark_gray"},{"text":"UHC","color":"dark_red"},{"text":"][","color":"dark_gray"},{"text":"Config"},{"text":"]","color":"dark_gray"},{"text":" Displaying config ","color":"gray"},{"text":"'+str(Name)+'","color":"dark_purple"},{"text":" :","color":"gray"}]')
	for i in range(0, len(List)):
		e.npc.executeCommand('/tellraw @a ["",{"text":"[","color":"dark_gray"},{"text":"UHC","color":"dark_red"},{"text":"]","color":"dark_gray"},{"text":" - ","color":"gray"},{"text":"'+str(List[i])+'","color":"light_purple"},{"text":" : ","color":"gray"},{"text":"'+str(e.npc.world.getTempdata().get(List[i]))+'","color":"white"}]')


def HelperSays(e):
	Text = "If you want to edit your game settings, just hit the NPCs next to the Host Game bot. Then read the text, and go to the other side where hitting the others NPCs will make you edit the values of your game. When youre done, just hit once the Host Game NPC, and then wait because it will freeze a bit. Then fight for glory of UHC !"
	e.npc.executeCommand('/tellraw @a ["",{"text":"'+str(Text)+'","color": pink,"bold":true}]')
	
def interact(e):
	if e.npc.getDisplay().getName() == "Helper" :
		HelperSays(e)
	else :
		SayingConfig(e)
		
		
		

