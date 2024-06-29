import pygame
from game import Game

from constants import *
from world import World

from player import Player
from button import Button
import pickle
pygame.init()

enemy_group = pygame.sprite.Group()
coin_group = pygame.sprite.Group()
lava_group = pygame.sprite.Group()
door_group = pygame.sprite.Group()

screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()

player = Player(100,screen_height-600)

level = 1
with open("levels\level1", "rb") as f:
    world_data = pickle.load(f)

world = World(world_data, enemy_group, coin_group, lava_group, door_group)

restart_button = Button(screen_width/2, screen_height/2)
bg_img = pygame.image.load("assets/sky.png")
running = True
while running:
    print(Game.next_level)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.blit(bg_img, (0,0))
    world.draw(screen)
    player.draw(screen)
    if player.alive:
        player.move(world.tile_list, enemy_group, lava_group, door_group)
    else:
        restart_button.draw(screen)
        if restart_button.check_click():
            player.__init__(100,screen_height-600)
    enemy_group.draw(screen)
    lava_group.draw(screen)
    door_group.draw(screen)
    enemy_group.update()
    coin_group.draw(screen)
    coin_group.update()
    pygame.display.update()
    clock.tick(FPS)

