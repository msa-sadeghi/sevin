from constants import *
import random
from monster import Monster
class Game:
    def __init__(self, player, monster_group):
        self.player = player
        self.monster_group = monster_group
        self.score = 0
        self.level_number = 0
        self.font = pygame.font.Font("assets/Abrushow.ttf",32)

        blue_monster = pygame.image.load("assets/blue_monster.png")
        green_monster = pygame.image.load("assets/green_monster.png")
        purple_monster = pygame.image.load("assets/purple_monster.png")
        yellow_monster = pygame.image.load("assets/yellow_monster.png")

        self.all_monster_images = (
            blue_monster,
            green_monster,
            purple_monster,
            yellow_monster
        )
        self.target_monster_type = random.randint(0,3)
        self.target_monster_image = self.all_monster_images[self.target_monster_type]
        self.target_monster_rect = self.target_monster_image.get_rect()
        self.target_monster_rect.bottom = 100
        self.target_monster_rect.centerx = SCREEN_WIDTH/2
        self.catch_sound = pygame.mixer.Sound("assets/catch.wav")
        self.die_sound = pygame.mixer.Sound("assets/die.wav")
        self.next_level_sound = pygame.mixer.Sound("assets/next_level.wav")


    def start_new_level(self):
        self.level_number += 1
        self.player.warp_counter += 2
        for i in range(self.level_number):

            blue_monster = Monster(
                self.all_monster_images[0], 
                random.randint(0,SCREEN_WIDTH - 64),
                random.randint(100, SCREEN_HEIGHT - 164),
                0
                )
            self.monster_group.add(blue_monster)

            green_monster = Monster(
                self.all_monster_images[1],
                random.randint(0,SCREEN_WIDTH - 64),
                random.randint(100, SCREEN_HEIGHT - 164),
                1

            )
            self.monster_group.add(green_monster)
            purple_monster = Monster(
                self.all_monster_images[2], 
                random.randint(0,SCREEN_WIDTH - 64),
                random.randint(100, SCREEN_HEIGHT - 164),
                2
                )
            self.monster_group.add(purple_monster)

            yellow_monster = Monster(
                self.all_monster_images[3],
                random.randint(0,SCREEN_WIDTH - 64),
                random.randint(100, SCREEN_HEIGHT - 164),
                3

            )
            self.monster_group.add(yellow_monster)



    def draw(self):

        blue_color = (18,180,237)
        green_color = (111,220,41)
        purple_color = (223,23,246)
        yellow_color = (245,167,21)
        ALL_COLORS = (
            blue_color,
            green_color,
            purple_color,
            yellow_color
        )

        score_text = self.font.render(f"Score:{self.score}", True, (100,230,220))
        score_rect = score_text.get_rect(topleft=(0,10))
        lives_text = self.font.render(f"lives:{self.player.lives}", True, (100,230,220))
        lives_rect = lives_text.get_rect(topright=(SCREEN_WIDTH,10))
        warp_text = self.font.render(f"warp:{self.player.warp_counter}", True, (100,230,220))
        warp_rect = warp_text.get_rect(topleft=(0,50))
        SCREEN.blit(score_text, score_rect)
        SCREEN.blit(lives_text, lives_rect)
        SCREEN.blit(warp_text, warp_rect)
        SCREEN.blit(self.target_monster_image, self.target_monster_rect)

        pygame.draw.rect(SCREEN, ALL_COLORS[self.target_monster_type],(0, 100, SCREEN_WIDTH, SCREEN_HEIGHT - 200),6)

    
    def update(self):
        self.check_collisions()
    
    def change_target(self):
        target = random.choice(self.monster_group.sprites())
        self.target_monster_type = target.type
        self.target_monster_image = target.image

    def game_over(self):
        game_over_text = self.font.render("Game is over", True, (17,150,123))
        game_over_rect = game_over_text.get_rect(center = (SCREEN_WIDTH/2, SCREEN_HEIGHT/2))
        continue_text = self.font.render("Press 'Enter' to Continue...", True, (17,150,123))
        continue_rect = continue_text.get_rect(center = (SCREEN_WIDTH/2, SCREEN_HEIGHT/2 + 60))
        score_text = self.font.render(f"Score:{self.score}", True, (100,230,220))
        score_rect = score_text.get_rect(topleft=(0,10))
        lives_text = self.font.render(f"lives:{self.player.lives}", True, (100,230,220))
        lives_rect = lives_text.get_rect(topright=(SCREEN_WIDTH,10))
        SCREEN.fill((0,0,0))
        SCREEN.blit(score_text, score_rect)
        SCREEN.blit(lives_text, lives_rect)
        SCREEN.blit(game_over_text, game_over_rect)
        SCREEN.blit(continue_text, continue_rect)
        pygame.display.update()
        paused = True
        while paused:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        paused = False
                        self.score = 0
                        self.player.lives = 3
                        self.monster_group.empty()
                        self.player.reset()
                        self.level_number = 0
                        self.start_new_level()
                        

        


    def check_collisions(self):
        collided_monster = pygame.sprite.spritecollideany(self.player, self.monster_group)
        if collided_monster:
            if collided_monster.type == self.target_monster_type:
                collided_monster.remove(self.monster_group)
                self.catch_sound.play()
                self.score += 1
                if len(self.monster_group):
                    self.change_target()
                else:
                    self.start_new_level()
                    self.player.reset()
                    self.next_level_sound.play()
            else:
                self.player.lives -= 1
                self.die_sound.play()
                self.player.reset()
                if self.player.lives <= 0:
                    self.game_over()
