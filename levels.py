import constants as cn 
import os
import pygame

pygame.init()
pygame.font.init()

class Text(object):
    #all the variables stored in the player object
    def __init__(self, x, y, color, text, size):
        self.x = x
        self.y = y
        self.color = color
        self.text = text
        self.size = size
        self.font = pygame.font.SysFont('Atari Classic', self.size)
    
    def draw(self, win):
        renderText = self.font.render(self.text, False, self.color)
        text_width = renderText.get_width()
        text_height = renderText.get_height()
        win.blit(renderText, (self.x - text_width / 2, self.y - text_height / 2))


class Furniture(pygame.sprite.Sprite):
    #all the variables stored in the player object
    def __init__(self,x,y,width,height):
        pygame.sprite.Sprite.__init__(self)
        self.x = x
        self.y = y
        self.width = width
        self.height = height

class Room(object):
    def __init__(self, furniture, coords, image):
        self.furniture = furniture
        self.coords = coords
        self.image = image

    def draw(self, win):
        cn.bg = self.image
        win.blit(cn.bg, (0,0))

        for i in furniture:
            win.blit(furniture[i], coords[i])

playText = Text(640, 360, cn.WHITE, "Play", 40)
titleText = Text(640, 100, cn.WHITE, "Room 27", 150)

def room1():
    cn.bg = pygame.image.load(os.path.join(cn.BG_DIR, 'checkinRoom.png'))