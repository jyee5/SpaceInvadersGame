'''
spaceInvaders.py
This class and file has everything to do with the player
If you moving the player left, right or firing, it is in this class
If you win the level, it is in this class, or if u get hit by the enemy, it is in this class
Wining and losing title screen in this class as well, as the player can only win or lose
'''
import turtle
import time

class gamePlayer(): #This class creates the player and other objects related to the player, so the movement,
    #winning/losing, and alsothe firing component.    
    def __init__(self, player, playerspeed, laser, firing): #constructor
        self.playerspeed = playerspeed
        self.player = player
        self.laser = laser
        self.firing = firing
    def playerCreator(self): # creates the player that moves back and forth to fire at the enemy
        self.player = turtle.Turtle()
        self.player.color("blue")
        self.player.shape("triangle")
        self.player.penup()
        self.player.speed(0)
        self.player.setposition(0,-250)
        self.player.setheading(90)
    def move_left(self): # method called when left arrow key is hit
        x = self.player.xcor()
        x = x - self.playerspeed
        if x < -280:
            x = -280
        self.player.setx(x)
    def move_right(self): # method called when right arrow key is hit
        x = self.player.xcor()
        x = x + self.playerspeed
        if x > 280:
            x = 280
        self.player.setx(x)

    def laserCreator(self): # method called when space bar is hit
        self.laser = turtle.Turtle()
        self.laser.hideturtle()
        self.laser.color("White")
        self.laser.shape("circle")
        self.laser.penup()
        self.laser.speed(0)
        self.laser.setheading(90)
        self.laser.shapesize(0.5,0.5)
        self.laser.setposition(self.player.xcor(),-250 + 15)
    def laserStarting(self): #puts the laser at the certain spot where the player is
        if self.firing == True:
            self.laser.setposition(self.player.xcor(),-250 + 15)
            self.laser.showturtle()
            self.firing = False
    def shoot(self): # moves the laser up the screen
        y = self.laser.ycor()
        y += 40
        self.laser.sety(y)
    def firing(self):# allows the player to fire again when the first laser is gone
        self.firing == True
    def loser(self): #displays you have lost, on the screen
        lost = turtle.Turtle()
        lost.hideturtle()
        lost.color("white")
        lost.write("You Lost", align = "center",font =("Ariel", 32, "normal"))
    def win(self, level): # displays you won and continues to the next level
        win = turtle.Turtle()
        win.hideturtle()
        win.color("white")
        win.write("You Won... Level " + str(level) + " Complete", align = "center",font =("Ariel", 32, "normal"))
        time.sleep(1)
        win.clear()
        win.write("Next Level...", align = "center", font=("Ariel", 32, "normal"))
        turtle.listen()
        time.sleep(1)
        win.clear()
    def clearing(self): # clears the screen for the next level.  
        self.laser.hideturtle()
        self.player.hideturtle()

        

