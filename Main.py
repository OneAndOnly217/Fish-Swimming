import pygame
import sys
import random
from pygame.locals import *

pygame.init()

screen_info = pygame.display.Info()
# set the width and height to the size of the screen
#size = (width, height) = (int(screen_info.current_w), int(screen_info.current_h))
size = (800, 600)
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
color = (0, 127, 255)

fish_image = pygame.image.load("fishy.png")
fish_image = pygame.transform.smoothscale(fish_image, (300, 200))
fish_rect = fish_image.get_rect()
speed = pygame.math.Vector2(0, 10)
rotation = random.randint(40, 360)
print(rotation)
speed.rotate_ip(rotation)
fish_image = pygame.transform.rotate(fish_image, 180 - rotation)

def move_fish():
    fish_rect.move_ip(speed)


def main():
    while True:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == QUIT:
                sys.exit
        screen.fill((0, 127, 255))
        screen.blit(fish_image, fish_rect)
        pygame.display.flip()


if __name__ == '__main__':
    main()
