import colorama
import copy
from game import Game
from input import get_input 
from townHall import TownHall
from huts import Hut
from barbarian import Barbarian
from cannon import Cannon

from king import King
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

king = King(game,10,12,1)
game.addKing(king)


cannon = Cannon(game,10,10,4,3,'C')
game.addCannon(cannon)


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

while game.status=='playing':
    key = get_input()
    game.board = copy.deepcopy(emptyBoard)
    game.cboard = copy.deepcopy(emptyBoard)
    print("\033[H\033[J", end="")

    cannon.display()
    cannon.attack()

    townHall.display()

    for building in game.buildings:
        if(building.health<=0):
            game.buildings.remove(building)
            if(building.char=='H'):
                game.huts.remove(building)
        else:
            building.display()

    for barbarian in game.barbarians:
        if(barbarian.health<=0):
            game.barbarians.remove(barbarian)
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
    elif(key=='2'):
        barbarain = Barbarian(game,20,10)
        game.addBarbarain(barbarain)    
    elif(key=='3'):
        barbarain = Barbarian(game,7,25)
        game.addBarbarain(barbarain)
    
    
    king.display()
    king.move(key)
    game.display()