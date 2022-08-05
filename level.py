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
                    Player((x,y), self.player)


    def Vertical_Collision(self):
        player = self.player.sprite
        player.Apply_Gravity()
        for sprite in self.collidable_sprites:
            has_collided = sprite.rect.colliderect(player)
            if has_collided:
                if player.direction.y > 0:
                    player.rect.bottom = sprite.rect.top
                    player.direction.y = 0
                if player.direction.y < 0:
                    player.rect.top = sprite.rect.bottom
                    player.direction.y = 0

  


    def Horizontal_Collision(self):
        player = self.player.sprite
        player.Move_Horizontal()
        for sprite in self.collidable_sprites:
            has_collided = sprite.rect.colliderect(player)
            if has_collided:
                if player.direction.x < 0:
                    player.rect.left = sprite.rect.right
                if player.direction.x > 0:
                    player.rect.right = sprite.rect.left

    def run(self):
        self.visible_sprites.draw(self.surface)
        self.visible_sprites.update()
        self.player.draw(self.surface)
        self.player.update()
        self.Vertical_Collision()
        self.Horizontal_Collision()
        self.player.update()