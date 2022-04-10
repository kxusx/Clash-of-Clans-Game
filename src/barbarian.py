import math
from src.utils import brickCOLOR
import colorama
from colorama import Fore, Back, Style


class Barbarian():
    def __init__(self, game, x, y):
        self.game = game
        self.health = 10
        self.damage = 1
        self.color = brickCOLOR[self.health]
        self.char = 'B'
        self.x = x
        self.y = y
        self.width = 1
        self.height = 1
        self.speed = 1
        self.direction = 'w'
        self.status = 'alive'

    def move(self):
        minDist = 10000
        for building in self.game.buildings:
            if(building.char=='T' or building.char=='H' or building.char=='C' or building.char=='W'):
                dist = abs(building.x - self.x) + abs(building.y - self.y)
                if(dist < minDist):
                    minDist = dist
                    minBuilding = building

        if(minDist<1000):
            if(minBuilding.x > self.x):
                if(self.x < self.game.m-1 and (self.game.cboard[self.x + 1][self.y] == 'X' or self.game.cboard[self.x + 1][self.y] == 'B')):
                    self.x += self.speed
                    self.direction = 's'            
            elif(minBuilding.x < self.x):
                if(self.x > 0 and (self.game.cboard[self.x - 1][self.y] == 'X' or self.game.cboard[self.x - 1][self.y] == 'B')):
                    self.x -= self.speed
                    self.direction = 'w'

            if(minBuilding.y > self.y):
                if(self.y < self.game.n-1 and (self.game.cboard[self.x][self.y + 1] == 'X' or self.game.cboard[self.x][self.y + 1] == 'B')):
                    self.y += self.speed
                    self.direction = 'd'
            elif(minBuilding.y < self.y):
                if(self.y > 0 and (self.game.cboard[self.x][self.y - 1] == 'X' or self.game.cboard[self.x][self.y - 1] == 'B')):
                    self.y -= self.speed
                    self.direction = 'a'

    def display(self):
        if(self.health > 0):
            cArr = self.game.cboard
            arr = self.game.board

            arr[self.x][self.y] = self.color + self.char + Style.RESET_ALL
            cArr[self.x][self.y] = self.char

            self.game.board = arr
            self.game.cboard = cArr

    def attack(self):
        if(self.x > 0 and (self.game.cboard[self.x - 1][self.y] == 'T' 
           or self.game.cboard[self.x - 1][self.y] == 'H' 
           or self.game.cboard[self.x - 1][self.y] == 'C'
           or self.game.cboard[self.x - 1][self.y] == '#'
           or self.game.cboard[self.x - 1][self.y] == 'W')):
            for building in self.game.buildings:
                if(self.game.cboard[self.x - 1][self.y] == 'T' and building.char == 'T'):
                    building.health -= self.damage
                    if(building.health<=0):
                        building.color = brickCOLOR[0]
                    else:
                        building.color = brickCOLOR[math.floor(building.health)]
                elif(building.x == self.x - 1 and building.y == self.y):
                    building.health -= self.damage
                    if(building.health<=0):
                        building.color = brickCOLOR[0]
                    else:
                        building.color = brickCOLOR[math.floor(building.health)]
            return

        if(self.y > 0 and (self.game.cboard[self.x][self.y - 1] == 'T' 
           or self.game.cboard[self.x][self.y - 1] == 'H' 
           or self.game.cboard[self.x][self.y - 1] == 'C'
           or self.game.cboard[self.x][self.y - 1] == '#'
           or self.game.cboard[self.x][self.y - 1] == 'W')):
            for building in self.game.buildings:
                if(self.game.cboard[self.x][self.y - 1] == 'T' and building.char == 'T'):
                    building.health -= self.damage
                    if(building.health<=0):
                        building.color = brickCOLOR[0]
                    else:
                        building.color = brickCOLOR[math.floor(building.health)]
                elif(building.x == self.x and building.y == self.y - 1):
                    building.health -= self.damage
                    if(building.health<=0):
                        building.color = brickCOLOR[0]
                    else:
                        building.color = brickCOLOR[math.floor(building.health)]
            return

        if(self.x < self.game.m-1 and (self.game.cboard[self.x + 1][self.y] == 'T' 
           or self.game.cboard[self.x + 1][self.y] == 'H' 
           or self.game.cboard[self.x + 1][self.y] == 'C'
           or self.game.cboard[self.x + 1][self.y] == '#'
           or self.game.cboard[self.x + 1][self.y] == 'W')):
            for building in self.game.buildings:
                if(self.game.cboard[self.x + 1][self.y] == 'T' and building.char == 'T'):
                    building.health -= self.damage
                    if(building.health<=0):
                        building.color = brickCOLOR[0]
                    else:
                        building.color = brickCOLOR[math.floor(building.health)]
                elif(building.x == self.x + 1 and building.y == self.y):
                    building.health -= self.damage
                    if(building.health<=0):
                        building.color = brickCOLOR[0]
                    else:
                        building.color = brickCOLOR[math.floor(building.health)]
            return

        if(self.y < self.game.n-1 and (self.game.cboard[self.x][self.y + 1] == 'T' 
           or self.game.cboard[self.x][self.y + 1] == 'H' 
           or self.game.cboard[self.x][self.y + 1] == 'C'
           or self.game.cboard[self.x][self.y + 1] == '#'
           or self.game.cboard[self.x][self.y + 1] == 'W')):
            for building in self.game.buildings:
                if(self.game.cboard[self.x][self.y + 1] == 'T' and building.char == 'T'):
                    building.health -= self.damage
                    if(building.health<=0):
                        building.color = brickCOLOR[0]
                    else:
                        building.color = brickCOLOR[math.floor(building.health)]
                elif(building.x == self.x and building.y == self.y + 1):
                    building.health -= self.damage
                    if(building.health<=0):
                        building.color = brickCOLOR[0]
                    else:
                        building.color = brickCOLOR[math.floor(building.health)]
            return
