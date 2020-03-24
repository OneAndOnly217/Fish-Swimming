import pygame

from pygame.locals import *

pygame.init()

screen_info = pygame.display.Info()
# set the width and height to the size of the screen
size = (width, height) = (int(screen_info.current_w), int(screen_info.current_h))
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
color = (0, 127, 255)


def main():
    while True:
        clock.tick(60)
        screen.fill((0, 127, 255))
        pygame.display.flip()


if __name__ == '__main__':
    main()
