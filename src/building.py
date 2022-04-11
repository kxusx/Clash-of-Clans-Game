from src.utils import brickCOLOR
import colorama
from colorama import Fore, Back, Style

 
class Building(): 
    def __init__(self,game,x,y,width,height,type):
        self.game = game
        self.health = 10
        self.x=x 
        self.y=y
        self.status = 'alive'
        self.color = brickCOLOR[self.health]
        self.char = type
        self.width=width
        self.height=height
