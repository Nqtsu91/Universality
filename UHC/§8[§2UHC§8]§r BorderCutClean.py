
import random
import os

def SuperHeroes(e):
    """
    Display message to choose a power
    """
    e.npc.executeCommand('/tellraw @a ["",{"text":"[","color":"dark_gray"},{"text":"UHC","color":"dark_red"},{"text":"][","color":"dark_gray"},{"text":"SuperHeroes","color":"gold"},{"text":"]","color":"dark_gray"},{"text":" Click on a button below to choose ONE power","color":"gray"},{"text":"\n"},{"text":"[Resistance II]","color":"dark_gray","clickEvent":{"action":"run_command","value":"/effect @p minecraft:resistance 9999 1 true"}},{"text":" - ","color":"gray"},{"text":"[Speed II]","color":"yellow","clickEvent":{"action":"run_command","value":"/effect @p minecraft:speed 9999 1 true"}},{"text":" - ","color":"gray"},{"text":"[JumpBoost IV]","color":"green","clickEvent":{"action":"run_command","value":"/effect @p minecraft:jump_boost 9999 3 true"}},{"text":" - ","color":"gray"},{"text":"[HealthBoost V]","color":"blue","clickEvent":{"action":"run_command","value":"/effect @p minecraft:health_boost 9999 4 true"}},{"text":" - ","color":"gray"},{"text":"[Strength I]","color":"red","clickEvent":{"action":"run_command","value":"/effect @p minecraft:strength 9999 0 true"}}]')


def FinalHeal(e):
    e.npc.executeCommand('/effect @a minecraft:instant_health 1 45 true')
    e.npc.executeCommand('/tellraw @a ["",{"text":"[","color":"dark_gray"},{"text":"UHC","color":"dark_red"},{"text":"]","color":"dark_gray"},{"text":" - Final Heal has been given, dont ask for another one !","color":"gray"}]')

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
            e.npc.world.getTempdata().put("EnchantProbability", EProba+0.5)      # Increase Enchant proba
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
        e.npc.executeCommand("/worldborder set 61.1")

def CountingPlayersOnKill(e):
    if (e.npc.world.getStoreddata().get("TeamsAlive") == 1 ) and (e.npc.getStoreddata().get("EndGameSaid") != True):
        #e.npc.executeCommand('/tellraw @a ["",{"text":"[","color":"dark_gray"},{"text":"UHC","color":"dark_red"},{"text":"] ","color":"dark_gray"},{"text":"[","color": gray,"bold":true},{"text":"Players","color" : dark_green},{"text":"] ","color": gray,"bold":true},{ "text" :"We now have a winner ! Congratulation !","color" : aqua,"bold":true}]')
        e.npc.getStoreddata().put("EndGameSaid", True)
        EndGame(e)
        UpdatingStats(e)
        EndMessages(e)
        e.npc.world.getTempdata().clear()
        e.npc.world.getStoreddata().clear()
        e.npc.despawn()

