from league import *
import pygame


class Player(Character):
    def __init__(self, z=0, x=0, y=0):
        super().__init__(z, x, y)
        self.health = 100
        self.delta = 512
        self.x = x
        self.y = y
        self.change_x = 0
        self.change_y = 0
        self.image = pygame.image.load('./assets/knight/knight-blue-IDLE-00.png').convert_alpha()
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

    def jump(self, time):
        if self.rect.y + self.rect.height >= 364:
            self.change_y = -10

    def update(self, time):
        self.gravity_calc()
        self.rect.x = self.x
        self.rect.y += self.change_y

    def gravity_calc(self):
        if self.change_y == 0:
            self.change_y = 10
        else:
            self.change_y += 1.0
            
        if self.rect.y + self.rect.height >= 364 and self.change_y >= 0:
            self.change_y = 0
            self.rect.y = 364 - self.rect.height

