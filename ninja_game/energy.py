from pygame.sprite import Sprite
import pygame
class Energy(Sprite):
    def __init__(self, image, x,y, group):
        super().__init__()
        self.image = pygame.transform.scale(
            pygame.image.load(image),
            (50,50)
        )
        self.rect = self.image.get_rect(topleft=(x,y))
        group.add(self)
        self.start_x = x

    def update(self,scroll, player):
        self.rect.x = self.start_x - scroll
        if pygame.sprite.collide_rect(player,self):
            self.kill()
            player.energy +=  1