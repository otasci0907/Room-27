import pygame

pygame.init()

WIDTH = 1280
HEIGHT = 720

win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Room 27")

clock = pygame.time.Clock()

class Player(object):
    def __init__(self,x,y,width,height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 10
        self.left = False
        self.right = False

    def draw(self, win):
        pygame.draw.rect(win, (255,0,0), (self.x, self.y, self.width, self.height))

def redrawGameWindow():
    win.fill((0,0,0))
    player.draw(win)
    pygame.display.update()

player = Player(604, 300, 76, 120)
run = True
while run:
    clock.tick(27)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] or keys[pygame.K_a]:
        player.x -= player.vel

    if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
        player.x += player.vel

    if keys[pygame.K_UP] or keys[pygame.K_w]:
        player.y -= player.vel

    if keys[pygame.K_DOWN] or keys[pygame.K_s]:
        player.y += player.vel
            
    redrawGameWindow()

pygame.quit()
