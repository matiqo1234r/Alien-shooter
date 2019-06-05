import pygame

from background import Background

pygame.init()

window_size = (800, 600)
screen = pygame.display.set_mode(window_size)

done = False

background = Background(window_size)

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    background.draw(screen)

    # Add this somewhere after the event pumping and before the display.flip()
    pygame.display.flip()
