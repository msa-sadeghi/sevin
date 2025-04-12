from pygame.sprite import Sprite

import pygame

class Bullet(Sprite):
    def __init__(self, x,y, direction):
        super().__init__()

        self.all_images = [
            pygame.transform.scale_by(
                pygame.image.load(f"./Objects/Bullet/Bullet_00{i}.png"),
                0.2
            ) for i in range(5)
        ]
        self.image = self.all_images[0]
        self.rect = self.image.get_rect(center=(x,y))
        self.direction = direction
        self.frame_index = 0
        self.last_change_time = pygame.time.get_ticks()

    def update(self):
        image = self.all_images[self.frame_index]
        self.image = pygame.transform.flip(image, self.direction == -1, False)
        if pygame.time.get_ticks() - self.last_change_time >= 100:
            self.frame_index += 1
            if self.frame_index >= len(self.all_images):
                self.frame_index = 0
        
        self.rect.x += self.direction * 10
        if self.rect.x < 0 or self.rect.x > 1000:
            self.kill()
        
            

