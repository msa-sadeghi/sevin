from pygame.sprite import Sprite
import pygame


class Castle(Sprite):
    def __init__(self, x,y, health):
        super().__init__()
        self.all_images = []
        for i in ("25", "50", "100"):
            img = pygame.image.load(f"assets/castle/castle_{i}.png")
            imgw = img.get_width()
            imgh = img.get_height()
            img = pygame.transform.scale(img, (imgw * 0.3, imgh * 0.3))
            self.all_images.append(img)
            
            