import pygame, sys
import pygame.locals as gameGlobals
import random
window = pygame.display.set_mode((1000,800))
pygame.init()
pygame.font.init()
clock = pygame.time.Clock()
Red = (255,0,0)
green = (0,255,0)
black = (0,0,0)
white =(255,255,255)
k = (34,98,2)
purple = (128,0,128)

myfont = pygame.font.SysFont("Comic Sans MS",24)
class target():
    def __init__(self,x = 500,y = 400,hp = 2,col1 = Red,col2 = white,cx = 5,cy = 5):
        self.x = x
        self.y = y
        self.hp = hp
        self.col1 = col1
        self.col2 = col2
        self.cx = cx
        self.cy = cy
    def update(self):
        if self.hp >0:
            if self.x >= 925 or self.x <=75:
                self.cx = -self.cx
            if self.y >= 725 or self.y <= 75:
                self.cy =-self.cy
            self.x += self.cx
            self.y += self.cy
            self.rect = pygame.draw.circle(window,self.col1,(self.x,self.y), 75)
            pygame.draw.circle(window,self.col2,(self.x,self.y), 50)
            pygame.draw.circle(window,self.col1,(self.x,self.y),25)
        elif self.hp == 0:
            a.score +=1
            self.hp -= 1

    def clickDetection(self,pos):
        self.pos = pos
        self.hp -= 1
        self.col1 = white
        self.col2 = Red
class score():
    def __init__(self,score = 0,myfont = pygame.font.SysFont("Comic Sans MS",24)):
        self.score = score
        self.myfont = myfont
    def update(self):
        textSurface = (self.myfont).render(str(self.score),False,white)
        window.blit(textSurface,(20,20))


a = score()    
a.update()
ts = []
for x in range(10):
    ts.append(target(random.randint(75,925),random.randint(75,725),2,Red,white,5,5))
while True:
    clock.tick(60)
    window.fill(black)
    a.update()
    for x in ts:
        x.update()
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()
            for x in ts:
                if x.rect.collidepoint(pos):
                    x.clickDetection(pos)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                if a.score == 10:
                    for x in ts:
                        x.hp = 2
                        x.col1 = Red
                        x.col2 = white
                        a.score = 0


        if event.type == gameGlobals.QUIT:
            pygame.quit()
            sys.exit()