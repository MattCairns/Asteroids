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
        self.rect.y = random.randint(100, 600) * -1
        self.rect.x = random.randint(80, 720)

        self.pxlen = 80

    def random_location(self):
        location = random.randint(1, 4)


    def update(self):
        self.rect.y += 2
        if self.rect.x < 0 - self.pxlen:
            self.rect.x = 800
        if self.rect.x > 800 + self.pxlen:
            self.rect.x = 0
        if self.rect.y < 0 - self.pxlen:
            self.rect.y = 600
        if self.rect.y > 600 + self.pxlen:
            self.rect.y = 0


def create_random_enemy(sprite_list):
    n = random.randint(0, 120)
    if n > 118:
        sprite_list.add(Enemy())

    return sprite_list