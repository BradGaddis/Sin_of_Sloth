import pygame
from settings.settings import *


class Drawable_Object(pygame.sprite.Sprite):
    def __init__(self, pos , groups, img_path = None, size = None):
        super().__init__(groups)
        if img_path:
            self.image = pygame.image.load(img_path).convert_alpha()
            self.rect = self.image.get_rect(topleft = pos)
        elif size:
            self.surf = pygame.surface(size)
            # self.surf.fill("Black")
            self.rect = self.surf.get_rect(topleft = pos)
            print("was called")

    def update(self, x = 0, y = 0):
        self.rect.x += x
        self.rect.y += y
        