def UpdatingStats(e):
    try:
        Path = os.path.dirname(os.path.abspath("__file__"))
        Path += "\\CustomNPC Config\\UHC\\Stats\\stats"
        Path = Path.replace("\\", str(os.path.sep))
        with open (str(Path)+".csv", "r") as File :
            Config = File.read()
            Config = Config.split(u'\n')
            Title = Config[0]
            Config.pop(0)
            # Config = file in list

            WinnerList = e.npc.world.getTempdata().get("WinnerList")
            if WinnerList == None :
                WinnerList = []
                for i in range (0, len(e.npc.world.getAllPlayers())):
                    WinnerList.append(e.npc.world.getAllPlayers()[i].getName())

            e.npc.executeCommand('/tellraw @a ["",{"text":"[","color":"dark_gray"},{"text":"UHC","color":"dark_red"},{"text":"]","color":"dark_gray"},{"text":" - ","color":"gray"},{"text":"Winner","color":"gold"},{"text":"(","color":"gray"},{"text":"s","color":"gold"},{"text":") ","color":"gray"},{"text":":","color":"white"}]')
            for i in range(0, len(WinnerList)):
                e.npc.executeCommand('/tellraw @a ["",{"text":"[","color":"dark_gray"},{"text":"UHC","color":"dark_red"},{"text":"]","color":"dark_gray"},{"text":" - ","color":"gray"},{"text":"'+str(WinnerList[i])+'","color":"white"}]')

            KillList = e.npc.world.getStoreddata().get("KillList")

            KillList = KillList.split("//")
            for i in range (0, len(KillList)):
                KillList[i] = KillList[i].split("|")
            KillList.pop(0)
            for i in range (0, len(KillList)):
                if KillList[i][1] == None :
                    KillList[i][1] = 0

            FinalList = []
            
            for z in range(len(Config)-1, -1, -1):
                try:
                    for i in range (len(KillList)-1, -1, -1):
                        Line = Config[z].split(",")
                        if Line[0] == KillList[i][0] :                      # Adding kills
                            Newz = str(KillList[i][1].replace(".0", ""))
                            KillList[i][1] = Newz
                            New = int(Line[1]) + int(KillList[i][1])
                            Line[1] = str(New) 
                            if not Line[0] in WinnerList :
                                New = int(Line[2]) + 1        # Adding Deaths
                                Line[2] = str(New) 
                            else:
                                New = int(Line[3]) + 1        # Adding Wins
                                Line[3] = str(New) 

                            New = int(Line[1])/int(Line[2])        # Updating KDR
                            Line[4] = str(New)   

                            Config[z] = ",".join(Line)                  
                            FinalList.append(Config[z])  
                            KillList.pop(i)
                            Config.pop(z)
                except:
                    pass

            for i in range(0, len(Config)):
                FinalList.append(Config[i])

            for i in range(0, len(KillList)):         
                Line = []
                Line.append(str(KillList[i][0]))
                Line.append("0")
                Line.append("0")
                Line.append("0")
                Line.append("0")
                Done = True
                if KillList[i][1] == None:
                    KillList[i][1] = 0

                    
                New = int(KillList[i][1])
                Line[1] = str(New) 
                if not Line[0] in WinnerList :
                    New = 1        # Adding Deaths
                    Line[2] = str(New) 
                    New = 0        # Adding Wins
                    Line[3] = str(New) 
                else:
                    New = 1        # Adding Wins
                    Line[3] = str(New) 
                if str(Line[2]) == '0' :
                    Line[4] = str(int(Line[1]))
                else:
                    New = int(Line[1])/int(Line[2])        # Updating KDR
                    Line[4] = str(New)   


                Config = ",".join(Line)                 
                FinalList.append(Config)                   


            Path = os.path.dirname(os.path.abspath("__file__"))                 # Updating Final stats file
            Path += "\\CustomNPC Config\\UHC\\Stats\\stats"
            Path = Path.replace("\\", str(os.path.sep))
            with open (str(Path)+".csv", "w") as File :
                File.write(str(Title))
                for i in range(0, len(FinalList)):
                    File.write(u'\n')
                    File.write(str(FinalList[i]))
        
        e.npc.executeCommand('/tellraw @a ["",{"text":"[","color":"dark_gray"},{"text":"UHC","color":"dark_red"},{"text":"]","color":"dark_gray"},{"text":" Stats saved","color":"gray"},{"text":" successfully","color":"green"}]')
        e.npc.world.getTempdata().put("GameStarted", 0)
    except:
        e.npc.executeCommand('/tellraw @a ["",{"text":"[","color":"dark_gray"},{"text":"UHC","color":"dark_red"},{"text":"]","color":"dark_gray"},{"text":" Failed updating stats !","color":"gray"}]')

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
			e.npc.executeCommand('/tellraw @a ["",{"text":"[","color":"dark_gray"},{"text":"UHC","color":"dark_red"},{"text":"] ","color":"dark_gray"},{"text":"[","color": gray,"bold":true},{"text":"Kills","color" : blue},{"text":"] ","color": gray,"bold":true},{ "text" :"'+str(i+1)+' : ","bold":flase},{ "text" :"'+str(FinalList[i][0])+' --- ","color": '+str(ColorList[i])+',"bold":false},{ "text" :"'+str(FinalList[i][1])+' Kills ","bold":false}]')
	except:
		pass
	
	e.npc.world.spawnClone(13, 203, 0, 2, "Host UHC")

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
    e.npc.executeCommand('/tellraw @a ["",{"text":"[","color":"dark_gray"},{"text":"UHC","color":"dark_red"},{"text":"][","color":"dark_gray"},{"text":"Border","color":"gold"},{"text":"]","color":"dark_gray"},{"text":" Borders have shrunk to ","color":"gray"},{"text":"-120 120","color":"gold"}]')
    for i in range(0, len(e.npc.world.getAllPlayers())):
        players = e.npc.world.getAllPlayers()
        e.npc.executeCommand("/playsound note.pling "+str(players[i].getName()))
        e.npc.world.spawnClone( int(0), 150, int(0), 2, "Spawner").setFaction(0)			# spawning classic bots

