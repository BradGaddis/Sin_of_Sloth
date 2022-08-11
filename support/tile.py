import pygame
from settings.settings import *
from support.drawable_object import *

class Tile(Drawable_Object):
    def __init__(self,pos,groups, offset = 0):
        self.img_path = "./assets/placeholder tile.png"
        super().__init__(pos,groups, self.img_path)
        
    def update(self, x = 0, y = 0):
        self.rect.x += x
        self.rect.y += y

class Cut_Tile_Placer(Tile):
    def __init__(self, pos, groups, value, tiles,):
        super().__init__(pos, groups)
        self.image = tiles[value]
        self.rect = self.image.get_rect(topleft = pos)

class Screen_Fill(Tile):
    def __init__(self, pos, groups, size):
        super().__init__(pos, groups)
        self.image = pygame.Surface(size).convert_alpha()
        self.image.set_alpha(1)
        self.rect = self.image.get_rect(topleft = pos)
        # print("was called")
