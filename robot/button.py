import pygame
class Button:
    def __init__(self, x,y, image):
        self.image = image
        self.rect = self.image.get_rect(topleft=(x,y))


    def update(self, screen):
        screen.blit(self.image, self.rect)
        click = False
        mouse_pos = pygame.mouse.get_pos()
        if pygame.mouse.get_pressed()[0]:
            if self.rect.collidepoint(mouse_pos):
                click = True

        return click
