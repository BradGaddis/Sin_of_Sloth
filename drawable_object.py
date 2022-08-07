import pygame
from settings import *

class Drawable_Object(pygame.sprite.Sprite):
    def __init__(self,pos,groups, img_path):
        super().__init__(groups)
        if img_path:
            self.image = pygame.image.load(img_path).convert_alpha()
            self.rect = self.image.get_rect(topleft = pos)
        
        