'''
spaceInvadersBoard.py
This starts the screen to where all the other objects will be placed
It also will draw a border for us, so it looks like a real 80's style game
Creates the background color to make it look like space
Should also have stars, which are moving, but we had trouble with that part of incorporating the code, so we decided not to incorporate it
'''

import turtle
class gameStarting():#Class creates all of the turtle screen and the border for the game
    def __init__(self):
        pass
    def gamebox(self):#Turtle screen creation
        game = turtle.Screen()
        game.bgcolor("black")
        game.title ("Space Invaders")
    def gameborder(self): # Game border creation
        self.border = turtle.Turtle()
        self.border.speed(0)
        self.border.color("White")
        self.border.penup()
        self.border.setposition(-300,-300)
        self.border.pendown()
        self.border.pensize(3)
        for side in range(4):
            self.border.fd(600)
            self.border.lt(90)
        self.border.hideturtle()
    def titleScreen(self): #Makes the title screen
        self.title = turtle.Turtle()
        self.title.hideturtle()
        self.title.penup()
        self.title.color("white")
        self.title.goto(-100,100)
        self.title.write("Space Invaders", font=("Ariel", 32, "normal"))
        self.title.goto(-150,0)
        self.title.write("Click anywhere to start", font = ("Ariel", 32, "normal"))
    def titleClear(self): #Clears the title screen
        self.title.clear()
        

        
