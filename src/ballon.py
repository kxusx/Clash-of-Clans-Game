import math
from src.utils import brickCOLOR
import colorama
from colorama import Fore, Back, Style


class Ballon():
    def __init__(self, game, x, y,spawnTime):
        self.game = game
        self.health = 10
        self.damage = 4
        self.color = brickCOLOR[self.health]
        self.char = 'b'
        self.x = x
        self.y = y
        self.width = 1
        self.height = 1
        self.speed = 2
        self.direction = 'w'
        self.range=1
        self.spawnTime = 0
        self.status = 'alive'

    def move(self,timenow):
        minDist = 10000
        
        if(len(self.game.cannons) > 0 or len(self.game.wizardTowers)>0):
            for building in self.game.buildings:
                if( building.char == 'C' or building.char == 'W'):
                    dist = abs(building.x - self.x) + abs(building.y - self.y)
                    if(dist < minDist):
                        minDist = dist
                        minBuilding = building
        else:
            for building in self.game.buildings:
                if(building.char == 'T' or building.char == 'H' ):
                    dist = abs(building.x - self.x) + abs(building.y - self.y)
                    if(dist < minDist):
                        minDist = dist
                        minBuilding = building
        
        if((self.spawnTime-timenow)%1==0):
            if(minDist<1000):
                if(minBuilding.x > self.x):
                    if(self.x < self.game.m-1 and (self.game.cboard[self.x + 1][self.y] == 'X' or self.game.cboard[self.x + 1][self.y] == 'B') or self.game.cboard[self.x + 1][self.y] == 'b' or self.game.cboard[self.x + 1][self.y] == '#' or self.game.cboard[self.x + 1][self.y] == 'T'):
                        self.x += 1
                        self.direction = 's'            
                elif(minBuilding.x < self.x):
                    if(self.x > 0 and (self.game.cboard[self.x - 1][self.y] == 'X' or self.game.cboard[self.x - 1][self.y] == 'B') or self.game.cboard[self.x - 1][self.y] == 'b' or self.game.cboard[self.x - 1][self.y] == '#' or self.game.cboard[self.x - 1][self.y] == 'T'):
                        self.x -= 1
                        self.direction = 'w'

                if(minBuilding.y > self.y):
                    if(self.y < self.game.n-1 and (self.game.cboard[self.x][self.y + 1] == 'X' or self.game.cboard[self.x][self.y + 1] == 'B') or self.game.cboard[self.x][self.y + 1] == 'b' or self.game.cboard[self.x][self.y + 1] == '#' or self.game.cboard[self.x][self.y + 1] == 'T'):
                        self.y += 1
                        self.direction = 'd'
                elif(minBuilding.y < self.y):
                    if(self.y > 0 and (self.game.cboard[self.x][self.y - 1] == 'X' or self.game.cboard[self.x][self.y - 1] == 'B') or self.game.cboard[self.x][self.y - 1] == 'b' or self.game.cboard[self.x][self.y - 1] == '#' or self.game.cboard[self.x][self.y - 1] == 'T'):
                        self.y -= 1
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
        if(self.x > 0 and (self.game.cboard[self.x - self.range][self.y] == 'T' 
           or self.game.cboard[self.x - self.range][self.y] == 'H' 
           or self.game.cboard[self.x - self.range][self.y] == 'C'
           or self.game.cboard[self.x - self.range][self.y] == 'W'
           )):
            for building in self.game.buildings:
                if(self.game.cboard[self.x - self.range][self.y] == 'T' and building.char == 'T'):
                    building.health -= self.damage
                    if(building.health<=0):
                        building.color = brickCOLOR[0]
                    else:
                        building.color = brickCOLOR[math.floor(building.health)]
                elif(building.x == self.x - self.range and building.y == self.y):
                    building.health -= self.damage
                    if(building.health<=0):
                        building.color = brickCOLOR[0]
                    else:
                        building.color = brickCOLOR[math.floor(building.health)]
            return

        if(self.y > 0 and (self.game.cboard[self.x][self.y - self.range] == 'T' 
           or self.game.cboard[self.x][self.y - self.range] == 'H' 
           or self.game.cboard[self.x][self.y - self.range] == 'C'
           or self.game.cboard[self.x][self.y - self.range] == 'W'
           )):
            for building in self.game.buildings:
                if(self.game.cboard[self.x][self.y - self.range] == 'T' and building.char == 'T'):
                    building.health -= self.damage
                    if(building.health<=0):
                        building.color = brickCOLOR[0]
                    else:
                        building.color = brickCOLOR[math.floor(building.health)]
                elif(building.x == self.x and building.y == self.y - self.range):
                    building.health -= self.damage
                    if(building.health<=0):
                        building.color = brickCOLOR[0]
                    else:
                        building.color = brickCOLOR[math.floor(building.health)]
            return

        if(self.x < self.game.m-self.range and (self.game.cboard[self.x + self.range][self.y] == 'T' 
           or self.game.cboard[self.x + self.range][self.y] == 'H' 
           or self.game.cboard[self.x + self.range][self.y] == 'C'
              or self.game.cboard[self.x + self.range][self.y] == 'W'
           )):
            for building in self.game.buildings:
                if(self.game.cboard[self.x + self.range][self.y] == 'T' and building.char == 'T'):
                    building.health -= self.damage
                    if(building.health<=0):
                        building.color = brickCOLOR[0]
                    else:
                        building.color = brickCOLOR[math.floor(building.health)]
                elif(building.x == self.x + self.range and building.y == self.y):
                    building.health -= self.damage
                    if(building.health<=0):
                        building.color = brickCOLOR[0]
                    else:
                        building.color = brickCOLOR[math.floor(building.health)]
            return

        if(self.y < self.game.n-self.range and (self.game.cboard[self.x][self.y + self.range] == 'T' 
           or self.game.cboard[self.x][self.y + self.range] == 'H' 
           or self.game.cboard[self.x][self.y + self.range] == 'C'
              or self.game.cboard[self.x][self.y + self.range] == 'W'
           )):
            for building in self.game.buildings:
                if(self.game.cboard[self.x][self.y + self.range] == 'T' and building.char == 'T'):
                    building.health -= self.damage
                    if(building.health<=0):
                        building.color = brickCOLOR[0]
                    else:
                        building.color = brickCOLOR[math.floor(building.health)]
                elif(building.x == self.x and building.y == self.y + self.range):
                    building.health -= self.damage
                    if(building.health<=0):
                        building.color = brickCOLOR[0]
                    else:
                        building.color = brickCOLOR[math.floor(building.health)]
            return

    # def move(self):
    #     minDist = 10000
    #     for building in self.game.buildings:
    #         if(building.char == 'T' or building.char == 'H' or building.char == 'C'):
    #             dist = abs(building.x - self.x) + abs(building.y - self.y)
    #             if(dist < minDist):
    #                 minDist = dist
    #                 minBuilding = building

    #     if(minDist < 1000):
    #         jump = 5*self.speed
    #         #-----------------------------------------------------
    #         if(minBuilding.x > self.x):
    #             if(abs(minBuilding.x-self.x) <= self.speed):
    #                 jump = abs(minBuilding.x-self.x)-1
    #                 if(jump == 0):
    #                     jump = 1
    #             if(jump > 2):
    #                 jump = self.speed
    #             if(self.x < self.game.m-1 and (self.game.cboard[self.x + jump][self.y] == 'X' or self.game.cboard[self.x + jump][self.y] == 'B') or self.game.cboard[self.x + jump][self.y] == 'b' or self.game.cboard[self.x + jump][self.y] == '#' or self.game.cboard[self.x + jump][self.y] == 'T'):
    #                 self.x += jump
    #                 self.direction = 's'
    #         #-----------------------------------------------------
    #         elif(minBuilding.x < self.x):
    #             if(abs(minBuilding.x-self.x) <= self.speed):
    #                 jump = abs(minBuilding.x-self.x)-1
    #                 if(jump == 0):
    #                     jump = 1
    #             if(jump > 2):
    #                 jump = self.speed
    #             if(self.x > 0 and(self.game.cboard[self.x - jump][self.y] == 'X' or self.game.cboard[self.x - jump][self.y] == 'B') or self.game.cboard[self.x - jump][self.y] == 'b' or self.game.cboard[self.x - jump][self.y] == '#' or self.game.cboard[self.x - jump][self.y] == 'T' ):
    #                 self.x -= jump
    #                 self.direction = 'w'
    #         #-----------------------------------------------------
    #         jump = 5*self.speed
    #         #-----------------------------------------------------
    #         if(minBuilding.y > self.y):
    #             if(abs(minBuilding.y-self.y) <= self.speed):
    #                 jump = abs(minBuilding.y-self.y)-1
    #                 if(jump == 0):
    #                     jump = 1
    #             if(jump > 2):
    #                 jump = self.speed
    #             if(self.y < self.game.n-1 and (self.game.cboard[self.x][self.y + jump] == 'X' or self.game.cboard[self.x][self.y + jump] == 'B') or self.game.cboard[self.x][self.y + jump] == 'b' or self.game.cboard[self.x][self.y + jump] == '#' or self.game.cboard[self.x][self.y + jump] == 'T'):
    #                 self.y += jump
    #                 self.direction = 'd'
    #         #-----------------------------------------------------
    #         elif(minBuilding.y < self.y):
    #             if(abs(minBuilding.y-self.y) <= self.speed):
    #                 jump = abs(minBuilding.y-self.y)-1
    #                 if(jump == 0):
    #                     jump = 1
    #             if(jump > 2):
    #                 jump = self.speed
    #             if(self.y > 0 and (self.game.cboard[self.x][self.y - jump] == 'X' or self.game.cboard[self.x][self.y - jump] == 'B') or self.game.cboard[self.x][self.y - jump] == 'b' or self.game.cboard[self.x][self.y - jump] == '#' or self.game.cboard[self.x][self.y - jump] == 'T'):
    #                 self.y -= jump
    #                 self.direction = 'a'
    #         #-----------------------------------------------------