from utils import brickCOLOR
import colorama
from colorama import Fore, Back, Style
from building import Building


class TownHall(Building):
    def __init__(self,game,x,y):
        super().__init__(game,x,y,5,5,'T')

    def display(self):
        if(self.health>0):
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
    
    


