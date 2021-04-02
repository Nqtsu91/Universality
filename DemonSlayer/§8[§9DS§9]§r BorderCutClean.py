
import random
import os

def SuperHeroes(e):
    """
    Display message to choose a power
    """
    e.npc.executeCommand('/tellraw @a ["",{"text":"[","color":"dark_gray"},{"text":"DS","color":"dark_red"},{"text":"][","color":"dark_gray"},{"text":"SuperHeroes","color":"gold"},{"text":"]","color":"dark_gray"},{"text":" Click on a button below to choose ONE power","color":"gray"},{"text":"\n"},{"text":"[Resistance II]","color":"dark_gray","clickEvent":{"action":"run_command","value":"/effect @p minecraft:resistance 9999 1 true"}},{"text":" - ","color":"gray"},{"text":"[Speed II]","color":"yellow","clickEvent":{"action":"run_command","value":"/effect @p minecraft:speed 9999 1 true"}},{"text":" - ","color":"gray"},{"text":"[JumpBoost IV]","color":"green","clickEvent":{"action":"run_command","value":"/effect @p minecraft:jump_boost 9999 3 true"}},{"text":" - ","color":"gray"},{"text":"[HealthBoost V]","color":"blue","clickEvent":{"action":"run_command","value":"/effect @p minecraft:health_boost 9999 4 true"}},{"text":" - ","color":"gray"},{"text":"[Strength I]","color":"red","clickEvent":{"action":"run_command","value":"/effect @p minecraft:strength 9999 0 true"}}]')

def FinalHeal(e):
    e.npc.executeCommand('/effect @a minecraft:instant_health 1 45 true')
    e.npc.executeCommand('/tellraw @a ["",{"text":"[","color":"dark_gray"},{"text":"DS","color":"dark_red"},{"text":"]","color":"dark_gray"},{"text":" - Final Heal has been given, dont ask for another one !","color":"gray"}]')

def Minute(e):
    try:

        DIncreaseTick = e.npc.getTempdata().get("DiamondIncreaseTick")
        GapIncreaseTick = e.npc.getTempdata().get("GapIncreaseTick")
        EIncreaseTick = e.npc.getTempdata().get("EIncreaseTick")
        SharpIncreaseTick = e.npc.getTempdata().get("SharpIncreaseTick")
        ProtIncreaseTick = e.npc.getTempdata().get("ProtIncreaseTick")

        e.npc.getTempdata().put("DiamondIncreaseTick", DIncreaseTick+int(1))               # Ticking counters
        e.npc.getTempdata().put("GapIncreaseTick", GapIncreaseTick+int(1))
        e.npc.getTempdata().put("EIncreaseTick", EIncreaseTick+int(1))               # Ticking counters
        e.npc.getTempdata().put("ProtIncreaseTick", ProtIncreaseTick+int(1))
        e.npc.getTempdata().put("SharpIncreaseTick", SharpIncreaseTick+int(1))               # Ticking counters

        MaxProt = e.npc.world.getTempdata().get("MaxProt")
        MaxGap = e.npc.world.getTempdata().get("MaxGap")
        MaxSharp = e.npc.world.getTempdata().get("MaxSharp")
        DProba = e.npc.world.getTempdata().get("DiamondProbability")
        EProba = e.npc.world.getTempdata().get("EnchantProbability")
        EIncreaseTime = e.npc.world.getTempdata().get("EnchantIncreaseTime")
        EIncreaseRate = e.npc.world.getTempdata().get("EnchantIncreaseRate")
        DIncreaseRate = e.npc.world.getTempdata().get("DiamondIncreaseRate")
        DIncreaseTime = e.npc.world.getTempdata().get("DiamondIncreaseTime")

        GapIncreaseRate = e.npc.world.getTempdata().get("GapIncreaseRate")
        GapIncreaseTime = e.npc.world.getTempdata().get("GapIncreaseTime")

        ProtIncreaseTime = e.npc.world.getTempdata().get("ProtIncreaseTime")
        SharpIncreaseTime = e.npc.world.getTempdata().get("SharpIncreaseTime")


        DIncreaseTick = e.npc.getTempdata().get("DiamondIncreaseTick")
        GapIncreaseTick = e.npc.getTempdata().get("GapIncreaseTick")
        EIncreaseTick = e.npc.getTempdata().get("EIncreaseTick")
        SharpIncreaseTick = e.npc.getTempdata().get("SharpIncreaseTick")
        ProtIncreaseTick = e.npc.getTempdata().get("ProtIncreaseTick")


        if DIncreaseTick == DIncreaseTime:
            e.npc.world.getTempdata().put("DiamondProbability", e.npc.world.getTempdata().get("DiamondProbability")+int(DIncreaseRate))      # Increase Diamond proba
            e.npc.getTempdata().put("DiamondIncreaseTick", 0)

        if GapIncreaseTick == GapIncreaseTime:
            e.npc.world.getTempdata().put("MaxGap", e.npc.world.getTempdata().get("MaxGap")+int(GapIncreaseRate))      # Increase gap maximum 
            e.npc.getTempdata().put("GapIncreaseTick", 0)

        if EIncreaseTime == EIncreaseTick:
            e.npc.world.getTempdata().put("EnchantProbability", EProba+int(EIncreaseRate))      # Increase Enchant proba
            e.npc.getTempdata().put("EIncreaseTick", 0)


        if ProtIncreaseTick == ProtIncreaseTime:
            if (e.npc.world.getTempdata().get("MaxProt")+int(1)) != 5:
                e.npc.world.getTempdata().put("MaxProt", e.npc.world.getTempdata().get("MaxProt")+int(1))      # Increase Prot Max
                e.npc.getTempdata().put("ProtIncreaseTick", 0)


        if SharpIncreaseTick == SharpIncreaseTime:
            if (e.npc.world.getTempdata().get("MaxSharp")+int(1)) != 6:
                e.npc.world.getTempdata().put("MaxSharp", e.npc.world.getTempdata().get("MaxSharp")+int(1))      # Increase Sharp Max
                e.npc.getTempdata().put("SharpIncreaseTick", 0)





        
    except Exception as err:
        #e.npc.world.broadcast(str(err))
        pass

def CatEyes(e):
	CatEyesOn = e.npc.world.getTempdata().get("CatEyes")
	if CatEyesOn == True :
		e.npc.executeCommand('/effect @a minecraft:night_vision 1000000 0 true')

def HasteyBoys(e):
    if e.npc.world.getTempdata().get("HasteyBoys") == True:
        Players = e.npc.world.getAllPlayers()
        for i in range(0, len(Players)):
            for z in range(0, len(Players[i].getInventory())):
                try:
                    if Players[i].getInventory()[z] != None:
                        List = ["minecraft:iron_pickaxe","minecraft:iron_axe","minecraft:iron_shovel","minecraft:diamond_pickaxe","minecraft:diamond_axe","minecraft:diamond_shovel","minecraft:gold_pickaxe","minecraft:gold_axe","minecraft:gold_shovel","minecraft:stone_pickaxe","minecraft:stone_axe","minecraft:shears","minecraft:stone_shovel","minecraft:wooden_pickaxe","minecraft:wooden_axe","minecraft:wooden_shovel"]
                        if (Players[i].getInventory()[z].getName() in List) and (Players[i].getInventory()[z].getTag('ench') == None):
                            Ench = '{ench:[{id:32,lvl:3},{id:34,lvl:2}]}'
                            e.npc.executeCommand('/replaceitem entity '+str(Players[i].getName())+' slot.container.'+str(int(round(z)))+' '+str(Players[i].getInventory()[z].getName())+' 1 0 '+str(Ench)+'')
                except Exception as ess:
                    e.npc.say(str(ess))
                    pass

def CutClean(e):
    if e.npc.world.getTempdata().get("CutClean") == True:
        Players = e.npc.world.getAllPlayers()
        for i in range(0, len(Players)):

            # Iron CutClean

            Iron = e.npc.world.getScoreboard().getPlayerScore(str(Players[i].getName()), "Iron", "")
            IronDone = e.npc.getStoreddata().get("Iron"+str(Players[i].getName()))
            if IronDone == None :
                IronDone = 0
                e.npc.getStoreddata().put("Iron"+str(Players[i].getName()), 0)
            if IronDone <= Iron :
                IronToDo = Iron - IronDone

                for j in range(0, int(IronToDo)):                   # Giving xp + actualising temp data
                    e.npc.executeCommand("/xp "+str(e.npc.world.getTempdata().get("XpMultiplicator")*2)+" "+str(Players[i].getName())+"")
                    e.npc.getStoreddata().put("Iron"+str(Players[i].getName()), e.npc.getStoreddata().get("Iron"+str(Players[i].getName()))+1)


                for z in range(0, len(Players[i].getInventory())):          # Replacing ore with ingot
                    try:
                        if Players[i].getInventory()[z].getItemName() == "Iron Ore":
                            Stack = int(Players[i].getInventory()[z].getStackSize())
                            Players[i].removeAllItems(Players[i].getInventory()[z])
                            e.npc.executeCommand("/give "+str(Players[i].getName())+" minecraft:iron_ingot "+str(Stack)+"")
                    except Exception as ess:
                        pass

            # Gold CutClean

            Gold = e.npc.world.getScoreboard().getPlayerScore(str(Players[i].getName()), "Gold", "")
            GoldDone = e.npc.getStoreddata().get("Gold"+str(Players[i].getName()))
            if GoldDone == None :
                GoldDone = 0
                e.npc.getStoreddata().put("Gold"+str(Players[i].getName()), 0)
            if GoldDone <= Gold :
                GoldToDo = Gold - GoldDone

                for j in range(0, int(GoldToDo)):                   # Giving xp + actualising temp data
                    e.npc.executeCommand("/xp "+str(e.npc.world.getTempdata().get("XpMultiplicator")*2)+" "+str(Players[i].getName())+"")
                    e.npc.getStoreddata().put("Gold"+str(Players[i].getName()), e.npc.getStoreddata().get("Gold"+str(Players[i].getName()))+1)


                for z in range(0, len(Players[i].getInventory())):          # Replacing ore with ingot
                    try:
                        if Players[i].getInventory()[z].getItemName() == "Gold Ore":
                            Stack = int(Players[i].getInventory()[z].getStackSize())
                            Players[i].removeAllItems(Players[i].getInventory()[z])
                            e.npc.executeCommand("/give "+str(Players[i].getName())+" minecraft:gold_ingot "+str(Stack)+"")
                    except Exception as ess:
                        pass


            #Food CutClean
            for z in range(0, len(Players[i].getInventory())):          # Replacing ore with ingot
                    try:
                        List = ["Raw Beef","Raw Chicken","Raw Mutton","Raw Rabbit","Potato","Raw Porkchop"]
                        if Players[i].getInventory()[z].getItemName() in List:
                            Stack = int(Players[i].getInventory()[z].getStackSize())
                            Players[i].removeAllItems(Players[i].getInventory()[z])
                            e.npc.executeCommand("/give "+str(Players[i].getName())+" minecraft:cooked_beef "+str(Stack)+"")
                    except Exception as ess:
                        pass
    else:
        pass

