from re import L, M
import time
from tkinter import N
 
class Game():
    def __init__(self,board,m,n):
        self.status = 'playing'
        self.score = 0
        self.board = board
        self.cboard = board
        self.huts=[]
        self.barbarians=[]
        self.n=n
        self.m=m    
        
    def addKing(self, king):
        self.king = king
        # self.cboard[self.king.y][self.king.x] = self.king.char 
    
    def addTownHall(self, townHall):
        self.townHall = townHall
        # self.cboard[self.townHall.y][self.townHall.x] = self.townHall.char
    
    def addHut(self, hut):
        self.huts.append(hut)
        # self.cboard[hut.y][hut.x] = hut.char

    def addBarbarain(self, hut):
        self.barbarians.append(hut)

    def display(self):
        for i in range(self.m):
            for j in range(self.n):
                print(self.board[i][j], end=" ")
            print()     




