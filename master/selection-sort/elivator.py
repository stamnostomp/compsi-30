class elevator():
 def __init__(self,currentFloor = 1,inServiceMode = False):
   self.currentFloor = currentFloor
   self.inServiceMode = inServiceMode
 def goToFloor(self,floor = 1):
      self.floor = floor
      if self.inServiceMode == False:
          return "The elevator has moved to floor %s" % (str(floor))
      else:
          return "SERVICE MODE"
 def toString(self):
      return "The Elevator is on floor %s" % (str(self.currentFloor))
class smart(elevator):
    def __init__(self,currentFloor = 1,inServiceMode = False):
        self. currentFloor = currentFloor
        self.inServiceMode = inServiceMode

    def goToFloor(self,currenFloor,floor):
        self.floor = floor
        somethin = ""
        if self.inServiceMode == False:
            if int(self.currentFloor) > int(self.floor):
                self.currentFloor = int(self.currentFloor) - 1
                for x in range (self.currentFloor - int(self.floor)):
                    self.currentFloor = int(self.currentFloor) - 1
                    somethin = somethin + str(self.currentFloor + 1)
                    somethin = somethin + ", "
                somethin = somethin + self.floor + "."
            elif int(self.currentFloor) < int(self.floor):
                self.currentFloor = self.currentFloor + 1
                for x in range (int(self.floor) - self.currentFloor):
                    self.currentFloor = self.currentFloor + 1
                    somethin = somethin + str(self.currentFloor - 1)
                    somethin = somethin + ", "
                somethin = somethin + self.floor + "."
            else:
                somethin = "nope"
            self.currentFloor = floor
            return somethin
        else:
            return "SERVICE MODE"
somethin = ""
min = 1
max = 20
while True:
    min = input("What is the lowest level the elevator can go to? ")
    max = input("What is the highest level the elevator can go to? ")
    try:
        if int(min) < int(max):
            break
        else:
            print("The min has to be snmaller than the max value")
    except:
        print("Please enter valid numbers")
min = int(min)
max = int(max)
a = elevator()
while True:
    choice = input("What would like to do, you may enter go, service, print or quit(quit will take you to the smart elevator): ")
    if choice.lower() == "print":
        print(a.toString())
    elif choice.lower() == "go":
        while True:
            floor = input("What floor would you like the elevator to go to: ")
            try:
                if int(floor) >= min and int(floor) <= max:
                    break
                else:
                    print("The floor has to be inbetween %s and %s" %(min,max))
            except:
                print("Please enter a valid number")
        a = elevator(floor,a.inServiceMode)
        print(a.goToFloor(floor))
    elif choice.lower() == "service":
        if a.inServiceMode == True:
            inServiceMode = False
            a = elevator(a.currentFloor,inServiceMode)
        else:
            inServiceMode = True
            a = elevator(a.currentFloor,inServiceMode)
    elif choice.lower() == "quit":
        break
b = smart()
print("Smart Elevator")
while True:
    choice = input("What would like to do, you may enter go, service, print or quit: ")
    if choice.lower() == "print":
        print(b.toString())
    elif choice.lower() == "go":
        while True:
            floor = input("What floor would you like the elevator to go to: ")
            try:
                if int(floor) >= min and int(floor) <= max:
                    break
                else:
                    print("The floor has to be inbetween %s and %s" %(min,max))
            except:
                print("Please enter a valid number")
        b = smart(b.currentFloor,a.inServiceMode)
        print(b.goToFloor(b.currentFloor,floor))
    elif choice.lower() == "service":
        if b.inServiceMode == True:
            inServiceMode = False
            b = elevator(b.currentFloor,inServiceMode)
        else:
            inServiceMode = True
            b = elevator(b.currentFloor,inServiceMode)
    elif choice.lower() == "quit":
        break
