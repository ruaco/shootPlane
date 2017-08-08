import pygame
from util import rect_intersects


class Player:
    def __init__(self):
        self.image = pygame.image.load("resource/player.png")
        self.x = 145
        self.y = 250
        rect = self.image.get_rect()
        self.width = rect.right - rect.left
        self.height = rect.bottom - rect.top
        self.speed = 5

    def position(self):
        return [self.x, self.y]

    def move(self, x, y):
        if x < 0:
            x = 0
        if x > 300 - self.width:
            x = 300 - self.width
        self.x = x
        if y < 0:
            y = 0
        if y > 350 - self.height:
            y = 350 - self.height
        self.y = y

    def move_left(self):
        self.move(self.x - self.speed, self.y)

    def move_right(self):
        self.move(self.x + self.speed, self.y)

    def move_up(self):
        self.move(self.x, self.y - self.speed)

    def move_down(self):
        self.move(self.x, self.y + self.speed)

    def collide(self, ball):
        return rect_intersects(self, ball) or rect_intersects(ball, self)
