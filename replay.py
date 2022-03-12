import colorama
import copy
import ast
from src.gameClass import Game
from src.input import get_input 
from src.townHall import TownHall
from src.huts import Hut
from src.barbarian import Barbarian
from src.cannon import Cannon
from src.spells import Spells
import time
from src.king import King
from colorama import Back
from colorama import Fore, Back, Style
from src.wall import Wall
colorama.init()

emptyBoard = []
m=30  # rows
n=30 # columns

for i in range(m):
    row = ['X']*n
    row.append('\n')
    emptyBoard .append(row)

game=Game(emptyBoard ,m,n)

townHall=TownHall(game,15,15)
game.addTownHall(townHall)
game.addBuilding(townHall)

king = King(game,5,20,1)
game.addKing(king)


cannon = Cannon(game,10,10,1,6)
game.addCannon(cannon)
game.addBuilding(cannon)

cannon = Cannon(game,15,20,1,6)
game.addCannon(cannon)
game.addBuilding(cannon)

cannon = Cannon(game,25,28,1,6)
game.addCannon(cannon)
game.addBuilding(cannon)

hut = Hut(game,2,4)
game.addHut(hut)
game.addBuilding(hut)

hut = Hut(game,5,6)
game.addHut(hut)
game.addBuilding(hut)

hut = Hut(game,17,20)
game.addHut(hut)
game.addBuilding(hut)

hut = Hut(game,20,25)
game.addHut(hut)
game.addBuilding(hut)

hut = Hut(game,26,29)
game.addHut(hut)
game.addBuilding(hut)

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


spell=Spells(game)

initTime = time.time()

gameNo = input("Enter which Game you want to replay : ")
file = open("replays/replay.txt","r")
lines = file.readlines()
print(lines)
dict = ast.literal_eval(lines[int(gameNo) - 1])


noOfPersons = 1

counter=0
while game.status=='playing':
    timenow = int(time.time()-initTime)
    lifecard = "Health: " + ' | '*king.health + ' - '*(10-king.health) + "\t\t\t\t\t"

    key = dict[counter]
    game.board = copy.deepcopy(emptyBoard)
    game.cboard = copy.deepcopy(emptyBoard)
    print("\033[H\033[J", end="")

    townHall.display()

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
        else:
            building.display()

    for cannon in game.cannons:
        cannon.attack()

    for barbarian in game.barbarians:
        if(barbarian.health<=0):
            game.barbarians.remove(barbarian)
            noOfPersons -= 1
        else:
            barbarian.display()
            barbarian.move()
            barbarian.attack()


    if(key =='q'):
        game.status="over"
    elif(key == ' '):
        king.attack()
    elif(key == '1'):
        barbarain = Barbarian(game,0,17)
        game.addBarbarain(barbarain)
        noOfPersons += 1
    elif(key=='2'):
        barbarain = Barbarian(game,20,10)
        game.addBarbarain(barbarain)   
        noOfPersons += 1 
    elif(key=='3'):
        barbarain = Barbarian(game,7,25)
        game.addBarbarain(barbarain)
        noOfPersons += 1
    elif(key=='r'):
        spell.rage()
    elif(key=='h'):
        spell.heal()
    elif(key=='l'):
        king.leviathonAttack(5)

    if(king.health>0):
        king.display()
        king.move(key)
    else:
        noOfPersons-=1
    
    game.display()
    print(lifecard)
    print("Time : "+str(timenow))

    if(noOfPersons==0):
        game.status="over"
        print("\033[H\033[J", end="")
        print("Game Over")
        print(" You Lose")
    if(game.noOfBuildings==0):
        game.status="over"
        print("\033[H\033[J", end="")
        print("Game Over")
        print(" You Win")
        game.status="over"
    
    counter+=1
    time.sleep(0.1)
