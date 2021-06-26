import random, pygame, sys, os, time
from pygame.locals import *
from gameMenu import *
WIDTH = 300
HEIGHT = 400
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
pygame.init()
clk = pygame.time.Clock()
font = pygame.font.Font(None, 25)
whiterect = pygame.Rect(0,0,300,100)
starttimer = True
fc = 0
fr = 60
st = 90
m = 0
s = 0
noOfFlags = 10
WON = pygame.image.load("Sprites/youWin.png")
WINDOW = pygame.display.set_mode((WIDTH,HEIGHT))
bv = displayMenu(WINDOW)
if bv:
    pygame.quit()
    sys.exit()
pygame.display.set_caption("Minesweeper")
WINDOW.fill(WHITE)
pos = (-1,-1)
mouseboolgrid = []
flagList = []
rst = "RESET".format()
rstbutton = font.render(rst, True, GREEN)
rstclicked = False
mineExploded = False
class Sumedh:
    def __init__(self,n,bombs):
        self.n = n
        self.bombs = bombs
        self.table = self.make_table()
        self.mine()

    def mine(self): # this function creates the grid, places the mines and places numbers accordingly
        self.table = self.bomb_placing()
        self.table = self.chk_table()

    def make_table(self): # function to make a square grid
      return [[0] *self.n  for i in range(0,self.n)]

    def bomb_placing(self): # function to place mines
      for i in range(0,self.bombs):
        is_bomb = False
        while not is_bomb:
          x = random.randint(0,len(self.table)-1)
          y = random.randint(0,len(self.table)-1)
          if self.table[x][y]!=-1:
            self.table[x][y]=-1;
            is_bomb=True
      return self.table

    #bomb_placing(table,1)
    #print(bomb_placing(table,2))

    def chk_table(self): # checks for mines in adjacent cells. If no mines are there, places numbers accordingly
      for x in range(0,len(self.table)):
        for y in range(0,len(self.table[x])):
          if self.table[x][y] == -1:
            self.table = self.chk_dl(x,y)
            self.table = self.chk_dr(x,y)
            self.table = self.chk_d(x,y)
            self.table = self.chk_ul(x,y)
            self.table = self.chk_ur(x,y)
            self.table = self.chk_u(x,y)
            self.table = self.chk_r(x,y)
            self.table = self.chk_l(x,y)
      return self.table

    def chk_dl(self,x,y): # checks lower left position
        if x+1 < len(self.table[x]) and y -1 >=0:
            if self.table[x+1][y-1] != -1:
                self.table[x+1][y-1] += 1
        return self.table

    def chk_dr(self,x,y): # checks lower right position
        if(x+1 < len(self.table[0]) and y+1 < len(self.table)):
          if self.table[x+1][y+1] != -1:
            self.table[x+1][y+1] += 1
        return self.table

    def chk_d(self,x,y): # checks lower position
        if x+1 < len(self.table[0]):
          if self.table[x+1][y] != -1:
            self.table[x+1][y] += 1
        return self.table

    def chk_ul(self,x,y): # checks upper left position
        if x-1>=0 and y -1 >=0:
          if self.table[x-1][y-1] != -1:
            self.table[x-1][y-1] += 1
        return self.table

    def chk_ur(self,x,y): # checks upper right position
        if x-1>=0 and y+1< len(self.table[x]):
          if self.table[x-1][y+1] != -1:
            self.table[x-1][y+1] += 1
        return self.table

    def chk_u(self,x,y): # checks upper position
        if x-1>=0:
          if self.table[x-1][y] != -1:
            self.table[x-1][y] += 1
        return self.table

    def chk_r(self,x,y): # checks right position
        if y+1 < len(self.table):
          if self.table[x][y+1] != -1:
            self.table[x][y+1] += 1
        return self.table

    def chk_l(self,x,y): # checks left position
        if y-1 >=0:
          if self.table[x][y-1] != -1:
            self.table[x][y-1] += 1
        return self.table

    def getTable(self):
        return self.table
a = Sumedh(10,10)
t = a.getTable()
# adnan's part
def loadSprites():
    imgs = [pygame.transform.scale(pygame.image.load('Sprites/'+str(i)+'.png'),(30,30)) for i in range(1,14)]
    return tuple(imgs)
def initMouseBoolGrid():
    global mouseboolgrid
    mouseboolgrid = []
    for r in range(0,len(t)):
        te = []
        for c in range(0,len(t)):
            te.append(0)
        mouseboolgrid.append(te)
# for r in range(0,len(t)):
#     te = []
#     for c in range(0,len(t)):
#         te.append(0)
#     mouseboolgrid.append(te)
timgs = loadSprites()
def beWithinRange(x,y):
    if x in range(len(t)) and y in range(len(t)):
        return True