def AppleFlintRate(e):
    Players = e.npc.world.getAllPlayers()
    for i in range(0, len(Players)):

        Apple = e.npc.world.getScoreboard().getPlayerScore(str(Players[i].getName()), "Apple", "")
        AppleDone = e.npc.world.getStoreddata().get("Apple"+str(Players[i].getName()))  
        if AppleDone == None :
            AppleDone = 0
            e.npc.world.getStoreddata().put("Apple"+str(Players[i].getName()), 0)
        if AppleDone < Apple :
            AppleToDo = Apple - AppleDone
            for z in range(0, int(AppleToDo)):
                if random.randint(int(0), int(100)) <= int(e.npc.world.getTempdata().get("AppleRate")) :
                    e.npc.executeCommand("/give "+str(Players[i].getName())+" minecraft:apple")
                e.npc.world.getStoreddata().put("Apple"+str(Players[i].getName()), e.npc.world.getStoreddata().get("Apple"+str(Players[i].getName()))+1)

        Gravel = e.npc.world.getScoreboard().getPlayerScore(str(Players[i].getName()), "Gravel", "")
        GravelDone = e.npc.world.getStoreddata().get("Gravel"+str(Players[i].getName()))  
        if GravelDone == None :
            GravelDone = 0
            e.npc.world.getStoreddata().put("Gravel"+str(Players[i].getName()), 0)
        if GravelDone < Gravel :
            GravelToDo = Gravel - GravelDone
            for z in range(0, int(GravelToDo)):
                if random.randint(int(0), int(100)) <= int(e.npc.world.getTempdata().get("FlintRate")) :
                    e.npc.executeCommand("/give "+str(Players[i].getName())+" minecraft:flint")
                e.npc.world.getStoreddata().put("Gravel"+str(Players[i].getName()), e.npc.world.getStoreddata().get("Gravel"+str(Players[i].getName()))+1)

def ShrinkBorder(e):
    if e.npc.world.getTempdata().get("DeathMatchTP") != True:
        First = e.npc.world.getStoreddata().get("FirstBorder")
        Second = e.npc.world.getStoreddata().get("SecondBorder")
        Final = e.npc.world.getStoreddata().get("FinalBorder")
        if Final <= e.npc.world.getTotalTime():
            e.npc.executeCommand("/worldborder set 101")
            PlayerTP(e)
        elif Second <= e.npc.world.getTotalTime():
            e.npc.executeCommand("/worldborder set 161")
            PlayerTP(e)
        elif First <= e.npc.world.getTotalTime():
            e.npc.executeCommand("/worldborder set 241")
            PlayerTP(e)
    else:
        e.npc.executeCommand("/worldborder set 61")

def CountingPlayersOnKill(e):
    if (e.npc.world.getStoreddata().get("TeamsAlive") == 1 ) and (e.npc.getStoreddata().get("EndGameSaid") != True):
        #e.npc.executeCommand('/tellraw @a ["",{"text":"[","color":"dark_gray"},{"text":"DS","color":"dark_red"},{"text":"] ","color":"dark_gray"},{"text":"[","color": gray,"bold":true},{"text":"Players","color" : dark_green},{"text":"] ","color": gray,"bold":true},{ "text" :"We now have a winner ! Congratulation !","color" : aqua,"bold":true}]')
        e.npc.getStoreddata().put("EndGameSaid", True)
        EndGame(e)
        UpdatingStats(e)
        EndMessages(e)
        e.npc.world.getTempdata().clear()
        e.npc.world.getStoreddata().clear()
        e.npc.despawn()

def UpdatingStats(e):
    """
    Update stats database
    """
    try:
        #Getting datas from the game
        WinnerList = e.npc.world.getTempdata().get("WinnerList")
        KillList = e.npc.world.getStoreddata().get("KillList")
        KillList = KillList.split("//")
        for i in range(len(KillList)-1, -1, -1):
            if KillList[i] == "":
                KillList.pop(i)
            else:
                KillList[i] = KillList[i].split("|")


        if WinnerList == None :
            WinnerList = []
            for i in range (0, len(e.npc.world.getAllPlayers())):
                WinnerList.append(e.npc.world.getAllPlayers()[i].getName())

        e.npc.executeCommand('/tellraw @a ["",{"text":"[","color":"dark_gray"},{"text":"DS","color":"dark_red"},{"text":"]","color":"dark_gray"},{"text":" - ","color":"gray"},{"text":"Winner","color":"gold"},{"text":"(","color":"gray"},{"text":"s","color":"gold"},{"text":") ","color":"gray"},{"text":":","color":"white"}]')
        for i in range(0, len(WinnerList)):
            e.npc.executeCommand('/tellraw @a ["",{"text":"[","color":"dark_gray"},{"text":"DS","color":"dark_red"},{"text":"]","color":"dark_gray"},{"text":" - ","color":"gray"},{"text":"'+str(WinnerList[i])+'","color":"white"}]')


        #Preparing datas for stats update
        AllData = []
        NewAllData = []

        #Hooking to csv file
        Path = os.path.dirname(os.path.abspath("__file__"))
        Path += "\\CustomNPC Config\\DS\\Stats\\stats"
        Path = Path.replace("\\", str(os.path.sep))
        with open (str(Path)+".csv", "r") as File :
            Config = File.read()
            Config = Config.split(u'\n')
            Title = Config[0]
            Config.pop(0)

            for i in range(0, len(Config)):
                LocalLine = Config[i].split(";")
                if LocalLine[0] != "":
                    AllData.append(LocalLine)

        #Exploiting datas
        for i in range(len(KillList)-1, -1, -1):
            AlreadyFound = False
            for j in range(len(AllData)-1, -1, -1):                #If player already have stats
                if AlreadyFound != True:                     # To avoid index out of range
                    if KillList[i][0] == AllData[j][0]:
                        NewLine = []
                        NewLine.append(str(KillList[i][0]))                        # Saving name
                        NewLine.append(str(int(KillList[i][1]) + int(AllData[j][1])))            # Updating kills
                        if KillList[i][0] in WinnerList:
                            NewLine.append(str(AllData[j][2]))                    #Keeping Death if won the game
                            NewLine.append(str(int(AllData[j][3])+1))                #Increasing Wins also
                        else:
                            NewLine.append(str(int(AllData[j][2])+1))        #Increasing Deaths
                            NewLine.append(str(int(AllData[j][3])))                    #Keeping Wins if loose the game    

                        if int(NewLine[2]) != 0:                    # if player died once
                            NewLine.append(str(int(round(int(NewLine[1])/int(NewLine[2])))))
                        else:
                            NewLine.append(str(NewLine[1]))
                        KillList.pop(i)
                        AllData.pop(j)
                        AlreadyFound = True
                        NewAllData.append(';'.join(NewLine))            #Saving into new stats

        # if player have no stats
        for i in range(0, len(KillList)):            
            NewLine = []
            NewLine.append(str(KillList[i][0]))            #Saving name
            NewLine.append(str(KillList[i][1]))
            if KillList[i][0] in WinnerList:            # if player won the game
                NewLine.append("0")
                NewLine.append("1")
            else:
                NewLine.append("1")
                NewLine.append("0")

            if int(NewLine[2]) != 0:                    # if player died once
                NewLine.append(str(int(round(int(NewLine[1])/int(NewLine[2])))))
            else:
                NewLine.append(str(NewLine[1]))
            NewAllData.append(';'.join(NewLine))            #Saving into new stats    

        #If player have stats but isnt in the game
        for i in range(0, len(AllData)):
            NewAllData.append(';'.join(AllData[i]))

        # Re-hooking to csv file to save
        Path = os.path.dirname(os.path.abspath("__file__"))
        Path += "\\CustomNPC Config\\DS\\Stats\\stats"
        Path = Path.replace("\\", str(os.path.sep))
        with open (str(Path)+".csv", "w") as File :
            File.write(Title)
            for i in range(0, len(NewAllData)):
                File.write(u'\n')
                File.write(NewAllData[i])

        e.npc.executeCommand('/tellraw @a ["",{"text":"[","color":"dark_gray"},{"text":"DS","color":"dark_red"},{"text":"]","color":"dark_gray"},{"text":" Stats saved","color":"gray"},{"text":" successfully","color":"green"}]')
        e.npc.world.getTempdata().put("GameStarted", 0)

    except:
        e.npc.executeCommand('/tellraw @a ["",{"text":"[","color":"dark_gray"},{"text":"DS","color":"dark_red"},{"text":"]","color":"dark_gray"},{"text":" Failed updating stats !","color":"gray"}]')

def EndGame(e):
	try :
		PlayerList = e.npc.world.getAllPlayers()
		for i in range (0, len(PlayerList)):
			NewList = (("//" + PlayerList[i].getName())+ '|' +str(int(e.npc.world.getStoreddata().get(str(PlayerList[i].getName()) +"Kills"))))
			e.npc.world.getStoreddata().put("KillList", e.npc.world.getStoreddata().get("KillList") + NewList)
	except:
		pass
	KillList = e.npc.world.getStoreddata().get("KillList")
	Max = 0
	i = 0
	SortedList = []
	KillList = KillList.split("//")
	for i in range (0, len(KillList)):
		KillList[i] = KillList[i].split("|")


	IntList = []
	Max =["", 0]
	Count = 0
	MaxDisplay = 10
	if MaxDisplay >= len(KillList):
		MaxDisplay = len(KillList)-1

	FinalList = []
	MaxForWhile = len(KillList)

		

	for i in range(len(KillList)-1, 0, -1):
		ToInt = KillList[i][1].split(".")
		KillList[i][1] = ToInt[0]

	while len(FinalList) != MaxDisplay:
 		for i in range(len(KillList)-1, 0, -1):
			if (KillList[i][1] == None) or (KillList[i][1] == "None"):
				KillList[i][1] = 0
 			if int(KillList[i][1]) >= int(Max[1]):
				Max = KillList[i]
				Integrer = i
		FinalList.insert(Count, Max)
		try:
			KillList.pop(Integrer)
		except :
				KillList.pop(Integrer-1)
		Count += 1
		Max = ['', 0]

	ColorList = ["red","gold","yellow","aqua","aqua","white","white","white","white","white"]
	try:
		for i in range (0, 10):
			e.npc.executeCommand('/tellraw @a ["",{"text":"[","color":"dark_gray"},{"text":"DS","color":"dark_red"},{"text":"] ","color":"dark_gray"},{"text":"[","color": gray,"bold":true},{"text":"Kills","color" : blue},{"text":"] ","color": gray,"bold":true},{ "text" :"'+str(i+1)+' : ","bold":flase},{ "text" :"'+str(FinalList[i][0])+' --- ","color": '+str(ColorList[i])+',"bold":false},{ "text" :"'+str(FinalList[i][1])+' Kills ","bold":false}]')
	except:
		pass
	
	e.npc.world.spawnClone(13, 203, 0, 4, "Host DS")

