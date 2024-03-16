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

def check_bullet_collisions() :
    if pygame.sprite.groupcollide(player_bullet_group, enemy_group, True, True):
        pass
    if pygame.sprite.spritecollide(my_player, egg_group, True):
        pass
    
    if pygame.sprite.groupcollide(player_bullet_group, egg_group, True, True):
        pass
   
my_player = Player()
enemy_group = pygame.sprite.Group()
player_bullet_group = pygame.sprite.Group()
egg_group = pygame.sprite.Group()


spawn_enemies()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
            if event.key == pygame.K_SPACE:
                my_player.shoot(player_bullet_group)
    check_bullet_collisions()
    screen.fill((0,0,0)) 
    check_on_edge()
    my_player.move()
    my_player.draw()  
    enemy_group.update(egg_group)       
    enemy_group.draw(screen)
    player_bullet_group.update()       
    player_bullet_group.draw(screen)
    egg_group.update()       
    egg_group.draw(screen)
    pygame.display.update()
    CLOCK.tick(FPS)