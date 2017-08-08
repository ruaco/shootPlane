import pygame


class Bullet:
    def __init__(self, pos):
        self.image = pygame.image.load("resource/bullet1.png")
        rect = self.image.get_rect()
        self.width = rect.right - rect.left
        self.height = rect.bottom - rect.top
        self.x = pos[0]
        self.y = pos[1]
        self.speed = 3
        self.fired = False
        self.valid = True

    def size(self):
        return [self.width, self.height]

    def position(self):
        return [self.x, self.y]

    def fire(self):
        self.fired = True

    def invalid(self):
        self.valid = False

    def move(self):
        if self.fired:
            self.y = self.y - self.speed
