import random
class spaceship():
    def __init__(self,name="Rocketman",location= 0,fuel = 100):
        self.name = name
        self.location = location
        self.fuel = fuel
    def fly(self,location,fuel):
        self.fuel = self.fuel - 1
        self.location = self.location + 10000000
    def __str__(self):
        return "The spaceship %s is %s km from earth and has %s percent of its fuel left" % (self.name, self.location,self.fuel)
class warboi(spaceship):
    def __init__(self,name="Rocketman2",location = 0 ,fuel = 100,warp1 = 5):
        spaceship.__init__(self,name,location,fuel)
        self.warp1 = warp1
    def warp(self,location,fuel,warp1):
        if warp1 > 0:
            self.warp1 = self.warp1 - 1
            jump = random.randint(1,60000000)
            self.location = self.location + jump
            self.fuel = self.fuel - 3
    def __str__(self):
        return "The spaceship %s is %s km from earth and has %s percent of its fuel left. %s warp(s) remaining" % (self.name, self.location,self.fuel,self.warp1)
a = spaceship()
b = warboi()
while a.location < 628743036:
    a.fly(a.location,a.fuel)
    print(a)
for x in range(5):
    b.warp(b.location,b.fuel,b.warp1)
    print(b)
while b.location < 628743036:
    b.fly(b.location,b.fuel)
    print(b)