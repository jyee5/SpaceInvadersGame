'''
spaceInvaders.py
Setting up the screen of space invaders.
This is the main file for running the Space Invaders Game
It will call the rest of the files and functions, to run cohertly
'''


import turtle
from spaceInvadersBoard import gameStarting#Allows you to import classes from a certain file
from spaceInvadersEnemy import gameEnemy#Allows you to import classes from a certain file
from spaceInvadersPlayer import gamePlayer#Allows you to import classes from a certain file

def creatingGame():#Allows you to create the turtle screen and the border for the game
    starting = gameStarting()
    starting.gamebox()
    starting.gameborder()
    starting.titleScreen()
    def clicked(x,y):
        turtle.onscreenclick(None)
        starting.titleClear()
        playingGame(10,0)
    turtle.onscreenclick(clicked) #If clicked on screen, it will run the clicked() function
    turtle.mainloop() #keeps turtle screen running

def playingGame(speed, level):#This function runs all of the other classes and functions that is necessary to play the game
    #This Function also has a infinte loop that keeps running until someone wins or loses
    player1 = gamePlayer(0,15,0, True)
    player1.playerCreator()
    enemy = gameEnemy(0,speed, -150, 250, 0,0)
    enemy.enemyCreator()
    enemy.enemyMovement()
    enemy.enemyLaserCreator()
    enemy1 = gameEnemy(0,speed, -180, 250,0,0)
    enemy1.enemyCreator()
    enemy1.enemyMovement()
    enemy1.enemyLaserCreator()
    enemy2 = gameEnemy(0,speed, -210, 250,0,0)
    enemy2.enemyCreator()
    enemy2.enemyMovement()
    enemy2.enemyLaserCreator()
    enemy3 = gameEnemy(0,speed, -240, 250,0,0)
    enemy3.enemyCreator()
    enemy3.enemyMovement()
    enemy3.enemyLaserCreator()
    enemy4 = gameEnemy(0,speed, -270, 250,0,0)
    enemy4.enemyCreator()
    enemy4.enemyMovement()
    enemy4.enemyLaserCreator()
    player1.laserCreator()
    turtle.listen()
    turtle.onkey(player1.move_left, "Left")
    turtle.onkey(player1.move_right, "Right")
    turtle.onkey(player1.laserStarting, "space")
    destroyed = False
    destroyed1 = False
    destroyed2 = False
    destroyed3 = False
    destroyed4 = False
    counter = 0
    while True:#allows the game to run all the time
        player1.shoot()
        enemy3.enemyFiring(speed)
        if player1.laser.ycor() > 280:
            player1.firing = True
        enemy.enemyMovement()
        enemy1.enemyMovement()
        enemy2.enemyMovement()
        enemy3.enemyMovement()
        enemy4.enemyMovement()
        if counter > 150 - speed:
            enemy3.newLaser()
            counter = 0
        if enemy.enemy.ycor() <= player1.player.ycor():
            break
        if (player1.laser.xcor() >= enemy1.enemy.xcor() - 15 and player1.laser.xcor()<= enemy1.enemy.xcor() + 15) and (player1.laser.ycor() >= enemy1.enemy.ycor() - 15 and player1.laser.ycor()<= enemy1.enemy.ycor() + 15):
            destroyed = enemy1.destroyedEnemy()
        if (player1.laser.xcor() >= enemy2.enemy.xcor() - 15 and player1.laser.xcor()<= enemy2.enemy.xcor() + 15) and (player1.laser.ycor() >= enemy2.enemy.ycor() - 15 and player1.laser.ycor()<= enemy2.enemy.ycor() + 15):
            destroyed1 = enemy2.destroyedEnemy()
        if (player1.laser.xcor() >= enemy3.enemy.xcor() - 15 and player1.laser.xcor()<= enemy3.enemy.xcor() + 15) and (player1.laser.ycor() >= enemy3.enemy.ycor() - 15 and player1.laser.ycor()<= enemy3.enemy.ycor() + 15):
            destroyed2 = enemy3.destroyedEnemy()
        if (player1.laser.xcor() >= enemy4.enemy.xcor() - 15 and player1.laser.xcor()<= enemy4.enemy.xcor() + 15) and (player1.laser.ycor() >= enemy4.enemy.ycor() - 15 and player1.laser.ycor()<= enemy4.enemy.ycor() + 15):
            destroyed3 = enemy4.destroyedEnemy()
        if (player1.laser.xcor() >= enemy.enemy.xcor() - 15 and player1.laser.xcor()<= enemy.enemy.xcor() + 15) and (player1.laser.ycor() >= enemy.enemy.ycor() - 15 and player1.laser.ycor()<= enemy.enemy.ycor() + 15):
            destroyed4 = enemy.destroyedEnemy()
        if destroyed and destroyed1 and destroyed2 and destroyed3 and destroyed4:
            break
        if (enemy3.enemyLaser.xcor() >= player1.player.xcor() - 20 and enemy3.enemyLaser.xcor() <= player1.player.xcor() + 20) and (enemy3.enemyLaser.ycor()  >= player1.player.ycor()-20 and enemy3.enemyLaser.ycor() <= player1.player.ycor()+20):
            break
        counter += 5
    if destroyed and destroyed1 and destroyed2 and destroyed3 and destroyed4:
        level = level + 1
        player1.win(level)
        player1.clearing()
        enemy3.clearing()
        playingGame(speed + 5, level)
    else:
        player1.loser()
    delay = input("Enter to end")
def main(): #Starts everything
    creatingGame()#Runs creating game function
    
main()