def PlayerTP(e):
    Players = e.npc.world.getAllPlayers()
    for i in range(0, len(e.npc.world.getAllPlayers())):
        X = Players[i].getX()
        Y = Players[i].getY()
        Z = Players[i].getZ()



        if (e.npc.world.getStoreddata().get("FinalBorder") <= e.npc.world.getTotalTime()):
            if e.npc.world.getStoreddata().get("FinalPlayerTP") != 1 :
                e.npc.executeCommand("/effect @a minecraft:resistance 4 45 true")
                if (X >= 45) :
                    X = 40
                    Y = 95
                elif (-45 >= X):
                    X = -40
                    Y = 95

                if (Z >= 45) :
                    Z = 40
                    Y = 95
                elif (-45 >= Z):
                    Z = -40
                    Y = 95
                
                Players[i].setPosition(X, Y, Z)
                if i == len(e.npc.world.getAllPlayers())-1 :
                    e.npc.world.getStoreddata().put("FinalPlayerTP", 1)
            

        elif (e.npc.world.getStoreddata().get("SecondBorder") <= e.npc.world.getTotalTime()):
            if e.npc.world.getStoreddata().get("SecondPlayerTP") != 1 :
                e.npc.executeCommand("/effect @a minecraft:resistance 4 45 true")
                if (X >= 80) :
                    X = 75
                    Y = 95
                elif (-80 >= X):
                    X = -75
                    Y = 95

                if (Z >= 80) :
                    Z = 75
                    Y = 95
                elif (-80 >= Z):
                    Z = -75
                    Y = 95
                
                Players[i].setPosition(X, Y, Z)
                if i == len(e.npc.world.getAllPlayers())-1 :
                    e.npc.world.getStoreddata().put("SecondPlayerTP", 1)

        elif (e.npc.world.getStoreddata().get("FirstBorder") <= e.npc.world.getTotalTime()):
            if e.npc.world.getStoreddata().get("FirstPlayerTP") != 1 :
                e.npc.executeCommand("/effect @a minecraft:resistance 4 45 true")
                if (X >= 120) :
                    X = 115
                    Y = 95
                elif (-120 >= X):
                    X = -115
                    Y = 95

                if (Z >= 120) :
                    Z = 115
                    Y = 95
                elif (-120 >= Z):
                    Z = -115
                    Y = 95
                Players[i].setPosition(X, Y, Z)
                if i == len(e.npc.world.getAllPlayers())-1 :
                    e.npc.world.getStoreddata().put("FirstPlayerTP", 1)

def RodBlock(e):
	List = e.npc.world.getAllPlayers()
	for i in range (0, len(List)):
		try:
			List[i].getMCEntity().field_71104_cf.field_146043_c = None
		except Exception as err:
			pass

def ShrinkFirstBorder(e):
    
    e.npc.getStoreddata().put("Forced1Border", 1)
    e.npc.world.getStoreddata().put("FirstBorder", 0)
    e.npc.world.getTempdata().put("FirstBorder", 0)
    e.npc.executeCommand('/tellraw @a ["",{"text":"[","color":"dark_gray"},{"text":"DS","color":"dark_red"},{"text":"][","color":"dark_gray"},{"text":"Border","color":"gold"},{"text":"]","color":"dark_gray"},{"text":" Borders have shrunk to ","color":"gray"},{"text":"-120 120","color":"gold"}]')
    for i in range(0, len(e.npc.world.getAllPlayers())):
        players = e.npc.world.getAllPlayers()
        e.npc.executeCommand("/playsound note.pling "+str(players[i].getName()))
        e.npc.world.spawnClone( int(0), 150, int(0), 4, "Spawner").setFaction(0)			# spawning classic bots

def ShrinkSecondBorder(e):
    e.npc.getStoreddata().put("Forced2Border", 1)
    e.npc.world.getStoreddata().put("SecondBorder", 0)
    e.npc.world.getTempdata().put("SecondBorder", 0)
    e.npc.executeCommand('/tellraw @a ["",{"text":"[","color":"dark_gray"},{"text":"DS","color":"dark_red"},{"text":"][","color":"dark_gray"},{"text":"Border","color":"gold"},{"text":"]","color":"dark_gray"},{"text":" Borders have shrunk to ","color":"gray"},{"text":"-80 80","color":"gold"}]')
    for i in range(0, len(e.npc.world.getAllPlayers())):
        players = e.npc.world.getAllPlayers()
        e.npc.executeCommand("/playsound note.pling "+str(players[i].getName()))
        e.npc.world.spawnClone( int(0), 150, int(0), 4, "Spawner").setFaction(0)			# spawning classic bots

def ShrinkFinalBorder(e):
    e.npc.getStoreddata().put("Forced3Border", 1)
    e.npc.world.getStoreddata().put("FinalBorder", 0)
    e.npc.world.getTempdata().put("FinalBorder", 0)
    e.npc.executeCommand('/tellraw @a ["",{"text":"[","color":"dark_gray"},{"text":"DS","color":"dark_red"},{"text":"][","color":"dark_gray"},{"text":"Border","color":"gold"},{"text":"]","color":"dark_gray"},{"text":" Borders have shrunk to ","color":"gray"},{"text":"-50 50","color":"gold"}]')
    for i in range(0, len(e.npc.world.getAllPlayers())):
        players = e.npc.world.getAllPlayers()
        e.npc.executeCommand("/playsound note.pling "+str(players[i].getName()))
        e.npc.world.spawnClone( int(0), 150, int(0), 4, "Spawner").setFaction(0)			# spawning classic bots

def EnablePvP(e):
    e.npc.getStoreddata().put("ForcedPvP", 1)
    e.npc.world.getStoreddata().put("PvPTime", 0)
    e.npc.world.getTempdata().put("PvPTime", 0)
    e.npc.executeCommand('/tellraw @a ["",{"text":"[","color":"dark_gray"},{"text":"DS","color":"dark_red"},{"text":"]","color":"dark_gray"},{"text":" PvP is now enabled !","color":"gray"}]')
    if (e.npc.world.getStoreddata().get("PvPDisplayed") != "True"):
        e.npc.executeCommand('/title @a times 20 100 20')
        e.npc.executeCommand('/title @a subtitle {"text":"Good luck and have fun !","color":"dark_gray"}')
        e.npc.executeCommand('/title @a title {"text":"PvP Enabled !","color":"dark_red"}')
        e.npc.world.getStoreddata().put("PvPDisplayed", "True")
        for i in range(0, len(e.npc.world.getAllPlayers())):
            players = e.npc.world.getAllPlayers()
            e.npc.executeCommand("/playsound mob.enderdragon.growl "+str(players[i].getName()))

def ForceCommands(e):
    Players = e.npc.world.getAllPlayers()
    for i in range(0, len(Players)):
        Spawn = e.npc.world.getScoreboard().getPlayerScore(str(Players[i].getName()), "Spawn", "")
        Heal = e.npc.world.getScoreboard().getPlayerScore(str(Players[i].getName()), "HealTrigger", "")
        FirstBorder = e.npc.world.getScoreboard().getPlayerScore(str(Players[i].getName()), "1BorderTrigger", "")
        SecondBorder = e.npc.world.getScoreboard().getPlayerScore(str(Players[i].getName()), "2BorderTrigger", "")
        FinalBorder = e.npc.world.getScoreboard().getPlayerScore(str(Players[i].getName()), "3BorderTrigger", "")
        PvPTrigger = e.npc.world.getScoreboard().getPlayerScore(str(Players[i].getName()), "PvPTrigger", "")

        if str(Heal) != "0":
            FinalHeal(e)
            e.npc.executeCommand('/scoreboard objectives remove HealTrigger')
            e.npc.executeCommand('/scoreboard objectives add HealTrigger trigger')

        if str(Spawn) != "0":
            e.npc.executeCommand('/scoreboard objectives remove Spawn')
            e.npc.executeCommand('/scoreboard objectives add Spawn trigger')
            e.npc.world.getTempdata().put("ForceSpawn", 1)

        if str(FirstBorder) != "0":
            ShrinkFirstBorder(e)
            e.npc.executeCommand('/scoreboard objectives remove 1BorderTrigger')
            e.npc.executeCommand('/scoreboard objectives add 1BorderTrigger trigger')

        if str(SecondBorder) != "0":
            ShrinkSecondBorder(e)
            e.npc.executeCommand('/scoreboard objectives remove 2BorderTrigger')
            e.npc.executeCommand('/scoreboard objectives add 2BorderTrigger trigger')

        if str(FinalBorder) != "0":
            ShrinkFinalBorder(e)
            e.npc.executeCommand('/scoreboard objectives remove 3BorderTrigger')
            e.npc.executeCommand('/scoreboard objectives add 3BorderTrigger trigger')

        if str(PvPTrigger) != "0":
            EnablePvP(e)
            e.npc.executeCommand('/scoreboard objectives remove PvPTrigger')
            e.npc.executeCommand('/scoreboard objectives add PvPTrigger trigger')

def ShowConfig(e):
	Name = e.npc.world.getStoreddata().get("ConfigName")
	if Name == None :
		Name = "Unamed"

	List = ["BotNumber","TeamSize","DiamondProbability","NoCleanRegen","BleedingDiamonds","BleedingIron","BleedingGold","PvPTime","MinTimeSpread","MaxTimeSpread","MolePerTeam","FinalBorder","SecondBorder","FirstBorder","AppleRate","FlintRate","CutClean","BadlionKillsSystem","NoCleanUpEnabled","ThunderStrike","WitherSoundI","WitherSoundII","IronGolemSound","WaterAllowed","CatEyes","MasterLevel","SuperHeroes","BookCeption","DoubleHealth","OneShot","BleedingSweets","Rodless","Mole","RedditDSDisplay","GoldenHeads","ExplodeOnDeath","FireAspectAllowed","AbsoLess","ForcedType","BadlionKB","ArcticMeta","ScatterMessageEnabled","LoadTeams"]

	e.npc.executeCommand('/tellraw @a ["",{"text":"[","color":"dark_gray"},{"text":"DS","color":"dark_red"},{"text":"]","color":"dark_gray"},{"text":" Game title :","color":"white"},{"text":"\n"},{"text":" - ","color":"gray"},{"text":"'+str(Name)+'","color":"red"}]')
	for i in range(0, len(List)):
		Color = "white"
		if str(e.npc.world.getTempdata().get(List[i])) == "True":
			Color = "green"
		elif str(e.npc.world.getTempdata().get(List[i])) == "False":
			Color = "red"
		elif str(e.npc.world.getTempdata().get(List[i])) == "None" :
			Color = "black"
		if (Color == "green") or (Color == "white") and (e.npc.world.getTempdata().get(List[i]) != 0):
			e.npc.executeCommand('/tellraw @a ["",{"text":"[","color":"dark_gray"},{"text":"DS","color":"dark_red"},{"text":"]","color":"dark_gray"},{"text":" - ","color":"gray"},{"text":"'+str(List[i])+'","color":"light_purple"},{"text":" : ","color":"gray"},{"text":"'+str(e.npc.world.getTempdata().get(List[i]))+'","color":"'+str(Color)+'"}]')

def InitInternal(e):
    e.npc.getTempdata().put("DiamondIncreaseTick", 0)
    e.npc.getTempdata().put("GapIncreaseTick", 0)
    e.npc.getTempdata().put("EIncreaseTick", 0)
    e.npc.getTempdata().put("SharpIncreaseTick", 0)
    e.npc.getTempdata().put("ProtIncreaseTick", 0)

