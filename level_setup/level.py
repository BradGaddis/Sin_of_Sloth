import pygame
from player.player import Player, player_speed
from settings.settings import *
from support.support import Import_CSV, Split_TileSet
from support.tile import Cut_Tile_Placer, Tile
from .layer_loader import tile_grouper
from distutils.log import debug


class Level:
    def __init__(self, csv_path = "tilesets\\export_map\\prototype\\", level_path = "assets\placeholder tileset.png"):
        
        # set sprite groups
        self.world_sprites = pygame.sprite.Group()
        self.collidable_sprites = pygame.sprite.Group()
        self.player = pygame.sprite.GroupSingle()
    
        # group the sprite groups
        self.groups = [self.world_sprites,self.collidable_sprites,self.player]

        # tiling stuff
        self.layers = None
        self.surface = pygame.display.get_surface()
        self.path = csv_path
        # self.layout = Import_CSV(csv_path)
        self.tiles = Split_TileSet(level_path)
        self.setup_level()

        # optics
        self.initial_pos = self.Get_init_pos()
        self.level_shift = 0
        self.align = 0
        # self.map_height = len(self.layout)
        # self.map_offset = SCREEN_HEIGHT - self.map_height * TILE_SIZE
        
    
    def Side_Scroll(self):
        player = self.player.sprite
        player_x = player.rect.centerx
        x_direct = player.direction.x

        LEFT_BOUND = SCREEN_WIDTH / 4
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

    def Get_init_pos(self):
        pos = []
        for sprite in self.world_sprites:
            pos.append(sprite.rect.y)
        return pos

    def Vertical_Align(self):
        for index, sprite in enumerate(self.world_sprites):
            if sprite.rect.y == self.initial_pos[index]:
                sprite.rect.centery += self.map_offset 

    def setup_level(self):
        # for row_index, row in enumerate(self.layout):
        #     for col_index, col in enumerate(row):
        #         value = int(self.layout[row_index][col_index])
        #         if value > -1:
        #             x = col_index * TILE_SIZE 
        #             y = row_index * TILE_SIZE 
        #                 # Place_Holder_Tiles((x,y), [self.world_sprites, self.collidable_sprites])
        #             # print(value)
        #             Cut_Tile_Placer((x,y),[self.world_sprites, self.collidable_sprites], value, self.tiles)
        #         # if col == 'P':
        # Player((1*TILE_SIZE,1 * TILE_SIZE), self.player)
        # groups = [self.world_sprites, self.collidable_sprites, self.player]
        tile_grouper(self.player, self.path,self.tiles, self.groups)
   

    def Vertical_Collision(self):
        player = self.player.sprite
        player.Apply_Gravity()
        grounded = False
        for sprite in self.collidable_sprites:
            has_collided = sprite.rect.colliderect(player)
            if has_collided:
                if player.direction.y > 0:
                    player.rect.bottom = sprite.rect.top
                    player.is_grounded = True
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

    def Draw(self):
        self.player.update()
        self.player.draw(self.surface)
        self.world_sprites.update(self.level_shift)
        self.world_sprites.draw(self.surface)
 
    def Check_Collisions(self):
        self.Horizontal_Collision()
        self.Vertical_Collision()
    
    def Check_Grounded(self):
        return self.player.sprite.is_grounded
    
    def run(self):
        self.Side_Scroll()
        self.Draw()
        self.Check_Collisions()
        debug(self.level_shift)
        # self.Vertical_Align()