from src.utils import brickCOLOR
import colorama
from colorama import Fore, Back, Style


class Spells():
    def __init__(self, game):
        self.game = game

    def rage(self):
        for barbarian in self.game.barbarians:
            barbarian.damage += 1
            barbarian.speed += 1


        self.game.king.damage += 1
        self.game.king.speed += 1

    def heal(self):
        for barbarian in self.game.barbarians:
            if(barbarian.health*1.5 <= 10):
                barbarian.health = int(barbarian.health*1.5)
            else:
                barbarian.health = 10
            barbarian.color = brickCOLOR[barbarian.health]

        if (self.game.king.health*1.5 <= 10):
            self.game.king.health = int(self.game.king.health*1.5)
        else:
            self.game.king.health = 10
        self.game.king.color = brickCOLOR[self.game.king.health]