def DoubleHealth(e):
    DoubleHealth = e.npc.world.getTempdata().get("DoubleHealth")
    HasDoneDoubleHealth = e.npc.getTempdata().get("HasDoneDoubleHealth")
    if (DoubleHealth == True) and (HasDoneDoubleHealth != True):
        e.npc.executeCommand('/effect @a minecraft:health_boost 10000 4 true')
        e.npc.getTempdata().put("HasDoneDoubleHealth", True)

def Counter(e):
    try:
        if e.npc.getStoreddata().get("OneSecTicker") == 1 :

            if e.npc.getStoreddata().get("Second") == None :                   # Counting seconds
                e.npc.getStoreddata().put("Second", 0)

            if (e.npc.getStoreddata().get("Second") == 5) and (e.npc.getStoreddata().get("Minutes") == 0):                   # Counting seconds
                ShowConfig(e)

            e.npc.getStoreddata().put("Second", e.npc.getStoreddata().get("Second")+1)
            ClearingTimeBomb(e)

            if e.npc.getStoreddata().get("Second") == 60 :
                if e.npc.getStoreddata().get("Minutes") == None :                   # Counting minutes
                    e.npc.getStoreddata().put("Minutes", 0)
                e.npc.getStoreddata().put("Minutes", e.npc.getStoreddata().get("Minutes")+1)
                Minute(e)
                e.npc.getStoreddata().put("Second", 0)

            if (e.npc.getStoreddata().get("Minutes") == 10) and (e.npc.getStoreddata().get("Second") == 0) and (e.npc.world.getTempdata().get("MeetUp") <= e.npc.world.getTotalTime()):
                FinalHeal(e)
            e.npc.getStoreddata().put("OneSecTicker", 0)

            VarToCount = ["PvPTime","FirstBorder","SecondBorder","FinalBorder"]
            for i in range(0, len(VarToCount)):

                Until = (e.npc.world.getTempdata().get(VarToCount[i])) - (e.npc.getStoreddata().get("Minutes"))

                if Until == 15 and (e.npc.getStoreddata().get(VarToCount[i]+"15") != 1):
                    e.npc.getStoreddata().put(VarToCount[i]+"15", 1)
                    if (VarToCount[i] == "PvPTime") and (e.npc.getStoreddata().get("ForcedPvP") != 1):
                        e.npc.executeCommand('/tellraw @a ["",{"text":"[","color":"dark_gray"},{"text":"DS","color":"dark_red"},{"text":"]","color":"dark_gray"},{"text":" PvP will enable in ","color":"gray"},{"text":"15 minutes","color":"white"}]')
                    if (VarToCount[i] == "FirstBorder") and (e.npc.getStoreddata().get("Forced1Border") != 1):
                        e.npc.executeCommand('/tellraw @a ["",{"text":"[","color":"dark_gray"},{"text":"DS","color":"dark_red"},{"text":"][","color":"dark_gray"},{"text":"Border","color":"gold"},{"text":"]","color":"dark_gray"},{"text":" Border will shrink to ","color":"gray"},{"text":"-120 120","color":"gold"},{"text":" in","color":"gray"},{"text":" 15 minutes","color":"dark_gray"}]')
                    if (VarToCount[i] == "SecondBorder") and (e.npc.getStoreddata().get("Forced2Border") != 1):
                        e.npc.executeCommand('/tellraw @a ["",{"text":"[","color":"dark_gray"},{"text":"DS","color":"dark_red"},{"text":"][","color":"dark_gray"},{"text":"Border","color":"gold"},{"text":"]","color":"dark_gray"},{"text":" Border will shrink to ","color":"gray"},{"text":"-80 80","color":"gold"},{"text":" in","color":"gray"},{"text":" 15 minutes","color":"dark_gray"}]')
                    if (VarToCount[i] == "FinalBorder") and (e.npc.getStoreddata().get("Forced3Border") != 1):
                        e.npc.executeCommand('/tellraw @a ["",{"text":"[","color":"dark_gray"},{"text":"DS","color":"dark_red"},{"text":"][","color":"dark_gray"},{"text":"Border","color":"gold"},{"text":"]","color":"dark_gray"},{"text":" Border will shrink to ","color":"gray"},{"text":"-50 50","color":"gold"},{"text":" in","color":"gray"},{"text":" 15 minutes","color":"dark_gray"}]')
                    e.npc.getStoreddata().put(VarToCount[i]+"15", 1)

                if Until == 10 and (e.npc.getStoreddata().get(VarToCount[i]+"10") != 1):
                    if (VarToCount[i] == "PvPTime") and (e.npc.getStoreddata().get("ForcedPvP") != 1):
                        e.npc.executeCommand('/tellraw @a ["",{"text":"[","color":"dark_gray"},{"text":"DS","color":"dark_red"},{"text":"]","color":"dark_gray"},{"text":" PvP will enable in ","color":"gray"},{"text":"10 minutes","color":"white"}]')
                    if (VarToCount[i] == "FirstBorder") and (e.npc.getStoreddata().get("Forced1Border") != 1):
                        e.npc.executeCommand('/tellraw @a ["",{"text":"[","color":"dark_gray"},{"text":"DS","color":"dark_red"},{"text":"][","color":"dark_gray"},{"text":"Border","color":"gold"},{"text":"]","color":"dark_gray"},{"text":" Border will shrink to ","color":"gray"},{"text":"-120 120","color":"gold"},{"text":" in","color":"gray"},{"text":" 10 minutes","color":"dark_gray"}]')
                    if (VarToCount[i] == "SecondBorder") and (e.npc.getStoreddata().get("Forced2Border") != 1):
                        e.npc.executeCommand('/tellraw @a ["",{"text":"[","color":"dark_gray"},{"text":"DS","color":"dark_red"},{"text":"][","color":"dark_gray"},{"text":"Border","color":"gold"},{"text":"]","color":"dark_gray"},{"text":" Border will shrink to ","color":"gray"},{"text":"-80 80","color":"gold"},{"text":" in","color":"gray"},{"text":" 10 minutes","color":"dark_gray"}]')
                    if (VarToCount[i] == "FinalBorder") and (e.npc.getStoreddata().get("Forced3Border") != 1):
                        e.npc.executeCommand('/tellraw @a ["",{"text":"[","color":"dark_gray"},{"text":"DS","color":"dark_red"},{"text":"][","color":"dark_gray"},{"text":"Border","color":"gold"},{"text":"]","color":"dark_gray"},{"text":" Border will shrink to ","color":"gray"},{"text":"-50 50","color":"gold"},{"text":" in","color":"gray"},{"text":" 10 minutes","color":"dark_gray"}]')
                    e.npc.getStoreddata().put(VarToCount[i]+"10", 1)

                if Until == 5 and (e.npc.getStoreddata().get(VarToCount[i]+"5") != 1):
                    if (VarToCount[i] == "PvPTime") and (e.npc.getStoreddata().get("ForcedPvP") != 1):
                        e.npc.executeCommand('/tellraw @a ["",{"text":"[","color":"dark_gray"},{"text":"DS","color":"dark_red"},{"text":"]","color":"dark_gray"},{"text":" PvP will enable in ","color":"gray"},{"text":"5 minutes","color":"white"}]')
                    if (VarToCount[i] == "FirstBorder") and (e.npc.getStoreddata().get("Forced1Border") != 1):
                        e.npc.executeCommand('/tellraw @a ["",{"text":"[","color":"dark_gray"},{"text":"DS","color":"dark_red"},{"text":"][","color":"dark_gray"},{"text":"Border","color":"gold"},{"text":"]","color":"dark_gray"},{"text":" Border will shrink to ","color":"gray"},{"text":"-120 120","color":"gold"},{"text":" in","color":"gray"},{"text":" 5 minutes","color":"dark_gray"}]')
                    if (VarToCount[i] == "SecondBorder") and (e.npc.getStoreddata().get("Forced2Border") != 1):
                        e.npc.executeCommand('/tellraw @a ["",{"text":"[","color":"dark_gray"},{"text":"DS","color":"dark_red"},{"text":"][","color":"dark_gray"},{"text":"Border","color":"gold"},{"text":"]","color":"dark_gray"},{"text":" Border will shrink to ","color":"gray"},{"text":"-80 80","color":"gold"},{"text":" in","color":"gray"},{"text":" 5 minutes","color":"dark_gray"}]')
                    if (VarToCount[i] == "FinalBorder") and (e.npc.getStoreddata().get("Forced3Border") != 1):
                        e.npc.executeCommand('/tellraw @a ["",{"text":"[","color":"dark_gray"},{"text":"DS","color":"dark_red"},{"text":"][","color":"dark_gray"},{"text":"Border","color":"gold"},{"text":"]","color":"dark_gray"},{"text":" Border will shrink to ","color":"gray"},{"text":"-50 50","color":"gold"},{"text":" in","color":"gray"},{"text":" 5 minutes","color":"dark_gray"}]')
                    e.npc.getStoreddata().put(VarToCount[i]+"5", 1)

                if Until == 1 and (e.npc.getStoreddata().get(VarToCount[i]+"1") != 1):
                    e.npc.getStoreddata().put(VarToCount[i]+"1", 1)
                    if (VarToCount[i] == "PvPTime") and (e.npc.getStoreddata().get("ForcedPvP") != 1):
                        e.npc.executeCommand('/tellraw @a ["",{"text":"[","color":"dark_gray"},{"text":"DS","color":"dark_red"},{"text":"]","color":"dark_gray"},{"text":" PvP will enable in ","color":"gray"},{"text":"1 minute","color":"white"}]')
                    if (VarToCount[i] == "FirstBorder") and (e.npc.getStoreddata().get("Forced1Border") != 1):
                        e.npc.executeCommand('/tellraw @a ["",{"text":"[","color":"dark_gray"},{"text":"DS","color":"dark_red"},{"text":"][","color":"dark_gray"},{"text":"Border","color":"gold"},{"text":"]","color":"dark_gray"},{"text":" Border will shrink to ","color":"gray"},{"text":"-120 120","color":"gold"},{"text":" in","color":"gray"},{"text":" 1 minute","color":"dark_gray"}]')
                        e.npc.world.getTempdata().put("Radius", 110)
                    if (VarToCount[i] == "SecondBorder") and (e.npc.getStoreddata().get("Forced2Border") != 1):
                        e.npc.executeCommand('/tellraw @a ["",{"text":"[","color":"dark_gray"},{"text":"DS","color":"dark_red"},{"text":"][","color":"dark_gray"},{"text":"Border","color":"gold"},{"text":"]","color":"dark_gray"},{"text":" Border will shrink to ","color":"gray"},{"text":"-80 80","color":"gold"},{"text":" in","color":"gray"},{"text":" 1 minute","color":"dark_gray"}]')
                        e.npc.world.getTempdata().put("Radius", 70)
                    if (VarToCount[i] == "FinalBorder") and (e.npc.getStoreddata().get("Forced3Border") != 1):
                        e.npc.executeCommand('/tellraw @a ["",{"text":"[","color":"dark_gray"},{"text":"DS","color":"dark_red"},{"text":"][","color":"dark_gray"},{"text":"Border","color":"gold"},{"text":"]","color":"dark_gray"},{"text":" Border will shrink to ","color":"gray"},{"text":"-50 50","color":"gold"},{"text":" in","color":"gray"},{"text":" 1 minute","color":"dark_gray"}]')
                        e.npc.world.getTempdata().put("Radius", 40)
                    e.npc.getStoreddata().put(VarToCount[i]+"1", 1)

                if Until == 0 and (e.npc.getStoreddata().get(VarToCount[i]+"0") != 1):
                    e.npc.getStoreddata().put(VarToCount[i]+"0", 1)
                    if (VarToCount[i] == "PvPTime") and (e.npc.getStoreddata().get("ForcedPvP") != 1):
                        EnablePvP(e)
                    if (VarToCount[i] == "FirstBorder") and (e.npc.getStoreddata().get("Forced1Border") != 1):
                        ShrinkFirstBorder(e)
                    if (VarToCount[i] == "SecondBorder") and (e.npc.getStoreddata().get("Forced2Border") != 1):
                        ShrinkSecondBorder(e)
                    if (VarToCount[i] == "FinalBorder") and (e.npc.getStoreddata().get("Forced3Border") != 1):
                        ShrinkFinalBorder(e)

        else:
            e.npc.getStoreddata().put("OneSecTicker", 1)
    except:
        pass

