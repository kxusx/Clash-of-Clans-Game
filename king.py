from utils import brickCOLOR
import colorama
from colorama import Fore, Back, Style


class King():
    def __init__(self, game, x, y):
        self.status = 'alive'
        self.game = game
        self.health = 10
        self.color = brickCOLOR[self.health]
        self.char = 'K'
        self.x = x
        self.y = y
        self.width = 1
        self.height = 1
        self.direction = 'w'

    def display(self):
        arr = self.game.board
        arr[self.y][self.x] = self.color + self.char + Style.RESET_ALL
        self.game.board = arr

    def move(self, dir):
        if(dir == 'w'):  # w
            if(self.y > 0 and self.game.cboard[self.y - 1][self.x] == 'X'):
                self.y -= 1
                self.direction = 'w'
        if(dir == 'a'):  # a
            if(self.x > 0 and self.game.cboard[self.y][self.x - 1] == 'X'):
                self.x -= 1
                self.direction = 'a'
        if(dir == 's'):  # s
            if(self.y < self.game.m-1 and self.game.cboard[self.y + 1][self.x] == 'X'):
                self.y += 1
                self.direction = 's'
        if(dir == 'd'):  # d
            if(self.x < self.game.n-1 and self.game.cboard[self.y][self.x + 1] == 'X'):
                self.x += 1
                self.direction = 'd'

    def attack(self):
        if(self.direction == 'w'):
            if(self.y > 0 and self.game.cboard[self.y - 1][self.x] == 'T'):
                print("shh")
                self.game.townHall.health -= 1
                self.game.townHall.color = brickCOLOR[self.game.townHall.health]
                # self.game.townHall.display()
        if(self.direction == 'a'):
            if(self.x > 0 and self.game.cboard[self.y][self.x - 1] == 'T'):
                self.game.townHall.health -= 1
                self.game.townHall.color = brickCOLOR[self.game.townHall.health]
                # self.game.townHall.display()
        if(self.direction == 's'):
            if(self.y < self.game.m-1 and self.game.cboard[self.y + 1][self.x] == 'T'):
                self.game.townHall.health -= 1
                self.game.townHall.color = brickCOLOR[self.game.townHall.health]
                # self.game.townHall.display()
        if(self.direction == 'd'):
            if(self.x < self.game.n-1 and self.game.cboard[self.y][self.x + 1] == 'T'):
                self.game.townHall.health -= 1
                self.game.townHall.color = brickCOLOR[self.game.townHall.health]
                # self.game.townHall.display()
        