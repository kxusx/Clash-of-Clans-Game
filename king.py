from utils import brickCOLOR
import colorama
from colorama import Fore, Back, Style



class King():
    def __init__(self, game, x, y,damage):
        self.status = 'alive'
        self.game = game
        self.health = 10
        self.damage = damage
        self.color = brickCOLOR[self.health]
        self.char = 'K'
        self.x = x
        self.y = y
        self.width = 1
        self.height = 1
        self.direction = 'w'

    def display(self):
        arr = self.game.board
        arr[self.x][self.y] = self.color + self.char + Style.RESET_ALL
        self.game.board = arr

    def move(self, dir):
        if(dir == 'w'):  # w
            if(self.x > 0 and self.game.cboard[self.x - 1][self.y] == 'X'):
                self.x -= 1
                self.direction = 'w'
        if(dir == 'a'):  # a
            if(self.y > 0 and self.game.cboard[self.x][self.y - 1] == 'X'):
                self.y -= 1
                self.direction = 'a'
        if(dir == 's'):  # s
            if(self.x < self.game.m-1 and self.game.cboard[self.x + 1][self.y] == 'X'):
                self.x += 1
                self.direction = 's'
        if(dir == 'd'):  # d
            if(self.y < self.game.n-1 and self.game.cboard[self.x][self.y + 1] == 'X'):
                self.y += 1
                self.direction = 'd'

    def attack(self):

        if(self.direction == 'w'):
            # print( self.game.cboard[self.x - 1][self.y])
            if(self.x > 0 and self.game.cboard[self.x - 1][self.y] == 'T'):
                self.game.townHall.health -= 1
                self.game.townHall.color = brickCOLOR[self.game.townHall.health]
            elif(self.x > 0 and self.game.cboard[self.x - 1][self.y] == 'H'):
                print("hit")
                for hut in self.game.huts:
                    if(hut.x == self.x - 1 and hut.y == self.y):
                        hut.health -= self.damage
                        hut.color = brickCOLOR[hut.health]
                        hut.display()

        if(self.direction == 'a'):
            # print(self.game.cboard[self.x][self.y - 1])
            if(self.y > 0 and self.game.cboard[self.x][self.y - 1] == 'T'):
                self.game.townHall.health -= 1
                self.game.townHall.color = brickCOLOR[self.game.townHall.health] 
            elif(self.y > 0 and self.game.cboard[self.x][self.y - 1] == 'H'):
                for hut in self.game.huts:
                    if(hut.x == self.x and hut.y == self.y - 1):
                        hut.health -= self.damage
                        hut.color = brickCOLOR[hut.health]
                        hut.display()

        if(self.direction == 's'):
            # print(self.game.cboard[self.x + 1][self.y])
            if(self.x < self.game.m-1 and self.game.cboard[self.x + 1][self.y] == 'T'):
                self.game.townHall.health -= 1
                self.game.townHall.color = brickCOLOR[self.game.townHall.health]
            elif(self.x < self.game.m-1 and self.game.cboard[self.x + 1][self.y] == 'H'):
                for hut in self.game.huts:
                    if(hut.x == self.x + 1 and hut.y == self.y):
                        hut.health -= self.damage
                        hut.color = brickCOLOR[hut.health]
                        hut.display()
               
        if(self.direction == 'd'):
            # print(self.game.cboard[self.x][self.y + 1])
            if(self.y < self.game.n-1 and self.game.cboard[self.x][self.y + 1] == 'T'):
                self.game.townHall.health -= 1
                self.game.townHall.color = brickCOLOR[self.game.townHall.health]
            elif(self.y < self.game.n-1 and self.game.cboard[self.x][self.y + 1] == 'H'):
                for hut in self.game.huts:
                    if(hut.x == self.x and hut.y == self.y + 1):
                        hut.health -= self.damage
                        hut.color = brickCOLOR[hut.health]
                        hut.display()
                
        