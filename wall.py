from utils import brickCOLOR
import colorama
from colorama import Fore, Back, Style
from building import Building

class Wall(Building):
    def __init__(self, game, x, y):
        super().__init__(game, x, y, 1, 1, '#')
        
    def display(self):
        if(self.health>0):
            cArr = self.game.cboard
            arr = self.game.board

            arr[self.x][self.y] = self.color + self.char + Style.RESET_ALL
            cArr[self.x][self.y] = self.char

            self.game.board = arr
            self.game.cboard = cArr