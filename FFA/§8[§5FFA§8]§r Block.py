import random
import math
#API Link :http://www.kodevelopment.nl/customnpcs/api/1.8.9/
#Credits : Script UHC vs Bots BotScatteringV4 By Natsu91

#===================================#
#_______{ Creating Algorithm }______#
#===================================#

def CheckTimer(e):
    
    NeedStop = e.npc.world.getTempdata().get("NeedStop")
    if NeedStop == None :
        e.npc.despawn()

    Factions = e.npc.world.getStoreddata().get("Factions")
    #e.npc.say("&1=====================")
    #e.npc.say("&5MeetUp : " + str(MeetUp))
    #e.npc.say("&4Time : " + str(e.npc.world.getTotalTime()))
    #e.npc.say("&6SpawnChoice : " + str(e.npc.getTempdata().get("Spawn")))
    #e.npc.say("&1Players left : "+ str(e.npc.world.getStoreddata().get("BotsToSpawn")))
    #e.npc.say("&bPlayers left : "+ str(Players))

    TeamMode = e.npc.world.getTempdata().get("TeamSize")
    Factions = Factions.split("/")
    if len(Factions) >= 2 and Factions[0] == '':
        Factions.pop(0)
    try :
        Test = int(Factions[0])


        if True :
            try :
                if len(Factions) != 0:                      # If there is empty faction 
                    IdHere = random.choice(Factions)
                    Factions.remove(IdHere)
                    Factions = "/".join(Factions)                           # Deleting the faction from the list
                    e.npc.world.getStoreddata().put("Factions", str(Factions))    
                    X = e.npc.getX()
                    Z = e.npc.getZ()     
                        
                    for i in range (0, TeamMode):
                        e.npc.world.spawnClone( int(X), 120, int(Z), 3, "Disabled").setFaction(int(IdHere))             #Spawning a team with the deleted faction id
            


                # IMPORTANT, if in FFA, to avoid 1Spawner - 1 NPC, Make the others Spawner spawn.

                    X = random.randint(-120, 120)
                    Z = random.randint(-120, 120)

                    NeedStop = e.npc.world.getTempdata().get("NeedStop")
                    if NeedStop == None :
                        e.npc.despawn()
                    else :
                        e.npc.world.spawnClone( X, 120, Z, 3, "Spawner").setFaction(0)

                    e.npc.world.getStoreddata().put(str(IdHere), TeamMode)

                    e.npc.despawn()
                else :
                    e.npc.say("&2No available factions, waiting for one.....")      


            except Exception as Err:
                e.npc.world.broadcast(str(Err))
                

    except: 
        pass

def MayStopArena(e):
	NeedStop = e.npc.world.getTempdata().get("NeedStop")
	if NeedStop == None :
		e.npc.despawn()
		pass



#===============================#
#_______{ Calling Events }______#
#===============================#

def init(e):
    if e.npc.getStoreddata().get("Test") == None :
        e.npc.getStoreddata().put("Test", 1)
        e.npc.reset()
        e.npc.setPosition(e.npc.getX(), 200, e.npc.getZ())

def tick(e):
    GameStarted = e.npc.world.getTempdata().get("GameStarted")
    if GameStarted == 1:
        CheckTimer(e)
        
    MayStopArena(e)

def interact(e):
    e.npc.getStoreddata().clear()