def ShrinkSecondBorder(e):
    e.npc.getStoreddata().put("Forced2Border", 1)
    e.npc.world.getStoreddata().put("SecondBorder", 0)
    e.npc.world.getTempdata().put("SecondBorder", 0)
    e.npc.executeCommand('/tellraw @a ["",{"text":"[","color":"dark_gray"},{"text":"UHC","color":"dark_red"},{"text":"][","color":"dark_gray"},{"text":"Border","color":"gold"},{"text":"]","color":"dark_gray"},{"text":" Borders have shrunk to ","color":"gray"},{"text":"-80 80","color":"gold"}]')
    for i in range(0, len(e.npc.world.getAllPlayers())):
        players = e.npc.world.getAllPlayers()
        e.npc.executeCommand("/playsound note.pling "+str(players[i].getName()))
        e.npc.world.spawnClone( int(0), 150, int(0), 2, "Spawner").setFaction(0)			# spawning classic bots

def ShrinkFinalBorder(e):
    e.npc.getStoreddata().put("Forced3Border", 1)
    e.npc.world.getStoreddata().put("FinalBorder", 0)
    e.npc.world.getTempdata().put("FinalBorder", 0)
    e.npc.executeCommand('/tellraw @a ["",{"text":"[","color":"dark_gray"},{"text":"UHC","color":"dark_red"},{"text":"][","color":"dark_gray"},{"text":"Border","color":"gold"},{"text":"]","color":"dark_gray"},{"text":" Borders have shrunk to ","color":"gray"},{"text":"-50 50","color":"gold"}]')
    for i in range(0, len(e.npc.world.getAllPlayers())):
        players = e.npc.world.getAllPlayers()
        e.npc.executeCommand("/playsound note.pling "+str(players[i].getName()))
        e.npc.world.spawnClone( int(0), 150, int(0), 2, "Spawner").setFaction(0)			# spawning classic bots

