import pygame
from util import rect_intersects
import random
import math


class Enemy:
    def __init__(self, position, rd=False):
        self.image = pygame.image.load("resource/enemy0.png")
        self.alive = True
        rect = self.image.get_rect()
        self.width = rect.right - rect.left
        self.height = rect.bottom - rect.top
        self.speed = 1
        self.x = position[0]
        self.y = position[1]
        self.boom_fps = 12
        self.boom_status = False
        if rd:
            self.x = math.floor(random.randint(self.width, 300) - self.width)
            self.y = -math.floor(random.random()*200)

        self.boom = []
        for i in range(self.boom_fps):
            self.boom.append(pygame.image.load("resource/boom{}.png".format(i+1)))

    def kill(self):
        self.boom_status = True

    def size(self):
        return [self.width, self.height]

    def position(self):
        return [self.x, self.y]

    def move(self):
        if self.boom_status:
            if self.boom_fps is not 1:
                self.boom_fps -= 1
                self.image = self.boom[12 - self.boom_fps]
            else:
                self.alive = False
        self.y = self.y + self.speed
        if self.y > 350:
            self.alive = False

    def collide(self, o):
        return self.alive and (rect_intersects(self, o) or rect_intersects(o, self))
