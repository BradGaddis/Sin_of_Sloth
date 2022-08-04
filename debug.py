import pygame
pygame.init()
font = pygame.font.Font(None, 30)


def Debug(info, x = 10, y = 10):
    def __init__(self):
        display_surface = pygame.display.get_surface()
        debug_surface = font.render(str(info),False, "white")
        debug_rect = debug_surface.get_rect(topleft = (x,y))
        pygame.draw.rect(display_surface,"black",debug_rect)