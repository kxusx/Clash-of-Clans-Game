from utils import brickCOLOR
import colorama
from colorama import Fore, Back, Style
from building import Building


class TownHall(Building):
    def __init__(self,game,y,x):
        super().__init__(game,y,x,5,5,'T')

    def display(self):
        if(self.health>0):
            x = self.x
            y = self.y
            w = self.width
            h = self.height
            arr = self.game.board
            cArr = self.game.cboard
            for j in range(self.x-int(h/2)-1,self.x+int(h/2)):
                for i in range(self.y-int(w/2)-1, self.y+int(w/2)):     
                    arr[j][i] = self.color + self.char
                    arr[j][self.y + int(w/2)] = Style.RESET_ALL + arr[j][self.y + w]
                    cArr[j][i] = self.char
            self.game.board = arr
            self.game.cboard = cArr
    
    


