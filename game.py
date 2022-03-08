from re import L, M
import time
from tkinter import N
 
class Game():
    def __init__(self,board,m,n):
        self.status = 'playing'
        self.score = 0
        self.board = board
        self.cboard = board
        self.n=n
        self.m=m    
        # self.townHall= TownHall(self,15,15)

    def display(self):
        for i in range(self.m):
            for j in range(self.n):
                print(self.board[i][j], end=" ")
            print()     




