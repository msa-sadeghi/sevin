import pygame


from constants import *
from world import World

from player import Player
from levels.level_creator import world_data
pygame.init()

enemy_group = pygame.sprite.Group()
coin_group = pygame.sprite.Group()

screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()

player = Player(100,screen_height-600)
world = World(world_data, enemy_group, coin_group)

bg_img = pygame.image.load("assets/sky.png")
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.blit(bg_img, (0,0))
    world.draw(screen)
    player.draw(screen)
    player.move(world.tile_list)
    enemy_group.draw(screen)
    enemy_group.update()
    coin_group.draw(screen)
    coin_group.update()
    pygame.display.update()
    clock.tick(FPS)

