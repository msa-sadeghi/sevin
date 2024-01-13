from constants import *
from player import Player
from game import Game
pygame.init()

my_player = Player()
monster_group = pygame.sprite.Group()

my_game = Game(my_player,monster_group)
my_game.start_new_level()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False


    SCREEN.fill(BLACK)
    my_game.draw()
    my_game.update()
    my_player.draw()
    my_player.move()
    monster_group.update()
    monster_group.draw(SCREEN)
    pygame.display.update()
    CLOCK.tick(FPS)