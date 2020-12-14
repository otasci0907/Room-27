import pygame
import constants as cn
import os

pygame.init()
pygame.font.init()

#create player class
class Player(pygame.sprite.Sprite):
    #all the variables stored in the player object
    def __init__(self,x,y,width,height):
        pygame.sprite.Sprite.__init__(self)
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
        self.gameState = "title"

    #draw and animate the player
    def draw(self, win):
        if self.gameState != "title" and self.gameState != "win" and self.gameState != "lose":
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