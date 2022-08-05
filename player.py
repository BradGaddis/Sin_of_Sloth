import pygame
from debug import Debug
from settings import *
from drawable_object import Drawable_Object

class Player(Drawable_Object):
    def __init__(self,pos,groups):
        self.img_path = "./assets/player.png"
        super().__init__(pos,groups,self.img_path)

        self.direction = pygame.math.Vector2(0,0)

        # player movement variable factors
        self.gravity_factor = 0.8
        self.jump_speed = -16
        self.speed = 8

    def Get_Input(self):
        keys = pygame.key.get_pressed()
        
        if keys[pygame.K_RIGHT]:
            self.direction.x = 1
        elif keys[pygame.K_LEFT]:
            self.direction.x = -1
        else:
            self.direction.x = 0
        
        if keys[pygame.K_SPACE]:
            self.Jump()

    def Collide(self):
        # get directons and move back against it
        pass

    def Apply_Gravity(self):
        self.direction.y += self.gravity_factor
        self.rect.y += self.direction.y

    def Jump(self):
        self.direction.y = self.jump_speed 
 
    def Move_Horizontal(self):
        self.rect.x += self.direction.x  * self.speed

    def update(self):
        # Debug(self.direction)
        self.Get_Input()
        



    