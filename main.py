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
import os

#initialize pygame
pygame.init()
pygame.font.init()
win = pygame.display.set_mode((cn.WIDTH, cn.HEIGHT))
pygame.display.set_caption("Room 27")
clock = pygame.time.Clock()

#create player class
class Player(object):
    #all the variables stored in the player object
    def __init__(self,x,y,width,height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 6
        self.left = False
        self.right = False
        self.up = False
        self.down = False
        self.walkCount = 0
        self.score = 0
        self.gameState = 0

    #draw and animate the player
    def draw(self, win):
        if self.gameState > 0:
            #set an upper bound for the walk count to control how long each image is shown in the animation
            if self.walkCount + 1 >= 12:
                self.walkCount = 0

            #display and animate the player in each direction
            if self.left:
                win.blit(cn.walkLeft[self.walkCount//3], (self.x,self.y))
                self.walkCount += 1

            elif self.right:
                win.blit(cn.walkRight[self.walkCount//3], (self.x,self.y))
                self.walkCount +=1

            elif self.up:
                win.blit(cn.walkBack[self.walkCount//3], (self.x,self.y))
                self.walkCount +=1

            elif self.down:
                win.blit(cn.walkForward[self.walkCount//3], (self.x,self.y))
                self.walkCount +=1

            #if the player stops moving, display the standing image in the last direction it was moving
            else:
                win.blit(cn.char, (self.x,self.y))

#function to store the procedures to redraw the game window
def redrawGameWindow():
    player.score = int(pygame.time.get_ticks() / 1000)
    textsurface = cn.myfont.render(str(player.score), False, (255, 255, 255))
    win.blit(cn.bg, (0,0))
    player.draw(win)
    win.blit(textsurface,(10,10))
    pygame.display.update()

def titleScreen():
    cn.bg = pygame.image.load(os.path.join(cn.BG_DIR, 'titleScreen.png'))
    cn.fontsize = 40
    textsurface = cn.myfont.render("Play", False, cn.WHITE)

#create main player object
player = Player(cn.WIDTH / 2, cn.HEIGHT / 2, 76, 108)

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

    if player.gameState == 1:
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

    if player.gameState == 0:
        titleScreen()

    elif player.gameState == 1:
        pass

    elif player.gameState == 2:
        pass

    elif player.gameState == 3:
        pass

    elif player.gameState == 4:
        pass

    elif player.gameState == 5:
        pass

    #call the game window update function from earlier
    redrawGameWindow()

pygame.quit()
