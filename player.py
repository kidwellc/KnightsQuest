from league import *
import pygame


class Player(Character):
    def __init__(self, z=0, x=0, y=0):
        super().__init__(z, x, y)
        self.health = 100
        self.delta = 512
        self.x = x
        self.y = y
        self.image = pygame.image.load('./assets/porcupine.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (64, 64))
        self.rect = self.image.get_rect()
        self.world_size = (Settings.width, Settings.height)

    def move_left(self, time):
        amount = self.delta * time
        try:
            if self.x - amount < 0:
                raise OffScreenLeftException
            else:
                self.x = self.x - amount
                self.update(0)

        except:
            pass

    def move_right(self, time):
        amount = self.delta * time
        try:
            if self.x + amount > self.world_size[0] - Settings.tile_size:
                raise OffScreenRightException
            else:
                self.x = self.x + amount
                self.update(0)

        except:
            pass

    def update(self, time):
        self.rect.x = self.x
        self.rect.y = self.y
        self.gravityCalc()
"""
    def gravity_calc(self):
        if self.y == 0:
            self.y = 1
        else:
            self.y += .35
            
        if self.rect.y >= SCREEN_HEIGHT - self.rect.height and self.y >= 0:
            self.y = 0
            self.rect.y = SCREEN_HEIGHT - self.rect.height
"""
