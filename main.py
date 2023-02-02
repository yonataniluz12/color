import pygame
from constants import *


def main():
    pygame.init()
    color = (RED, WHITE)
    screen_size = (WINDOW_WIDTH, WINDOW_HEIGHT)
    screen = pygame.display.set_mode(screen_size)
    pygame.display.set_caption("color game")
    finish = False
    while not finish:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                screen.fill(color)
            if event.type == pygame.QUIT:
                finish = True
        pygame.display.flip()
    pygame.quit()


main()
