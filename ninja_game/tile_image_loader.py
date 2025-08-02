import pygame
import os
from button import Button
objects_images_list = []
tiles_images_list = list()
TILE_SIZE = 50
WIDTH = 1000
HEIGHT = 640
objects_names = os.listdir('./freescifiplatform/png/Objects')
tiles_names = os.listdir('./freescifiplatform/png/tiles')

for obj in objects_names:
    img = f"./freescifiplatform/png/Objects/{obj}"
    objects_images_list.append(img)
for tile in tiles_names:
    img = f"./freescifiplatform/png/Tiles/{tile}"
    tiles_images_list.append(img)

objects_buttons = []
r = 0
for i,obj in enumerate(objects_images_list):
    if i % 4 == 0:
        r += 1
    btn = Button(WIDTH + 50 + i % 4 * 70 , r * 70, objects_images_list[i], TILE_SIZE)
    objects_buttons.append(btn)

tiles_buttons = []

for i,obj in enumerate(tiles_images_list):
    if i % 4 == 0:
        r += 1
    btn = Button(WIDTH + 50 + i % 4 * 70 , r * 70, tiles_images_list[i], TILE_SIZE)
    tiles_buttons.append(btn)



print(len(objects_images_list))
print(len(tiles_images_list))

def show_tiles(screen):
    for obj in objects_buttons:
        screen.blit(obj.image, obj.rect)
    for t in tiles_buttons:
        screen.blit(t.image, t.rect)
