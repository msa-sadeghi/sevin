import pygame
from ninja import Ninja
from button import Button
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


menu_image = pygame.image.load("freegui/png/windows/Window_06.png")
menu_image = pygame.transform.scale(menu_image, (WIDTH, HEIGHT))
start_button_image_path = "freegui/png/buttons/Button_03.png"
start_button = Button(WIDTH//2, HEIGHT//2, start_button_image_path)
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
        my_ninja.draw(screen)
    
    pygame.display.update()

    dt = clock.tick(FPS) / 1000
    
    my_ninja.move(dt)