import pygame
from settings import *
from drawable_object import Drawable_Object

class Player(Drawable_Object):
    def __init__(self,pos,groups):
        self.img_path = "./assets/player.png"
        super().__init__(pos,groups,self.img_path)

        self.direction = pygame.math.Vector2(0,0)
        self.jumpforce = 1

    def get_input(self):
        keys = pygame.key.get_pressed()
        
        if keys[pygame.K_RIGHT]:
            self.direction.x = 1
        elif keys[pygame.K_LEFT]:
            self.direction.x = -1
        else:
            self.direction.x = 0
        
        if keys[pygame.K_SPACE]:
            self.direction.y += self.jump_force
        else:
            self.jumpforce = 0

    def Collide(self):
        pass

    def Create_Gravity(self):
        pass

    def Jump(self):
        pass

    def Move_Horizontal(self):
        self.rect.x += self.direction.x

    def update(self):
        self.get_input()
        self.Move_Horizontal()


    