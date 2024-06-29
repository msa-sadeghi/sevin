from pygame.sprite import Sprite
import pygame
class Lava(Sprite):
    def __init__(self, x,y, group):
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load("assets/lava.png"), (50,50))
        self.rect = self.image.get_rect(topleft=(x,y))
        group.add(self)
 
        