def LoadMap(e):
    if e.npc.getStoreddata().get("Loc") == "1":
        if (e.npc.getX() > -120) and (e.npc.getZ() > -120): 
            e.npc.navigateTo(e.npc.getX()-10, 150, e.npc.getZ()-10, 2)
        else:
            e.npc.getStoreddata().put("ClearedTp", True)

    elif e.npc.getStoreddata().get("Loc") == "2":
        if (e.npc.getX() < 120) and (e.npc.getZ() < 120): 
            e.npc.navigateTo(e.npc.getX()+10, 150, e.npc.getZ()+10, 2)
        else:
            e.npc.getStoreddata().put("ClearedTp", True)

    elif e.npc.getStoreddata().get("Loc") == "3":
        if (e.npc.getX() > -120) and (e.npc.getZ() < 120): 
            e.npc.navigateTo(e.npc.getX()-10, 150, e.npc.getZ()+10, 2)        
        else:
            e.npc.getStoreddata().put("ClearedTp", True)

    elif e.npc.getStoreddata().get("Loc") == "4":
        if (e.npc.getX() < 120) and (e.npc.getZ() > -120): 
            e.npc.navigateTo(e.npc.getX()+10, 150, e.npc.getZ()-10, 2)
        else:
            e.npc.getStoreddata().put("ClearedTp", True)

def Displaying(e):
	if e.npc.getStoreddata().get("OneSecTick") != 1:
		Time = e.npc.world.getTotalTime()
		if e.npc.getStoreddata().get("AllSec") == None:
			e.npc.getStoreddata().put("AllSec", 0)
		else:
			pass
		#OBJLIST = [10*60, None, 8*60]11

		if e.npc.getStoreddata().get("PlayersSaved") == None:
			e.npc.getStoreddata().put("PlayersSaved", e.npc.world.getStoreddata().get("Players"))

		OBJLIST = [10*60, None, None, None, int(e.npc.world.getTempdata().get("PvPTime"))*60, None, None, None, None, None, "Players"]
		e.npc.executeCommand('/scoreboard players set __'+u'\xa7'+'8['+u'\xa7'+'4Players'+u'\xa7'+'8]'+u'\xa7'+'r__ Kills 12')
		e.npc.executeCommand('/scoreboard players set '+u'\xa7'+'1 Kills -1')
		e.npc.executeCommand('/scoreboard players set '+u'\xa7'+'2 Kills 99')
		e.npc.executeCommand('/scoreboard players set '+u'\xa7'+'7BotDS_by_'+u'\xa7'+'cNatsu91'+u'\xa7'+'r Kills -2')
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
					Obj = str(int(e.npc.getStoreddata().get("PlayersSaved")))+'/'+str(int(e.npc.world.getStoreddata().get("PlayersMax")))
					e.npc.executeCommand('/scoreboard players reset '+str(Obj)+' Kills')
					e.npc.getStoreddata().put("PlayersSaved", e.npc.world.getStoreddata().get("Players"))
					Obj = str(int(e.npc.world.getStoreddata().get("Players")))+'/'+str(int(e.npc.world.getStoreddata().get("PlayersMax")))
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

def GoldenHead(e):
    if e.npc.world.getTempdata().get("GoldenHeads") == True:
        Players = e.npc.world.getAllPlayers()
        for i in range(0, len(Players)):

            # GHead CutClean

            GHead = e.npc.world.getScoreboard().getPlayerScore(str(Players[i].getName()), "GHead", "")
            GHeadDone = e.npc.getStoreddata().get("GHead"+str(Players[i].getName()))
            GHeadBefore = e.npc.getStoreddata().get("GHeadBefore"+str(Players[i].getName()))
            if GHeadBefore == None:
                GHeadBefore = 0
            

            if GHeadDone == None :
                GHeadDone = 0
                e.npc.getStoreddata().put("GHead"+str(Players[i].getName()), 0)
            if (GHeadDone <= GHead) and (Players[i].getPotionEffect(10) == 1) and (CountingGHead(e, Players[i]) < e.npc.getStoreddata().get("GHeadBefore"+str(Players[i].getName()))):
                GHeadToDo = GHead - GHeadDone

                for j in range(0, int(GHeadToDo)):                   # Giving xp + actualising temp data
                    e.npc.getStoreddata().put("GHeadBefore"+str(Players[i].getName()), CountingGHead(e, Players[i]))
                    e.npc.say("Eat a Golden head")
                    e.npc.executeCommand("/effect "+str(Players[i].getName())+" minecraft:regeneration 8 1")
                    e.npc.getStoreddata().put("GHead"+str(Players[i].getName()), e.npc.getStoreddata().get("GHead"+str(Players[i].getName()))+1)


            e.npc.getStoreddata().put("GHeadBefore"+str(Players[i].getName()), CountingGHead(e, Players[i]))
            #e.npc.say("You have now : "+str(e.npc.getStoreddata().get("GHeadBefore"+str(Players[i].getName()))))
            #e.npc.say("Before you had : "+str(e.npc.getStoreddata().get("GHeadBefore"+str(Players[i].getName()))))

def CountingGHead(e, Player):
    """Return an INT value of the number of "golden_head" item in the inventory of a player"""
    Total = 0
    for z in range(0, len(Player.getInventory())):                  # Counting GHead
        try:
            if (Player.getInventory()[z].getItemName() == "Golden Apple") and (Player.getInventory()[z].hasCustomName()):
                if Player.getInventory()[z].getTag("ishead") == "[0:{True}]" :
                    Stack = int(Player.getInventory()[z].getStackSize())
                    #e.npc.getStoreddata().put("GHeadBefore"+str(Player.getName()), e.npc.getStoreddata().get("GHeadBefore"+str(Player.getName()))+Stack)
                    Total += Stack
        except Exception as ess:
            #e.npc.say(str(ess))
            pass
    return(Total)

def ClearingTimeBomb(e):
    """
    Clear the chests generated by TimeBomb 15 seconds after their spawn
    """
    if len(e.npc.world.getTempdata().get("TimeBombList")) != 0:
        for i in range(len(e.npc.world.getTempdata().get("TimeBombList"))-1, -1, -1):
            TBL = e.npc.world.getTempdata().get("TimeBombList")
            if TBL[i][3] == 0:
                X = int(TBL[i][0])
                Y = int(TBL[i][1])
                Z = int(TBL[i][2])
                if e.npc.world.getTempdata().get("TimeBombExplode") == True:
                    e.npc.world.explode(X,Y,Z,2, True, True)
                    e.npc.world.explode(X,Y,Z,2, True, True)
                else:
                    e.npc.executeCommand('/fill '+str(X-1)+' '+str(Y)+' '+str(Z-1)+' '+str(X+1)+' '+str(Y)+' '+str(Z+1)+' minecraft:air 0 replace minecraft:chest')
                
                del TBL[i]
            else:
                TBL[i][3] = int(TBL[i][3])-1
        e.npc.world.getTempdata().put("TimeBombList", TBL)

def EndMessages(e):
    '''
    Print messages at the end of the game
    '''
    WinnerList = e.npc.world.getTempdata().get("WinnerList")
    if WinnerList == None :
        WinnerList = []
        for i in range (0, len(e.npc.world.getAllPlayers())):
            WinnerList.append(e.npc.world.getAllPlayers()[i].getName())

    for i in range(0, len(WinnerList)):
        MessageList = ["gg","Gg","ty4h",'ez lol',"GG",'GG !',"gg !","gg","gg","gg","gg wp"]
        a = '/tellraw @a ["",{"text":"[","color":"dark_gray"},{"text":"DS","color":"dark_red"},{"text":"] ","color":"dark_gray"},{"text":"[","color":"gray"},{"text":"Winner","color":"gold"},{"text":"] ","color":"gray"},{"text":"'+str(WinnerList[i])+'","color":"white"},{"text":" : ","color":"white"},{"text":"'+str(random.choice(MessageList))+'","color":"white"}]'
        e.npc.executeCommand(a)
    for i in range(0, random.randint(0, 4)):
        MessageList = ["gg","holly","Gg","ty4p",'ez lol',"GG",'GG !',"He's crack :o",":O !","wp","Pvp god be like","gg !","gg","gg","gg"]
        SpecList = ["TryHard","Tylarzz","xNestorio","Gonzaloo","Apexay",'RaiN_DyNasty','jdegoederen',"dedreviil","Davuki","Fukano","Etoiles","Pickachu","Mentally"]
        a = '/tellraw @a ["",{"text":"[","color":"gray"},{"text":"Host","color":"dark_aqua"},{"text":"] ","color":"gray"},{"text":"[","color":"gray"},{"text":"Spec","color":"aqua"},{"text":"] ","color":"gray"},{"text":"'+str(random.choice(SpecList))+'","color":"gold"},{"text":" : ","color":"white"},{"text":"'+str(random.choice(MessageList))+'","color":"white"}]'
        e.npc.executeCommand(a)


#Demon slayer specials

