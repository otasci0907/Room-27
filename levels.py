import constants as cn 
import os
import pygame

pygame.init()
pygame.font.init()

def titleScreen():
    cn.bg = pygame.image.load(os.path.join(cn.BG_DIR, 'titleScreen.jpg'))
    playText = cn.basicText.render("Play", False, (255, 255, 255))

def room1():
    cn.bg = pygame.image.load(os.path.join(cn.BG_DIR, 'checkinRoom.png'))