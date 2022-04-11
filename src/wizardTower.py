from src.utils import brickCOLOR
import colorama
from colorama import Fore, Back, Style
from src.building import Building
import math

class WizardTower(Building):

    def __init__(self,game,x,y,damage,range):
        super().__init__(game,x,y,1,1,'W')
        self.range= range
        self.damage = 0.5
    
    def display(self):
        cArr = self.game.cboard
        arr = self.game.board
        
        arr[self.x][self.y] = self.color + 'W' + Style.RESET_ALL
        cArr[self.x][self.y] = 'W'
        self.color=brickCOLOR[self.health]    
        self.game.board = arr
        self.game.cboard = cArr
    

    def attack(self):
        for person in self.game.persons:
            
            dist = (person.x-self.x)**2+(person.y-self.y)**2
            if(dist<=(self.range)**2):
                
                centerX = person.x
                centerY = person.y
                for person in self.game.persons:
                    if(person.x>=centerX-1 and person.x<=centerX+1 and person.y>=centerY-1 and person.y<=centerY+1):
                        person.health-=self.damage
        
                        if(person.health<=0):
                            self.game.persons.remove(person)
                            person.color=brickCOLOR[0]
                        else:
                            person.color = brickCOLOR[math.floor(person.health)]
                        return