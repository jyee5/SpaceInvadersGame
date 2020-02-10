'''
spaceInvadersEnemy.py
This class and file has everything to do with the enemy.
It includes the side to side movement of the enemy
Includes the enemy firing back, and includes the enemy getting destoryed
'''

import turtle

class gameEnemy():#Enemy class contains everything related to the enemy, like the enemies itself, the movement left
    #to right, and the firing down on the player.  
    def __init__(self, enemy, enemyspeed, positionX, positionY, enemyLaserSpeed, enemyLaser): #Constructor
        self.enemy = enemy
        self.enemyspeed = enemyspeed
        self.positionX = positionX
        self.positionY = positionY
        self.enemyLaserSpeed = enemyLaserSpeed
        self.enemyLaser = enemyLaser
    def enemyCreator(self): #Creates different enemies on the screen in a row, which are the targets
        self.enemy = turtle.Turtle()
        self.enemy.color("red")
        self.enemy.shape("square")
        self.enemy.setheading(45)
        self.enemy.penup()
        self.enemy.speed(0)
        self.enemy.setposition(self.positionX,self.positionY)
    def enemyMovement(self): #Moves the enemy to the right and back to the left if all the way to the right and moves down each time it hits side
        location = self.enemy.xcor()
        ylocation = self.enemy.ycor()
        location = location + self.enemyspeed
        if location > 280 or location < -280:
            self.enemyspeed = self.enemyspeed * -1
            ylocation = ylocation - 15
        self.enemy.sety(ylocation)
        self.enemy.setx(location)
    def destroyedEnemy(self): #destroys enemy
        self.enemy.hideturtle()
        return True
    def enemyLaserCreator(self): # creates a laser and can only fire once the laser is finished firing, to make it more difficult
        self.enemyLaser = turtle.Turtle()
        self.enemyLaser.color("Red")
        self.enemyLaser.shape("circle")
        self.enemyLaser.penup()
        self.enemyLaser.speed(0)
        self.enemyLaser.shapesize(0.5,0.5)
        self.enemyLaser.setposition(self.enemy.xcor(),self.enemy.ycor())
        self.enemyLaser.hideturtle()
    def enemyFiring(self,speed): #moves the laser down to try to hit the player
        laserY = self.enemyLaser.ycor()
        laserY -= 2*speed
        self.enemyLaser.sety(laserY)
    def newLaser(self): #creates new laser at the location of the enemy to fire back
        self.enemyLaser.setposition(self.enemy.xcor(),self.enemy.ycor())
        self.enemyLaser.showturtle()
    def clearing(self): #clears board, for new level
        self.enemyLaser.hideturtle()
        

        
        
        

