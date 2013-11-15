import pygame
from pygame.locals import *
import sys

pygame.init()

#Set screen resolution
screen = pygame.display.set_mode((640, 480))


#Load the player assets
ship = pygame.image.load('Assets/spaceship.png').convert()


while True:
    for event in pygame.event.get():
        if event.type in (QUIT, KEYDOWN):
            sys.exit()

    pygame.display.update()
    screen.blit(ship, (320, 240))
