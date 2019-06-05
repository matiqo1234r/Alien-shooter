import pygame, sys
from pygame.locals import *


class Background():

    def __init__(self, window):
        self.background_image = pygame.Surface(window)
        self.background_image = pygame.image.load(
            'images/galaxy_background.jpeg')


    def draw(self, screen):
        screen.blit(self.background_image, (0, 0))