def EnablePvP(e):
    e.npc.getStoreddata().put("ForcedPvP", 1)
    e.npc.world.getStoreddata().put("PvPTime", 0)
    e.npc.world.getTempdata().put("PvPTime", 0)
    e.npc.executeCommand('/tellraw @a ["",{"text":"[","color":"dark_gray"},{"text":"UHC","color":"dark_red"},{"text":"]","color":"dark_gray"},{"text":" PvP is now enabled !","color":"gray"}]')
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
            e.npc.executeCommand('/scoreboard objectives remove HealTrigger')
            e.npc.executeCommand('/scoreboard objectives add HealTrigger trigger')
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

	List = ["BotNumber","TeamSize","DiamondProbability","NoCleanRegen","BleedingDiamonds","BleedingIron","BleedingGold","PvPTime","MinTimeSpread","MaxTimeSpread","MolePerTeam","FinalBorder","SecondBorder","FirstBorder","AppleRate","FlintRate","CutClean","BadlionKillsSystem","NoCleanUpEnabled","ThunderStrike","WitherSoundI","WitherSoundII","IronGolemSound","WaterAllowed","CatEyes","MasterLevel","SuperHeroes","BookCeption","DoubleHealth","OneShot","BleedingSweets","Rodless","Mole","RedditUHCDisplay","GoldenHeads","ExplodeOnDeath","FireAspectAllowed","AbsoLess","ForcedType","BadlionKB","ArcticMeta","ScatterMessageEnabled","LoadTeams"]

	e.npc.executeCommand('/tellraw @a ["",{"text":"[","color":"dark_gray"},{"text":"UHC","color":"dark_red"},{"text":"]","color":"dark_gray"},{"text":" Game title :","color":"white"},{"text":"\n"},{"text":" - ","color":"gray"},{"text":"'+str(Name)+'","color":"red"}]')
	for i in range(0, len(List)):
		Color = "white"
		if str(e.npc.world.getTempdata().get(List[i])) == "True":
			Color = "green"
		elif str(e.npc.world.getTempdata().get(List[i])) == "False":
			Color = "red"
		elif str(e.npc.world.getTempdata().get(List[i])) == "None" :
			Color = "black"
		if (Color == "green") or (Color == "white") and (e.npc.world.getTempdata().get(List[i]) != 0):
			e.npc.executeCommand('/tellraw @a ["",{"text":"[","color":"dark_gray"},{"text":"UHC","color":"dark_red"},{"text":"]","color":"dark_gray"},{"text":" - ","color":"gray"},{"text":"'+str(List[i])+'","color":"light_purple"},{"text":" : ","color":"gray"},{"text":"'+str(e.npc.world.getTempdata().get(List[i]))+'","color":"'+str(Color)+'"}]')

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
                        e.npc.executeCommand('/tellraw @a ["",{"text":"[","color":"dark_gray"},{"text":"UHC","color":"dark_red"},{"text":"]","color":"dark_gray"},{"text":" PvP will enable in ","color":"gray"},{"text":"15 minutes","color":"white"}]')
                    if (VarToCount[i] == "FirstBorder") and (e.npc.getStoreddata().get("Forced1Border") != 1):
                        e.npc.executeCommand('/tellraw @a ["",{"text":"[","color":"dark_gray"},{"text":"UHC","color":"dark_red"},{"text":"][","color":"dark_gray"},{"text":"Border","color":"gold"},{"text":"]","color":"dark_gray"},{"text":" Border will shrink to ","color":"gray"},{"text":"-120 120","color":"gold"},{"text":" in","color":"gray"},{"text":" 15 minutes","color":"dark_gray"}]')
                    if (VarToCount[i] == "SecondBorder") and (e.npc.getStoreddata().get("Forced2Border") != 1):
                        e.npc.executeCommand('/tellraw @a ["",{"text":"[","color":"dark_gray"},{"text":"UHC","color":"dark_red"},{"text":"][","color":"dark_gray"},{"text":"Border","color":"gold"},{"text":"]","color":"dark_gray"},{"text":" Border will shrink to ","color":"gray"},{"text":"-80 80","color":"gold"},{"text":" in","color":"gray"},{"text":" 15 minutes","color":"dark_gray"}]')
                    if (VarToCount[i] == "FinalBorder") and (e.npc.getStoreddata().get("Forced3Border") != 1):
                        e.npc.executeCommand('/tellraw @a ["",{"text":"[","color":"dark_gray"},{"text":"UHC","color":"dark_red"},{"text":"][","color":"dark_gray"},{"text":"Border","color":"gold"},{"text":"]","color":"dark_gray"},{"text":" Border will shrink to ","color":"gray"},{"text":"-50 50","color":"gold"},{"text":" in","color":"gray"},{"text":" 15 minutes","color":"dark_gray"}]')
                    e.npc.getStoreddata().put(VarToCount[i]+"15", 1)

                if Until == 10 and (e.npc.getStoreddata().get(VarToCount[i]+"10") != 1):
                    if (VarToCount[i] == "PvPTime") and (e.npc.getStoreddata().get("ForcedPvP") != 1):
                        e.npc.executeCommand('/tellraw @a ["",{"text":"[","color":"dark_gray"},{"text":"UHC","color":"dark_red"},{"text":"]","color":"dark_gray"},{"text":" PvP will enable in ","color":"gray"},{"text":"10 minutes","color":"white"}]')
                    if (VarToCount[i] == "FirstBorder") and (e.npc.getStoreddata().get("Forced1Border") != 1):
                        e.npc.executeCommand('/tellraw @a ["",{"text":"[","color":"dark_gray"},{"text":"UHC","color":"dark_red"},{"text":"][","color":"dark_gray"},{"text":"Border","color":"gold"},{"text":"]","color":"dark_gray"},{"text":" Border will shrink to ","color":"gray"},{"text":"-120 120","color":"gold"},{"text":" in","color":"gray"},{"text":" 10 minutes","color":"dark_gray"}]')
                    if (VarToCount[i] == "SecondBorder") and (e.npc.getStoreddata().get("Forced2Border") != 1):
                        e.npc.executeCommand('/tellraw @a ["",{"text":"[","color":"dark_gray"},{"text":"UHC","color":"dark_red"},{"text":"][","color":"dark_gray"},{"text":"Border","color":"gold"},{"text":"]","color":"dark_gray"},{"text":" Border will shrink to ","color":"gray"},{"text":"-80 80","color":"gold"},{"text":" in","color":"gray"},{"text":" 10 minutes","color":"dark_gray"}]')
                    if (VarToCount[i] == "FinalBorder") and (e.npc.getStoreddata().get("Forced3Border") != 1):
                        e.npc.executeCommand('/tellraw @a ["",{"text":"[","color":"dark_gray"},{"text":"UHC","color":"dark_red"},{"text":"][","color":"dark_gray"},{"text":"Border","color":"gold"},{"text":"]","color":"dark_gray"},{"text":" Border will shrink to ","color":"gray"},{"text":"-50 50","color":"gold"},{"text":" in","color":"gray"},{"text":" 10 minutes","color":"dark_gray"}]')
                    e.npc.getStoreddata().put(VarToCount[i]+"10", 1)

                if Until == 5 and (e.npc.getStoreddata().get(VarToCount[i]+"5") != 1):
                    if (VarToCount[i] == "PvPTime") and (e.npc.getStoreddata().get("ForcedPvP") != 1):
                        e.npc.executeCommand('/tellraw @a ["",{"text":"[","color":"dark_gray"},{"text":"UHC","color":"dark_red"},{"text":"]","color":"dark_gray"},{"text":" PvP will enable in ","color":"gray"},{"text":"5 minutes","color":"white"}]')
                    if (VarToCount[i] == "FirstBorder") and (e.npc.getStoreddata().get("Forced1Border") != 1):
                        e.npc.executeCommand('/tellraw @a ["",{"text":"[","color":"dark_gray"},{"text":"UHC","color":"dark_red"},{"text":"][","color":"dark_gray"},{"text":"Border","color":"gold"},{"text":"]","color":"dark_gray"},{"text":" Border will shrink to ","color":"gray"},{"text":"-120 120","color":"gold"},{"text":" in","color":"gray"},{"text":" 5 minutes","color":"dark_gray"}]')
                    if (VarToCount[i] == "SecondBorder") and (e.npc.getStoreddata().get("Forced2Border") != 1):
                        e.npc.executeCommand('/tellraw @a ["",{"text":"[","color":"dark_gray"},{"text":"UHC","color":"dark_red"},{"text":"][","color":"dark_gray"},{"text":"Border","color":"gold"},{"text":"]","color":"dark_gray"},{"text":" Border will shrink to ","color":"gray"},{"text":"-80 80","color":"gold"},{"text":" in","color":"gray"},{"text":" 5 minutes","color":"dark_gray"}]')
                    if (VarToCount[i] == "FinalBorder") and (e.npc.getStoreddata().get("Forced3Border") != 1):
                        e.npc.executeCommand('/tellraw @a ["",{"text":"[","color":"dark_gray"},{"text":"UHC","color":"dark_red"},{"text":"][","color":"dark_gray"},{"text":"Border","color":"gold"},{"text":"]","color":"dark_gray"},{"text":" Border will shrink to ","color":"gray"},{"text":"-50 50","color":"gold"},{"text":" in","color":"gray"},{"text":" 5 minutes","color":"dark_gray"}]')
                    e.npc.getStoreddata().put(VarToCount[i]+"5", 1)

                if Until == 1 and (e.npc.getStoreddata().get(VarToCount[i]+"1") != 1):
                    e.npc.getStoreddata().put(VarToCount[i]+"1", 1)
                    if (VarToCount[i] == "PvPTime") and (e.npc.getStoreddata().get("ForcedPvP") != 1):
                        e.npc.executeCommand('/tellraw @a ["",{"text":"[","color":"dark_gray"},{"text":"UHC","color":"dark_red"},{"text":"]","color":"dark_gray"},{"text":" PvP will enable in ","color":"gray"},{"text":"1 minute","color":"white"}]')
                    if (VarToCount[i] == "FirstBorder") and (e.npc.getStoreddata().get("Forced1Border") != 1):
                        e.npc.executeCommand('/tellraw @a ["",{"text":"[","color":"dark_gray"},{"text":"UHC","color":"dark_red"},{"text":"][","color":"dark_gray"},{"text":"Border","color":"gold"},{"text":"]","color":"dark_gray"},{"text":" Border will shrink to ","color":"gray"},{"text":"-120 120","color":"gold"},{"text":" in","color":"gray"},{"text":" 1 minute","color":"dark_gray"}]')
                        e.npc.world.getTempdata().put("Radius", 110)
                    if (VarToCount[i] == "SecondBorder") and (e.npc.getStoreddata().get("Forced2Border") != 1):
                        e.npc.executeCommand('/tellraw @a ["",{"text":"[","color":"dark_gray"},{"text":"UHC","color":"dark_red"},{"text":"][","color":"dark_gray"},{"text":"Border","color":"gold"},{"text":"]","color":"dark_gray"},{"text":" Border will shrink to ","color":"gray"},{"text":"-80 80","color":"gold"},{"text":" in","color":"gray"},{"text":" 1 minute","color":"dark_gray"}]')
                        e.npc.world.getTempdata().put("Radius", 70)
                    if (VarToCount[i] == "FinalBorder") and (e.npc.getStoreddata().get("Forced3Border") != 1):
                        e.npc.executeCommand('/tellraw @a ["",{"text":"[","color":"dark_gray"},{"text":"UHC","color":"dark_red"},{"text":"][","color":"dark_gray"},{"text":"Border","color":"gold"},{"text":"]","color":"dark_gray"},{"text":" Border will shrink to ","color":"gray"},{"text":"-50 50","color":"gold"},{"text":" in","color":"gray"},{"text":" 1 minute","color":"dark_gray"}]')
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

