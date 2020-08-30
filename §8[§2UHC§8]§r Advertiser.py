def SayingConfig(e):
	pass

def interact(e):
	if e.npc.getDisplay().getName() == "Discord" :
		e.npc.executeCommand('/tellraw @a ["",{"text":"[","color":"gray"},{"text":"Dev","color":"gold"},{"text":"]","color":"gray"},{"text":"Natsu91 ","color":"red"},{"text":": Join my ","color":"gray"},{"text":"Discord","color":"blue","clickEvent":{"action":"open_url","value":"https://discord.gg/XKhrjqs"}},{"text":" to ask any question about ","color":"gray"},{"text":"Universality !","color":"dark_red"}]')
	elif e.npc.getDisplay().getName() == "Youtube" :
		e.npc.executeCommand('/tellraw @a ["",{"text":"[","color":"gray"},{"text":"Dev","color":"gold"},{"text":"]","color":"gray"},{"text":"Natsu91 ","color":"red"},{"text":": See my ","color":"gray"},{"text":"Youtube Channel","color":"dark_red","clickEvent":{"action":"open_url","value":"https://www.youtube.com/channel/UCC11O0EUfQowZVu92RQZK8w"}},{"text":" to see every update !","color":"gray"}]')
	e.setCanceled(True)
		
		
def damaged(e):
	e.setCanceled(True)