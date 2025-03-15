import pygame
from player import Player
pygame.init()


width = 1000
height = 600

clock = pygame.time.Clock()
screen = pygame.display.set_mode((width, height))
fps = 60

my_player = Player(100, 300)

running = True
while running == True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    if my_player.moving_state == True:
        my_player.change_animation("Run")
    elif my_player.in_air == True:
        my_player.change_animation('Jump')
    elif my_player.sliding == True:
        my_player.change_animation('Slide')
    else:
        my_player.change_animation("Idle")
    
    
    screen.fill("lightblue")
    my_player.draw(screen)
    my_player.move()
    pygame.display.update()
    clock.tick(fps)