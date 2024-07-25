import pygame
from game import Game
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

CLOCK = pygame.time.Clock()
FPS = 60


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.blit(Game.bg_image, (0,0))        
    pygame.display.update()
    CLOCK.tick(FPS)