import pygame
from settings import *
from drawable_object import *

class Tile(Drawable_Object):
    def __init__(self,pos,groups):
        self.img_path = "./assets/placeholder tile.png"
        super().__init__(pos,groups, self.img_path)
        