def GiveRoles(e):
    """
    Give Role to players
    """
    if len(e.npc.world.getTempdata().get('RolesList')) == len(e.npc.world.getAllPlayers()):
        for i in range(0, len(e.npc.world.getAllPlayers())):
            Name = e.npc.world.getAllPlayers()[i].getName()
            if e.npc.world.getStoreddata().get(str(Name)+"Role") == None:
                if e.npc.world.getTempdata().get(Name) != None:
                    RoleSelected = e.npc.world.getTempdata().get(Name)
                else:
                    RolesList = e.npc.world.getTempdata().get('RolesList')
                    RoleSelected = random.choice(RolesList)
                    RolesList.remove(RoleSelected)
                    e.npc.world.getTempdata().put('RolesList', RolesList)
                e.npc.world.getStoreddata().put(str(e.npc.world.getAllPlayers()[i].getName())+"Role", RoleSelected)
                e.npc.world.broadcast(str(e.npc.world.getAllPlayers()[i].getName())+ ' is now '+str(RoleSelected))
                RolesMessages(e, RoleSelected, str(Name))
                BadList = ["Muzan",
                        "Nakime",
                        "Kokushibo",
                        "Doma",
                        "Akaza",
                        "Gyokko",
                        "Daki",
                        "Gyutaro",
                        "Rui",
                        "Kaigaku",
                        "Sasumaru",
                        "Kyogai",
                        "Yahaba",
                        "Kumo",
                        "Furuto",
                        "Demon"
                        ]

                GoodList = ["Tanjiro",
                        "Zenitsu",
                        "Inosuke",
                        "Kagaya",
                        "Tomioka",
                        "Shinobu",
                        "Kyojuro",
                        "Tengen",
                        "Muichiro",
                        "Mitsuri",
                        "Sanemi",
                        "Obanai",
                        "Gyomei",
                        "Urokodaki",
                        "Kanae",
                        "Sabito",
                        "Kanao",
                        "Genya",
                        "Hotaru",
                        "Slayer",
                        "Jigoro",
                        "Yoriichi",
                        "Shinjuro"]
                if RoleSelected in BadList:
                    e.npc.executeCommand('/noppes faction '+str(Name)+' 42 set 1500')
                    e.npc.executeCommand('/noppes faction '+str(Name)+' 41 set 0')
                else:
                    e.npc.executeCommand('/noppes faction '+str(Name)+' 41 set 1500')
                    e.npc.executeCommand('/noppes faction '+str(Name)+' 42 set 0')

                e.npc.world.getTempdata().put("TanjiroTarget", random.choice(BadList))
                e.npc.world.getTempdata().put("YahabaTarget", random.choice(GoodList))

def RolesEffects(e):
    '''
    Apply role effects to players
    '''
    Players = e.npc.world.getAllPlayers()
    for i in range(0, len(Players)):
        Role = e.npc.world.getStoreddata().get(str(e.npc.world.getAllPlayers()[i].getName())+"Role")
        Time = e.npc.world.isDay()
        if (Role == "Tanjiro") and (e.npc.world.getTempdata().get("NezukoDied") == True):
            e.npc.addPotionEffect(18, 100000, 0, True)

        elif (Role == "Zenitsu"):
            if (e.npc.world.getAllPlayers()[i].getHealth() >= 10):
                e.npc.world.getAllPlayers()[i].addPotionEffect(18, 10, 0, True)
            else:
                e.npc.world.getAllPlayers()[i].addPotionEffect(1, 10, 1, True)	

        elif (Role == "Inosuke") and (Time == False):
            e.npc.world.getAllPlayers()[i].addPotionEffect(11, 10, 0, True)

        elif (Role == "Tomioka"):
            e.npc.world.getAllPlayers()[i].addPotionEffect(1, 10, 1, True)
            if e.npc.world.getTempdata().get("SabitoDied") == True:
                e.npc.world.getAllPlayers()[i].addPotionEffect(11, 10000, 0, True)

        elif (Role == "Shinobu"):
            e.npc.world.getAllPlayers()[i].addPotionEffect(18, 10000, 0, True)

        elif (Role == "Kyojuro") or (Role == "Shinjuro"):
            e.npc.world.getAllPlayers()[i].addPotionEffect(12, 10000, 0, True)
            e.npc.getStats().getMelee().setEffect(1,1,5)

        elif (Role == "Tengen"):
            e.npc.world.getAllPlayers()[i].addPotionEffect(3, 10000, 0, True)
            e.npc.world.getAllPlayers()[i].addPotionEffect(1, 10000, 0, True)

        elif (Role == "Sanemi"):
            if (Time == False):
                e.npc.world.getAllPlayers()[i].addPotionEffect(1, 10, 1, True)
            else:
                e.npc.world.getAllPlayers()[i].addPotionEffect(1, 10, 0, True)
        
        elif (Role == "Gyomei"):
            if (Time == False):
                e.npc.world.getAllPlayers()[i].addPotionEffect(11, 10, 0, True)

        elif (Role == "Urokodaki"):
            if (Time == True):
                e.npc.world.getAllPlayers()[i].addPotionEffect(1, 10, 0, True)

        elif (Role == "Sabito"):
            if (Time == False):
                e.npc.world.getAllPlayers()[i].addPotionEffect(1, 10, 0, True)

        elif (Role == "Jigoro"):
            e.npc.world.getAllPlayers()[i].addPotionEffect(1, 1000, 0, True)

        elif (Role == "Yoriichi"):
            e.npc.world.getAllPlayers()[i].addPotionEffect(1, 1000, 0, True)
            if Time == True:
                e.npc.world.getAllPlayers()[i].addPotionEffect(11, 10, 0, True)

        elif (Role == "Muzan"):
            e.npc.world.getAllPlayers()[i].addPotionEffect(11, 1000, 0, True)
            if Time == True:
                e.npc.world.getAllPlayers()[i].addPotionEffect(1, 10, 0, True)
            if e.npc.world.getTempdata().get("MuzanKilledNezuko") == True:
                e.npc.world.getAllPlayers()[i].addPotionEffect(11, 1000, 1, True)

        elif (Role == "Nakime"):
            e.npc.world.getAllPlayers()[i].addPotionEffect(18, 1000, 0, True)

        elif (Role == "Kokushibo"):
            e.npc.world.getAllPlayers()[i].addPotionEffect(1, 1000, 0, True)

        elif (Role == "Daki") and (Time == True):
            e.npc.world.getAllPlayers()[i].addPotionEffect(18, 10, 0, True)

        elif (Role == "Rui") and (Time == True):
            e.npc.world.getAllPlayers()[i].addPotionEffect(18, 10, 0, True)		

        elif (Role == "Kaigaku"):
            e.npc.world.getAllPlayers()[i].addPotionEffect(1, 10000, 0, True)
            if (Time == True) and (e.npc.world.getTempdata().get("KaigakuKilledZenitsu") == False):
                e.npc.world.getAllPlayers()[i].addPotionEffect(18, 10, 0, True)

        elif (Role == "Furuto") and (Time == True):
            e.npc.world.getAllPlayers()[i].addPotionEffect(18, 10, 0, True)

        elif (Role == "Demon") and (Time == True):
            e.npc.world.getAllPlayers()[i].addPotionEffect(18, 10, 0, True)