def CheckingConfig(e):
	IntList = ["ProtIncreaseTime","SharpIncreaseTime","EnchantIncreaseTime","DiamondIncreaseTime","DiamondIncreaseRate","GapIncreaseTime","GapIncreaseRate","BotNumber","TeamSize","TeamAliveLimit","PvPTime","MinTimeSpread","MaxTimeSpread","FinalBorder","SecondBorder","KBValue","FirstBorder","DiamondProbability","EnchantProbability","XpMultiplicator","AppleRate","FlintRate","NoCleanRegen","BleedingDiamond","BleedingIron","BleedingGold","MolePerTeam"]
	BooleanList = ["TimeBomb",'MeetUpMode',"ClearedLoot","CutClean","HasteyBoys","NoCleanUpEnabled","CatEyes","MasterLevel","SuperHeroes","BookCeption","DoubleHealth","BleedingSweets","Rodless","Mole","OneShot","GoldenHeads","FireAspectAllowed","AbsoLess","WaterAllowed","ForcedType","ArcticMeta","LoadTeams","RedditUHCDisplay","BadlionKillsSystem","ThunderStrike","WitherSoundI","WitherSoundII","IronGolemSound","VanillaDeathStyle","ExplodeOnDeath","ScatterMessageEnabled"]
	for i in range(0, len(IntList)):
		if isinstance(e.npc.world.getTempdata().get(str(IntList[i])), int) != True:
			e.npc.executeCommand('/tellraw @a ["",{"text":"ConfigChecker found errors in your config, some value are not the right type (ex: BotNumber = True)","color":"green"}]')
			e.npc.executeCommand('/noppes script reload')
	for i in range(0, len(BooleanList)):
		if isinstance(e.npc.world.getTempdata().get(str(BooleanList[i])), bool) != True:
			e.npc.executeCommand('/tellraw @a ["",{"text":"ConfigChecker found errors in your config, some value are not the right type (ex: BotNumber = True)","color":"green"}]')
			e.npc.executeCommand('/noppes script reload')
 