def getPos(pos): # (x,y)
    global mouseboolgrid
    row = pos[0] // 30
    col = (pos[1] - 100) // 30
    if pos[1] >= 100 and pos[1] < 400:
        # mouseboolgrid[row][col] = 1
        return row,col
    else:
        return -1,-1
def drawInitial():
    global t
    print(t)
    for i in range(0,len(t)):
        for j in range(0,len(t)):
            WINDOW.blit(timgs[10],(i*30,j*30+100))
def neighbours(r, col):
    global t, flagList # this is t
    global mouseboolgrid
    # If the cell already not visited
    if not mouseboolgrid[r][col] and (r,col) not in flagList:
        # Mark the cell visited
        mouseboolgrid[r][col] = 1
        if t[r][col] in range(1,9):
            WINDOW.blit(timgs[t[r][col]-1],(r*30,col*30+100))
            return
        elif t[r][col] == 0:
            WINDOW.blit(timgs[11],(r*30,col*30+100))
        # Recursive calls for the neighbouring cells
        if r > 0:
            neighbours(r-1, col)
        if r < len(t)-1:
            neighbours(r+1, col)
        if col > 0:
            neighbours(r, col-1)
        if col < len(t)-1:
            neighbours(r, col+1)
def drawStaticTable(pos):
    global t, WINDOW, mineExploded, starttimer
    x = pos[0]
    y = pos[1]
    if t[x][y] in range(0,9):
        neighbours(x,y)
    elif t[x][y] == -1:
        for i in range(len(t)):
            for j in range(len(t)):
                if t[i][j] in range(1,9):
                    WINDOW.blit(timgs[t[i][j]-1],(i*30,j*30+100))
                elif t[i][j] == 0:
                    WINDOW.blit(timgs[11],(i*30,j*30+100))
                elif t[i][j] == -1:
                    WINDOW.blit(timgs[8],(i*30,j*30+100))
                    # drawTable(pos)
                    starttimer = False
                    mineExploded = True
        WINDOW.blit(timgs[9],(x*30,y*30+100))
def displayTimer():
    global m, s
    global fc, fr, noOfFlags, starttimer
    f = "Flags: "+str(noOfFlags)+""
    ft = font.render(f, True, BLACK)
    WINDOW.blit(ft, [120,80])
    if starttimer:
        if fc % 60 == 0:
            s += 1
        if s == 60:
            m += 1
            s = 0
    if (s//10) % 10 == 0:
        o_s = "0"+str(s)
    else:
        o_s = str(s)
    if (m//10) % 10 == 0:
        o_m = "0"+str(m)
    else:
        o_m = str(m)
    td = "Time: "+o_m+":"+o_s
    o_t = font.render(td, True, BLACK)
    WINDOW.blit(o_t, [10,80])
    fc += 1
    clk.tick(fr)
def win():
    global flagList, t
    c = 0
    if len(flagList) == 10:
        for i,j in flagList:
            if t[i][j] == -1:
                c += 1
        if c == 10:
            WINDOW.blit(WON,(0,0))
            starttimer = False
def resetClicked():
    global noOfFlags, mineExploded, flagList, a, t, starttimer, rstclicked, s, m
    initMouseBoolGrid()
    drawInitial()
    s = 0
    m = 0
    noOfFlags = 10
    mineExploded = False
    flagList = []
    a = Sumedh(10,10)
    t = a.getTable()
    starttimer = True
    rstclicked = False
# apeksha is explaining from here
def drawFlag(tup): #(x,y)
    global noOfFlags, WINDOW
    x = tup[0]
    y = tup[1]
    if noOfFlags:
        WINDOW.blit(timgs[12],(x*30,y*30+100))
        noOfFlags -= 1
        flagList.append(tup)
initMouseBoolGrid()
drawInitial()
while not bv:# main game loop
    pygame.draw.rect(WINDOW, WHITE, whiterect)
    pos = getPos(pygame.mouse.get_pos())
    ppp = pygame.mouse.get_pos()
    if 7*WIDTH//10+10 <= ppp[0] <= 7*WIDTH//10+50 and HEIGHT//10+20 <= ppp[1] <= HEIGHT//10+50:
        rstclicked = True
        pygame.draw.rect(WINDOW, RED, [7*WIDTH//10+20, HEIGHT//10+30, 7*WIDTH//10, 30])
    else:
        rstclicked = False
    WINDOW.blit(rstbutton, [240,80])
    for event in pygame.event.get():
        if event.type == QUIT:
            bv = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                if rstclicked:
                    resetClicked()
                elif pos not in flagList:
                    drawStaticTable(pos)
                    # neighbours(pos[0], pos[1])
            elif event.button == 3 and not mineExploded:
                pos = getPos(pygame.mouse.get_pos())
                drawFlag(pos)
    displayTimer()
    win()
    pygame.display.flip()
pygame.quit()
