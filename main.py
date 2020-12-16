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
pygame.mixer.init()
win = pygame.display.set_mode((cn.WIDTH, cn.HEIGHT))
pygame.display.set_caption("Room 27")
clock = pygame.time.Clock()
volume = 0.5
first = pygame.mixer.Sound(os.path.join(cn.MUSIC_DIR, 'rustboro.mp3'))
first.play(-1)

#function to store the procedures to redraw the game window
def redrawGameWindow():
    win.blit(cn.bg, (0,0))
    if player.gameState == "title":
        lvl.playText.draw(win)
        lvl.titleText.draw(win)

    if player.gameState == "1":
        player.score = int(pygame.time.get_ticks() / 5000)
        scoreText = lvl.Text(45, 40, cn.BLACK, str(player.score), 40)
        scoreText.draw(win)
        lvl.room1.draw(win)
        pygame.draw.rect(win, cn.WHITE, (840, 600, 400, 60))
        if lvl.room1Text == 1:
            lvl.puzzleDirections.draw(win)
            lvl.puzzleDirections2.draw(win)
        elif lvl.room1Text == 2:
            lvl.pressEnter.draw(win)
        player.draw(win)
        if lvl.gamemode == True:
            pygame.draw.rect(win, cn.BLACK, (0, 0, 1280, 720))
    pygame.display.update()

#create main player object
player = pl.Player(cn.WIDTH / 2 - 32, cn.HEIGHT / 2 + 100, 76, 108)

#main loop
run = True
while run:
    #get the clock ticking
    clock.tick(27)
    keys = pygame.key.get_pressed()

    #if the program is quit, close it (duh)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            first.stop()

    for i in range(len(lvl.room1.furniture)):
        if player.rect.colliderect(lvl.room1.furniture[i].get_rect(topleft = lvl.room1.coords[i])):
            player.collided = True

    deskRect = lvl.room1.furniture[8].get_rect(topleft = lvl.room1.coords[8])
    if player.rect.top - 10 <= deskRect.top + deskRect.height and player.rect.left + player.rect.width + 10 >= deskRect.left and player.rect.left - 10 <= deskRect.left + deskRect.width and player.rect.top + player.rect.height + 10 >= deskRect.top:
        lvl.room1Text = 2
        if keys[pygame.K_RETURN]:
            lvl.gamemode = True
        elif keys[pygame.K_w]:
            lvl.gamemode = False
    else:
        lvl.room1Text = 1

    if player.gameState != "title" and player.gameState != "win" and player.gameState != "lose":
        #detect arrow key presses and move the player accordingly
        if keys[pygame.K_LEFT] and player.x > player.vel  and player.collided == False:
            player.rect.left -= player.vel
            player.x -= player.vel
            player.left = True
            player.right = False
            player.up = False
            player.down = False
            cn.char = cn.standLeft

        elif keys[pygame.K_RIGHT] and player.rect.x < cn.WIDTH - player.rect.width - player.vel  and player.collided == False:
            player.rect.left += player.vel
            player.x += player.vel
            player.right = True
            player.left = False
            player.up = False
            player.down = False
            cn.char = cn.standRight

        elif keys[pygame.K_UP] and player.rect.y > player.vel + 100  and player.collided == False:
            player.rect.top -= player.vel
            player.y -= player.vel
            player.left = False
            player.right = False
            player.up = True
            player.down = False
            cn.char = cn.standBack

        elif keys[pygame.K_DOWN] and player.rect.y < cn.HEIGHT - player.rect.height - player.vel  and player.collided == False:
            player.rect.top += player.vel
            player.y += player.vel
            player.right = False
            player.left = False
            player.up = False
            player.down = True
            cn.char = cn.standForward
        
        elif player.collided == True:
            if cn.char == cn.standLeft:
                player.x += player.vel
                player.rect.left += player.vel
                player.right = True
                player.left = False
                player.up = False
                player.down = False
                player.collided = False
                cn.char = cn.standRight
            elif cn.char == cn.standRight:
                player.x -= player.vel
                player.rect.left -= player.vel
                player.right = False
                player.left = True
                player.up = False
                player.down = False
                player.collided = False
                cn.char = cn.standLeft
            elif cn.char == cn.standBack:
                player.rect.top += player.vel
                player.y += player.vel
                player.right = False
                player.left = False
                player.up = False
                player.down = True
                player.collided = False
                cn.char = cn.standForward
            elif cn.char == cn.standForward:
                player.rect.top -= player.vel
                player.y -= player.vel
                player.right = False
                player.left = False
                player.up = True
                player.down = False
                player.collided = False
                cn.char = cn.standBack

        #if the player is not moving, reset the walking animation
        else:
            player.right = False
            player.left = False
            player.up = False
            player.down = False
            player.walkCount = 0
            player.collided = False

    #if X or ESC are pressed, quit the game
    if keys[pygame.K_ESCAPE]:
        pygame.quit()

    if keys[pygame.K_y]:
        player.gameState = "1"

    if keys[pygame.K_x]:
        player.gameState = "title"

    if player.gameState == "title":
        cn.bg = pygame.image.load(os.path.join(cn.BG_DIR, 'titleScreen.jpg'))

    elif player.gameState == "win":
        pass

    elif player.gameState == "lose":
        pass

    #call the game window update function from earlier
    redrawGameWindow()

pygame.quit()
