import pygame
from player import Player

pygame.init()


width = 1000
height = 600

clock = pygame.time.Clock()
screen = pygame.display.set_mode((width, height))
fps = 60

my_player = Player(100, 300)
player_bullet_group = pygame.sprite.Group()
running = True
while running == True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    if my_player.sliding == True:
        my_player.change_animation('Slide')
    elif my_player.shooting == True:
        my_player.change_animation('Shoot')
    elif my_player.moving_state == True:
        my_player.change_animation("Run")
    elif my_player.in_air == True:
        my_player.change_animation('Jump')
    else:
        my_player.change_animation("Idle")
    
    
    screen.fill("lightblue")
    my_player.draw(screen)
    my_player.move()
    my_player.shoot(bullet_group=player_bullet_group)
    player_bullet_group.update()
    player_bullet_group.draw(screen)
    pygame.display.update()
    clock.tick(fps)