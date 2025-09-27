import pygame
from ninja import Ninja
from button import Button
import pickle
from world import World
from tile_image_loader import all_images
pygame.init()
WIDTH = 1000
HEIGHT = 640

screen = pygame.display.set_mode((WIDTH, HEIGHT))
bg_image = pygame.image.load("./freegui/png/BG.png")
bg_image = pygame.transform.scale(bg_image, (WIDTH, HEIGHT))
FPS = 60
clock = pygame.time.Clock()

my_ninja = Ninja(400, 200)

def draw_background():
    for i in range(4):
        screen.blit(bg_image, (i * bg_image.get_size()[0] - scroll ,0))


menu_image = pygame.image.load("freegui/png/windows/Window_06.png")
menu_image = pygame.transform.scale(menu_image, (WIDTH, HEIGHT))
start_button_image_path = "freegui/png/buttons/Button_03.png"
start_button = Button(WIDTH//2, HEIGHT//2, start_button_image_path, 200)
menu_rect = menu_image.get_rect()
game_started = False
def show_menu():
    global game_started
    screen.blit(menu_image, menu_rect)
    start_button.draw(screen)
    if start_button.check_click():
        game_started = True

time_to_scroll = 0
scroll = 0
left_border = WIDTH//3
right_border = WIDTH - WIDTH//3 - 150

level = 1

world_data = []

def load_level(level_number):
    global world_data
    with open(f"levels\level{level_number}", "rb") as f:
        world_data = pickle.load(f)


load_level(level)
box_group = pygame.sprite.Group()
energy_group = pygame.sprite.Group()
game_world = World(world_data, box_group, energy_group)

energy_count = 0
font = pygame.font.SysFont("arial", 22)
energy_count_text = font.render(f"{energy_count}", True, "black")

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    if my_ninja.moving:
        my_ninja.change_animation("Run")
    elif my_ninja.moving == False:
        my_ninja.change_animation("Idle")
    
    if my_ninja.rect.right > right_border and my_ninja.animation == "Run" and my_ninja.direction == 1 and scroll < 3 * bg_image.get_size()[0]:
        
        scroll += 100 * dt
    if my_ninja.rect.left < left_border and my_ninja.animation == "Run" and my_ninja.direction == -1 and scroll > 0:
        
        scroll -= 100 * dt
    if not game_started:
        show_menu()
    else:
        
        draw_background()
        screen.blit(
            pygame.transform.scale(
                pygame.image.load(all_images[1])
                , (40, 40)),
            (10, 10)
        )
        energy_count_text = font.render(f"{my_ninja.energy}", True, "black")
        screen.blit(energy_count_text, (60, 20))
        my_ninja.draw(screen)
        box_group.draw(screen)
        box_group.update(scroll)
        energy_group.draw(screen)
        energy_group.update(scroll, my_ninja)
        my_ninja.move(dt, box_group)
    
    pygame.display.update()
    dt = clock.tick(FPS) / 1000
    