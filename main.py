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
        self.time_since_start = 0

    def run(self):
        while True:
            self.clock.tick(FPS)
            # self.time_since_start += 1 / 60
            # if self.time_since_start >= 10:
            #     Destroy(self.demo_level)
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