def DeathMatch(e):
    """
    Summon the DeathMatch arena
    """
    if (e.npc.world.getStoreddata().get("TeamsAlive") == e.npc.world.getTempdata().get("StartDeathmatchAt")) and (e.npc.world.getTempdata().get("DeathMatchTP") == None) and (e.npc.world.getTempdata().get("StartDeathmatchAt") != None):
        e.npc.executeCommand("/fill -30 140 -30 30 140 30 minecraft:barrier")
        e.npc.executeCommand("/fill -30 141 -30 30 147 30 minecraft:stone")
        e.npc.executeCommand("/fill -30 148 -30 30 150 30 minecraft:grass")

        e.npc.executeCommand("/fill -30 151 -30 -30 160 30 minecraft:bedrock")
        e.npc.executeCommand("/fill -30 151 -30 30 160 -30 minecraft:bedrock")
        e.npc.executeCommand("/fill 30 151 30 -30 160 30 minecraft:bedrock")
        e.npc.executeCommand("/fill 30 151 30 30 160 -30 minecraft:bedrock")

        e.npc.executeCommand("/fill -30 161 -30 30 161 30 minecraft:barrier")

        e.npc.executeCommand("/tp @a -15 152 -15")
        e.npc.executeCommand("/effect @a minecraft:resistance 15 4 true")
        e.npc.executeCommand('/worldborder set 61.1')
        e.npc.world.getTempdata().put("DeathMatchTP", "True")
        SpecMessageDeathMatch(e)

