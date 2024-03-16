from pygame.sprite import Sprite
import pygame
from egg import Egg
import random
class Enemy(Sprite):
    def __init__(self, x,y, group):
        super().__init__()
        img= pygame.image.load("assets/chick.png")
        img_w = img.get_width()
        img_h = img.get_height()
        self.image = pygame.transform.scale(img, (img_w * 1, img_h * 1))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x,y)
        group.add(self)
        self.direction = 1
        self.speed = 3
        
    def update(self, group):
        self.rect.x += self.speed * self.direction
        self.fire(group)
        
    def fire(self, group):
        if random.randint(1,1000) == 1000:
            Egg(self.rect.centerx, self.rect.bottom, group)
        
        
        
    