from box import Box
from tile_image_loader import all_images
class World:
    def __init__(self, world_data,box_group):
        self.data = world_data

        for i in range(len(world_data)):
            for j in range(len(world_data[i])):
                if world_data[i][j] in (13,14):
                    b = Box(
                        all_images[world_data[i][j]],
                        j * 50, i  * 50, box_group
                            )
