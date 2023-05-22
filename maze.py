import turtle
import math

wn = turtle.Screen()
# wn.bgcolor("black")
wn.bgpic("bg.gif")
wn.title("Maze")
wn.setup(700,700)
#register shapes
# turtle.register_shape("omar1.gif")
turtle.register_shape("omar1.gif")
turtle.register_shape("ball.gif")
# turtle.register_shape("treasure.gif")
turtle.register_shape("wall.gif")

#create pen
class Pen(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("white")
        self.penup()
        self.speed(0)

class Player(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("omar1.gif")
        # self.color("blue")
        self.penup()
        self.speed(0)
        self.gold=0

    def go_up(self):
        move_to_x=player.xcor()
        move_to_y=player.ycor()+24

        # self.goto(self.xcor(),self.ycor()+24)
        if(move_to_x,move_to_y) not in walls:
            self.goto(move_to_x,move_to_y)
            
    def go_down(self):
        move_to_x=player.xcor()
        move_to_y=player.ycor()-24        
        if(move_to_x,move_to_y) not in walls:
            self.goto(move_to_x,move_to_y)
        # self.goto(self.xcor(),self.ycor()-24)
        
    def go_right(self):
        move_to_x=player.xcor()+24
        move_to_y=player.ycor()
        self.shape("omar1.gif")

        if(move_to_x,move_to_y) not in walls:
            self.goto(move_to_x,move_to_y)
        # self.goto(self.xcor()+24,self.ycor())
        
    def go_left(self):
        move_to_x=player.xcor()-24
        move_to_y=player.ycor()
        self.shape("omar1.gif")
        if(move_to_x,move_to_y) not in walls:
            self.goto(move_to_x,move_to_y)
        # self.goto(self.xcor()-24,self.ycor())
        
    def is_collision(self,other):
        a=self.xcor()-other.xcor()
        b=self.ycor()-other.ycor()
        distance=math.sqrt((a**2)+(b**2))

        if distance <5:
            return True
        else:
            return False

class Treasure(turtle.Turtle):
    def __init__(self,x,y):
        turtle.Turtle.__init__(self)
        self.shape("ball.gif")
        self.color("gold")
        self.penup()
        self.speed(0)
        self.gold=100
        self.goto(x,y)
    def destroy(self):
        self.goto(2000,2000)
        self.hideturtle

#create levels list
levels=[""]

#define first level
level_1=[
"XXXXXXXXXXXXXXXXXXXXXXXXX",
"XPX    XXX          XX  X",
"X X XXXXXX  XXXXXX  XXX X",
"X   XXX XX  XXXX    XX  X",
"XX      XX  XXXXXXX    XX",
"XXXXXX XXX   XX     XXXXX",
"XXXXXX XXX X XXXXX  XXXXX",
"XXXXXX  XX    XXXX  XXXXX",
"X   XXX    XXXXXXX    XXX",
"X  XXX  XXXXXXXXXXXXX XXX",
"X  XX X   XXXXXXXXX   XXX",
"X                X  XXXXX",
"XXXXXXXXXXXX     X XXX  X",
"XX   XXXXXXXXXX XXXXXX  X",
"XX X XXXXXXXXXX  XXXX  XX",
"XXXX XXX         X      X",
"XXXX        XXXXXXXXXXXXX",
"XXXXXXXXXX XXXXXXXX     X",
"XXXXXXXXXX  X XXXXXXXXX X",
"XX   XX  X              X",
"XX  XXXX XXXXXXXXX  XXX X",
"XX    XX XXXXX      X   X",
"X XXX       XX XXXXXXXXXX",
"X      XXX             TX",
"XXXXXXXXXXXXXXXXXXXXXXXXX"]



level_0=[
"XXXXXXXXXXXXXXXXXXXXXXXXX",
"XXXXXXXXXXXXXXXXXXXXXXXXX",
"XXXXXXXXXXXXXXXXXXXXXXXXX",
"XXXXXXXXXXXXXXXXXXXXXXXXX",
"XXXXXXXXXXXXXXXXXXXXXXXXX",
"XXXXXXXXXXXXXXXXXXXXXXXXX",
"XXXXXXXXXXXXXXXXXXXXXXXXX",
"XXXXXXXXXXXXXXXXXXXXXXXXX",
"XXXXXXXXXXXXXXXXXXXXXXXXX",
"XXXXXXXXXXXXXXXXXXXXXXXXX",
"XXXXXXXXXXXXXXXXXXXXXXXXX",
"XXXXXXXXXXXXXXXXXXXXXXXXX",
"XXXXXXXXXXXXXXXXXXXXXXXXX",
"XXXXXXXXXXXXXXXXXXXXXXXXX",
"XXXXXXXXXXXXXXXXXXXXXXXXX",
"XXXXXXXXXXXXXXXXXXXXXXXXX",
"XXXXXXXXXXXXXXXXXXXXXXXXX",
"XXXXXXXXXXXXXXXXXXXXXXXXX",
"XXXXXXXXXXXXXXXXXXXXXXXXX",
"XXXXXXXXXXXXXXXXXXXXXXXXX",
"XXXXXXXXXXXXXXXXXXXXXXXXX",
"XXXXXXXXXXXXXXXXXXXXXXXXX",
"XXXXXXXXXXXXXXXXXXXXXXXXX",
"XXXXXXXXXXXXXXXXXXXXXXXXX",
"XXXXXXXXXXXXXXXXXXXXXXXXX"]
#add treasure list
treasures=[]

#add maze to maze list
levels.append(level_1)
levels.append(level_0)


#create level setup function
def setup_maze(level):
    for y in range(len(level)):
        for x in range(len(level[y])):
            character =level[x][y]
            screen_x=-288 +(x*24)
            screen_y=288-(y*24)
            if character=="X":
                pen.goto(screen_x,screen_y)
                pen.shape("wall.gif")
                pen.stamp()
                #add coordinates to wall list
                walls.append((screen_x,screen_y))
            if character=="P":
                player.goto(screen_x,screen_y)
            if character=="T":
                treasures.append(Treasure(screen_x,screen_y))
#creae instances
pen=Pen()
player=Player()

#create wall coordinate list
walls=[]

setup_maze(levels[1])


#ketboard binding
turtle.listen()
turtle.onkey(player.go_right,"Right")
turtle.onkey(player.go_left,"Left")
turtle.onkey(player.go_up,"Up")
turtle.onkey(player.go_down,"Down")
#turn off screen updates
wn.tracer()

#main game loop
while True:
    #check for player collision with treasure
    for treasure in treasures:
        if player.is_collision(treasure):
            player.gold+=treasure.gold
            print ("Player Gold: {}".format(player.gold))
            treasure.destroy()
            setup_maze(levels[2])
            #wn.title("Winner Winner Chicken Dinner")
            treasures.remove(treasure)
    
    wn.update()
