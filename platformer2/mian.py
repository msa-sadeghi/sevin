import pygame
from character import Character
WIDTH = 800

HEIGHT  = 600
FPS  = 60
clock = pygame.time.Clock()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
bullet_group = pygame.sprite.Group()
player = Character("player", 100, 300, 50, 10)
moving_left, moving_right = (False, False)
bullet_shoot = False
jumped = False
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                moving_left = True
            if event.key == pygame.K_RIGHT:
                moving_right = True
            if event.key == pygame.K_UP:
                jumped = True
            if event.key == pygame.K_SPACE:
                bullet_shoot = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                moving_left = False
            if event.key == pygame.K_RIGHT:
                moving_right = False
            if event.key == pygame.K_UP:
                jumped = False
            if event.key == pygame.K_SPACE:
                bullet_shoot = False
    
    if moving_left or moving_right:
        player.change_animation("Run")
    else:
        player.change_animation("Idle")
        
    if jumped and not player.in_air:
        player.gravity = -15
        player.in_air= True
    if player.in_air:
        player.change_animation("Jump")
        
    if bullet_shoot:
        player.shoot("bullet", bullet_group)
    screen.fill("black")       
    player.move(moving_left, moving_right)
    player.draw(screen) 
    bullet_group.update()
    bullet_group.draw(screen)       
    pygame.display.update()
    clock.tick(FPS)