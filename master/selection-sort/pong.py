import pygame, sys
import pygame.locals as gameGlobals
import random
import time
white =(255,255,255)
black = (0,0,0)
window = pygame.display.set_mode((1000,800))
pygame.init()
pygame.font.init()
clock = pygame.time.Clock()
intro = (pygame.font.SysFont("Comic Sans MS",24)).render("Press e for easy, n for normal, and i for impossible",False,white)
window.blit(intro,(250,400))
pygame.display.update()
lvl = 0
while True:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_e:
                lvl = 1
                break
            if event.key == pygame.K_m:
                lvl = 3
                break
            if event.key == pygame.K_i:
                lvl = 5
                break
        if event.type == gameGlobals.QUIT:
            pygame.quit()
            sys.exit()
    if lvl != 0:
        break
class paddle():
    def __init__(self,x=0,y=400):
        self.x = x
        self.y = y
    def move(self,change,speed):
        self.change = change
        self.speed = speed
        if self.change == "up":
            if self.y > 0:
                self.y-= speed
        elif self.change == "down":
            if self.y < 700:
                self.y += speed
        self.rect = pygame.draw.rect(window,white,(self.x,self.y,20,100))
    def update(self):
        self.rect = pygame.draw.rect(window,white,(self.x,self.y,20,100))
class ball():
    def __init__(self,x= 500,y =400,changex = 5,changey =5):
        self.x =x
        self.y =y
        self.changey = changey
        self.changex = changex
    def update(self):
        self.x += self.changex
        if self.y <= 20 or self.y >= 780:
            self.changey = -self.changey
        self.y += self.changey
        self.rect = pygame.draw.circle(window,white,(self.x,self.y), 20)
    def bounce(self,obj):
        self.obj = obj
        if self.y >= self.obj and self.y <= (self.obj + 100):
            self.changex =-self.changex
            self.x += self.changex
class score():
    def __init__(self,lscore = 0, rscore =0 ,myfont = pygame.font.SysFont("Comic Sans MS",24)):
        self.lscore = lscore
        self.rscore = rscore
        self.myfont = myfont
    def update(self):
        textSurface = (self.myfont).render(str(self.lscore),False,white)
        r = (self.myfont).render(str(self.rscore),False,white)
        window.blit(textSurface,(30,20))
        window.blit(r,(960,20))
    def gameOver(self):
        g = (self.myfont).render("Game over. Press r to play again",False,white)
        window.blit(g,(300,400))

#class speed():
    #def __init__(self,x,y):
l = paddle()
r = paddle(980,400)
b = ball()
s = score()
while True:
    if s.lscore == 10 or s.rscore == 10:
        s.gameOver()
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    s = score(0,0,s.myfont)
        if event.type == gameGlobals.QUIT:
            pygame.quit()
            sys.exit()
    else:
        clock.tick(60)
        window.fill(black)
        l.update()
        r.update()
        b.update()
        s.update()
        if b.x >= 970 and b.x <= 990:
            b.bounce(r.y)
        if b.x <= 30 and b.x >= 10:
            b.bounce(l.y)
        if b.x == 1020:
            s.lscore += 1
            b.x = 500
            b.y = 400
            pygame.time.wait(1000)
            b.update()
        if b.x == -20:
            s.rscore += 1
            b.x = 500
            b.y = 400
            pygame.time.wait(1000)
            b.update()

        #b.bounce()
        
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            r.move("up",5)
        if keys[pygame.K_DOWN]:
            r.move("down",5)
        #if keys[pygame.K_w]:
        if (l.y + 10) > b.y:
            l.move("up",lvl)
        #if keys[pygame.K_s]:
        if (l.y + 10) < b.y:
            l.move("down",lvl)
        if s.lscore == 10 or s.rscore == 10:
            s.gameOver()
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                if s.lscore == 10 or s.rscore == 10:
                    s = score(0,0,s.myfont)
        if event.type == gameGlobals.QUIT:
            pygame.quit()
            sys.exit()