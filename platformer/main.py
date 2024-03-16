import pygame

from constants import *
from world import World

from player import Player
from levels.level_creator import world_data
pygame.init()

screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()

player = Player(100,screen_height-600)
world = World(world_data)

bg_img = pygame.image.load("assets/sky.png")
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.blit(bg_img, (0,0))
    world.draw(screen)
    pygame.display.update()
    clock.tick(FPS)

