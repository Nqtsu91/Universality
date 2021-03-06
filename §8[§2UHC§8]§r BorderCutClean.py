
import random
import os

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
    First = e.npc.world.getStoreddata().get("FirstBorder")
    Second = e.npc.world.getStoreddata().get("SecondBorder")
    Final = e.npc.world.getStoreddata().get("FinalBorder")
    if Final <= e.npc.world.getTotalTime():
        e.npc.executeCommand("/worldborder set 91")
        PlayerTP(e)
    elif Second <= e.npc.world.getTotalTime():
        e.npc.executeCommand("/worldborder set 161")
        PlayerTP(e)
    elif First <= e.npc.world.getTotalTime():
        e.npc.executeCommand("/worldborder set 241")
        PlayerTP(e)

def Counter(e):
    try:
        if e.npc.getStoreddata().get("OneSecTicker") == 1 :

            if e.npc.getStoreddata().get("Second") == None :                   # Counting seconds
                e.npc.getStoreddata().put("Second", 0)
            e.npc.getStoreddata().put("Second", e.npc.getStoreddata().get("Second")+1)

            if e.npc.getStoreddata().get("Second") == 60 :
                if e.npc.getStoreddata().get("Minutes") == None :                   # Counting minutes
                    e.npc.getStoreddata().put("Minutes", 0)
                e.npc.getStoreddata().put("Minutes", e.npc.getStoreddata().get("Minutes")+1)
                e.npc.getStoreddata().put("Second", 0)

            if (e.npc.getStoreddata().get("Minutes") == 10) and (e.npc.getStoreddata().get("Second") == 0) :
                e.npc.executeCommand('/effect @a minecraft:instant_health 1 45 true')
                e.npc.executeCommand('/tellraw @a ["",{"text":"[","color":"dark_gray"},{"text":"UHC","color":"dark_red"},{"text":"]","color":"dark_gray"},{"text":" - Final Heal has been given, dont ask for another one !","color":"gray"}]')

            e.npc.getStoreddata().put("OneSecTicker", 0)

            VarToCount = ["PvPTime","FirstBorder","SecondBorder","FinalBorder"]
            for i in range(0, len(VarToCount)):

                Until = (e.npc.world.getTempdata().get(VarToCount[i])) - (e.npc.getStoreddata().get("Minutes"))

                if Until == 15 and (e.npc.getStoreddata().get(VarToCount[i]+"15") != 1):
                    e.npc.getStoreddata().put(VarToCount[i]+"15", 1)
                    if VarToCount[i] == "PvPTime":
                        e.npc.executeCommand('/tellraw @a ["",{"text":"[","color":"dark_gray"},{"text":"UHC","color":"dark_red"},{"text":"]","color":"dark_gray"},{"text":" PvP will enable in ","color":"gray"},{"text":"15 minutes","color":"white"}]')
                    if VarToCount[i] == "FirstBorder":
                        e.npc.executeCommand('/tellraw @a ["",{"text":"[","color":"dark_gray"},{"text":"UHC","color":"dark_red"},{"text":"][","color":"dark_gray"},{"text":"Border","color":"gold"},{"text":"]","color":"dark_gray"},{"text":" Border will shrink to ","color":"gray"},{"text":"-120 120","color":"gold"},{"text":" in","color":"gray"},{"text":" 15 minutes","color":"dark_gray"}]')
                    if VarToCount[i] == "SecondBorder":
                        e.npc.executeCommand('/tellraw @a ["",{"text":"[","color":"dark_gray"},{"text":"UHC","color":"dark_red"},{"text":"][","color":"dark_gray"},{"text":"Border","color":"gold"},{"text":"]","color":"dark_gray"},{"text":" Border will shrink to ","color":"gray"},{"text":"-80 80","color":"gold"},{"text":" in","color":"gray"},{"text":" 15 minutes","color":"dark_gray"}]')
                    if VarToCount[i] == "FinalBorder":
                        e.npc.executeCommand('/tellraw @a ["",{"text":"[","color":"dark_gray"},{"text":"UHC","color":"dark_red"},{"text":"][","color":"dark_gray"},{"text":"Border","color":"gold"},{"text":"]","color":"dark_gray"},{"text":" Border will shrink to ","color":"gray"},{"text":"-50 50","color":"gold"},{"text":" in","color":"gray"},{"text":" 15 minutes","color":"dark_gray"}]')
                    e.npc.getStoreddata().put(VarToCount[i]+"15", 1)

                if Until == 10 and (e.npc.getStoreddata().get(VarToCount[i]+"10") != 1):
                    if VarToCount[i] == "PvPTime":
                        e.npc.executeCommand('/tellraw @a ["",{"text":"[","color":"dark_gray"},{"text":"UHC","color":"dark_red"},{"text":"]","color":"dark_gray"},{"text":" PvP will enable in ","color":"gray"},{"text":"10 minutes","color":"white"}]')
                    if VarToCount[i] == "FirstBorder":
                        e.npc.executeCommand('/tellraw @a ["",{"text":"[","color":"dark_gray"},{"text":"UHC","color":"dark_red"},{"text":"][","color":"dark_gray"},{"text":"Border","color":"gold"},{"text":"]","color":"dark_gray"},{"text":" Border will shrink to ","color":"gray"},{"text":"-120 120","color":"gold"},{"text":" in","color":"gray"},{"text":" 10 minutes","color":"dark_gray"}]')
                    if VarToCount[i] == "SecondBorder":
                        e.npc.executeCommand('/tellraw @a ["",{"text":"[","color":"dark_gray"},{"text":"UHC","color":"dark_red"},{"text":"][","color":"dark_gray"},{"text":"Border","color":"gold"},{"text":"]","color":"dark_gray"},{"text":" Border will shrink to ","color":"gray"},{"text":"-80 80","color":"gold"},{"text":" in","color":"gray"},{"text":" 10 minutes","color":"dark_gray"}]')
                    if VarToCount[i] == "FinalBorder":
                        e.npc.executeCommand('/tellraw @a ["",{"text":"[","color":"dark_gray"},{"text":"UHC","color":"dark_red"},{"text":"][","color":"dark_gray"},{"text":"Border","color":"gold"},{"text":"]","color":"dark_gray"},{"text":" Border will shrink to ","color":"gray"},{"text":"-50 50","color":"gold"},{"text":" in","color":"gray"},{"text":" 10 minutes","color":"dark_gray"}]')
                    e.npc.getStoreddata().put(VarToCount[i]+"10", 1)

                if Until == 5 and (e.npc.getStoreddata().get(VarToCount[i]+"5") != 1):
                    if VarToCount[i] == "PvPTime":
                        e.npc.executeCommand('/tellraw @a ["",{"text":"[","color":"dark_gray"},{"text":"UHC","color":"dark_red"},{"text":"]","color":"dark_gray"},{"text":" PvP will enable in ","color":"gray"},{"text":"5 minutes","color":"white"}]')
                    if VarToCount[i] == "FirstBorder":
                        e.npc.executeCommand('/tellraw @a ["",{"text":"[","color":"dark_gray"},{"text":"UHC","color":"dark_red"},{"text":"][","color":"dark_gray"},{"text":"Border","color":"gold"},{"text":"]","color":"dark_gray"},{"text":" Border will shrink to ","color":"gray"},{"text":"-120 120","color":"gold"},{"text":" in","color":"gray"},{"text":" 5 minutes","color":"dark_gray"}]')
                    if VarToCount[i] == "SecondBorder":
                        e.npc.executeCommand('/tellraw @a ["",{"text":"[","color":"dark_gray"},{"text":"UHC","color":"dark_red"},{"text":"][","color":"dark_gray"},{"text":"Border","color":"gold"},{"text":"]","color":"dark_gray"},{"text":" Border will shrink to ","color":"gray"},{"text":"-80 80","color":"gold"},{"text":" in","color":"gray"},{"text":" 5 minutes","color":"dark_gray"}]')
                    if VarToCount[i] == "FinalBorder":
                        e.npc.executeCommand('/tellraw @a ["",{"text":"[","color":"dark_gray"},{"text":"UHC","color":"dark_red"},{"text":"][","color":"dark_gray"},{"text":"Border","color":"gold"},{"text":"]","color":"dark_gray"},{"text":" Border will shrink to ","color":"gray"},{"text":"-50 50","color":"gold"},{"text":" in","color":"gray"},{"text":" 5 minutes","color":"dark_gray"}]')
                    e.npc.getStoreddata().put(VarToCount[i]+"5", 1)

                if Until == 1 and (e.npc.getStoreddata().get(VarToCount[i]+"1") != 1):
                    e.npc.getStoreddata().put(VarToCount[i]+"1", 1)
                    if VarToCount[i] == "PvPTime":
                        e.npc.executeCommand('/tellraw @a ["",{"text":"[","color":"dark_gray"},{"text":"UHC","color":"dark_red"},{"text":"]","color":"dark_gray"},{"text":" PvP will enable in ","color":"gray"},{"text":"1 minute","color":"white"}]')
                    if VarToCount[i] == "FirstBorder":
                        e.npc.executeCommand('/tellraw @a ["",{"text":"[","color":"dark_gray"},{"text":"UHC","color":"dark_red"},{"text":"][","color":"dark_gray"},{"text":"Border","color":"gold"},{"text":"]","color":"dark_gray"},{"text":" Border will shrink to ","color":"gray"},{"text":"-120 120","color":"gold"},{"text":" in","color":"gray"},{"text":" 1 minute","color":"dark_gray"}]')
                    if VarToCount[i] == "SecondBorder":
                        e.npc.executeCommand('/tellraw @a ["",{"text":"[","color":"dark_gray"},{"text":"UHC","color":"dark_red"},{"text":"][","color":"dark_gray"},{"text":"Border","color":"gold"},{"text":"]","color":"dark_gray"},{"text":" Border will shrink to ","color":"gray"},{"text":"-80 80","color":"gold"},{"text":" in","color":"gray"},{"text":" 1 minute","color":"dark_gray"}]')
                    if VarToCount[i] == "FinalBorder":
                        e.npc.executeCommand('/tellraw @a ["",{"text":"[","color":"dark_gray"},{"text":"UHC","color":"dark_red"},{"text":"][","color":"dark_gray"},{"text":"Border","color":"gold"},{"text":"]","color":"dark_gray"},{"text":" Border will shrink to ","color":"gray"},{"text":"-50 50","color":"gold"},{"text":" in","color":"gray"},{"text":" 1 minute","color":"dark_gray"}]')
                    e.npc.getStoreddata().put(VarToCount[i]+"1", 1)

                if Until == 0 and (e.npc.getStoreddata().get(VarToCount[i]+"0") != 1):
                    e.npc.getStoreddata().put(VarToCount[i]+"0", 1)
                    if VarToCount[i] == "PvPTime":
                        e.npc.executeCommand('/tellraw @a ["",{"text":"[","color":"dark_gray"},{"text":"UHC","color":"dark_red"},{"text":"]","color":"dark_gray"},{"text":" PvP is now enabled !","color":"gray"}]')
                        if (e.npc.world.getStoreddata().get("PvPDisplayed") != "True"):
                            e.npc.executeCommand('/title @a times 20 100 20')
                            e.npc.executeCommand('/title @a subtitle {"text":"Good luck and have fun !","color":"dark_gray"}')
                            e.npc.executeCommand('/title @a title {"text":"PvP Enabled !","color":"dark_red"}')
                            e.npc.world.getStoreddata().put("PvPDisplayed", "True")
                            for i in range(0, len(e.npc.world.getAllPlayers())):
                                players = e.npc.world.getAllPlayers()
                                e.npc.executeCommand("/playsound mob.enderdragon.growl "+str(players[i].getName()))
                    if VarToCount[i] == "FirstBorder":
                        e.npc.executeCommand('/tellraw @a ["",{"text":"[","color":"dark_gray"},{"text":"UHC","color":"dark_red"},{"text":"][","color":"dark_gray"},{"text":"Border","color":"gold"},{"text":"]","color":"dark_gray"},{"text":" Borders have shrunk to ","color":"gray"},{"text":"-120 120","color":"gold"}]')
                        for i in range(0, len(e.npc.world.getAllPlayers())):
                                players = e.npc.world.getAllPlayers()
                                e.npc.executeCommand("/playsound note.pling "+str(players[i].getName()))
                    if VarToCount[i] == "SecondBorder":
                        e.npc.executeCommand('/tellraw @a ["",{"text":"[","color":"dark_gray"},{"text":"UHC","color":"dark_red"},{"text":"][","color":"dark_gray"},{"text":"Border","color":"gold"},{"text":"]","color":"dark_gray"},{"text":" Borders have shrunk to ","color":"gray"},{"text":"-80 80","color":"gold"}]')
                        for i in range(0, len(e.npc.world.getAllPlayers())):
                                players = e.npc.world.getAllPlayers()
                                e.npc.executeCommand("/playsound note.pling "+str(players[i].getName()))
                    if VarToCount[i] == "FinalBorder":
                        e.npc.executeCommand('/tellraw @a ["",{"text":"[","color":"dark_gray"},{"text":"UHC","color":"dark_red"},{"text":"][","color":"dark_gray"},{"text":"Border","color":"gold"},{"text":"]","color":"dark_gray"},{"text":" Borders have shrunk to ","color":"gray"},{"text":"-50 50","color":"gold"}]')
                        for i in range(0, len(e.npc.world.getAllPlayers())):
                                players = e.npc.world.getAllPlayers()
                                e.npc.executeCommand("/playsound note.pling "+str(players[i].getName()))

        else:
            e.npc.getStoreddata().put("OneSecTicker", 1)
    except:
        pass

