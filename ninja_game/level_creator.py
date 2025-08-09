import pygame
from tile_image_loader import *
pygame.init()
WIDTH = 1000
HEIGHT = 640

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
                screen.blit(tiles_objects_buttons[world_data[i][j]].image, (j * TILE_SIZE, i * TILE_SIZE))

def draw_background():
    for i in range(4):
        screen.blit(bg_image, (i * bg_image.get_size()[0] - scroll ,0))

    for i  in  range(ROWS + 1):
        pygame.draw.line(screen, "black", (0, i * TILE_SIZE), (WIDTH, i * TILE_SIZE))
    for i  in  range(COLS + 1):
        pygame.draw.line(screen, "black", (i * TILE_SIZE, 0), (i * TILE_SIZE, HEIGHT))
    pygame.draw.rect(screen, "white", (WIDTH, 0, SIDE_MARGIN, HEIGHT + BOTTOM_MARIN))
    pygame.draw.rect(screen, "white", (0, HEIGHT, WIDTH + SIDE_MARGIN,  BOTTOM_MARIN))

tile_index = 0
col_index = 0
row_index = 0

tiles_objects_buttons = objects_buttons + tiles_buttons
def check_click_on_tiles():
    global tile_index
    for i, btn in enumerate(tiles_objects_buttons):
        if btn.check_click():
            tile_index = i



running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    draw_background()
    show_tiles(screen)
    check_click_on_tiles()
    show_tiles_on_the_grid()
    mouse_position = pygame.mouse.get_pos()
    col_index = mouse_position[0] // TILE_SIZE
    row_index = mouse_position[1] // TILE_SIZE
    if mouse_position[0] < WIDTH and mouse_position[1] < HEIGHT:
        if pygame.mouse.get_pressed()[0]:
            world_data[row_index][col_index] =  tile_index

   

    pygame.display.update()

    dt = clock.tick(FPS) / 1000
    
