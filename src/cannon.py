from src.utils import brickCOLOR
import colorama
from colorama import Fore, Back, Style
from src.building import Building

class Cannon(Building):

    def __init__(self,game,x,y,damage,range):
        super().__init__(game,x,y,1,1,'C')
        self.range= range
        self.damage = damage
    
    def display(self):
        cArr = self.game.cboard
        arr = self.game.board
        
        arr[self.x][self.y] = self.color + 'C' + Style.RESET_ALL
        cArr[self.x][self.y] = 'C'
        self.color=brickCOLOR[self.health]    
        self.game.board = arr
        self.game.cboard = cArr
    

    def attack(self):
        for barbarian in self.game.barbarians:
            dist=(barbarian.x-self.x)**2+(barbarian.y-self.y)**2
            if(dist<=(self.range)**2):
                self.color=Back.BLUE
                barbarian.health-=self.damage
                barbarian.color = brickCOLOR[barbarian.health]
                if(barbarian.health<=0):
                    barbarian.status='dead'
                    self.game.barbarians.remove(barbarian)
                
                return
        
        distToKing = (self.game.king.x-self.x)**2+(self.game.king.y-self.y)**2
        if(distToKing<=(self.range)**2):
            self.color=Back.BLUE
            if(self.game.king.health>=0):
                self.game.king.health-=self.damage
                self.game.king.color = brickCOLOR[self.game.king.health]
            if(self.game.king.health<0):
                self.game.king.status='dead'
            
            return
            


