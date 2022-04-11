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
        self.noOfBarbarians = 0
        self.noOfArchers = 0
        self.noOfBallons = 0
        self.n=n
        self.m=m    
        self.level=1
        
    #----------------------------------------------------------------------------------------------------------------------
    # PERSONS
    # KING , QUEEN 
    # ARCHER , BARBARIAN , BALLON
    def addKing(self, king):
        self.king = king
        self.persons.append(king)
        # self.cboard[self.king.y][self.king.x] = self.king.char 
    
    def addQueen(self, queen):
        self.queen = queen
        self.persons.append(queen)
        # self.cboard[self.queen.y][self.queen.x] = self.queen.char
    
    def addBarbarain(self, barbarian):
        self.barbarians.append(barbarian)
        self.noOfBarbarians += 1
        self.persons.append(barbarian)

    def addArcher(self, archer):
        self.archers.append(archer)
        self.noOfArchers += 1
        self.persons.append(archer)

    def addBallon(self, ballon):
        self.ballons.append(ballon)
        self.noOfBallons += 1
        self.persons.append(ballon)

    #-----------------------------------------------------------------
    # BUILDINGS
    # HUT , TOWNHALL , CANNON , WIZARDTOWER, WALL

    def addTownHall(self, townHall):
        self.townHall = townHall
        self.addBuilding(townHall)
    
    def addHut(self, hut):
        self.huts.append(hut)
        self.addBuilding(hut)
    
    def addWizardTower(self, wizardTower):
        self.wizardTowers.append(wizardTower)
        self.addBuilding(wizardTower)
    
    def addCannon(self, cannon):
        self.cannons.append(cannon)
        self.addBuilding(cannon)
    
    def addBuilding(self, building):
        self.buildings.append(building)
        if(building.char=='H' or building.char=='T' or building.char=='C' or building.char=='W'):
            self.noOfBuildings += 1
        
    #-----------------------------------------------------------------

    def display(self):
        self.board[2][12]='U'
        for i in range(self.m):
            for j in range(self.n):
                print(self.board[i][j], end=" ")
            print()     

    def deleteBarbarian(self, i):
        self.barbarians.pop(i)



