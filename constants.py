'''
Room 27

Orhan Tasci
William Zhong
Benjamin Li
'''

'''
constants.py

This file contains some predetermined constant variables. 
This file is imported into main.py to be used accordingly.
'''

#import needed modules
import os
import pygame

#initialized things
pygame.init()
pygame.font.init()

#constants
WIDTH = 1280
HEIGHT = 720

RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

#directories and image loading
ASSETS_DIR = "assets"
BG_DIR = os.path.join(ASSETS_DIR, "backgroundAssets")
PUZZLE_DIR = os.path.join(ASSETS_DIR, "puzzleAssets")
PLAYER_DIR = os.path.join(ASSETS_DIR, "playerAssets")

walkRight = [pygame.image.load(os.path.join(PLAYER_DIR, 'r2.png')), pygame.image.load(os.path.join(PLAYER_DIR, 'r1.png')), pygame.image.load(os.path.join(PLAYER_DIR, 'r3.png')), pygame.image.load(os.path.join(PLAYER_DIR, 'r1.png'))]
walkLeft = [pygame.image.load(os.path.join(PLAYER_DIR, 'l2.png')), pygame.image.load(os.path.join(PLAYER_DIR, 'l1.png')), pygame.image.load(os.path.join(PLAYER_DIR, 'l3.png')), pygame.image.load(os.path.join(PLAYER_DIR, 'l1.png'))]
walkBack = [pygame.image.load(os.path.join(PLAYER_DIR, 'b2.png')), pygame.image.load(os.path.join(PLAYER_DIR, 'b1.png')), pygame.image.load(os.path.join(PLAYER_DIR, 'b3.png')), pygame.image.load(os.path.join(PLAYER_DIR, 'b1.png'))]
walkForward = [pygame.image.load(os.path.join(PLAYER_DIR, 'f2.png')), pygame.image.load(os.path.join(PLAYER_DIR, 'f1.png')), pygame.image.load(os.path.join(PLAYER_DIR, 'f3.png')), pygame.image.load(os.path.join(PLAYER_DIR, 'f1.png'))]

bg = pygame.image.load(os.path.join(BG_DIR, 'checkinRoom.png'))
standRight = pygame.image.load(os.path.join(PLAYER_DIR, 'r1.png'))
standLeft = pygame.image.load(os.path.join(PLAYER_DIR, 'l1.png'))
standBack = pygame.image.load(os.path.join(PLAYER_DIR, 'b1.png'))
standForward = pygame.image.load(os.path.join(PLAYER_DIR, 'f1.png'))
char = pygame.image.load(os.path.join(PLAYER_DIR, 'f1.png'))

sofaBack = pygame.image.load(os.path.join(BG_DIR, 'bigCouchBack.png'))
sofaLeft = pygame.image.load(os.path.join(BG_DIR, 'bigCouchLeft.png'))
sofaRight = pygame.image.load(os.path.join(BG_DIR, 'bigCouchRight.png'))

desk = pygame.image.load(os.path.join(BG_DIR, 'desk.png'))
leaderboard = pygame.image.load(os.path.join(BG_DIR, 'leaderboard.png'))
table = pygame.image.load(os.path.join(BG_DIR, 'table.png'))