import pygame
from pygame.locals import *
import sys
import ship
import enemy

pygame.init()

#Set screen resolution
screen = pygame.display.set_mode((800, 600))
pygame.display.flip()
#Initialize clock to control framerate
clock = pygame.time.Clock()

#List of all sprites in the game
all_sprites_list = pygame.sprite.Group()

#Collidable objects for the player
collide_sprites_list = pygame.sprite.Group()



player_ship = ship.Ship(400, 300)

#for i in range(10):
#    #Create a new enemy
#    enemy_ufo = enemy.Enemy()
#
#    #Add the sprites to the sprite lists
#    all_sprites_list.add(enemy_ufo)
#    collide_sprites_list.add(enemy_ufo)

bullets = []

def main():
    while True:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE or event.type == pygame.QUIT:
                    sys.exit()
                if event.key == K_SPACE:
                    bullet = ship.Bullet(player_ship.rect.x, player_ship.rect.y, player_ship.get_ship_angle())
                    bullets.append(bullet)

        screen.fill((0, 0, 0))
        player_ship.controls()

        for i in range(len(bullets)):
            sprite_hit_list = pygame.sprite.spritecollide(bullets[i], collide_sprites_list, True)
            bullets[i].update()
            bullets[i].draw(screen)

        player_ship.check()
        player_ship.update_angle(screen)
        player_ship.update()


        pygame.display.update()



main()


