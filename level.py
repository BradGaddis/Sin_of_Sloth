import pygame
from debug import Debug
from player import Player, player_speed
from settings import *
from support import Import_CSV, Split_TileSet
from tile import Cut_Tile_Placer, Tile

class Level:
    def __init__(self, csv_path = "tilesets\export_map\prototype map.csv", level_path = "assets\placeholder tileset.png"):
        
        # set sprite groups
        self.world_sprites = pygame.sprite.Group()
        self.collidable_sprites = pygame.sprite.Group()
        self.player = pygame.sprite.GroupSingle()

        # tiling stuff
        self.surface = pygame.display.get_surface()
        self.level_path =  "assets\placeholder tileset.png"
        self.csv_path = "tilesets\export_map\prototype map.csv"
        self.level_shift = 0
        self.setup_level()
    
    def Side_Scroll(self):
        player = self.player.sprite
        player_x = player.rect.centerx
        x_direct = player.direction.x

        LEFT_BOUND = SCREEN_WIDTH / 8
        RIGHT_BOUND = SCREEN_WIDTH - LEFT_BOUND

        # if player_x <= LEFT_BOUND or player_x >= RIGHT_BOUND:
        #     self.level_shift = -player.direction.x * player_speed
        #     player.speed = 0
        if player_x <= LEFT_BOUND and x_direct < 0:
            self.level_shift = -player.direction.x * player_speed
            player.speed = 0
        elif player_x >= RIGHT_BOUND and x_direct > 0:
            self.level_shift = -player.direction.x * player_speed
            player.speed = 0
        else:
            self.level_shift = 0
            player.speed = player_speed



    def setup_level(self):
        tiles = Split_TileSet("assets\placeholder tileset.png")
        layout = Import_CSV(self.csv_path)
        for row_index, row in enumerate(layout):
            for col_index, col in enumerate(row):
                value = int(layout[row_index][col_index])
                if value > -1:
                    x = col_index * TILE_SIZE 
                    y = row_index * TILE_SIZE 
                        # Place_Holder_Tiles((x,y), [self.world_sprites, self.collidable_sprites])
                    # print(value)
                    Cut_Tile_Placer((x,y),[self.world_sprites, self.collidable_sprites], value, tiles)
                # if col == 'P':
        Player((1*TILE_SIZE,1 * TILE_SIZE), self.player)
   

    def Vertical_Collision(self):
        player = self.player.sprite
        player.Apply_Gravity()
        for sprite in self.world_sprites:
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
        for sprite in self.world_sprites:
            has_collided = sprite.rect.colliderect(player)
            if has_collided:
                if player.direction.x < 0:
                    player.rect.left = sprite.rect.right
                if player.direction.x > 0:
                    player.rect.right = sprite.rect.left

    def Draw(self):
        self.world_sprites.draw(self.surface)
        self.world_sprites.update(self.level_shift)
        self.collidable_sprites.update(self.level_shift)
        self.player.draw(self.surface)
        self.player.update()
 
    def Check_Collisions(self):
        self.Horizontal_Collision()
        self.Vertical_Collision()

    
    def run(self):
        self.Draw()
        self.Check_Collisions()
        self.Side_Scroll()