import colorama
import copy
from src.gameClass import Game
from src.input import get_input 
from src.townHall import TownHall
from src.huts import Hut
from src.barbarian import Barbarian
from src.cannon import Cannon
from src.spells import Spells
from src.archer import Archer
from src.ballon import Ballon
from src.archerQueen import ArcherQueen
from src.wizardTower import WizardTower
import time
from src.king import King
from colorama import Back
from colorama import Fore, Back, Style
from src.wall import Wall
from playsound import playsound
colorama.init()

def addBuildingsOneLevel():
    townHall=TownHall(game,15,15)
    game.addTownHall(townHall)

    for i in range(12,17):
        wall = Wall(game,12,i)
        game.addBuilding(wall)
        wall2 = Wall(game,16,i)
        game.addBuilding(wall2)

    for i in range(12,17):
        wall = Wall(game,i,11)
        game.addBuilding(wall)
        wall2 = Wall(game,i,17)
        game.addBuilding(wall2)

    # 3 CANNONS

    cannon = Cannon(game,10,10,1,6)
    game.addCannon(cannon)
    
    cannon = Cannon(game,15,20,1,6)
    game.addCannon(cannon)
    
    cannon = Cannon(game,25,28,1,6)
    game.addCannon(cannon)

    # # 2 WIZARD TOWERS
    
    wizardTower = WizardTower(game,15,10,3,6)
    game.addWizardTower(wizardTower)
    
    wizardTower = WizardTower(game,15,18,5,6)
    game.addWizardTower(wizardTower)
    
    # 5 HUTS

    hut = Hut(game,2,4)
    game.addHut(hut)
    
    hut = Hut(game,5,6)
    game.addHut(hut)
    
    hut = Hut(game,17,20)
    game.addHut(hut)

    hut = Hut(game,20,25)
    game.addHut(hut)

    hut = Hut(game,26,29)
    game.addHut(hut)

def addBuildingsTwoLevel():
    townHall=TownHall(game,15,15)
    game.addTownHall(townHall)

    for i in range(12,17):
        wall = Wall(game,12,i)
        game.addBuilding(wall)
        wall2 = Wall(game,16,i)
        game.addBuilding(wall2)

    for i in range(12,17):
        wall = Wall(game,i,11)
        game.addBuilding(wall)
        wall2 = Wall(game,i,17)
        game.addBuilding(wall2)

    # 4 CANNONS

    cannon = Cannon(game,10,10,1,6)
    game.addCannon(cannon)
    
    cannon = Cannon(game,15,20,1,6)
    game.addCannon(cannon)
    
    cannon = Cannon(game,25,28,1,6)
    game.addCannon(cannon)

    cannon = Cannon(game,25,24,1,6)
    game.addCannon(cannon)
    
    # 2 WIZARD TOWERS

    wizardTower = WizardTower(game,15,10,3,6)
    game.addWizardTower(wizardTower)
    
    wizardTower = WizardTower(game,15,18,5,6)
    game.addWizardTower(wizardTower)
    
    # 5 HUTS

    hut = Hut(game,2,4)
    game.addHut(hut)
    
    hut = Hut(game,5,6)
    game.addHut(hut)
    
    hut = Hut(game,17,20)
    game.addHut(hut)

    hut = Hut(game,20,25)
    game.addHut(hut)

    hut = Hut(game,26,29)
    game.addHut(hut)

def addBuildingsThreeLevel():
    townHall=TownHall(game,15,15)
    game.addTownHall(townHall)
    game.addBuilding(townHall)

    for i in range(12,17):
        wall = Wall(game,12,i)
        game.addBuilding(wall)
        wall2 = Wall(game,16,i)
        game.addBuilding(wall2)

    for i in range(12,17):
        wall = Wall(game,i,11)
        game.addBuilding(wall)
        wall2 = Wall(game,i,17)
        game.addBuilding(wall2)

    cannon = Cannon(game,10,10,1,6)
    game.addCannon(cannon)
    
    cannon = Cannon(game,15,20,1,6)
    game.addCannon(cannon)
    
    cannon = Cannon(game,25,28,1,6)
    game.addCannon(cannon)

    cannon = Cannon(game,25,30,1,6)
    game.addCannon(cannon)
    
    wizardTower = WizardTower(game,15,10,3,6)
    game.addWizardTower(wizardTower)
    
    wizardTower = WizardTower(game,15,18,5,6)
    game.addWizardTower(wizardTower)

    wizardTower = WizardTower(game,13,18,5,6)
    game.addWizardTower(wizardTower)
    
    hut = Hut(game,2,4)
    game.addHut(hut)
    
    hut = Hut(game,5,6)
    game.addHut(hut)
    
    hut = Hut(game,17,20)
    game.addHut(hut)

    hut = Hut(game,20,25)
    game.addHut(hut)

    hut = Hut(game,26,29)
    game.addHut(hut)

emptyBoard = []
m=30  # rows
n=30 # columns

for i in range(m):
    row = ['X']*n
    row.append('\n')
    emptyBoard.append(row)

game=Game(emptyBoard ,m,n)



king = King(game,5,20,2)
game.addKing(king)

queen = ArcherQueen(game,5,20,1)
game.addQueen(queen)

addBuildingsOneLevel()

spell=Spells(game)

initTime = time.time()

file = open("replays/replay.txt","a")
replaySteps = {}
noOfPersons = 1
counter=0

# choice = input ("Enter king(1) or queen(2) : ")
choice="1"