def SpecMessageDeathMatch(e):
	"""
	Display some message to make the game feel real
	"""
	MessageList = ["Gl","gl","GL","good luck","gl hf","Good Luck","GOOD LUCK","there we go","grats to the winner","DeathMatch started !","Gl Hf guys"]
	SpecList = ["Gonzaloo","dedreviil","Davuki","Fukano","Etoiles","Pickachu","Mentally"]
	a = '/tellraw @a ["",{"text":"[","color":"gray"},{"text":"Host","color":"dark_aqua"},{"text":"] ","color":"gray"},{"text":"[","color":"gray"},{"text":"Spec","color":"aqua"},{"text":"] ","color":"gray"},{"text":"'+str(random.choice(SpecList))+'","color":"gold"},{"text":" : ","color":"white"},{"text":"'+str(random.choice(MessageList))+'","color":"white"}]'
	e.npc.executeCommand(a)

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
        a = '/tellraw @a ["",{"text":"[","color":"dark_gray"},{"text":"UHC","color":"dark_red"},{"text":"] ","color":"dark_gray"},{"text":"[","color":"gray"},{"text":"Winner","color":"gold"},{"text":"] ","color":"gray"},{"text":"'+str(WinnerList[i])+'","color":"white"},{"text":" : ","color":"white"},{"text":"'+str(random.choice(MessageList))+'","color":"white"}]'
        e.npc.executeCommand(a)
    for i in range(0, random.randint(0, 4)):
        MessageList = ["gg","holly","Gg","ty4p",'ez lol',"GG",'GG !',"He's crack :o",":O !","wp","Pvp god be like","gg !","gg","gg","gg"]
        SpecList = ["TryHard","Tylarzz","xNestorio","Gonzaloo","Apexay",'RaiN_DyNasty','jdegoederen',"dedreviil","Davuki","Fukano","Etoiles","Pickachu","Mentally"]
        a = '/tellraw @a ["",{"text":"[","color":"gray"},{"text":"Host","color":"dark_aqua"},{"text":"] ","color":"gray"},{"text":"[","color":"gray"},{"text":"Spec","color":"aqua"},{"text":"] ","color":"gray"},{"text":"'+str(random.choice(SpecList))+'","color":"gold"},{"text":" : ","color":"white"},{"text":"'+str(random.choice(MessageList))+'","color":"white"}]'
        e.npc.executeCommand(a)


