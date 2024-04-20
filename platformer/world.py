import pygame
from constants import *
from enemy import Enemy
from coin import Coin
class World:
    def __init__(self, data, enemy_group, coin_group):
        self.tile_list = []
        dirt_img = pygame.image.load("assets/dirt.png")
        grass_img = pygame.image.load("assets/grass.png")
       
        for row in range(len(data)):
            for col in range(len(data[row])):
                if data[row][col] == 1:
                    img = pygame.transform.scale(dirt_img, (TILE_SIZE, TILE_SIZE))
                    img_rect = img.get_rect()
                    img_rect.topleft = (col * TILE_SIZE, row * TILE_SIZE)
                    tile = (img, img_rect)
                    self.tile_list.append(tile)
                if data[row][col] == 2:
                    img = pygame.transform.scale(grass_img, (TILE_SIZE, TILE_SIZE))
                    img_rect = img.get_rect()
                    img_rect.topleft = (col * TILE_SIZE, row * TILE_SIZE)
                    tile = (img, img_rect)
                    self.tile_list.append(tile)
                if data[row][col] == 3:
                    Enemy(col * TILE_SIZE, row * TILE_SIZE + 15, enemy_group)
                if data[row][col] == 5:
                    Coin(col * TILE_SIZE, row * TILE_SIZE + 15, coin_group)
               

    def draw(self, screen):
        for tile in self.tile_list:
            screen.blit(tile[0], tile[1])
        
