from distutils.log import debug
import pygame
from debug import Debug
from player import Player
from settings import *
from tile import Tile

class Level:
    def __init__(self):
        self.surface = pygame.display.get_surface()
        
        # set sprite groups
        # self.tiles = pygame.sprite.Group()  
        self.visible_sprites = pygame.sprite.Group()
        self.collidable_sprites = pygame.sprite.Group()
        self.player = pygame.sprite.GroupSingle()

        self.setup_level()



    def setup_level(self):
        for row_index, row in enumerate(TEST_MAP):
            for col_index, col in enumerate(row):
                x = col_index * TILE_SIZE 
                y = row_index * TILE_SIZE 
                if col == 'X':
                    Tile((x,y), [self.visible_sprites, self.collidable_sprites])
                if col == 'P':
                    player_sprite = Player((x,y), [self.player, self.visible_sprites])
                    self.player.add()


    def collisions(self):
        for tile in self.collidable_sprites:
            if player_sprite 

    def run(self):
        self.visible_sprites.draw(self.surface)
        self.visible_sprites.update()
        self.player.update()
        self.collisions()