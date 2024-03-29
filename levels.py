import constants as cn 
import os
import pygame

pygame.init()
pygame.font.init()

gamemode = False
room1Text = 1
room27Text = 1
roomSuperText = 1

simonPattern = ["yellow", "blue", "green", "red"]
greenCoords = ((cn.WIDTH / 2) - (cn.BUTTONSIZE + cn.BUTTONGAPSIZE), (cn.HEIGHT / 2) - (cn.BUTTONSIZE + cn.BUTTONGAPSIZE))
yellowCoords = ((cn.WIDTH / 2) + cn.BUTTONGAPSIZE, (cn.HEIGHT / 2) - (cn.BUTTONSIZE + cn.BUTTONGAPSIZE))
blueCoords = ((cn.WIDTH / 2) + cn.BUTTONGAPSIZE, (cn.HEIGHT / 2) + cn.BUTTONGAPSIZE)
redCoords = ((cn.WIDTH / 2) - (cn.BUTTONSIZE + cn.BUTTONGAPSIZE), (cn.HEIGHT / 2) + cn.BUTTONGAPSIZE)
buttonSizes = (cn.BUTTONSIZE, cn.BUTTONSIZE)

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

class Room(object):
    def __init__(self, furniture, coords, image):
        self.furniture = furniture
        self.coords = coords
        self.image = image

    def draw(self, win):
        cn.bg = self.image

        for i in range(len(self.furniture)):
            rect = self.furniture[i].get_rect(topleft = self.coords[i])
            win.blit(self.furniture[i], rect)

titleText = Text(640, 100, cn.WHITE, "Room 27", 150)
puzzleDirections = Text(1040, 630, cn.BLACK, "Explore the room!", 40)
pressEnter = Text(1040, 630, cn.BLACK, "Press [Enter]!", 50)

room1Image = pygame.image.load(os.path.join(cn.BG_DIR, 'checkinRoom.png'))
room1Furn = [cn.sofaBack, cn.sofaBack, cn.sofaLeft, cn.sofaLeft, cn.sofaLeft, cn.sofaRight, cn.sofaRight, cn.sofaRight, cn.desk, cn.table, cn.table]
room1Coords = [(132, 500), (1020, 500), (276, 204), (1162, 204), (1164, 356), (48, 204), (48, 356), (928, 204), (544, 212), (160, 248), (1040, 248)]
room1 = Room(room1Furn, room1Coords, room1Image)

room27Image = pygame.image.load(os.path.join(cn.BG_DIR, 'room27.png'))
room27Furn = [cn.chair, cn.couchLeft, cn.dresser, cn.coffeeDesk, cn.bed1]
room27Coords = [(316, 160), (408, 408), (604, 72), (304, 392), (736, 88)]
room27 = Room(room27Furn, room27Coords, room27Image)

roomSuperImage = pygame.image.load(os.path.join(cn.BG_DIR, 'superRoom.png'))
roomSuperFurn = [cn.couchBack, cn.sofaRight, cn.dresser,  cn.redBed, cn.bookshelf, cn.laptopDesk]
roomSuperCoords = [(400, 396), (308, 256), (604, 72), (736, 88), (304, 116), (304, 540)]
roomSuper = Room(roomSuperFurn, roomSuperCoords, roomSuperImage)

simonSetup = Text(cn.WIDTH / 2, 40, cn.WHITE, "You enter the hotel lobby in order to begin your vacation! You hear the doors lock behind you!", 40)
simonSetup2 = Text(cn.WIDTH / 2, 70, cn.WHITE, "The door lock has been replaced by what seems like a simon says sequence lock!", 40)
simonDirections = Text(cn.WIDTH / 2, 100, cn.WHITE, "Enter the parts of the sequence that you have found around the room to unlock the door!", 40)
first = Text(1040, 630, cn.BLACK, "1: yellow", 50)
second = Text(1040, 630, cn.BLACK, "2: blue", 50)
third = Text(1040, 630, cn.BLACK, "3: green", 50)
fourth = Text(1040, 630, cn.BLACK, "4: red", 50)

instructions1 = Text(640, 70, cn.WHITE, "Instructions", 100)
instructions2 = Text(640, 150, cn.WHITE, "Use arrow keys to move your character around the screen!", 30)
instructions3 = Text(640, 180, cn.WHITE, "For each room, explore the room and find any secrets inside of them!", 30)
instructions4 = Text(640, 210, cn.WHITE, "Once you have thoroughly investigated the room, walk up to the piece of furniture that says 'press [enter]' to bring the puzzle!", 30)
instructions5 = Text(640, 240, cn.WHITE, "Use the clues that you found around the room to solve the puzzles to move onto the next room!", 30)
instructions6 = Text(640, 690, cn.WHITE, "Press [w] to return to the title screen", 30)
