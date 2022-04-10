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
        self.wizardTowers=[]
        self.persons=[] # king, queen, archer, barbarian, ballon
        self.noOfBuildings = 0
        self.n=n
        self.m=m    
        
    def addKing(self, king):
        self.king = king
        self.persons.append(king)
        # self.cboard[self.king.y][self.king.x] = self.king.char 
    
    def addQueen(self, queen):
        self.queen = queen
        self.persons.append(queen)
        # self.cboard[self.queen.y][self.queen.x] = self.queen.char

    def addTownHall(self, townHall):
        self.townHall = townHall
        # self.cboard[self.townHall.y][self.townHall.x] = self.townHall.char
    
    def addHut(self, hut):
        self.huts.append(hut)
        # self.cboard[hut.y][hut.x] = hut.char
    
    def addWizardTower(self, wizardTower):
        self.wizardTowers.append(wizardTower)
        # self.cboard[self.wizardTower.y][self.wizardTower.x] = self.wizardTower.char
    
    def addBuilding(self, building):
        self.buildings.append(building)
        if(building.char=='H' or building.char=='T' or building.char=='C'):
            self.noOfBuildings += 1
        # self.cboard[building.y][building.x] = building.char

    def addBarbarain(self, barbarian):
        self.barbarians.append(barbarian)
        self.persons.append(barbarian)

    def addArcher(self, archer):
        self.archers.append(archer)
        self.persons.append(archer)
    
    def addCannon(self, cannon):
        self.cannons.append(cannon)
    
    def addBallon(self, ballon):
        self.ballons.append(ballon)
        self.persons.append(ballon)

    def display(self):
        self.board[2][12]='U'
        for i in range(self.m):
            for j in range(self.n):
                print(self.board[i][j], end=" ")
            print()     

    def deleteBarbarian(self, i):
        self.barbarians.pop(i)



