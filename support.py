import csv
from sys import flags
from settings import TILE_SIZE
import pygame


def Draw_Map():
    pass

MAP_DIRECTORY = "./assets/"

TEST_MAP_NAME = "placeholder tileset.png"

TEST_MAP = MAP_DIRECTORY + TEST_MAP_NAME

def Split_TileSet(path):
    split_tiles = []
    surf_to_split = pygame.image.load(path).convert_alpha()
    num_tiles_x = int(surf_to_split.get_size()[0] / TILE_SIZE)
    num_tiles_y = int(surf_to_split.get_size()[1] / TILE_SIZE)
    for row in range(num_tiles_y):
        for col in range(num_tiles_x):
            x = col * TILE_SIZE            
            y = row * TILE_SIZE
            new_surf = pygame.Surface((TILE_SIZE,TILE_SIZE), flags = pygame.SRCALPHA)
            new_surf.blit(surf_to_split, (0,0), pygame.Rect(x,y,TILE_SIZE, TILE_SIZE))
            split_tiles.append(new_surf)
    return split_tiles



def Import_CSV(path):
    output = []
    with open(path) as map:
        level = csv.reader(map, delimiter=",")
        for row in level: 
            new_index = []
            for col in row:
                new_index.append(col)
            output.append(new_index)
        # print(output)
    return output

# Import_CSV("tilesets\export_map\prototype map.csv")