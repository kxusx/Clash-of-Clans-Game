import math
from src.utils import brickCOLOR
import colorama
from colorama import Fore, Back, Style

class Archer():
    def __init__(self, game, x, y):
        self.game = game
        self.health = 5
        self.damage = 4
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
            if(building.char == 'T' or building.char == 'H' or building.char == 'C'):
                dist = abs(building.x - self.x) + abs(building.y - self.y)
                if(dist < minDist):
                    minDist = dist
                    minBuilding = building

        if(minDist < 1000):
            jump = 5*self.speed
            #-----------------------------------------------------
            if(minBuilding.x > self.x):
                if(abs(minBuilding.x-self.x) <= self.speed):
                    jump = abs(minBuilding.x-self.x)-1
                    if(jump == 0):
                        jump = 1
                if(jump > 2):
                    jump = self.speed
                if(self.x < self.game.m-1 and (self.game.cboard[self.x + jump][self.y] == 'X' or self.game.cboard[self.x + jump][self.y] == 'B')):
                    self.x += jump
                    self.direction = 's'

                for i in range(self.speed+1):
                    if(self.game.cboard[self.x + i][self.y] == '#'):
                        self.attackWall(self.x+i, self.y)
                        break
            #-----------------------------------------------------
            elif(minBuilding.x < self.x):

                if(abs(minBuilding.x-self.x) <= self.speed):
                    jump = abs(minBuilding.x-self.x)-1
                    if(jump == 0):
                        jump = 1
                if(jump > 2):
                    jump = self.speed
                if(self.x > 0 and (self.game.cboard[self.x - jump][self.y] == 'X' or self.game.cboard[self.x - jump][self.y] == 'B')):
                    self.x -= jump
                    self.direction = 'w'
                for i in range(self.speed+1):
                    if(self.game.cboard[self.x - i][self.y] == '#'):
                        self.attackWall(self.x-i, self.y)
                        break
            #-----------------------------------------------------
            jump = 5*self.speed
            #-----------------------------------------------------
            if(minBuilding.y > self.y):
                if(abs(minBuilding.y-self.y) <= self.speed):
                    jump = abs(minBuilding.y-self.y)-1
                    if(jump == 0):
                        jump = 1
                if(jump > 2):
                    jump = self.speed
                if(self.y < self.game.n-1 and (self.game.cboard[self.x][self.y + jump] == 'X' or self.game.cboard[self.x][self.y + jump] == 'B')):
                    self.y += jump
                    self.direction = 'd'
                for i in range(self.speed+1):
                    if(self.game.cboard[self.x][self.y + i] == '#'):

                        self.attackWall(self.x, self.y+i)
                        break
            #-----------------------------------------------------
            elif(minBuilding.y < self.y):
                if(abs(minBuilding.y-self.y) <= self.speed):
                    jump = abs(minBuilding.y-self.y)-1
                    if(jump == 0):
                        jump = 1
                if(jump > 2):
                    jump = self.speed
                if(self.y > 0 and (self.game.cboard[self.x][self.y - jump] == 'X' or self.game.cboard[self.x][self.y - jump] == 'B')):
                    self.y -= jump
                    self.direction = 'a'
                for i in range(self.speed+1):
                    if(self.game.cboard[self.x][self.y - i] == '#'):

                        self.attackWall(self.x, self.y-i)
                        break
            #-----------------------------------------------------

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
        min = 1000

        for building in self.game.buildings:
            if(building.char == 'T' or building.char == 'H' or building.char == 'C'):
                dist = (self.x - building.x)**2 + (self.y - building.y)**2
                if(dist < min and dist < range**2):
                    min = dist
                    minBuilding = building

        if min < 1000:
            minBuilding.health -= self.damage
            minBuilding.color = brickCOLOR[minBuilding.health]
            return True

    def attackWall(self, x, y):
        range = 5
        min = 1000

        for building in self.game.buildings:
            if(building.char == '#'):
                if(building.x == x and building.y == y):
                    building.health -= self.damage
                    building.color = brickCOLOR[building.health]
                    return True


# if(minDist<1000):
#     if(minBuilding.x > self.x):
#         jump = 0
#         for i in range(self.speed):
#            if(self.game.cboard[self.x + i][self.y] == 'T' or self.game.cboard[self.x + i][self.y] == 'H' or self.game.cboard[self.x + i][self.y] == 'C' or self.game.cboard[self.x + i][self.y] == 'W'):
#                jump = i
#                break
#         if(jump > 0):
#             self.x+= jump-1
#         else:
#             self.x += self.speed
#         self.direction = 's'
#     elif(minBuilding.x < self.x):
#         jump = 0
#         for i in range(self.speed):
#            if(self.game.cboard[self.x - i][self.y] == 'T' or self.game.cboard[self.x - i][self.y] == 'H' or self.game.cboard[self.x - i][self.y] == 'C' or self.game.cboard[self.x - i][self.y] == 'W'):
#                jump = i
#                break
#         if(jump > 0):
#             self.x-= jump-1
#         else:
#             self.x -= self.speed
#         self.direction = 'w'
#     if(minBuilding.y > self.y):
#         jump = 0
#         for i in range(self.speed):
#            if(self.game.cboard[self.x][self.y + i] == 'T' or self.game.cboard[self.x][self.y + i] == 'H' or self.game.cboard[self.x][self.y + i] == 'C' or self.game.cboard[self.x][self.y + i] == 'W'):
#                jump = i
#                break
#         if(jump > 0):
#             self.y+= jump-1
#         else:
#             self.y += self.speed
#         self.direction = 'd'
#     elif(minBuilding.y < self.y):
#         jump = 0
#         for i in range(self.speed):
#            if(self.game.cboard[self.x][self.y - i] == 'T' or self.game.cboard[self.x][self.y - i] == 'H' or self.game.cboard[self.x][self.y - i] == 'C' or self.game.cboard[self.x][self.y - i] == 'W'):
#                jump = i
#                break
#         if(jump > 0):
#             self.y-= jump-1
#         else:
#             self.y -= self.speed
#         self.direction = 'a'
