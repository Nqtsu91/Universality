def SayingConfig(e):
	BotNumber = e.npc.world.getTempdata().get("BotNumber")
	TeamMode = e.npc.world.getTempdata().get("TeamSize")
	DiamondProba = e.npc.world.getTempdata().get("DiamondProbability")
	BadlionKillSystem = e.npc.world.getTempdata().get("BadlionKillsSystem")
	NoCleanUp = e.npc.world.getTempdata().get("NoCleanUpEnabled")
	e.npc.executeCommand('/tellraw @a ["",{"text":"BotNumber : '+str(BotNumber)+'","color": green,"bold":true},{"text":" TeamMode : '+str(TeamMode)+'","color": dark_green,"bold":true},{"text":" DiamondProbability : '+str(DiamondProba)+'","color": aqua,"bold":true},{"text":" BadlionMode : '+str(BadlionKillSystem)+'","color": red,"bold":true},{"text":" NoCleanUp : '+str(NoCleanUp)+'","color": gold,"bold":true}]')


def HelperSays(e):
	Text = "If you want to edit your game settings, just hit the NPCs next to the Host Game bot. Then read the text, and go to the other side where hitting the others NPCs will make you edit the values of your game. When youre done, just hit once the Host Game NPC, and then wait because it will freeze a bit. Then fight for glory of UHC !"
	e.npc.executeCommand('/tellraw @a ["",{"text":"'+str(Text)+'","color": pink,"bold":true}]')
	
def interact(e):
	if e.npc.getDisplay().getName() == "Helper" :
		HelperSays(e)
	else :
		SayingConfig(e)
		
		
		

