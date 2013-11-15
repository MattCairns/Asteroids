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

    def controls(self, screen):
        keys = pygame.key.get_pressed()
        if keys[K_LEFT]:
            self.x -= 5
        if keys[K_RIGHT]:
            self.x += 5


class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y, screen):
        pygame.sprite.Sprite.__init__(self)
        self.bullet = pygame.image.load('Assets/bullet.png').convert()
        print 'BULLET'
        self.x = x
        self.y = y

    def draw(self, screen):
        screen.blit(self.bullet, (self.x, self.y))

    def update(self):
        self.y -= 10


