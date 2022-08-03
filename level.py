import pygame
from settings import *
from tile import Tile

class Level:
    def __init__(self):
        self.surface = pygame.display.get_surface()
        
        # set sprite groups
        self.visible_sprites = pygame.sprite.Group()
        self.obstacle_sprites = pygame.sprite.Group()

        self.draw_map()


    def draw_map(self):
        for row_index, row in enumerate(TEST_MAP):
            for col_index, col in enumerate(row):
                x = col_index * TILE_SIZE 
                y = row_index * TILE_SIZE 
                if col == 'X':
                    Tile((x,y), [self.visible_sprites])
    
    def run(self):
        self.visible_sprites.draw(self.surface)
        self.visible_sprites.update()