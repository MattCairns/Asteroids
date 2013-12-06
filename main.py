import pygame
from pygame.locals import *
import sys
import ship
import enemy
import helper

pygame.init()

#Set screen resolution
screen = pygame.display.set_mode((800, 600))
pygame.display.flip()

#Initialize clock to control framerate
clock = pygame.time.Clock()

#Text in corner
font = pygame.font.SysFont('Helvetica', 12)
font2 = pygame.font.SysFont('Helvetica', 15)
SCORE = 0
game_over = False

#Collidable objects for the player
collide_sprites_list = pygame.sprite.Group()

player_ship = ship.Ship(400, 300)


bullets = []


def main():
    global SCORE
    global game_over
    while True:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    sys.exit()
                if event.key == K_SPACE:
                    bullet = ship.Bullet(player_ship.rect.x,
                                         player_ship.rect.y,
                                         player_ship.get_ship_angle())
                    bullets.append(bullet)

        screen.fill((0, 0, 0))

        for bullet in bullets[:]:
            sprite_hit_list = pygame.sprite.spritecollide(bullet, collide_sprites_list, True)
            bullet.update()
            bullet.draw(screen)

            for hit in sprite_hit_list[:]:
                bullets.remove(bullet)
                SCORE += 1
                print 'collide'
                break

            if bullet.rect.y > 600 or bullet.rect.y < 0 or bullet.rect.x > 800 or bullet.rect.x < 0:
                bullets.remove(bullet)
                print 'remove'
                break

        player_hit_test = pygame.sprite.spritecollide(player_ship, collide_sprites_list, True)
        for hit in player_hit_test[:]:
            game_over = True

        enemy.create_random_enemy(collide_sprites_list)

        collide_sprites_list.update()
        collide_sprites_list.draw(screen)

        player_ship.controls()
        player_ship.draw(screen)
        player_ship.update()

        #Display text
        fps_label = font.render('FPS: %d' %(clock.get_fps()), 1, (255, 255, 255))
        screen.blit(fps_label, (10, 10))
        score_label = font2.render('Score: %d' % SCORE, 1, (255, 255, 255))
        screen.blit(score_label, (10, 30))

        while game_over:
            helper.game_over(screen)

        pygame.display.flip()

main()


