import pygame



def game_over(screen, game_over):
    font = pygame.font.SysFont('Helvetica', 30)
    fps_label = font.render('GAME OVER', 1, (255, 0, 0))
    screen.blit(fps_label, (400,300))


