import pygame
import constants as cn

pygame.init()
pygame.font.init()

myfont = pygame.font.SysFont('Atari Classic', 40)

win = pygame.display.set_mode((cn.WIDTH, cn.HEIGHT))
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
        self.score = 0

    def draw(self, win):
        pygame.draw.rect(win, cn.RED, (self.x, self.y, self.width, self.height))

def redrawGameWindow():
    win.fill((0,0,0))
    player.draw(win)
    win.blit(textsurface,(10,10))
    pygame.display.update()

player = Player(cn.WIDTH / 2, cn.HEIGHT / 2, 76, 120)
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

    if keys[pygame.K_x] or keys[pygame.K_ESCAPE]:
        pygame.quit()

    player.score = int(pygame.time.get_ticks() / 1000)
    textsurface = myfont.render(str(player.score), False, (255, 255, 255))

    redrawGameWindow()

pygame.quit()
