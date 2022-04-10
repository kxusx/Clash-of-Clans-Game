from distutils.command.build import build
from src.utils import brickCOLOR
import colorama
from colorama import Fore, Back, Style
from playsound import playsound


class ArcherQueen():
    def __init__(self, game, x, y,damage):
        self.status = 'alive'
        self.game = game
        self.health = 10
        self.damage = damage
        self.color = brickCOLOR[self.health]
        self.char = 'Q'
        self.x = x
        self.y = y
        self.width = 1
        self.height = 1
        self.speed=1
        self.direction = 'w'

    def display(self):
        if(self.health>0):
            arr = self.game.board
            arr[self.x][self.y] = self.color + self.char + Style.RESET_ALL
            self.game.board = arr

    def move(self, dir):
        if(dir == 'w'):  # w
            if(self.x > 0 and self.game.cboard[self.x - 1][self.y] == 'X'):
                self.x -= 1
                self.direction = 'w'    
        if(dir == 'a'):  # a
            if(self.y >= self.speed and self.game.cboard[self.x][self.y - self.speed] == 'X'):
                self.y -= self.speed
                self.direction = 'a'
        if(dir == 's'):  # s
            if(self.x < self.game.m-self.speed and self.game.cboard[self.x + self.speed][self.y] == 'X'):
                self.x += self.speed
                self.direction = 's'
        if(dir == 'd'):  # d
            if(self.y < self.game.n-self.speed and self.game.cboard[self.x][self.y + self.speed] == 'X'):
                self.y += self.speed
                self.direction = 'd'
        if(self.x==2 and self.y==12):
            self.health-=4
            self.color = brickCOLOR[self.health]

    def attack(self):
        if(self.direction == 'w'):
            centerX = self.x-8
            if centerX<0:
                centerX = 0
            centerY = self.y

            for building in self.game.buildings:
                if(building.char == 'T' or building.char == 'H' or building.char == 'C' or building.char=='#'):
                    if(building.x >= centerX-2 and building.x <= centerX+2 and building.y >= centerY-2 and building.y<=centerY+2):
                        building.health -= self.damage
                        building.color = brickCOLOR[building.health]

                        
        if(self.direction == 'a'):
            centerX = self.x
            if centerX<0:
                centerX = 0
            centerY = self.y-8

            for building in self.game.buildings:
                if(building.char == 'T' or building.char == 'H' or building.char == 'C' or building.char=='#'):
                    if(building.x >= centerX-2 and building.x <= centerX+2 and building.y >= centerY-2 and building.y<=centerY+2):
                        building.health -= self.damage
                        building.color = brickCOLOR[building.health]


        if(self.direction == 's'):
            centerX = self.x+8
            if centerX>self.game.m:
                centerX = self.game.m
            centerY = self.y

            for building in self.game.buildings:
                if(building.char == 'T' or building.char == 'H' or building.char == 'C' or building.char=='#'):
                     if(building.x >= centerX-2 and building.x <= centerX+2 and building.y >= centerY-2 and building.y<=centerY+2):
                        building.health -= self.damage
                        building.color = brickCOLOR[building.health]

        if(self.direction == 'd'):
            centerX = self.x
            if centerX>self.game.m:
                centerX = self.game.m
            centerY = self.y+8

            for building in self.game.buildings:
                if(building.char == 'T' or building.char == 'H' or building.char == 'C' or building.char=='#'):
                     if(building.x >= centerX-2 and building.x <= centerX+2 and building.y >= centerY-2 and building.y<=centerY+2):
                        building.health -= self.damage
                        building.color = brickCOLOR[building.health]