def RolesMessages(e, Role, Player):
    """
    Send messages to player whane they get their roles
    """
    GdList = e.npc.world.getTempdata().get("GoodList")
    BdList = e.npc.world.getTempdata().get("BadList")
    MList = e.npc.world.getTempdata().get("MoonList")
    UpMList = e.npc.world.getTempdata().get("UpperMoonList")
    RandomMoon = random.choice(MList)
    RandomUpperMoon = random.choice(UpMList)
    Muzan = e.npc.world.getTempdata().get("Muzan")
    Daki = e.npc.world.getTempdata().get("Daki")
    Gyutaro = e.npc.world.getTempdata().get("Gyutaro")

    e.npc.executeCommand('/tellraw '+str(Player)+' {"text":"                                                                                 ","color":"dark_gray","strikethrough":true}')
    if Role == "Muzan":
        e.npc.executeCommand('/tellraw '+str(Player)+' ["",{"text":"DemonSlayer\u2502","color":"red"},{"text":"Roles\u2502","color":"gold"},{"text":" Votre role est :","color":"gray"},{"text":" Muzan\n"},{"text":"Vous appartenez au camp des ","color":"gray"},{"text":"demons","color":"dark_red"},{"text":".\nVous obtenez les effets ","color":"gray"},{"text":"Speed I","color":"yellow"},{"text":" et ","color":"gray"},{"text":"Resistance I","color":"yellow"},{"text":" permanents, ainsi que ","color":"gray"},{"text":"Force I","color":"yellow"},{"text":" la ","color":"gray"},{"text":"nuit","color":"dark_blue"},{"text":".\nVotre camp comporte neanmoins un traitre, ","color":"gray"},{"text":"Nezuko","color":"red"},{"text":". Si vous parvenez a tuer ","color":"gray"},{"text":"Nezuko","color":"red"},{"text":" de votre main, vous obtiendrez les effets ","color":"gray"},{"text":"Force I","color":"yellow"},{"text":" et ","color":"gray"},{"text":"Resistance II","color":"yellow"},{"text":" permanents. Vous connaissez egalement toutes les autres ","color":"gray"},{"text":"lunes demoniaques","color":"dark_green"},{"text":". Cependant, certains parmi eux ne possedent pas cette liste.","color":"gray"}]')
        for i in range(0, len(BdList)):
            e.npc.executeCommand('/tellraw '+str(Player)+' ["",{"text":"DemonSlayer\u2502","color":"red"},{"text":"Roles\u2502","color":"gold"},{"text":" Demons : ","color":"gray"},{"text":"'+str(BdList[i])+'","color":"white"}]')

    elif Role == "Nakime":
        e.npc.executeCommand('/tellraw '+str(Player)+' ["",{"text":"DemonSlayer\u2502","color":"red"},{"text":"Roles\u2502","color":"gold"},{"text":" Votre role est :","color":"gray"},{"text":" Nakime\n"},{"text":"Vous appartenez au camp des ","color":"gray"},{"text":"demons","color":"dark_red"},{"text":".\nVous obtenez un effet ","color":"gray"},{"text":"Weakness I","color":"yellow"},{"text":" permanent.\nVous connaissez le ","color":"gray"},{"text":"Muzan","color":"red"},{"text":" de votre equipe.","color":"gray"}]')
        e.npc.executeCommand('/tellraw '+str(Player)+' ["",{"text":"DemonSlayer\u2502","color":"red"},{"text":"Roles\u2502","color":"gold"},{"text":" Muzan : ","color":"gray"},{"text":"'+str(Muzan)+'","color":"white"}]')
    elif Role == "Kokushibo":
        e.npc.executeCommand('/tellraw '+str(Player)+' ["",{"text":"DemonSlayer\u2502","color":"red"},{"text":"Roles\u2502","color":"gold"},{"text":" Votre role est :","color":"gray"},{"text":" Nakime\n"},{"text":"Vous appartenez au camp des ","color":"gray"},{"text":"demons","color":"dark_red"},{"text":".\nVous obtenez un effet ","color":"gray"},{"text":"Weakness I","color":"yellow"},{"text":" permanent.\nVous connaissez le ","color":"gray"},{"text":"Muzan","color":"red"},{"text":" de votre equipe.","color":"gray"}]')
        e.npc.executeCommand('/tellraw '+str(Player)+' ["",{"text":"DemonSlayer\u2502","color":"red"},{"text":"Roles\u2502","color":"gold"},{"text":" Muzan : ","color":"gray"},{"text":"'+str(Muzan)+'","color":"white"}]')
        for i in range(0, len(BdList)):
            e.npc.executeCommand('/tellraw '+str(Player)+' ["",{"text":"DemonSlayer\u2502","color":"red"},{"text":"Roles\u2502","color":"gold"},{"text":" Demons : ","color":"gray"},{"text":"'+str(BdList[i])+'","color":"white"}]')

    elif Role == "Doma":
        e.npc.executeCommand('/tellraw '+str(Player)+' ["",{"text":"DemonSlayer\u2502","color":"red"},{"text":"Roles\u2502","color":"gold"},{"text":" Votre role est :","color":"gray"},{"text":" Doma\n"},{"text":"Vous appartenez au camp des ","color":"gray"},{"text":"demons","color":"dark_red"},{"text":".\nVous obtenez un effet de ","color":"gray"},{"text":"Force I","color":"yellow"},{"text":" la nuit.\nVous connaissez le ","color":"gray"},{"text":"Muzan","color":"dark_green"},{"text":" de votre equipe, et les autres ","color":"gray"},{"text":"lunes superieures.","color":"dark_green"}]')
        e.npc.executeCommand('/tellraw '+str(Player)+' ["",{"text":"DemonSlayer\u2502","color":"red"},{"text":"Roles\u2502","color":"gold"},{"text":" Muzan : ","color":"gray"},{"text":"'+str(Muzan)+'","color":"white"}]')

    elif Role == "Akaza":
        e.npc.executeCommand('/tellraw '+str(Player)+' ["",{"text":"DemonSlayer\u2502","color":"red"},{"text":"Roles\u2502","color":"gold"},{"text":" Votre role est :","color":"gray"},{"text":" Akaza\n"},{"text":"Vous appartenez au camp des ","color":"gray"},{"text":"demons","color":"dark_red"},{"text":".\nVous obtenez un effet de ","color":"gray"},{"text":"Force I","color":"yellow"},{"text":" permanent. Si un autre ","color":"gray"},{"text":"demon","color":"dark_red"},{"text":" se trouve dans un rayon de 20 blocs, vous obtiendrez les effets ","color":"gray"},{"text":"Weakness I","color":"yellow"},{"text":" et ","color":"gray"},{"text":"Slowness I","color":"yellow"},{"text":".\nVous connaissez le ","color":"gray"},{"text":"Muzan","color":"dark_green"},{"text":" de votre equipe, et les autres ","color":"gray"},{"text":"lunes superieures.","color":"dark_green"}]')
        e.npc.executeCommand('/tellraw '+str(Player)+' ["",{"text":"DemonSlayer\u2502","color":"red"},{"text":"Roles\u2502","color":"gold"},{"text":" Muzan : ","color":"gray"},{"text":"'+str(Muzan)+'","color":"white"}]')

    elif Role == "Gyokko":
        e.npc.executeCommand('/tellraw '+str(Player)+' ["",{"text":"DemonSlayer\u2502","color":"red"},{"text":"Roles\u2502","color":"gold"},{"text":" Votre role est :","color":"gray"},{"text":" Gyokko\n"},{"text":"Vous appartenez au camp des ","color":"gray"},{"text":"demons","color":"dark_red"},{"text":".\nVous obtenez un effet de ","color":"gray"},{"text":"Force I","color":"yellow"},{"text":" de ","color":"gray"},{"text":"nuit","color":"dark_blue"},{"text":". Vous pourrez a tout moment vous ","color":"gray"},{"text":"teleporter de maniere aleatoire","underlined":true,"color":"gray"},{"text":" sur un de vos pots de teleportation grace a la commande :","color":"gray"},{"text":"\n"},{"text":"/trigger GTP add 1","color":"white"},{"text":"\n"},{"text":"Vos pots se trouvent a des coordonnées aleatoire entre ","color":"gray"},{"text":"150 et 300 blocs du centre","color":"white"},{"text":".\nLorsque des joueurs brisent vos pots, vous perdez ","color":"gray"},{"text":"3 \u2764 permanents","color":"red"},{"text":".\nVous connaissez le ","color":"gray"},{"text":"Muzan","color":"dark_green"},{"text":" de votre equipe, et les autres ","color":"gray"},{"text":"lunes superieures.","color":"dark_green"}]')
        e.npc.executeCommand('/tellraw '+str(Player)+' ["",{"text":"DemonSlayer\u2502","color":"red"},{"text":"Roles\u2502","color":"gold"},{"text":" Muzan : ","color":"gray"},{"text":"'+str(Muzan)+'","color":"white"}]')
        for i in range(0, len(BdList)):
            e.npc.executeCommand('/tellraw '+str(Player)+' ["",{"text":"DemonSlayer\u2502","color":"red"},{"text":"Roles\u2502","color":"gold"},{"text":" Demons : ","color":"gray"},{"text":"'+str(BdList[i])+'","color":"white"}]')

    elif Role == "Daki":
        e.npc.executeCommand('/tellraw '+str(Player)+' ["",{"text":"DemonSlayer\u2502","color":"red"},{"text":"Roles\u2502","color":"gold"},{"text":" Votre role est :","color":"gray"},{"text":" Daki\n"},{"text":"Vous appartenez au camp des ","color":"gray"},{"text":"demons","color":"dark_red"},{"text":".\nVous obtenez un effet de ","color":"gray"},{"text":"Force I","color":"yellow"},{"text":" de nuit, et ","color":"gray"},{"text":"Weakness I","color":"yellow"},{"text":" le jour.","color":"gray"},{"text":"\n"},{"text":"======","color":"dark_purple"},{"text":" est ","color":"gray"},{"text":"Gyutaro","color":"dark_green"},{"text":". Si vous mourrez, temps que ","color":"gray"},{"text":"Gyutaro","color":"dark_green"},{"text":" sera en vie, vous pourrez reaparaitre apres 2 minutes. Il en vas de meme pour ","color":"gray"},{"text":"Gyutaro","color":"dark_green"},{"text":", il ","color":"gray"},{"text":"ressucitera","color":"white"},{"text":" si vous restez en vie. Neanmoins, si vous ","color":"gray"},{"text":"mourrez tous les 2 dans un delais de 2 minutes","color":"white"},{"text":", vous serez elimines de maniere classique.\nVous connaissez le ","color":"gray"},{"text":"Muzan","color":"dark_green"},{"text":" de votre equipe, et les autres ","color":"gray"},{"text":"lunes superieures.","color":"dark_green"}]')
        e.npc.executeCommand('/tellraw '+str(Player)+' ["",{"text":"DemonSlayer\u2502","color":"red"},{"text":"Roles\u2502","color":"gold"},{"text":" Muzan : ","color":"gray"},{"text":"'+str(Muzan)+'","color":"white"}]')
        e.npc.executeCommand('/tellraw '+str(Player)+' ["",{"text":"DemonSlayer\u2502","color":"red"},{"text":"Roles\u2502","color":"gold"},{"text":" Gyutaro : ","color":"gray"},{"text":"'+str(Gyutaro)+'","color":"white"}]')

    elif Role == "Gyutaro":
        e.npc.executeCommand('/tellraw '+str(Player)+' ["",{"text":"DemonSlayer\u2502","color":"red"},{"text":"Roles\u2502","color":"gold"},{"text":" Votre role est :","color":"gray"},{"text":" Gyutaro\n"},{"text":"Vous appartenez au camp des ","color":"gray"},{"text":"demons","color":"dark_red"},{"text":".\nVous obtenez un effet de ","color":"gray"},{"text":"Force I","color":"yellow"},{"text":" de nuit.","color":"gray"},{"text":"\n"},{"text":"======","color":"dark_purple"},{"text":" est ","color":"gray"},{"text":"Daki","color":"dark_green"},{"text":". Si vous mourrez, temps que ","color":"gray"},{"text":"Daki","color":"dark_green"},{"text":" sera en vie, vous pourrez reaparaitre apres 2 minutes. Il en vas de meme pour ","color":"gray"},{"text":"Daki","color":"dark_green"},{"text":", il ","color":"gray"},{"text":"ressucitera","color":"white"},{"text":" si vous restez en vie. Neanmoins, si vous ","color":"gray"},{"text":"mourrez tous les 2 dans un delais de 2 minutes","color":"white"},{"text":", vous serez elimines de maniere classique.\nVous connaissez le ","color":"gray"},{"text":"Muzan","color":"dark_green"},{"text":" de votre equipe, et les autres ","color":"gray"},{"text":"lunes superieures.","color":"dark_green"}]')
        e.npc.executeCommand('/tellraw '+str(Player)+' ["",{"text":"DemonSlayer\u2502","color":"red"},{"text":"Roles\u2502","color":"gold"},{"text":" Muzan : ","color":"gray"},{"text":"'+str(Muzan)+'","color":"white"}]')
        e.npc.executeCommand('/tellraw '+str(Player)+' ["",{"text":"DemonSlayer\u2502","color":"red"},{"text":"Roles\u2502","color":"gold"},{"text":" Daki : ","color":"gray"},{"text":"'+str(Daki)+'","color":"white"}]')

    elif Role == "Rui":
        e.npc.executeCommand('/tellraw '+str(Player)+' ["",{"text":"DemonSlayer\u2502","color":"red"},{"text":"Roles\u2502","color":"gold"},{"text":" Votre role est :","color":"gray"},{"text":" Rui\n"},{"text":"Vous appartenez au camp des ","color":"gray"},{"text":"demons","color":"dark_red"},{"text":".\nVous obtenez un effet de ","color":"gray"},{"text":"Weakness I","color":"yellow"},{"text":" permanent.\nVous obtenez un fil, qui vous servira a infliger des ","color":"gray"},{"text":"debuffs","color":"white"},{"text":" comme ","color":"gray"},{"text":"Poison, Weakness, ou Slowness","color":"yellow"},{"text":", avec un pourcentage aleatoire pour chacun des effets.","color":"gray"},{"text":"\n"},{"text":"Vous connaissez le ","color":"gray"},{"text":"Muzan","color":"dark_green"},{"text":" de votre equipe.","color":"gray"}]')
        e.npc.executeCommand('/tellraw '+str(Player)+' ["",{"text":"DemonSlayer\u2502","color":"red"},{"text":"Roles\u2502","color":"gold"},{"text":" Muzan : ","color":"gray"},{"text":"'+str(Muzan)+'","color":"white"}]')

    elif Role == "Kaigaku":
        e.npc.executeCommand('/tellraw '+str(Player)+' ["",{"text":"DemonSlayer\u2502","color":"red"},{"text":"Roles\u2502","color":"gold"},{"text":" Votre role est :","color":"gray"},{"text":" Kaigaku\n"},{"text":"Vous appartenez au camp des ","color":"gray"},{"text":"demons","color":"dark_red"},{"text":".\nVous obtenez un effet de ","color":"gray"},{"text":"Weakness I","color":"yellow"},{"text":" le jour, et de ","color":"gray"},{"text":"Speed I","color":"yellow"},{"text":" permanent.\nVous pouvez invoquer un ","color":"gray"},{"text":"eclair","color":"gold"},{"text":" pour retirer ","color":"gray"},{"text":"3 \u2764","color":"red"},{"text":" permanents a chaque joueur dans un rayon de ","color":"gray"},{"text":"15 blocs","underlined":true,"color":"gray"},{"text":" grace a la commande:","color":"gray"},{"text":"\n/trigger KL add 1\n"},{"text":"Vous connaissez une ","color":"gray"},{"text":"lune","color":"dark_green"},{"text":" de votre equipe.","color":"gray"}]')
        e.npc.executeCommand('/tellraw '+str(Player)+' ["",{"text":"DemonSlayer\u2502","color":"red"},{"text":"Roles\u2502","color":"gold"},{"text":" Muzan : ","color":"gray"},{"text":"'+str(Muzan)+'","color":"white"}]')    

    elif Role == "Sasumaru":
        e.npc.executeCommand('/tellraw '+str(Player)+' ["",{"text":"DemonSlayer\u2502","color":"red"},{"text":"Roles\u2502","color":"gold"},{"text":" Votre role est :","color":"gray"},{"text":" Sasumaru\n"},{"text":"Vous appartenez au camp des ","color":"gray"},{"text":"demons","color":"dark_red"},{"text":".\nVous obtenez un effet de ","color":"gray"},{"text":"Weakness I","color":"yellow"},{"text":" permanent.\nLorsque vous toucherez un joueur avec votre arc, il explosera dans un rayon de 4 blocs et fera apparaitre des flammes. Cette explosion ne detruit pas de blocs.","color":"gray"},{"text":"\n"},{"text":"Vous connaissez une ","color":"gray"},{"text":"lune","color":"dark_green"},{"text":" de votre equipe.","color":"gray"}]')
        e.npc.executeCommand('/tellraw '+str(Player)+' ["",{"text":"DemonSlayer\u2502","color":"red"},{"text":"Roles\u2502","color":"gold"},{"text":" Lune aleatoire : ","color":"gray"},{"text":"'+str(RandomMoon)+'","color":"white"}]')

    elif Role == "Kyogai":
        e.npc.executeCommand('/tellraw '+str(Player)+' ["",{"text":"DemonSlayer\u2502","color":"red"},{"text":"Roles\u2502","color":"gold"},{"text":" Votre role est :","color":"gray"},{"text":" Kyogai\n"},{"text":"Vous appartenez au camp des ","color":"gray"},{"text":"demons","color":"dark_red"},{"text":".\nVous obtenez un effet de ","color":"gray"},{"text":"Weakness I","color":"yellow"},{"text":" le jour.\nVous possedez un baton qui vous permettra de faire faire un ","color":"gray"},{"text":"180\u2218","color":"white"},{"text":" a votre cible, en plus de lui infliger ","color":"gray"},{"text":"Slowness I","color":"yellow"},{"text":" pendant 10 secondes et lui infliger un ","color":"gray"},{"text":"recul","color":"yellow"},{"text":" important.","color":"gray"},{"text":"\n"},{"text":"Vous connaissez une ","color":"gray"},{"text":"lune","color":"dark_green"},{"text":" de votre equipe.\n","color":"gray"},{"text":"Si le ","bold":true,"underlined":true,"color":"gray"},{"text":"Muzan","bold":true,"underlined":true,"color":"dark_green"},{"text":" de votre equipe vient a mourir, vous devrez gagner seul en eliminant ","bold":true,"underlined":true,"color":"gray"},{"text":"demons","bold":true,"underlined":true,"color":"dark_red"},{"text":" et ","bold":true,"underlined":true,"color":"gray"},{"text":"slayers","bold":true,"underlined":true,"color":"blue"},{"text":".","bold":true,"underlined":true,"color":"gray"}]')
        e.npc.executeCommand('/tellraw '+str(Player)+' ["",{"text":"DemonSlayer\u2502","color":"red"},{"text":"Roles\u2502","color":"gold"},{"text":" Lune aleatoire : ","color":"gray"},{"text":"'+str(RandomMoon)+'","color":"white"}]')

    elif Role == "Yahaba":
        e.npc.executeCommand('/tellraw '+str(Player)+' ["",{"text":"DemonSlayer\u2502","color":"red"},{"text":"Roles\u2502","color":"gold"},{"text":" Votre role est :","color":"gray"},{"text":" Yahaba\n"},{"text":"Vous appartenez au camp des ","color":"gray"},{"text":"demons","color":"dark_red"},{"text":".\nVous obtenez une cible du camp des ","color":"gray"},{"text":"slayers","color":"blue"},{"text":" : ","color":"gray"},{"text":"=====","color":"white"},{"text":"\n"},{"text":"Si vous tuez cette cible, vous obtiendrez ","color":"gray"},{"text":"Force I","color":"yellow"},{"text":" ainsi que ","color":"gray"},{"text":"2 \u2764","color":"red"},{"text":" permanents.","color":"gray"},{"text":"\n"},{"text":"Vous connaissez une ","color":"gray"},{"text":"lune","color":"dark_green"},{"text":" de votre equipe.","color":"gray"}]')
        e.npc.executeCommand('/tellraw '+str(Player)+' ["",{"text":"DemonSlayer\u2502","color":"red"},{"text":"Roles\u2502","color":"gold"},{"text":" Lune aleatoire : ","color":"gray"},{"text":"'+str(RandomMoon)+'","color":"white"}]')

    elif Role == "Kumo":
        e.npc.executeCommand('/tellraw '+str(Player)+' ["",{"text":"DemonSlayer\u2502","color":"red"},{"text":"Roles\u2502","color":"gold"},{"text":" Votre role est :","color":"gray"},{"text":" Kumo\n"},{"text":"Vous appartenez au camp des ","color":"gray"},{"text":"demons","color":"dark_red"},{"text":".\nVous subissez un effet de ","color":"gray"},{"text":"Weakness I","color":"yellow"},{"text":" permanent.\nVous obtenez un ","color":"gray"},{"text":"fil","color":"white"},{"text":", qui vous permet de faire apparaitre une ","color":"gray"},{"text":"toile","color":"white"},{"text":" sous les pieds de votre adversaire toutes les ","color":"gray"},{"text":"40 secondes","underlined":true,"color":"gray"},{"text":".","color":"gray"},{"text":"\n"},{"text":"Vous connaissez une ","color":"gray"},{"text":"lune superieure","color":"dark_green"},{"text":" de votre equipe.","color":"gray"}]')
        e.npc.executeCommand('/tellraw '+str(Player)+' ["",{"text":"DemonSlayer\u2502","color":"red"},{"text":"Roles\u2502","color":"gold"},{"text":" Lune aleatoire : ","color":"gray"},{"text":"'+str(RandomUpperMoon)+'","color":"white"}]')

    elif Role == "Furuto":
        e.npc.executeCommand('/tellraw '+str(Player)+' ["",{"text":"DemonSlayer\u2502","color":"red"},{"text":"Roles\u2502","color":"gold"},{"text":" Votre role est :","color":"gray"},{"text":" Furuto\n"},{"text":"Vous appartenez au camp des ","color":"gray"},{"text":"demons","color":"dark_red"},{"text":".\nVous subissez un effet de ","color":"gray"},{"text":"Weakness I","color":"yellow"},{"text":" le ","color":"gray"},{"text":"jour","color":"gold"},{"text":".\nVous pouvez perturber le systeme nerveux de vos ennemis dans un rayon de ","color":"gray"},{"text":"15 blocs","underlined":true,"color":"gray"},{"text":" grace a la commande : ","color":"gray"},{"text":"/trigger FS add 1","color":"white"},{"text":"\n"},{"text":"Vos ennemis subiront un recul dans une direction aleatoire toutes les secondes pendant 30 secondes.","color":"gray"},{"text":"\n"},{"text":"Vous connaissez une ","color":"gray"},{"text":"lune","color":"dark_green"},{"text":" de votre equipe.","color":"gray"}]')
        e.npc.executeCommand('/tellraw '+str(Player)+' ["",{"text":"DemonSlayer\u2502","color":"red"},{"text":"Roles\u2502","color":"gold"},{"text":" Lune aleatoire : ","color":"gray"},{"text":"'+str(RandomMoon)+'","color":"white"}]')

    elif Role == "Demon":
        e.npc.executeCommand('/tellraw '+str(Player)+' ["",{"text":"DemonSlayer\u2502","color":"red"},{"text":"Roles\u2502","color":"gold"},{"text":" Votre role est :","color":"gray"},{"text":" Demon\n"},{"text":"Vous appartenez au camp des ","color":"gray"},{"text":"demons","color":"dark_red"},{"text":".\nVous subissez un effet de ","color":"gray"},{"text":"Weakness I","color":"yellow"},{"text":" le ","color":"gray"},{"text":"jour","color":"gold"},{"text":", et ","color":"gray"},{"text":"Force I","color":"yellow"},{"text":" la ","color":"gray"},{"text":"nuit","color":"dark_blue"},{"text":".\nA chaque kill, cette force augmente legerement.","color":"gray"},{"text":"\n"},{"text":"Vous connaissez une ","color":"gray"},{"text":"lune","color":"dark_green"},{"text":" de votre equipe.","color":"gray"}]')
        e.npc.executeCommand('/tellraw '+str(Player)+' ["",{"text":"DemonSlayer\u2502","color":"red"},{"text":"Roles\u2502","color":"gold"},{"text":" Lune aleatoire : ","color":"gray"},{"text":"'+str(RandomUpperMoon)+'","color":"white"}]')


    e.npc.executeCommand('/tellraw '+str(Player)+' {"text":"                                                                                 ","color":"dark_gray","strikethrough":true}')

