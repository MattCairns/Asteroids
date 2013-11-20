import pygame
from pygame.locals import *
import math


class Ship(pygame.sprite.Sprite):
    """All of the logic for the players ship is contained
        within this class"""

    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('Assets/starship.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x

        self.vel_y = 0.0
        self.vel_x = 0.0

        self.velocity = 0.1
        self.friction = 0.98
        self.current_angle = 90.0

    def controls(self):
        radians = (math.pi/180) * self.current_angle
        keys = pygame.key.get_pressed()
        if keys[K_UP]:
            self.vel_x += math.sin(radians) * self.velocity
            self.vel_y += math.cos(radians) * self.velocity
        if keys[K_LEFT]:
            self.current_angle += 1
        if keys[K_RIGHT]:
            self.current_angle -= 1

    def check(self):
        if self.rect.x < 0:
            self.rect.x = 800
        if self.rect.x > 800:
            self.rect.x = 0
        if self.rect.y < 0:
            self.rect.y = 600
        if self.rect.y > 600:
            self.rect.y = 0
        if self.current_angle < 0:
            self.current_angle = 360
        if self.current_angle > 360:
            self.current_angle = 0

    def update_angle(self, screen):
        rot_image = pygame.transform.rotozoom(self.image, self.current_angle, 1)
        rot_rect = rot_image.get_rect(center=self.rect.center)
        screen.blit(rot_image, (self.rect.x, self.rect.y))

    def update(self):
        self.vel_y *= self.friction
        self.vel_x *= self.friction

        self.rect.x -= self.vel_x
        self.rect.y -= self.vel_y


class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y, screen):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('Assets/bullet.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def draw(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))

    def update(self):
        self.rect.y -= 10


