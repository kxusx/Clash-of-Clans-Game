from src.utils import brickCOLOR
import colorama
from colorama import Fore, Back, Style
from src.building import Building

 
class TownHall(Building):
    def __init__(self,game,x,y):
        super().__init__(game,x,y,4,3,'T')

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
    
    