def VictoryOfGroup(e):
    """
    Say if a group wins
    """
    if e.npc.world.getTempdata().get("TotalGroup") == 1:
        e.npc.world.broadcast('Game ended')


def init(e):
    if (e.npc.getStoreddata().get("HasReset") != 1):
        if e.npc.getDisplay().getName() == "Border": 
            e.npc.getStoreddata().put("HasReset", 1)
            e.npc.executeCommand("/noppes config chunkloaders 35")
            InitInternal(e)
            e.npc.executeCommand('/tellraw @a ["",{"text":"[","color":"dark_gray"},{"text":"DS","color":"dark_red"},{"text":"]","color":"dark_gray"},{"text":" - Server set up : ","color":"gray"},{"text":"successful","color":"green"}]')
            if e.npc.world.getTempdata().get("SuperHeroes") == True:
                SuperHeroes(e)
            e.npc.setPosition(0, 150, 0)
            e.npc.reset() 


def tick(e):
    if e.npc.world.getTempdata().get("GameStarted") == 1 :
        try:
            if e.npc.getDisplay().getName() == "Border":
                if e.npc.world.getTempdata().get("RedditDSDisplay") != True:
                    Displaying(e)
                RolesEffects(e)
                ForceCommands(e)
                DoubleHealth(e)
                RodBlock(e)
                CatEyes(e)
                GiveRoles(e)
                CountingPlayersOnKill(e)
                Counter(e)
                if (e.npc.world.getTempdata().get("DeathMatchTP") == None):
                    ShrinkBorder(e)
                CutClean(e)
                HasteyBoys(e)
                AppleFlintRate(e)
                GoldenHead(e)
        except Exception as err:
            if e.npc.world.getTempdata().get("GameStarted") == 1:
                e.npc.world.broadcast("Please screenshot this to the developper with youre game state and config :")
                e.npc.world.broadcast(str(err))
            pass
    else :
        if e.npc.getDisplay().getName() == "Border":
            e.npc.world.spawnClone(13, 203, 0, 4, "Host DS")
            e.npc.executeCommand('/tellraw @a ["",{"text":"[","color":"dark_gray"},{"text":"DS","color":"dark_red"},{"text":"]","color":"dark_gray"},{"text":" - Game ","color":"gray"},{"text":"stoped","color":"red"},{"text":" !","color":"gray"}]')
            e.npc.despawn()
        else:
            pass
