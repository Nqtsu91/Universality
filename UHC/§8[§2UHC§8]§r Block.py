import random
import math
#API Link :http://www.kodevelopment.nl/customnpcs/api/1.8.9/
#Credits : Script UHC vs Bots BotScatteringV4 By Natsu91

#===================================#
#_______{ Creating Algorithm }______#
#===================================#

def CheckTimer(e):
    Players = e.npc.world.getStoreddata().get("Players") - len(e.npc.world.getAllPlayers())		# Getting data for bots spawn
    GameStarted = e.npc.world.getTempdata().get("GameStarted")
    if (Players <= 0) or (GameStarted != 1) :
        e.npc.despawn()
        

    try:
        if Chosed == 1 :
            pass
        else : 
            Chosed = 0
    except:
        Chosed = 0
    

    BotsToSpawn = e.npc.world.getStoreddata().get("BotsToSpawn")
    
    if BotsToSpawn <= 0 :
        e.npc.despawn()
    
    MeetUp = e.npc.world.getStoreddata().get("MeetUp")
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


        if (e.npc.world.getTotalTime() >= MeetUp) :             # if PvP enabled
            try :
                Test = float(e.npc.getTempdata().get("Spawn")) + 1                # Just make the try except bug at the first loop, maybe not ideal
                if (e.npc.world.getTotalTime() >= e.npc.getTempdata().get("Spawn")) or (e.npc.world.getTempdata().get("ForceSpawn") == 1):             # If TimeSelected is passed
                    if len(Factions) != 0:                      # If there is empty faction 
                        IdHere = random.choice(Factions)
                        Factions.remove(IdHere)
                        Factions = "/".join(Factions)                           # Deleting the faction from the list
                        e.npc.world.getStoreddata().put("Factions", str(Factions))    
                        X = e.npc.getX()
                        Z = e.npc.getZ()     
                        
                        if e.npc.world.getStoreddata().get("BotsToSpawn") > 0 : 
                            TeamList = e.npc.world.getTempdata().get("TeamNameList")
                            try:
                                SelectedID = random.randint(-1, len(TeamList)-1) 
                                ToSend = TeamList[SelectedID]
                                TeamList.pop(SelectedID)
                                e.npc.world.getTempdata().put("TeamNameList", TeamList)
                            except:
                                ToSend = "None"
                            for i in range (0, TeamMode):
                                e.npc.world.spawnClone( int(X), 120, int(Z), 2, "Disabled").setFaction(int(IdHere))             #Spawning a team with the deleted faction id
                                e.npc.world.getTempdata().put(str(IdHere)+"Team", ToSend)
                                e.npc.world.getStoreddata().put("BotsToSpawn", int(e.npc.world.getStoreddata().get("BotsToSpawn")-1))


                # IMPORTANT, if in FFA, to avoid 1Spawner - 1 NPC, Make the others Spawner spawn.
                            Radius = int(e.npc.world.getTempdata().get("Radius"))
                            X = random.randint(-Radius, Radius)
                            Z = random.randint(-Radius, Radius)

                            BotsToSpawn = e.npc.world.getStoreddata().get("BotsToSpawn")
                            if BotsToSpawn <= 0 :
                                e.npc.despawn()
                                
                            else :
                                if random.randint(1, 3) == 2:
                                    e.npc.world.spawnClone( int(e.npc.getX()), 120, int(e.npc.getZ()), 2, "Spawner").setFaction(0)
                                else:
                                    e.npc.world.spawnClone( X, 120, Z, 2, "Spawner").setFaction(0)

                            e.npc.world.getStoreddata().put(str(IdHere), TeamMode)

                        e.npc.despawn()
                    else :
                        e.npc.say("&2No available factions, waiting for one.....")
                else :
                    pass       


            except:
                try:
                    MinTimeSpread = int(e.npc.world.getTempdata().get("MinTimeSpread"))
                    MaxTimeSpread = int(e.npc.world.getTempdata().get("MaxTimeSpread"))
                except:
                    MinTimeSpread = 0
                    MaxTimeSpread = 5
                    
                Random = random.randint(MinTimeSpread,MaxTimeSpread)                       # Selecting a random time to spawn the npcs
                TimeSelected = 8 
                Chosed = 1
                e.npc.getTempdata().put("Spawn", MeetUp + (Random * 1200))

    except: 
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
    else:
        e.npc.despawn()
        


def interact(e):
    e.npc.getStoreddata().clear()



