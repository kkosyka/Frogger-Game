# final3.py
# kalynn kosyka
# frogger game
# Goal: get the frog to the water without getting hit by any automobiles
# move the frog up and down: up - the water, down - the grass

WIDTH = 800
HEIGHT = 600
frogImg = "Frog3.gif"

#################################################################################################
#
#                                  LIBRARIES
#
#################################################################################################

from graphics import *
from random import*

#################################################################################################
#
#                                  CLASSES
#
#################################################################################################

class Banner:
     def __init__(self, message):
          # Creates a message at the top of the graphics window
          self.text = Text(Point(WIDTH//2, 50), message)
          self.text.setFill("white")
          self.text.setTextColor("white")
          self.text.setSize(20)
        
     def draw(self, win):
          #draws the text of the banner on the graphics window
          self.text.draw(win)
          self.win = win
        
     def setText(self, newMessage):
          #change the text of the banner
          self.text.setText(newMessage)
          
     def endText(self, newMessage):
          x = self.text.getAnchor()
          self.text.setText(newMessage)
          self.text.setSize(30)
          self.text.move(0, 250)
          
class Region:
     #Implements a button, which contains a label (text),
     #is rectangular (frame), and can be clicked (True) or not clicked
     def __init__(self, x1, y1):
          p1 = Point(x1, y1)
          p2 = Point(WIDTH + 10, (y1 + WIDTH *(1/4)))
          self.frame = Rectangle(p1, p2)
          self.frame.setFill("")
          self.frame.setOutline("")
          self.clicked = False
        
     def draw(self, win):
          #display region on window, but region will be invisible, like an invisible button
          self.frame.draw( win )

     def isClicked(self, p):
          #Checks if p is inside the frame of the button.  Returns True
          #if p inside frame, False otherwise.  If p inside, button
          #changes state and color
          x1, y1 = self.frame.getP1().getX(), self.frame.getP1().getY()
          x2, y2 = self.frame.getP2().getX(), self.frame.getP2().getY()

          if x1 <= p.getX() <= x2 and y1 <= p.getY() <= y2:
               self.clicked = not self.clicked
               return True
          else:
               return False

class AlienCar:
     def __init__(self, refPoint):        
          x1 = refPoint.getX()
          y1 = refPoint.getY()
          x2 = x1 + 100
          y2 = y1 + 50

          self.body = Oval(Point(x1,y1), Point(x2,y2))
          self.top = Oval(Point(x1 + 15,y1-10), Point(x2-15,y2-20))
          self.w1 = Wheel(Point(x1 + 5, y1 + 25), 13)
          self.w2 = Wheel(Point(x2 - 40, y1 + 25), 13)

          r1 = randint(0, 255)
          g1 = randint(0, 255)
          b1 = randint(0, 255)
          r2 = randint(0, 255)
          g2 = randint(0, 255)
          b2 = randint(0, 255)
          
          self.body.setFill(color_rgb(r1, g1, b1))
          self.top.setFill(color_rgb(r2, g2, b2))

     def body(self):
          return self.body
     
     def draw(self, win):
          self.body.draw(win)
          self.top.draw(win)
          self.w1.draw(win)
          self.w2.draw(win)

     def move( self, dx, dy ):
          #move the automobile on its own, and if the car happens to go beyond the screen
          #will move the car at the opposite end of the screen     
          self.body.move(dx, dy)
          self.top.move(dx,dy)
          self.w1.move(dx, dy)
          self.w2.move(dx, dy)

          # if car happens to disappear..
          x = self.body.getP1()
          x = x.getX()
          if x > WIDTH + 50:
               self.body.move(-WIDTH-50, 0)
               self.top.move(-WIDTH-50, 0)
               self.w1.move(-WIDTH-50, 0)
               self.w2.move(-WIDTH-50, 0)              
               
class reverseAlienCar(AlienCar):
     def __init__(self, refPoint):
          super().__init__(refPoint)

     def move(self, dx, dy):
          #move the automobile on its own, and if the car happens to go beyond the screen
          #will move the car at the opposite end of the screen     
          super().move(dx, dy)

          # if car happens to disappear
          x = super().body().getP1()
          x = x.getX()
          if x < 0 - 50:
               super().move(WIDTH+50, 0)
     
class Cars:
     def __init__(self, refPoint):         
          x1 = refPoint.getX()
          y1 = refPoint.getY()
          x2 = x1 + 100
          y2 = y1 + 50

          self.body = Rectangle(Point(x1,y1), Point(x2,y2))
          self.w1 = Wheel(Point(x1 + 5, y1 + 25), 13)
          self.w2 = Wheel(Point(x2 - 40, y1 + 25), 13)

          r1 = randint(0, 255)
          g1 = randint(0, 255)
          b1 = randint(0, 255)
          
          self.body.setFill(color_rgb(r1, g1, b1))

     def draw(self, win):
          self.body.draw(win)
          self.w1.draw(win)
          self.w2.draw(win)

     def body(self):
          return self.body

     def move(self, dx, dy):
          #move the automobile on its own, and if the car happens to go beyond the screen
          #will move the car at the opposite end of the screen     
          self.body.move(dx, dy)
          self.w1.move(dx, dy)
          self.w2.move(dx, dy)

          # if car happens to disappear
          x = self.body.getP1()
          x = x.getX()
          if x > WIDTH + 50:
               self.body.move(-WIDTH-50, 0)
               self.w1.move(-WIDTH-50, 0)
               self.w2.move(-WIDTH-50, 0)

class reverseCars(Cars):
     def __init__(self, refPoint):
          super().__init__(refPoint)

     def move(self, dx, dy):
          #move the automobile on its own, and if the car happens to go beyond the screen
          #will move the car at the opposite end of the screen     
          super().move(dx, dy)

          # if car happens to disappear
          x = super().body().getP1()
          x = x.getX()
          if x < 0 - 50:
               super().move(WIDTH+50, 0)

class Truck (Cars):
     def __init__(self, refPoint):
          super().__init__(refPoint)
          x = refPoint.getX()
          y = refPoint.getY()
          self.front = Polygon(Point(x+100,y+50), Point(x+150,y+50), Point(x+150,y+30),
                               Point(x+125,y+30), Point(x+100,y))
          r1 = randint(0, 255)
          g1 = randint(0, 255)
          b1 = randint(0, 255)
          
          self.front.setFill(color_rgb(r1, g1, b1))
          
          #extra wheel for the truck
          self.extraWheel = Circle(Point(x+115,y+50), 13)
          self.extraWheelInside = Circle(Point(x +115,y+50), 6.5)
          
     def draw(self, win):
          super().draw(win)
          self.front.draw(win)
          self.extraWheel.draw(win)
          self.extraWheel.setFill("black")
          self.extraWheelInside.draw(win)
          self.extraWheelInside.setFill("white")

     def move(self, dx, dy):
          #move the automobile on its own, and if the car happens to go beyond the screen
          #will move the car at the opposite end of the screen     
          super().move(dx, dy)
          self.front.move(dx,dy)
          self.extraWheel.move(dx, dy)
          self.extraWheelInside.move(dx, dy)

          # if car happens to disappear
          x = self.body.getP1()
          x = x.getX()
          if x > WIDTH:
               super().move(-WIDTH-50, 0)
               self.front.move(-WIDTH-50, 0)
               self.extraWheel.move(-WIDTH-50, 0)
               self.extraWheelInside.move(-WIDTH-50, 0)

class reverseTruck (Cars): 
     def __init__(self, refPoint):
          super().__init__(refPoint)
          x = refPoint.getX()
          y = refPoint.getY()
          self.front = Polygon(Point(x,y+50), Point(x-40,y+50), Point(x-32,y+30),
                               Point(x-16,y+30), Point(x,y))
          r1 = randint(0, 255)
          g1 = randint(0, 255)
          b1 = randint(0, 255)
          
          self.front.setFill(color_rgb(r1, g1, b1))
          
          #extra wheel for the truck
          self.extraWheel = Circle(Point(x-12,y+50), 13)
          self.extraWheelInside = Circle(Point(x - 12,y+50), 6.5)

     def draw(self, win):
          super().draw(win)
          self.front.draw(win)
          self.extraWheel.draw(win)
          self.extraWheel.setFill("black")
          self.extraWheelInside.draw(win)
          self.extraWheelInside.setFill("white")

     def move( self, dx, dy ):
          #move the automobile on its own, and if the car happens to go beyond the screen
          #will move the car at the opposite end of the screen     
          super().move(dx, dy)
          self.front.move(dx,dy)
          self.extraWheel.move(dx, dy)
          self.extraWheelInside.move(dx, dy)

          # if car happens to disappear
          x = self.body.getP1()
          x = x.getX()
          if x < 0 - 50:
               super().move(WIDTH+50, 0)
               self.front.move(WIDTH+50, 0)
               self.extraWheel.move(WIDTH+50, 0)
               self.extraWheelInside.move(WIDTH+50, 0)

class Wheel:
     #the wheel fo the car, creates 2 wheels with centers
     def __init__(self, refPoint, radius): 
          x1 = refPoint.getX() + 15
          y1 = refPoint.getY() + 25

          center = Point(x1, y1)
          self.c1 = Circle(center, radius)
          self.c2 = Circle(center, radius/2)
          self.c1.setFill("black")
          self.c2.setFill("white")

     def draw(self, win):
          self.c1.draw(win)
          self.c2.draw(win)

     def move(self, dx, dy):
          self.c1.move(dx, dy)
          self.c2.move(dx, dy)

#################################################################################################
#
#                              FUNCTIONS
#
#################################################################################################

def water(win):
     count = 0
     #creating "waves" to represent blue water
     for y in range(6, -1, -1):
          count += 1
          y = y * 30
          for x in range (0, 16, 1):
               x = x * 60
               if count % 2 == 0:
                    c = Circle(Point(x, y), 30)
                    c.setFill("blue")
                    c.setWidth(3)
                    c.draw(win)
               else:
                    c = Circle(Point(x+30, y), 30)
                    c.setFill("blue")
                    c.setWidth(3)
                    c.draw(win)
          
def grass(win):
     #creating "blades" to represent grass
     TipX = 1
     TipY = HEIGHT*(3/4)-5
     leftX = TipX - 5
     leftY = TipY + 20
     rightX = TipX+5
     rightY = TipY +20

     for x in range(90):
          x = x * 10
          for y in range(11):
               y = y*15
               bladeOfGrass = Polygon(Point(TipX+x, TipY+y), Point(leftX+x, leftY+y), Point(rightX+x, rightY+y))
               bladeOfGrass.setFill("green")
               bladeOfGrass.draw(win)

def stripes(win):
     #creating yellow stripes that divide the road in half
     x1 = 5
     y1 = (HEIGHT // 2) - 15
     x2 = x1 + 50
     y2 = y1 + 25

     for x in range(8):
          x = x * 100
          stripes = Rectangle(Point(x1 + x ,y1), Point(x2 + x ,y2))
          stripes.setFill("yellow")
          stripes.draw(win)

def background(win):
     #create the entire backgroun, including: water, grass, and road
     backgroundWater = Rectangle(Point(0,0), Point(WIDTH+5, HEIGHT * (1/4)))
     backgroundWater.draw(win)
     backgroundWater.setFill("lightblue")

     #water
     water(win)
     
     #road
     x1 = -10
     y1 = HEIGHT * (1/4)
     x2 = WIDTH + 10
     y2 = HEIGHT * (3/4)
     road = Rectangle(Point(x1,y1), Point(x2,y2))
     road.setFill("grey")
     road.setWidth(10)
     road.draw(win)
     stripes(win)
     
     #grass
     backgroundGrass = Rectangle(Point(0,HEIGHT*(3/4)+4), Point(WIDTH+5, HEIGHT+5))
     backgroundGrass.draw(win)
     backgroundGrass.setFill("darkgreen")
     grass(win)

def movingCars(win):
     global frogImg
     
     #displaying the frog image
     xFrog = WIDTH//2
     yFrog = HEIGHT * (3/4) + 25
     frog = Image( Point(xFrog, yFrog), frogImg )
     frog.draw(win)
     
     #create cars on upper half, moving left to right
     car1 = Cars(Point(10, 185))
     car1.draw(win)

     truck1 = Truck(Point(200, 185))    
     truck1.draw(win)

     alienCar1 = AlienCar(Point(550, 185))
     alienCar1.draw(win)

     #create cars on lower half, moving right to left
     car2 = reverseCars(Point(300, 350))
     car2.draw(win)

     truck2 = reverseTruck(Point(600, 350))    
     truck2.draw(win)

     alienCar2 = reverseAlienCar(Point(100, 350))
     alienCar2.draw(win)

     # creating the "invisible buttons"
     upRegion = Region(-10, -50)
     upRegion.draw( win )

     downRegion = Region(-10, HEIGHT * (3/4)-5)
     downRegion.draw( win )

     carList = [car1, truck1, alienCar1]
     revCarList = [car2, truck2, alienCar2]

     continueGame = True
     life = 3
     crossings = 0
     
     # draw the start banner at the top
     banner = Banner("{0:1} lives left, {1:1} crossing(s)".
                     format(life, crossings)) 
     banner.draw(win)         

     #to get the game moving
     while True and continueGame == True:
          clickedPoint = win.checkMouse()

          #if up or down is clicked, the frog either moves up or down
          if clickedPoint != None and upRegion.isClicked( clickedPoint ):
               frog.move(0,-30)
        
          if clickedPoint != None and downRegion.isClicked( clickedPoint ):
               frog.move(0, 30)

          #getting the automobiles to move
          for auto, revAuto in zip(carList, revCarList):
               auto.move(10, 0)
               revAuto.move(-10,0)

          frogXCoor = frog.getAnchor().getX()
          frogYCoor = frog.getAnchor().getY()

          #automobiles with their X & Y
          car1XP1 = car1.body.getP1().getX() - 15
          car1YP1 = car1.body.getP1().getY() - 20
          car1XP2 = car1XP1 + 100 + 25
          car1YP2 = car1YP1 + 63 + 50
          
          truck1XP1 = truck1.body.getP1().getX() - 15
          truck1YP1 = truck1.body.getP1().getY() - 20
          truck1XP2 = truck1XP1 + 150 + 25
          truck1YP2 = truck1YP1 + 63 + 50

          alienCar1XP1 = alienCar1.body.getP1().getX() - 9
          alienCar1YP1 = alienCar1.body.getP1().getY() - 10
          alienCar1XP2 = alienCar1XP1 + 100 + 15
          alienCar1YP2 = alienCar1YP1 + 83 + 25

          car2XP1 = car2.body.getP1().getX() - 15
          car2YP1 = car2.body.getP1().getY() - 15
          car2XP2 = car2XP1 + 100 + 15
          car2YP2 = car2YP1 + 63 + 50

          truck2XP1 = truck2.body.getP1().getX() - 45
          truck2YP1 = truck2.body.getP1().getY() - 15
          truck2XP2 = truck2XP1 + 140 + 15
          truck2YP2 = truck2YP1 + 63 + 60
          
          alienCar2XP1 = alienCar2.body.getP1().getX() - 25
          alienCar2YP1 = alienCar2.body.getP1().getY()
          alienCar2XP2 = alienCar2XP1 + 155 
          alienCar2YP2 = alienCar2YP1 + 83 + 15
          
          #if frog gets into water, then crossing point is gained
          if 0 < frogYCoor < 115:
               crossings += 1
               frog.move(0, yFrog-frogYCoor)

          #if frog gets hit but one of the cars, the frog will lose a life
          if car1XP1<frogXCoor<car1XP2 and car1YP1<frogYCoor<car1YP2:
               frog.move(0, yFrog-frogYCoor)
               life -= 1

          if truck1XP1<frogXCoor<truck1XP2 and truck1YP1<frogYCoor<truck1YP2:
               frog.move(0, yFrog-frogYCoor)
               life -= 1
 
          if alienCar1XP1<frogXCoor<alienCar1XP2 and alienCar1YP1<frogYCoor<alienCar1YP2:
               frog.move(0, yFrog-frogYCoor)
               life -= 1

          if car2XP1<frogXCoor<car2XP2 and car2YP1<frogYCoor<car2YP2:
               frog.move(0, yFrog-frogYCoor)
               life -= 1

          if truck2XP1<frogXCoor<truck2XP2 and truck2YP1<frogYCoor<truck2YP2:
               frog.move(0, yFrog-frogYCoor)
               life -= 1

          if alienCar2XP1<frogXCoor<alienCar2XP2 and alienCar2YP1<frogYCoor<alienCar2YP2:
               frog.move(0, yFrog-frogYCoor)
               life -= 1

          banner.setText("{0:1} lives left, {1:1} crossing(s)".
                format(life, crossings))

          #at the end of the game, when frog has 0 lives, states how many crossings have been achieved
          if life <= 0:
               continueGame = False
               banner.setText("")
               frog.move(0, yFrog-frogYCoor)
               #to create a statement polygon with the final results
               poly = Polygon(Point(376, 62), Point(422, 139), Point(563, 95), Point(568, 164), Point(729, 157), Point(704, 234),
                              Point(733, 301), Point(684, 344), Point(722, 421), Point(596, 411), Point(582, 504), Point(467, 444),
                              Point(416, 517), Point(318, 407), Point(244, 483), Point(203, 401), Point(92, 450), Point(154, 345),
                              Point(44, 265), Point(159, 254), Point(78, 143), Point(186, 152))
               poly.draw(win)
               poly.setFill("red")
               #new banner with the results of the game
               banner1 = Banner("Game OVER \n Froggy crossed {0:1} time(s) \n (click window to close)".
                     format(crossings))
               banner1.draw(win)
               banner1.endText("Game OVER \n Froggy crossed {0:1} time(s) \n \n (click window to close)".
                     format(crossings))

               return #to end the game (closing the window)

#################################################################################################
#
#                                  MAIN
#
#################################################################################################

def main():
     # creates a window
     win = GraphWin( "KOSYKA - Frogger Game", WIDTH, HEIGHT )
                               
     #create and play the game
     background(win)
     movingCars(win)
                               
     #close game when game is over
     win.getMouse()
     win.close()

main()
