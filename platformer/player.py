from pygame.sprite import Sprite
import pygame
from constants import *
from game import Game
class Player(Sprite):
    def __init__(self, x,y):
        super().__init__()
        self.right_images = []
        self.left_images = []
        for i in range(1, 5):
            img = pygame.image.load(f"assets/guy{i}.png")
            img = pygame.transform.scale(img, (64, 64))
            self.right_images.append(img)
            img = pygame.transform.flip(img, True, False)
            self.left_images.append(img)
            
        self.frame_index = 0
        self.counter = 0
        self.image = self.right_images[self.frame_index]
        self.rect = self.image.get_rect()
        self.rect.topleft = (x,y)
        self.vel_y = 0
        self.jumped = False
        self.direction = 1
        self.idle = True
        self.inair = False
        self.dead_image = pygame.image.load("assets/ghost.png")
        self.alive = True
        self.coin_sound = pygame.mixer.Sound("assets/coin.wav")
       

    def draw(self, screen):
        if not self.alive:
            self.image = self.dead_image
        screen.blit(self.image, self.rect)
        self.animation()
    def animation(self):
        self.counter += 1
        if self.counter >= 10:
            self.frame_index += 1
            self.counter = 0
            if self.frame_index >= len(self.right_images) or self.idle:
                self.frame_index = 0
        if self.direction == 1:
            self.image = self.right_images[self.frame_index]
        elif self.direction == -1:
            self.image = self.left_images[self.frame_index]
            
        
       
    def move(self, tiles, enemy_group, lava_group, door_group, coin_group):
        dx = 0
        dy = 0
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.direction = -1
            self.idle = False
            dx -= 5
        if keys[pygame.K_RIGHT]:
            self.direction = 1
            self.idle = False
            dx += 5
        if keys[pygame.K_SPACE] and not self.jumped:
            self.vel_y = -14
            self.jumped = True
        
        if not keys[pygame.K_LEFT] and not keys[pygame.K_RIGHT]:
            self.idle = True
        
        dy += self.vel_y
        self.vel_y += 1
        self.check_collisions(tiles,dx, dy,enemy_group, lava_group, door_group, coin_group)  
        
            
        

    def check_collisions(self, tiles,dx,dy,enemy_group, lava_group, door_group, coin_group):
        if pygame.sprite.spritecollide(self, door_group, False) :
            Game.next_level = True
        if pygame.sprite.spritecollide(self, coin_group, True) :
            self.coin_sound.play()
            # Game.next_level = True
            
        if pygame.sprite.spritecollide(self, enemy_group, False) :
            self.alive = False
        if pygame.sprite.spritecollide(self, lava_group, False) :
            self.alive = False
        for t in tiles:
            if t[1].colliderect(self.rect.x + dx, self.rect.y, self.rect.width, self.rect.height):
                dx = 0
            if t[1].colliderect(self.rect.x, self.rect.y + dy, self.rect.width, self.rect.height):
                if self.vel_y > 0:
                    dy = 0
                    self.vel_y = 0
                    self.jumped = False
                else:
                    dy = 0
                    self.vel_y = 0
                    
                
        self.rect.x += dx
        self.rect.y += dy