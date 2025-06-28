import pygame
from ninja import Ninja

pygame.init()
WIDTH = 1000
HEIGHT = 640

screen = pygame.display.set_mode((WIDTH, HEIGHT))
bg_image = pygame.image.load("./freegui/png/BG.png")
bg_image = pygame.transform.scale(bg_image, (WIDTH, HEIGHT))
FPS = 60
clock = pygame.time.Clock()

my_ninja = Ninja(100, 400)

def draw_background():
    for i in range(4):
        screen.blit(bg_image, (i * bg_image.get_size()[0] - scroll ,0))


time_to_scroll = 0
scroll = 0
left_border = WIDTH//3
right_border = WIDTH - WIDTH//3
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    if my_ninja.moving:
        my_ninja.change_animation("Run")
    elif my_ninja.moving == False:
        my_ninja.change_animation("Idle")
   
    if my_ninja.rect.right > right_border and my_ninja.animation == "Run" and my_ninja.direction == 1:
        
        scroll += 5
    if my_ninja.rect.left < left_border and my_ninja.animation == "Run" and my_ninja.direction == -1 and scroll > 0:
        
        scroll -= 5
        
        
    
        
    draw_background()
    my_ninja.draw(screen)
    my_ninja.move()
    pygame.display.update()

    clock.tick(FPS)