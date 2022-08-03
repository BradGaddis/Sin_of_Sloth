import pygame

class Player:
    def __init__(self):
        self.image_path = "./assets/player.png"
        self.image = pygame.image.load(self.image_path)