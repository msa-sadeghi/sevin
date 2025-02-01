from pygame.sprite import Sprite
import pygame

class Bullet(Sprite):
    def __init__(self, owner, x,y, group, direction):
        super().__init__()
        self.image = pygame.image.load("./assets/images/icons/bullet.png")
        self.rect = self.image.get_rect(topleft=(x,y))
        self.direction = direction
        group.add(self)
        self.owner = owner
        
        
    def update(self):
        self.rect.x += self.direction * 4
        if self.rect.x >= 800 or  self.rect.x <= 0:
            self.kill()