def CountingPlayersOnKill(e):
    if (e.npc.world.getStoreddata().get("TeamsAlive") == 1 ) and (e.npc.getStoreddata().get("EndGameSaid") != True):
        #e.npc.executeCommand('/tellraw @a ["",{"text":"[","color":"dark_gray"},{"text":"UHC","color":"dark_red"},{"text":"] ","color":"dark_gray"},{"text":"[","color": gray,"bold":true},{"text":"Players","color" : dark_green},{"text":"] ","color": gray,"bold":true},{ "text" :"We now have a winner ! Congratulation !","color" : aqua,"bold":true}]')
        e.npc.getStoreddata().put("EndGameSaid", True)
        EndGame(e)
        UpdatingStats(e)
        e.npc.world.getTempdata().clear()
        e.npc.world.getStoreddata().clear()

def UpdatingStats(e):
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
    
    e.npc.executeCommand('/tellraw @a ["",{"text":"[","color":"dark_gray"},{"text":"UHC","color":"dark_red"},{"text":"]","color":"dark_gray"},{"text":" Stats saved","color":"gray"},{"text":" successfully","color":"red"}]')
    e.npc.world.getTempdata().put("GameStarted", 0)

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
                if (X >= 45) :
                    X = 40
                    Y = 75
                elif (-45 >= X):
                    X = -40
                    Y = 75

                if (Z >= 45) :
                    Z = 40
                    Y = 75
                elif (-45 >= Z):
                    Z = -40
                    Y = 75
                
                Players[i].setPosition(X, Y, Z)
                if i == len(e.npc.world.getAllPlayers())-1 :
                    e.npc.world.getStoreddata().put("FinalPlayerTP", 1)
            

        elif (e.npc.world.getStoreddata().get("SecondBorder") <= e.npc.world.getTotalTime()):
            if e.npc.world.getStoreddata().get("SecondPlayerTP") != 1 :
                if (X >= 80) :
                    X = 75
                    Y = 75
                elif (-80 >= X):
                    X = -75
                    Y = 75

                if (Z >= 80) :
                    Z = 75
                    Y = 75
                elif (-80 >= Z):
                    Z = -75
                    Y = 75
                
                Players[i].setPosition(X, Y, Z)
                if i == len(e.npc.world.getAllPlayers())-1 :
                    e.npc.world.getStoreddata().put("SecondPlayerTP", 1)

        elif (e.npc.world.getStoreddata().get("FirstBorder") <= e.npc.world.getTotalTime()):
            if e.npc.world.getStoreddata().get("FirstPlayerTP") != 1 :
                if (X >= 120) :
                    X = 115
                    Y = 75
                elif (-120 >= X):
                    X = -115
                    Y = 75

                if (Z >= 120) :
                    Z = 115
                    Y = 75
                elif (-120 >= Z):
                    Z = -115
                    Y = 75
                Players[i].setPosition(X, Y, Z)
                if i == len(e.npc.world.getAllPlayers())-1 :
                    e.npc.world.getStoreddata().put("FirstPlayerTP", 1)

def init(e):
    if e.npc.getStoreddata().get("HasReset") != 1 :
        e.npc.getStoreddata().put("HasReset", 1)
        e.npc.executeCommand("/noppes config chunkloaders 24")
        e.npc.reset()
        e.npc.say("Reset")

def tick(e):
    if e.npc.world.getTempdata().get("GameStarted") == 1 :
        try:
            CountingPlayersOnKill(e)
            Counter(e)
            ShrinkBorder(e)
            CutClean(e)
            AppleFlintRate(e)
        except:
            pass
    else:
        e.npc.despawn()