def init(e):
    if (e.npc.getStoreddata().get("HasReset") != 1):
        if e.npc.getDisplay().getName() == "Border": 
            e.npc.getStoreddata().put("HasReset", 1)
            e.npc.executeCommand("/noppes config chunkloaders 35")
            InitInternal(e)
            CheckingConfig(e)
            e.npc.executeCommand('/tellraw @a ["",{"text":"[","color":"dark_gray"},{"text":"UHC","color":"dark_red"},{"text":"]","color":"dark_gray"},{"text":" - Server set up : ","color":"gray"},{"text":"successful","color":"green"}]')
            if e.npc.world.getTempdata().get("SuperHeroes") == True:
                SuperHeroes(e)
            e.npc.setPosition(0, 150, 0)
            e.npc.reset() 


def tick(e):
    if e.npc.world.getTempdata().get("GameStarted") == 1 :
        try:
            if e.npc.getDisplay().getName() == "Border":
                if e.npc.world.getTempdata().get("RedditUHCDisplay") != True:
                    Displaying(e) 
                ForceCommands(e)
                DoubleHealth(e)
                RodBlock(e)
                CatEyes(e)
                CountingPlayersOnKill(e)
                Counter(e)
                ShrinkBorder(e)
                CutClean(e)
                HasteyBoys(e)
                AppleFlintRate(e)
                GoldenHead(e)
                DeathMatch(e)
        except Exception as err:
            if e.npc.world.getTempdata().get("GameStarted") == 1:
                e.npc.world.broadcast("Please screenshot this to the developper with youre game state and config :")
                e.npc.world.broadcast(str(err))
            pass
    else :
        if e.npc.getDisplay().getName() == "Border":
            e.npc.world.spawnClone(13, 203, 0, 2, "Host UHC")
            e.npc.executeCommand('/tellraw @a ["",{"text":"[","color":"dark_gray"},{"text":"UHC","color":"dark_red"},{"text":"]","color":"dark_gray"},{"text":" - Game ","color":"gray"},{"text":"stoped","color":"red"},{"text":" !","color":"gray"}]')
            e.npc.despawn()
        else:
            pass

