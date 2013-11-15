import pygame
from pygame.locals import *
import sys
import ship

pygame.init()

#Set screen resolution
screen = pygame.display.set_mode((480, 800))
pygame.display.flip()
#Initialize clock to control framerate
clock = pygame.time.Clock()

player_ship = ship.Ship(240, 600)

bullets = []

def main():
    while True:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    sys.exit()
                if event.key == K_SPACE:
                    print 'SHOOT'
                    bullets.append(ship.Bullet(player_ship.x, player_ship.y, screen))
        screen.fill((0,0,0))
        player_ship.controls(screen)
        player_ship.draw(screen)

        for i in range(len(bullets)):
            bullets[i].update()
            bullets[i].draw(screen)

        pygame.display.update()



main()


