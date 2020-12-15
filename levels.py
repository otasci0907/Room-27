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

        for i in range(len(self.furniture)):
            win.blit(self.furniture[i], self.coords[i])

playText = Text(640, 360, cn.WHITE, "Play", 40)
titleText = Text(640, 100, cn.WHITE, "Room 27", 150)


room1Image = pygame.image.load(os.path.join(cn.BG_DIR, 'checkinRoom.png'))
room1Furn = [cn.sofaBack, cn.sofaBack, cn.sofaLeft, cn.sofaLeft, cn.sofaLeft, cn.sofaRight, cn.sofaRight, cn.sofaRight, cn.desk, cn.table, cn.table, cn.leaderboard]
room1Coords = [(132, 500), (1020, 500), (276, 204), (1162, 204), (1164, 356), (48, 204), (48, 356), (928, 204), (448, 244), (160, 248), (1040, 248), (576, 92)]
room1 = Room(room1Furn, room1Coords, room1Image)