from pygame.sprite import Sprite
import pygame
import os
WIDTH = 1000
HEIGHT = 640
left_border = WIDTH//3
right_border = WIDTH - WIDTH//3
class Ninja(Sprite):
    def __init__(self, x,y):
        super().__init__()
        self.all_images = {}
        self.all_animations = os.listdir("./ninjagirlnew/png")
        for animation in self.all_animations:
            images_list = list()
            name_of_images = os.listdir(f"./ninjagirlnew/png/{animation}")
            for name in name_of_images:
                image = pygame.image.load(f"./ninjagirlnew/png/{animation}/{name}")
                image = pygame.transform.scale_by(image, 0.3)
                images_list.append(image)
            self.all_images[animation] = images_list

        self.frame_index = 0
        self.animation = "Idle"
        self.image = self.all_images[self.animation][self.frame_index]
        self.rect = self.image.get_rect(topleft=(x,y))
        self.last_update_time = pygame.time.get_ticks()
        self.direction = 1
        self.moving = False
        self.yspeed = 0
        self.energy = 0

    def draw(self, screen):
        # pygame.draw.rect(screen, "red", self.rect, 3)
        image = self.all_images[self.animation][self.frame_index]
        self.image = pygame.transform.flip(image, self.direction == -1, False)
        screen.blit(self.image, self.rect)
        self.do_animation()

    def do_animation(self):
        if pygame.time.get_ticks() - self.last_update_time >= 100:
            self.last_update_time = pygame.time.get_ticks()
            self.frame_index += 1
            if self.frame_index >= len(self.all_images[self.animation]):
                self.frame_index = 0

    def move(self, dt, box_group):
        dx = 0
        dy = 0
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.direction =  -1
            self.moving = True
            dx -= 200 * dt
        if keys[pygame.K_RIGHT]:
            self.direction =  1
            self.moving = True
            dx += 200 * dt
        if not keys[pygame.K_LEFT] and not keys[pygame.K_RIGHT]:
            self.moving = False
        if keys[pygame.K_UP]:
            self.yspeed = -14
        if self.rect.right + dx >= 970:
            dx = 0
        if self.rect.left + dx <= 0:
            dx = 0

        if abs(dx) > 300 * dt:
            if dx > 0:
                dx = 300 * dt
            else:
                dx = -300 * dt
       
        for box in box_group:
            if box.rect.colliderect(self.rect.x + dx,\
                                     self.rect.y, self.rect.size[0], self.rect.size[1]):
                if dx > 0:
                    dx = box.rect.left - self.rect.right
                elif dx < 0:
                    dx = box.rect.right - self.rect.left
        self.rect.x += dx


        self.yspeed += 1
        dy += self.yspeed
        for box in box_group:
            if box.rect.colliderect(self.rect.x, self.rect.y + dy,\
                                     self.rect.size[0], self.rect.size[1]):
                if self.yspeed > 0:
                    dy = box.rect.top - self.rect.bottom
                    self.yspeed = 0
                elif self.yspeed < 0:
                    dy = box.rect.bottom - self.rect.top
                    self.yspeed = 0
        self.rect.y += dy

    def change_animation(self, new_animation):
        if self.animation != new_animation:
            self.animation = new_animation
            self.frame_index = 0
            self.last_update_time = pygame.time.get_ticks()




                





