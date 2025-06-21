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

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    if my_ninja.moving:
        my_ninja.change_animation("Run")
    elif my_ninja.moving == False:
        my_ninja.change_animation("Idle")
    screen.blit(bg_image, (0,0))
    my_ninja.draw(screen)
    my_ninja.move()
    pygame.display.update()

    clock.tick(FPS)