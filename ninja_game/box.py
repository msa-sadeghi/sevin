from pygame.sprite import Sprite
import pygame
class Box(Sprite):
    def __init__(self,image,x,y, box_group):
        super().__init__()

        self.image = pygame.transform.scale(
            pygame.image.load(image),
            (50,50)
        )

        self.rect = self.image.get_rect(topleft=(x,y))
        box_group.add(self)
        self.start_x = x

    def update(self,scroll):
        self.rect.x =self.start_x - scroll