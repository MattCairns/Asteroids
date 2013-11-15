class Ship(pygame.sprite.Sprite):
    """All of the logic for the players ship is contained
        within this class"""

    def __init__(self):
        pos = pygame.mouse.get_pos()
        self.rect.midtop = pos
