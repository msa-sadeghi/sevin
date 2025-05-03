import pygame
pygame.init()
import os
WIDTH = 800
HEIGHT = 600

SIDE_MARGIN = 400
LOWER_MARGIN = 100
TILE_SIZE = 50

ROWS = HEIGHT // TILE_SIZE
MAX_COLS = 150
FPS = 60
screen = pygame.display.set_mode((WIDTH + SIDE_MARGIN, HEIGHT + LOWER_MARGIN))
pygame.display.set_caption("Level Editor")  
clock = pygame.time.Clock()

objects = []
for img in os.listdir("./game_world/Objects"):
    objects.append(
        pygame.transform.scale_by(pygame.image.load(img), 0.5)
    )

tiles = []
for img in os.listdir("./game_world/Tiles"):
    objects.append(
        pygame.transform.scale_by(pygame.image.load(img), 0.5)
    )

def draw_grid():
    for i in range(ROWS + 1):
        pygame.draw.line(screen, "black", (0, i * TILE_SIZE), (WIDTH, i * TILE_SIZE))
    for j in range(MAX_COLS + 1):
        pygame.draw.line(screen, "black", (j * TILE_SIZE, 0), (j * TILE_SIZE, HEIGHT))

running = True  
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((255, 255, 255))  # Fill the screen with white
    draw_grid()
    pygame.draw.rect(screen, 'lightblue', (WIDTH, 0, WIDTH + SIDE_MARGIN, HEIGHT + LOWER_MARGIN))  
    pygame.draw.rect(screen, 'lightblue', (0, HEIGHT, WIDTH + SIDE_MARGIN, HEIGHT + LOWER_MARGIN))  
    # Update the display
    pygame.display.flip()
    clock.tick(FPS)
