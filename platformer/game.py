import pickle
class Game:
    next_level = False
    
    def go_next_level(level, enemy_group, coin_group, door_group, lava_group):
        enemy_group.empty()
        coin_group.empty()
        door_group.empty()
        lava_group.empty()
        with open(f"levels\level{level}", "rb") as f:
            world_data = pickle.load(f)
            
        return world_data