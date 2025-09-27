from box import Box
from energy import Energy
from tile_image_loader import all_images
class World:
    def __init__(self, world_data,box_group, energy_group):
        self.data = world_data

        for i in range(len(world_data)):
            for j in range(len(world_data[i])):
                if world_data[i][j] in (13,14):
                    b = Box(
                        all_images[world_data[i][j]],
                        j * 50, i  * 50, box_group
                            )
                elif world_data[i][j] == 1:
                    e = Energy(all_images[world_data[i][j]], j * 50, i  * 50, energy_group)

