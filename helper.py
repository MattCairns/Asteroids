import pygame


def game_over(screen):
    font = pygame.font.SysFont('Helvetica', 30)
    fps_label = font.render('GAME OVER', 1, (255, 0, 0))
    screen.blit(fps_label, (400,300))


def hud_display(screen, font, clock, score):
    #Display text
    fps_label = font.render('FPS: %d' %(clock.get_fps()), 1, (255, 255, 255))
    screen.blit(fps_label, (10, 10))
    score_label = font.render('Score: %d' % score, 1, (255, 255, 255))
    screen.blit(score_label, (10, 30))
