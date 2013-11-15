import pygame
from pygame.locals import *


class Ship(pygame.sprite.Sprite):
    """All of the logic for the players ship is contained
        within this class"""

    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.ship = pygame.image.load('Assets/spaceship.png').convert()
        self.y = y
        self.x = x

    def draw(self, screen):
        screen.blit(self.ship, (self.x, self.y))

    def controls(self):
        keys = pygame.key.get_pressed()
        if keys[K_LEFT]:
            self.x -= 5
        if keys[K_RIGHT]:
            self.x += 5