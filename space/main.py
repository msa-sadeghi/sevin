from constants import *
from player import Player
from enemy import Enemy

level = 0

def check_on_edge():
    on_edge = False
    for enemy in enemy_group:
        if enemy.rect.left < 0 or enemy.rect.right > SCREEN_WIDTH:
            on_edge = True
            break
    if on_edge:
        for enemy in enemy_group:
            enemy.direction *= -1
            enemy.rect.y += level *10


def spawn_enemies():
    global level
    level += 1
    for i in range(4):
        for j in range(10):
            Enemy(j * 96, i * 96, enemy_group)
        
my_player = Player()
enemy_group = pygame.sprite.Group()
spawn_enemies()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
    screen.fill((0,0,0)) 
    check_on_edge()
    my_player.move()
    my_player.draw()  
    enemy_group.update()       
    enemy_group.draw(screen)
    pygame.display.update()
    CLOCK.tick(FPS)