from league import *
import pygame


class Background2(Character):
    def __init__(self, z=0, x=0, y=0):
        super().__init__(z, x, y)

        self.delta = 512
        self.x = x
        self.y = y
        self.image = pygame.image.load('./assets/Background2.png').convert_alpha()

        self.rect = self.image.get_rect()
        self.world_size = (Settings.width, Settings.height)

    def update(self, time):
        self.rect.x = self.x
        self.rect.y = self.y
