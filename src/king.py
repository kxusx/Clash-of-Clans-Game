from src.utils import brickCOLOR
import colorama
from colorama import Fore, Back, Style
from playsound import playsound


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

    def attack(self):
        if(self.direction == 'w'):
            if(self.x > 0 and (self.game.cboard[self.x - 1][self.y] == 'T' 
            or self.game.cboard[self.x - 1][self.y] == 'H' 
            or self.game.cboard[self.x - 1][self.y] == 'C' 
            or self.game.cboard[self.x - 1][self.y] == '#')):
                for building in self.game.buildings:
                    if(self.game.cboard[self.x - 1][self.y] == 'T' and building.char == 'T'):
                        building.health -= self.damage
                        playsound("src/bullet1.mov")
                        building.color = brickCOLOR[building.health]    
                    elif(building.x == self.x - 1 and building.y == self.y):
                        playsound("src/bullet1.mov")
                        building.health -= self.damage
                        building.color = brickCOLOR[building.health]    
                        

        if(self.direction == 'a'):
            if(self.y > 0 and (self.game.cboard[self.x][self.y - 1] == 'T' 
               or self.game.cboard[self.x][self.y - 1] == 'H' 
               or self.game.cboard[self.x][self.y - 1] == 'C'
               or self.game.cboard[self.x][self.y - 1] == '-')):
                for building in self.game.buildings:
                    if(self.game.cboard[self.x][self.y - 1] == 'T' and building.char == 'T'):
                        building.health -= self.damage
                        playsound("src/bullet1.mov")
                        building.color = brickCOLOR[building.health]
                    elif(building.x == self.x and building.y == self.y - 1):
                        building.health -= self.damage
                        playsound("src/bullet1.mov")
                        building.color = brickCOLOR[building.health]

        if(self.direction == 's'):
            if(self.x < self.game.m-1 and (self.game.cboard[self.x + 1][self.y] == 'T' 
               or self.game.cboard[self.x + 1][self.y] == 'H' 
               or self.game.cboard[self.x + 1][self.y] == 'C'
               or self.game.cboard[self.x + 1][self.y] == '#')):
                for building in self.game.buildings:
                    if(self.game.cboard[self.x + 1][self.y] == 'T' and building.char == 'T'):
                        building.health -= self.damage
                        playsound("src/bullet1.mov")
                        building.color = brickCOLOR[building.health]
                    elif(building.x == self.x + 1 and building.y == self.y):
                        building.health -= self.damage
                        playsound("src/bullet1.mov")
                        building.color = brickCOLOR[building.health]
               
        if(self.direction == 'd'):
            if(self.y < self.game.n-1 and (self.game.cboard[self.x][self.y + 1] == 'T' 
               or self.game.cboard[self.x][self.y + 1] == 'H' 
               or self.game.cboard[self.x][self.y + 1] == 'C'
               or self.game.cboard[self.x][self.y + 1] == '#')):
                for building in self.game.buildings:
                    if(self.game.cboard[self.x][self.y + 1] == 'T' and building.char == 'T'):
                        building.health -= self.damage
                        playsound("src/bullet1.mov")
                        building.color = brickCOLOR[building.health]
                    elif(building.x == self.x and building.y == self.y + 1):
                        building.health -= self.damage
                        playsound("src/bullet1.mov")
                        building.color = brickCOLOR[building.health]
        
    def leviathonAttack(self,range):
        for building in self.game.buildings:
            dist = (self.x - building.x)**2 + (self.y - building.y)**2
            if(dist <= range**2):
                building.health -= self.damage
                building.color = brickCOLOR[building.health]

    