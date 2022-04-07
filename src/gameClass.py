from re import L, M
import time
 
class Game():
    def __init__(self,board,m,n):
        self.status = 'playing'
        self.score = 0
        self.board = board
        self.cboard = board
        self.huts=[]
        self.buildings= []
        self.barbarians=[]
        self.archers=[]
        self.cannons=[]
        self.ballons=[]
        self.noOfBuildings = 0
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
    
    def addBuilding(self, building):
        self.buildings.append(building)
        if(building.char=='H' or building.char=='T' or building.char=='C'):
            self.noOfBuildings += 1
        # self.cboard[building.y][building.x] = building.char

    def addBarbarain(self, hut):
        self.barbarians.append(hut)

    def addArcher(self, archer):
        self.archers.append(archer)
    
    def addCannon(self, cannon):
        self.cannons.append(cannon)
    
    def addBallon(self, ballon):
        self.ballons.append(ballon)
        # self.cboard[self.ballon.y][self.ballon.x] = self.ballon.char

    def display(self):
        self.board[2][12]='U'
        for i in range(self.m):
            for j in range(self.n):
                print(self.board[i][j], end=" ")
            print()     

    def deleteBarbarian(self, i):
        self.barbarians.pop(i)



