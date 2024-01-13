from constants import *
from pygame.sprite import Sprite
from random import randint, choice
class Monster(Sprite):
    def __init__(self, image, x,y, monster_type):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect(topleft=(x,y))
        self.xdirection = choice((-1,1))
        self.ydirection = choice((-1,1))
        self.speed = randint(1,5)
        self.type = monster_type

    def update(self):
        self.rect.x += self.xdirection * self.speed
        self.rect.y += self.ydirection * self.speed
        if self.rect.left <= 0 or self.rect.right >= SCREEN_WIDTH:
            self.xdirection *= -1
        if self.rect.top <= 100 or self.rect.bottom >= SCREEN_HEIGHT-100:
            self.ydirection *= -1

