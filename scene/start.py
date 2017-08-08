import pygame
import sys
import scene.base
import scene.core
from BackGround import BackGround


class StartScene(scene.base.BaseScene):

    def __init__(self, game):
        super().__init__(game)
        self.back_ground = BackGround("resource/title_bg.jpg")
        self.register_action(pygame.K_SPACE, self.enter)
        self.register_action(pygame.K_q, sys.exit)

    def enter(self):
        new_s = scene.core.CoreScene(self.game, 0)
        self.game.scene(new_s)

    def draw(self):
        self.draw_image(self.back_ground)

    def update(self):
        pass
