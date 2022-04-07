import math
from src.utils import brickCOLOR
import colorama
from colorama import Fore, Back, Style


class Archer():
    def __init__(self, game, x, y):
        self.game = game
        self.health = 5
        self.damage = 5
        self.color = brickCOLOR[self.health]
        self.char = 'A'
        self.x = x
        self.y = y
        self.width = 1
        self.height = 1
        self.speed = 2
        self.direction = 'w'
        self.status = 'alive'

    def move(self):
        minDist = 10000
        for building in self.game.buildings:
            if(building.char=='T' or building.char=='H' or building.char=='C'):
                dist = abs(building.x - self.x) + abs(building.y - self.y)
                if(dist < minDist):
                    minDist = dist
                    minBuilding = building

        if(minDist<1000):
            if(minBuilding.x > self.x):
                if(abs(minBuilding.x-self.x)<=self.speed):                 
                    self.speed = abs(minBuilding.x-self.x)-1
                    if(self.speed==0):
                        self.speed = 1
                if(self.x < self.game.m-1 and (self.game.cboard[self.x + self.speed][self.y] == 'X' or self.game.cboard[self.x + self.speed][self.y] == 'B')):
                    self.x += self.speed
                    self.direction = 's'            
            elif(minBuilding.x < self.x):
                if(abs(minBuilding.x-self.x)<=self.speed):
                    self.speed = abs(minBuilding.x-self.x)-1
                    if(self.speed==0):
                        self.speed = 1
                if(self.x > 0 and (self.game.cboard[self.x - self.speed][self.y] == 'X' or self.game.cboard[self.x - self.speed][self.y] == 'B')):
                    self.x -= self.speed
                    self.direction = 'w'

            if(minBuilding.y > self.y):
                if(abs(minBuilding.y-self.y)<=self.speed):
                    self.speed = abs(minBuilding.y-self.y)-1
                    if(self.speed==0):
                        self.speed = 1
                if(self.y < self.game.n-1 and (self.game.cboard[self.x][self.y + self.speed] == 'X' or self.game.cboard[self.x][self.y + self.speed] == 'B')):
                    self.y += self.speed
                    self.direction = 'd'
            elif(minBuilding.y < self.y):
                if(abs(minBuilding.y-self.y)<=self.speed): 
                    self.speed = abs(minBuilding.y-self.y)-1
                    if(self.speed==0):
                        self.speed = 1
                if(self.y > 0 and (self.game.cboard[self.x][self.y - self.speed] == 'X' or self.game.cboard[self.x][self.y - self.speed] == 'B')):
                    self.y -= self.speed
                    self.direction = 'a'
        self.speed=2

    def display(self):
        if(self.health > 0):
            cArr = self.game.cboard
            arr = self.game.board

            arr[self.x][self.y] = self.color + self.char + Style.RESET_ALL
            cArr[self.x][self.y] = self.char

            self.game.board = arr
            self.game.cboard = cArr

    def attack(self):
        range = 5
        for building in self.game.buildings:
            dist = (self.x - building.x)**2 + (self.y - building.y)**2
            if(dist <= range**2):
                building.health -= self.damage
                building.color = brickCOLOR[building.health]
                return True