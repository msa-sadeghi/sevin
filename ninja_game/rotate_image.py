import pygame

pygame.init()

image= pygame.image.load("./buttons/arrow.png")
rotated_image = pygame.transform.rotate(image, 180)
pygame.image.save(rotated_image, "down_arrow.png")