while game.status=='playing':
    timenow = int(time.time()-initTime)
    if choice == "1":
        lifecard = "Health: " + ' | '*king.health + ' - '*(10-king.health) + "\t\t\t\t\t"
    else :
        lifecard = "Health: " + ' | '*queen.health + ' - '*(10-queen.health) + "\t\t\t\t\t"
    key = get_input()
    game.board = copy.deepcopy(emptyBoard)
    game.cboard = copy.deepcopy(emptyBoard)
    print("\033[H\033[J", end="")

    # if game.townHall.health > 0:
    #     game.townHall.display()

    print(game.noOfBuildings)

    for building in game.buildings:
        if(building.health<=0):
            game.buildings.remove(building)
            if(building.char=='H'):
                game.huts.remove(building)
                game.noOfBuildings-=1
            elif(building.char=='C'):
                game.cannons.remove(building)
                game.noOfBuildings-=1
            elif(building.char=='T'):
                game.townHall = None
                game.noOfBuildings-=1
            elif(building.char=='W'):
                game.wizardTowers.remove(building)
                game.noOfBuildings-=1
        else:
            building.display()

    for cannon in game.cannons:
        cannon.attack()

    for wizardTower in game.wizardTowers:
        wizardTower.attack()

   

    for barbarian in game.barbarians:
        if(barbarian.health<=0):
            game.barbarians.remove(barbarian)
            noOfPersons -= 1
        else:
            barbarian.display()
            barbarian.move(timenow)
            barbarian.attack()
    
    for archer in game.archers:
        if(archer.health<=0):
            game.archers.remove(archer)
            noOfPersons -= 1
        else:
            archer.display()
            archer.move(timenow)
            archer.attack()

    for ballon in game.ballons:
        if(ballon.health<=0):
            game.ballons.remove(ballon)
            noOfPersons -= 1
        else:
            ballon.display()
            ballon.move(timenow)
            ballon.attack()

    if(key =='q'):
        game.status="over"
    elif(key == ' '):
        if choice == "1":
            king.attack()
        else:
            queen.attack()
    elif(key == '1'):
        if(game.noOfBarbarians<6):
            barbarain = Barbarian(game,0,17,timenow)
            game.addBarbarain(barbarain)
            noOfPersons += 1
    elif(key=='2'):
        if(game.noOfBarbarians<6):
            barbarain = Barbarian(game,20,10,timenow)
            game.addBarbarain(barbarain)   
            noOfPersons += 1 
    elif(key=='3'):
        if(game.noOfBarbarians<6):
            barbarain = Barbarian(game,7,25,timenow)
            game.addBarbarain(barbarain)
            noOfPersons += 1
    elif(key=='4'):
        if(game.noOfArchers<6):
            archer = Archer(game,1,1,timenow)
            game.addArcher(archer)
            noOfPersons += 1
    elif(key=='5'):
        if(game.noOfArchers<6):
            archer = Archer(game,28,1,timenow)
            game.addArcher(archer)
            noOfPersons += 1
    elif(key=='6'):
        if(game.noOfArchers<6):
            archer = Archer(game,1,28,timenow)
            game.addArcher(archer)
            noOfPersons += 1
    elif(key=='7'):
        if(game.noOfBallons<3):
            ballon = Ballon(game,1,10,timenow)
            game.addBallon(ballon)
            noOfPersons += 1
    elif(key=='8'):
        if(game.noOfBallons<3):
            ballon = Ballon(game,28,10,timenow)
            game.addBallon(ballon)
            noOfPersons += 1
    elif(key=='9'):
        if(game.noOfBallons<3):
            ballon = Ballon(game,10,1,timenow)
            game.addBallon(ballon)
            noOfPersons += 1
    elif(key=='r'):
        spell.rage()
    elif(key=='h'):
        spell.heal()
    elif(key=='l'):
        king.leviathonAttack(5)

    replaySteps[counter] = key

    if choice == "1":
        if(king.health>=0):
            king.display()
            king.move(key)
        else:
            noOfPersons-=1
    else :
        if(queen.health>=0):
            queen.display()
            queen.move(key)
        else:
            noOfPersons-=1
    
    game.display()
    print(lifecard)
    print("Time : "+str(timenow))
    print("Level : "+str(game.level))
    
    if(noOfPersons==0):
        game.status="over"
        print("\033[H\033[J", end="")
        print("Game Over")
        print("You Lose")
        playsound("src/lose1.mov")
    if(game.noOfBuildings==0):
        if(game.level<3):
            game.level+=1
            if(game.level==2):
                game.ballons.clear()
                game.archers.clear()
                game.barbarians.clear()
                game.noOfArchers=0
                game.noOfBarbarians=0
                game.noOfBallons=0
                addBuildingsTwoLevel()
            if(game.level==3):
                game.ballons.clear()
                game.archers.clear()
                game.barbarians.clear()
                game.noOfArchers=0
                game.noOfBarbarians=0
                game.noOfBallons=0
                addBuildingsThreeLevel()       
        else:
            game.status="over"
            print("\033[H\033[J", end="")
            print("Game Over")
            print("You Win!")
            playsound("src/victory1.mov")

    counter+=1
    
file.write(str(replaySteps))
file.write("\n")

 # for persons in game.persons:
    #     if(persons.health<=0):
    #         game.persons.remove(persons)
    #         noOfPersons-=1
    #         if(persons.char=='B'):
    #             game.barbarians.remove(persons)
    #         elif(persons.char=='A'):
    #             game.archers.remove(persons)
    #         elif(persons.char=='b'):
    #             game.ballons.remove(persons)
    #     else:
    #         if(persons.char=='B' or persons.char=='b' or persons.char=='A'):
    #             persons.display()
    #             persons.move()
    #             persons.attack()