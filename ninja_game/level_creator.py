import pygame
from tile_image_loader import objects_images_list, tiles_images_list, show_tiles
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
def draw_background():
    for i in range(4):
        screen.blit(bg_image, (i * bg_image.get_size()[0] - scroll ,0))

    for i  in  range(ROWS + 1):
        pygame.draw.line(screen, "black", (0, i * TILE_SIZE), (WIDTH, i * TILE_SIZE))
    for i  in  range(COLS + 1):
        pygame.draw.line(screen, "black", (i * TILE_SIZE, 0), (i * TILE_SIZE, HEIGHT))
    pygame.draw.rect(screen, "white", (WIDTH, 0, SIDE_MARGIN, HEIGHT + BOTTOM_MARIN))
    pygame.draw.rect(screen, "white", (0, HEIGHT, WIDTH + SIDE_MARGIN,  BOTTOM_MARIN))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    draw_background()
    show_tiles(screen)
    pygame.display.update()

    dt = clock.tick(FPS) / 1000
    
