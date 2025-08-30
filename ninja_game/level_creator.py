import pygame
from tile_image_loader import *
pygame.init()
WIDTH = 1000
HEIGHT = 650

SIDE_MARGIN = 300
BOTTOM_MARIN = 100
screen = pygame.display.set_mode((WIDTH + SIDE_MARGIN, HEIGHT + BOTTOM_MARIN))
bg_image = pygame.image.load("./freegui/png/BG.png")
bg_image = pygame.transform.scale(bg_image, (WIDTH , HEIGHT))
FPS = 60

TILE_SIZE = 50
ROWS = HEIGHT // TILE_SIZE
COLS = 150
clock = pygame.time.Clock()
scroll = 0

world_data = []

for i in range(ROWS):
    temp = [-1] * COLS
    world_data.append(temp)

def show_tiles_on_the_grid():
    for i in range(len(world_data)):
        for j in range(len(world_data[i])):
            if world_data[i][j] != -1:
                screen.blit(tiles_objects_buttons[world_data[i][j]].image, 
                            (j * TILE_SIZE - scroll, i * TILE_SIZE))

def draw_background():
    for i in range(4):
        screen.blit(bg_image, (i * bg_image.get_size()[0] - scroll ,0))

    for i  in  range(ROWS + 1):
        pygame.draw.line(screen, "black", (0, i * TILE_SIZE), (WIDTH, i * TILE_SIZE))
    for i  in  range(COLS + 1):
        pygame.draw.line(screen, "black", (i * TILE_SIZE - scroll, 0), (i * TILE_SIZE - scroll, HEIGHT))
    

tile_index = 0
col_index = 0
row_index = 0

tiles_objects_buttons = objects_buttons + tiles_buttons
def check_click_on_tiles():
    global tile_index
    for i, btn in enumerate(tiles_objects_buttons):
        if btn.check_click():
            tile_index = i

scroll = 0
scroll_left, scroll_right = (False, False)

current_level = 1

font = pygame.font.SysFont("arial", 24)
level_text = font.render(f"Level : {current_level}", True, "black")


up_arrow = "./buttons/arrow.png"
down_arrow = "./buttons/down_arrow.png"

up_button = Button(150, HEIGHT + BOTTOM_MARIN // 2, up_arrow, 50)
down_button = Button(200, HEIGHT + BOTTOM_MARIN // 2, down_arrow, 50)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                scroll_left = True
            if event.key == pygame.K_RIGHT:
                scroll_right = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                scroll_left = False
            if event.key == pygame.K_RIGHT:
                scroll_right = False

    if scroll_left and scroll > 0:
        scroll -= 5
    if scroll_right and scroll < 3 * bg_image.get_size()[0]:
        scroll += 5
    draw_background()
    show_tiles_on_the_grid()
    pygame.draw.rect(screen, "white", (WIDTH, 0, SIDE_MARGIN, HEIGHT + BOTTOM_MARIN))
    pygame.draw.rect(screen, "white", (0, HEIGHT, WIDTH + SIDE_MARGIN,  BOTTOM_MARIN))
    show_tiles(screen)
    check_click_on_tiles()
    screen.blit(level_text, (20, HEIGHT + 40))
    up_button.draw(screen)
    down_button.draw(screen)


    mouse_position = pygame.mouse.get_pos()
    col_index = (mouse_position[0] + scroll) // TILE_SIZE
    row_index = mouse_position[1] // TILE_SIZE
    if mouse_position[0] < WIDTH and mouse_position[1] < HEIGHT:
        if pygame.mouse.get_pressed()[0]:
            world_data[row_index][col_index] =  tile_index

        elif pygame.mouse.get_pressed()[2]:
            world_data[row_index][col_index] = -1


   

    pygame.display.update()

    dt = clock.tick(FPS) / 1000
    
