from utils import brickCOLOR
import colorama
from colorama import Fore, Back, Style




class Cannon():
    def __init__(self,game, x, y,damage,range, char):
        self.x = x
        self.y = y
        self.game = game
        self.range= range
        self.damage = damage
        self.health = 10
        self.char = char
        self.color = brickCOLOR[self.health]
    
    def display(self):
        cArr = self.game.cboard
        arr = self.game.board
        arr[self.x][self.y] = self.color + 'C' + Style.RESET_ALL
        cArr[self.x][self.y] = 'C'
        self.game.board = arr
        self.game.cboard = cArr
    

    def attack(self):
        for barbarian in self.game.barbarians:
            dist=(barbarian.x-self.x)**2+(barbarian.y-self.y)**2
            if(dist<=(self.range)**2):
                barbarian.health-=self.damage
                if(barbarian.health<=0):
                    barbarian.status='dead'
                    self.game.barbarians.remove(barbarian)
                return

