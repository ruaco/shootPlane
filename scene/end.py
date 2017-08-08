import pygame
import sys
import scene.base
import scene.start
from BackGround import BackGround


class EndScene(scene.base.BaseScene):

    def __init__(self, game, complete):
        super().__init__(game)
        self.back_ground = BackGround("resource/end_bg.jpg")
        self.complete = complete
        self.register_action(pygame.K_SPACE, self.enter)
        self.register_action(pygame.K_q, sys.exit)

    def enter(self):
        new_s = scene.start.StartScene(self.game)
        self.game.scene(new_s)

    def draw(self):
        self.draw_image(self.back_ground)

    def update(self):
        pass
