import pygame
from pygame.locals import *
import random
import math


class Enemy(pygame.sprite.Sprite):
    """All of the logic for the players ship is contained
        within this class"""

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('Assets/ufodark.png').convert_alpha()
        self.rect = self.image.get_rect()

        self.rect.x = int(800 * random.random())
        self.rect.y = int(600 * random.random())

        self.pxlen = 80

        self.enemy_angle = random.randint(0, 360)
        self.radians = (math.pi/180) * self.enemy_angle

        self.velocity = random.randint(1, 5)

        self.vel_x = math.sin(self.radians) * self.velocity
        self.vel_y = math.cos(self.radians) * self.velocity

    def update(self):
        self.rect.y -= self.vel_x
        self.rect.x -= self.vel_y

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