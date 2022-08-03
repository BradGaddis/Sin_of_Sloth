from ast import While
from turtle import Screen, screensize
import pygame,sys
from level import Level
from settings import *


class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        pygame.display.set_caption("Sin of Sloth")
        self.demo_level = Level()


    def run(self):
        while True:
            # self.clock.tick(FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            self.screen.fill('sky blue')
            self.demo_level.run()
            pygame.display.update()



if __name__ == "__main__":
    game = Game()
    game.run()