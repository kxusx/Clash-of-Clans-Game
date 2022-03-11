from utils import brickCOLOR
import colorama
from colorama import Fore, Back, Style

class Wall():
    def __init__(self, game, x, y):
        self.game = game
        self.health = 10
        self.x=x 
        self.y=y
        self.status = 'alive'
        self.color = brickCOLOR[self.health]
        self.char = '#'
        self.width=1
        self.height=1

    def display(self):
        if(self.health>0):
            cArr = self.game.cboard
            arr = self.game.board

            arr[self.x][self.y] = self.color + self.char + Style.RESET_ALL
            cArr[self.x][self.y] = self.char

            self.game.board = arr
            self.game.cboard = cArr