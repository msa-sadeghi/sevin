import pygame
class Button:
    def __init__(self, x,y, image, scale):
        self.image = pygame.image.load(image)
        self.image = pygame.transform.scale(self.image , (scale, scale))
        self.rect = self.image.get_rect(center=(x,y)) 
        self.is_clicked = False 
    def draw(self, screen):
        screen.blit(self.image, self.rect)
        
    def check_click(self):
        click = False
        if self.rect.collidepoint(pygame.mouse.get_pos()):
            if pygame.mouse.get_pressed()[0] and not self.is_clicked:
                click = True
                self.is_clicked = True
            elif not pygame.mouse.get_pressed()[0]:
                self.is_clicked = False
        return click