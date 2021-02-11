import random
import math
#API Link :http://www.kodevelopment.nl/customnpcs/api/1.8.9/
#Credits : Script UHC vs Bots Settings By Natsu91

#===================================#
#_______{ Creating Algorithm }______#
#===================================#

def DisplayStuff(e):
	if e.npc.getDisplay().getName() == "Melee mode":
		pass
	else:
		pass

def damaged(e):
	DisplayStuff(e)
	e.setCanceled(True)

def Despawn(e):
    if e.npc.world.getTempdata().get("InvMode") != True:
        e.npc.despawn()


def tick(e):
    Despawn(e)

def interact(e):
	e.setCanceled(True)


