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

        self.pxlen = 50

        self.vel_y = 0.0
        self.vel_x = 0.0

        self.velocity = 0.15
        self.friction = 0.98
        self.current_angle = 90.0

    def controls(self):
        radians = (math.pi/180) * self.current_angle
        keys = pygame.key.get_pressed()
        if keys[K_UP]:
            self.vel_x += math.sin(radians) * self.velocity
            self.vel_y += math.cos(radians) * self.velocity
        if keys[K_LEFT]:
            self.current_angle += 2
        if keys[K_RIGHT]:
            self.current_angle -= 2

    def check(self):
        if self.rect.x < 0 - self.pxlen:
            self.rect.x = 800
        if self.rect.x > 800 + self.pxlen:
            self.rect.x = 0
        if self.rect.y < 0 - self.pxlen:
            self.rect.y = 600
        if self.rect.y > 600 + self.pxlen:
            self.rect.y = 0
        if self.current_angle < 0:
            self.current_angle = 360
        if self.current_angle > 360:
            self.current_angle = 0

    def get_ship_angle(self):
        return self.current_angle

    def update(self):
        self.check()

        self.vel_y *= self.friction
        self.vel_x *= self.friction

        self.rect.x -= self.vel_x
        self.rect.y -= self.vel_y

    def draw(self, screen):
        rot_image = pygame.transform.rotozoom(self.image, self.current_angle, 1)
        rect = rot_image.get_rect().center
        screen.blit(rot_image, (self.rect.x-(rect[1]), self.rect.y-(rect[0])))


class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y, angle):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('Assets/projectile.png').convert_alpha()
        self.rect = self.image.get_rect()

        self.bullet_angle = angle
        self.radians = (math.pi/180) * self.bullet_angle



        self.velocity = 10

        self.vel_x = math.sin(self.radians) * self.velocity
        self.vel_y = math.cos(self.radians) * self.velocity

        self.rect.x = x
        self.rect.y = y

    def update(self):

        self.rect.y -= self.vel_y
        self.rect.x -= self.vel_x

    def draw(self, screen):
        rot_image = pygame.transform.rotozoom(self.image, self.bullet_angle, 1)
        rot_image.get_rect().center = rot_image.get_rect().center
        screen.blit(rot_image, (self.rect.x + 25, self.rect.y + 25))




