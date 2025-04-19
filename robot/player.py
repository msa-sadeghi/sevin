from pygame.sprite import Sprite
from bullet import Bullet
import pygame
import os
class Player(Sprite):
    def __init__(self, x,y):
        super().__init__()
        self.animation_types = os.listdir("./png")
        self.all_images = {}

        for animation in self.animation_types:
            temp = []
            num_of_images = len(os.listdir(f"./png/{animation}"))
            for i in range(1,num_of_images):
                img = pygame.image.load(f"./png/{animation}/{animation}{i}.png")
                img = pygame.transform.scale_by(img, 0.4)
                temp.append(img)

            self.all_images[animation] = temp

        self.frame_index = 0
        self.action = "Idle"
        self.image = self.all_images[self.action][self.frame_index]
        self.rect = self.image.get_rect(topleft=(x,y))
        self.last_animation_time = pygame.time.get_ticks()
        self.moving = False
        self.moving_state = False
        self.flip = False
        self.yspeed = 0
        self.in_air = False
        self.direction = 1
        self.sliding = False
        self.shooting = False
        self.run_shoot = False
        self.last_shoot_time = pygame.time.get_ticks()

    def move(self):
        dx = 0
        dy = 0
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.moving_state = True
            self.direction = -1
            self.flip = True
            dx -= 5
        if keys[pygame.K_RIGHT]:
            self.moving_state = True
            self.direction = 1
            self.flip = False
            dx += 5
        if not keys[pygame.K_LEFT] and not keys[pygame.K_RIGHT]:
            self.moving_state = False
        if keys[pygame.K_UP]:
            self.yspeed = -14
            self.in_air = True
        if keys[pygame.K_DOWN]:
            dx += self.direction * 10  
            self.sliding = True
            self.sliding_time = pygame.time.get_ticks()
        if not keys[pygame.K_DOWN] :
            self.sliding = False
        if keys[pygame.K_SPACE]:
            self.shooting = True
        if not keys[pygame.K_SPACE]:
            self.shooting = False
        dy += self.yspeed
        self.yspeed += 1
        if self.moving_state and self.shooting:
            self.run_shoot = True
        if self.rect.bottom + dy >= 600:
            dy = 600 - self.rect.bottom
            self.yspeed = 0
            self.in_air = False

        self.rect.x += dx
        self.rect.y += dy



    def draw(self, screen):
        screen.blit(pygame.transform.flip(self.image, self.flip, False), self.rect)
        self.animation()


    def animation(self):
        self.image = self.all_images[self.action][self.frame_index]
        if pygame.time.get_ticks() - self.last_animation_time >= 100:
            self.frame_index += 1
            if self.frame_index >= len(self.all_images[self.action]):
                self.frame_index = 0
            self.last_animation_time = pygame.time.get_ticks()


    def change_animation(self, new_animation):
        if self.action != new_animation:
            self.action = new_animation
            self.frame_index = 0

    def shoot(self, bullet_group):
      
        if self.shooting == True and pygame.time.get_ticks() - self.last_shoot_time >= 100:
            bullet = Bullet(self.rect.centerx + self.rect.size[0] * 0.4 * self.direction, self.rect.centery, self.direction)
            bullet_group.add(bullet)
            self.last_shoot_time = pygame.time.get_ticks()
            
            


