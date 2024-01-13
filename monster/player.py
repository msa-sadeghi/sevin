from pygame.sprite import Sprite
from constants import *
from pygame.locals import *
class Player(Sprite):
    def __init__(self):
        self.lives = 3
        self.warp_counter = 3
        self.speed = 5
        self.image = pygame.image.load("assets/knight.png")
        self.rect = self.image.get_rect()
        self.rect.bottom = SCREEN_HEIGHT
        self.rect.centerx = SCREEN_WIDTH/2
        self.catch_sound = pygame.mixer.Sound("assets/catch.wav")
        self.die_sound = pygame.mixer.Sound("assets/die.wav")
        self.warp_sound = pygame.mixer.Sound("assets/warp.wav")

    def draw(self):
        SCREEN.blit(self.image,self.rect)

    def move(self):
        keys = pygame.key.get_pressed()
        
        if keys[K_UP] and self.rect.top > 100:
            self.rect.y -= self.speed

        if keys[K_DOWN] and self.rect.bottom < SCREEN_HEIGHT - 100:
            self.rect.y += self.speed

        if keys[K_LEFT] and self.rect.left > 0:
            self.rect.x -= self.speed

        if keys[K_RIGHT] and self.rect.right < SCREEN_WIDTH:
            self.rect.x += self.speed

    def reset(self):
        self.rect.bottom = SCREEN_HEIGHT
        self.rect.centerx = SCREEN_WIDTH/2


