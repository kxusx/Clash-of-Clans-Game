from utils import brickCOLOR
import colorama
from colorama import Fore, Back, Style


class TownHall():
    def __init__(self,game,x,y):
        self.game = game
        self.health = 10
        self.x=x 
        self.y=y
        self.status = 'alive'
        self.color = brickCOLOR[self.health]
        self.char = 'T'
        self.width=5
        self.height=5

    def display(self):
        y = self.y
        x = self.x
        w = self.width
        h = self.height
        arr = self.game.board
        cArr = self.game.cboard
        for j in range(self.y-int(h/2)-1,self.y+int(h/2)):
            for i in range(self.x-int(w/2)-1, self.x+int(w/2)):     
                arr[j][i] = self.color + self.char
                arr[j][self.x + int(w/2)] = Style.RESET_ALL + arr[j][self.x + w]
                cArr[j][i] = self.char
        self.game.board = arr
        self.game.cboard = cArr
    
    


