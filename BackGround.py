import pygame


class BackGround:
    def __init__(self, source):
        self.image = pygame.image.load(source)
        rect = self.image.get_rect()
        self.width = rect.right - rect.left
        self.height = rect.bottom - rect.top
        self.x = 0
        self.y = 0

    def position(self):
        return [self.x, self.y]
