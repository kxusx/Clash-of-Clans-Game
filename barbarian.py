from utils import brickCOLOR
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
        self.direction = 'w'
        self.status = 'alive'

    def move(self):
        minDist = 10000
        for hut in self.game.huts:
            dist = abs(hut.x - self.x) + abs(hut.y - self.y)
            if(dist < minDist):
                minDist = dist
                minHut = hut
        
        if(minHut.x > self.x):
            if(self.x < self.game.m-1 and self.game.cboard[self.x + 1][self.y] == 'X'):
                self.x += 1
                self.direction = 's'
        elif(minHut.x < self.x):
            if(self.x > 0 and self.game.cboard[self.x - 1][self.y] == 'X'):
                self.x -= 1
                self.direction = 'w'
      
        if(minHut.y > self.y):
            if(self.y < self.game.n-1 and self.game.cboard[self.x][self.y + 1] == 'X'):
                self.y += 1
                self.direction = 'd'
        elif(minHut.y < self.y):
            if(self.y > 0 and self.game.cboard[self.x][self.y - 1] == 'X'):
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
        for hut in self.game.huts:
            if(hut.x == self.x and hut.y == self.y):
                hut.health -= self.damage
                hut.color = brickCOLOR[hut.health]
                hut.display()
                if(hut.health <= 0):
                    hut.status = 'dead'
                    hut.display()
                    self.game.huts.remove(hut)
                    self.game.huts_count -= 1
                    self.game.score += 1
                    self.game.display()
                    self.game.check_game_over()
                    break