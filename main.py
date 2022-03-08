import colorama
import copy
from game import Game
from input import get_input 
from townHall import TownHall
from huts import Hut

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
king = King(game,10,12)

huts = []
hut = Hut(game,2,4)
huts.append(hut)
game.addHut(hut)

hut = Hut(game,5,6)
huts.append(hut)
game.addHut(hut)

hut = Hut(game,17,20)
huts.append(hut)
game.addHut(hut)

hut = Hut(game,20,25)
huts.append(hut)
game.addHut(hut)

hut = Hut(game,26,29)
huts.append(hut)
game.addHut(hut)


game.addKing(king)
game.addTownHall(townHall)


while game.status=='playing':
    key = get_input()
    game.board = copy.deepcopy(emptyBoard)
    game.cboard = copy.deepcopy(emptyBoard)
    print("\033[H\033[J", end="")

    townHall.display()

    if(key =='q'):
        game.status="over"
    elif(key == ' '):
        king.attack()
    
    for i in range(len(huts)):
        huts[i].display()
    king.display()
    king.move(key)
    game.display()


