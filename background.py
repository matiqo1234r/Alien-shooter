import pygame, sys
from pygame.locals import *


class Background():

    def __init__(self):
        self.background_image = pygame.image.load(
            '/home/igor/Projects/Pygame/Alien-shooter/images/galaxy_background.jpeg')

    def draw(self, screen):
        screen.blit(self.background_image, (0, 0))
