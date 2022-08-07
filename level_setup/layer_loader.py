# from player.player import Player
# from settings.settings import TILE_SIZE
# from support.tile import Cut_Tile_Placer
from os import walk
from support.support import Import_CSV
from support.tile import Cut_Tile_Placer, Tile
from player.player import Player, player_speed
from settings.settings import TILE_SIZE

test_dir = "tilesets\export_map\prototype"

def Get_Layer_Paths(dir):
    layer_list = []
    for _, __, csv_file in walk(dir):
        layer_list = csv_file
    # print(layer_list)

    output = []
    for layer in layer_list:
        output.append(f"{dir}\{layer}")
    print(output)
    return output



def setup_level(path, tiles, groups = None):
    layers = Get_Layer_Paths(path)
    for layer in layers:
        add_tile_to_group(layer, tiles, groups) 

   
def add_tile_to_group(layer_csv, scliced_tiles,groups):
    layout = Import_CSV(layer_csv)
    for row_index, row in enumerate(layout):
        for col_index, col in enumerate(row):
            value = int( layout[row_index][col_index])
            if value > -1:
                x = col_index * TILE_SIZE 
                y = row_index * TILE_SIZE 
                Cut_Tile_Placer((x,y),groups, value, scliced_tiles)
    # Player((1*TILE_SIZE,1 * TILE_SIZE), player)


Get_Layer_Paths(test_dir)