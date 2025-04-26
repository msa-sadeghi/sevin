import pygame
pygame.init()

WIDTH = 800
HEIGHT = 600

SIDE_MARGIN = 200
LOWER_MARGIN = 100

FPS = 60
screen = pygame.display.set_mode((WIDTH + SIDE_MARGIN, HEIGHT + LOWER_MARGIN))
pygame.display.set_caption("Level Editor")  
clock = pygame.time.Clock()


running = True  
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((255, 255, 255))  # Fill the screen with white
    pygame.draw.rect(screen, 'lightblue', (WIDTH, 0, WIDTH + SIDE_MARGIN, HEIGHT + LOWER_MARGIN))  
    pygame.draw.rect(screen, 'lightblue', (0, HEIGHT, WIDTH + SIDE_MARGIN, HEIGHT + LOWER_MARGIN))  
    # Update the display
    pygame.display.flip()
    clock.tick(FPS)
