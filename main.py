'''
Room 27

Orhan Tasci
William Zhong
Benjamin Li
'''

'''
main.py

This file contains the main functions of the game.
This file displays all the images for the game and holds the player class.
'''

#import modules needed
import pygame
import constants as cn
import levels as lvl
import os
import player as pl

#initialize pygame
pygame.init()
pygame.font.init()
win = pygame.display.set_mode((cn.WIDTH, cn.HEIGHT))
pygame.display.set_caption("Room 27")
clock = pygame.time.Clock()

#function to store the procedures to redraw the game window
def redrawGameWindow():
    win.blit(cn.bg, (0,0))
    if player.gameState == "title":
        lvl.playText.draw(win)
        lvl.titleText.draw(win)

    if player.gameState == "1":
        player.draw(win)
        player.score = int(pygame.time.get_ticks() / 5000)
        scoreText = lvl.Text(20, 20, cn.WHITE, str(player.score), 40)
        scoreText.draw(win)
    pygame.display.update()

#create main player object
player = pl.Player(cn.WIDTH / 2, cn.HEIGHT / 2, 76, 108)

#main loop
run = True
while run:
    #get the clock ticking
    clock.tick(27)

    #if the program is quit, close it (duh)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    #store all teh key presses
    keys = pygame.key.get_pressed()

    if player.gameState != "title" and player.gameState != "win" and player.gameState != "lose":
        #detect arrow key presses and move the player accordingly
        if keys[pygame.K_LEFT] and player.x > player.vel:
            player.x -= player.vel
            player.left = True
            player.right = False
            player.up = False
            player.down = False
            cn.char = cn.standLeft

        elif keys[pygame.K_RIGHT] and player.x < cn.WIDTH - player.width - player.vel:
            player.x += player.vel
            player.right = True
            player.left = False
            player.up = False
            player.down = False
            cn.char = cn.standRight

        elif keys[pygame.K_UP] and player.y > player.vel + 100:
            player.y -= player.vel
            player.left = False
            player.right = False
            player.up = True
            player.down = False
            cn.char = cn.standBack

        elif keys[pygame.K_DOWN] and player.y < cn.HEIGHT - player.height - player.vel:
            player.y += player.vel
            player.right = False
            player.left = False
            player.up = False
            player.down = True
            cn.char = cn.standForward

        #if the player is not moving, reset the walking animation
        else:
            player.right = False
            player.left = False
            player.up = False
            player.down = False
            player.walkCount = 0

    #if X or ESC are pressed, quit the game
    if keys[pygame.K_x] or keys[pygame.K_ESCAPE]:
        pygame.quit()

    if keys[pygame.K_y]:
        player.gameState = "1"

    if player.gameState == "title":
        lvl.titleScreen()

    elif player.gameState == "1":
        lvl.room1()

    elif player.gameState == "2":
        pass

    elif player.gameState == "3":
        pass

    elif player.gameState == "win":
        pass

    elif player.gameState == "lose":
        pass

    #call the game window update function from earlier
    redrawGameWindow()

pygame.quit()
