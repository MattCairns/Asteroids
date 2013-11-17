import pygame
from pygame.locals import *
import random


class Enemy(pygame.sprite.Sprite):
    """All of the logic for the players ship is contained
        within this class"""

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('Assets/ufodark.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.y = random.randint(80, 400) * -1
        self.rect.x = random.randint(0, 480)

    def update(self):
        self.rect.y += 2