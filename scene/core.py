import pygame
import sys
from bullet import Bullet
from player import Player
from enemy import Enemy
import scene.base as base
import scene.end as end
from BackGround import BackGround


class CoreScene(base.BaseScene):

    level = 0

    player = None
    bullets = []
    enemys = []

    def __init__(self, game, level=0):
        super().__init__(game)
        self.level = level
        self.back_ground = BackGround("resource/bg.jpg")

        player = Player()
        self.player = player

        self.cool_down = 0
        enemys = []
        for i in game.config.get('level')[self.level]:
            enemys.append(Enemy(i))

        self.register_action(pygame.K_LEFT, player.move_left)
        self.register_action(pygame.K_RIGHT, player.move_right)
        self.register_action(pygame.K_UP, player.move_up)
        self.register_action(pygame.K_DOWN, player.move_down)
        self.register_action(pygame.K_SPACE, self.fire)
        self.register_action(pygame.K_ESCAPE, sys.exit)
        self.draw(player=player, enemys=enemys)

    def update(self):
        enemys = self.enemys
        bullets = self.bullets
        for i in enemys:
            for j in bullets:
                if i.collide(j):
                    i.kill()
                    j.invalid()
                    self.game.score += 100
            if i.collide(self.player):
                self.game.score = 0
                new_s = end.EndScene(self.game, False)
                self.game.scene(new_s)

    def fire(self):
        if self.cool_down == 0:
            pos = self.player.position()
            bullet = Bullet(pos)
            self.bullets.append(bullet)
            self.cool_down = 5
        else:
            self.cool_down -= 1

    def draw(self, **kwargs):
        self.draw_image(self.back_ground)
        for i in kwargs.keys():
            if i == 'player':
                self.player = kwargs.get(i)
            if i == 'enemys':
                self.enemys = kwargs.get(i)

        player = self.player
        if player is not None:
            self.draw_image(player)

        enemys = self.enemys
        enemys_exist = False
        for i in enemys:
            if i.alive:
                enemys_exist = enemys_exist or True
                self.draw_image(i)
                i.move()
        if not enemys_exist:
            self.enemys = []
            for i in range(3):
                e = Enemy([0, 0], True)
                self.enemys.append(e)
                e.move()

        bullets_temps = []
        for i in self.bullets:
            if i.valid:
                self.draw_image(i)
                i.fire()
                i.move()
                bullets_temps.append(i)
        self.bullets = bullets_temps

        self.draw_text('score: ' + str(self.game.score), [20, 20])

