import pygame
from debug.debug import Debug
from settings.settings import *

player_speed = 8

class Player(Drawable_Object):
    def __init__(self,pos,groups, speed = player_speed):
        self.img_path = "./assets/player.png"
        super().__init__(pos,groups,self.img_path)
        self.direction = pygame.math.Vector2(0,0)

        # player movement variable factors
        self.gravity_factor = 0.8
        self.jump_speed = -16
        self.speed = player_speed
        self.is_grounded = False

    def Get_Input(self):
        keys = pygame.key.get_pressed()
        
        if keys[pygame.K_RIGHT]:
            self.direction.x = 1
        elif keys[pygame.K_LEFT]:
            self.direction.x = -1
        else:
            self.direction.x = 0
        
        if keys[pygame.K_SPACE] and self.is_grounded:
            self.Jump()
            self.is_grounded = False


    def Apply_Gravity(self):
        self.direction.y += self.gravity_factor
        self.rect.y += self.direction.y

    def Jump(self):
        self.direction.y = self.jump_speed 
 
    def Move_Horizontal(self):
        self.rect.x += self.direction.x  * self.speed

    def update(self):
        self.Get_Input()
        



    