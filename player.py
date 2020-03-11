from league import *
import pygame


class Player(Character):
    def __init__(self, z=0, x=0, y=0):
        super().__init__(z, x, y)
        self.step_count = 0
        self.images = {}
        self.direction = settings.Direction.RIGHT
        self.state = State.IDLE
        self.state_time = pygame.time.get_ticks()
        self.images[State.IDLE] = self.load_images_idle("./assets/knight/knight-blue-IDLE-00")
        self.images[State.ATTACK] = self.load_images_attack("./assets/knight/knight-blue-ATTACK-00")
        self.images[State.JUMP] = self.load_images_jump("./assets/knight/knight-blue-JUMP-00")
        self.images[State.RUN] = self.load_images_run("./assets/knight/knight-blue-RUN-0")
        self.image = self.images[State.IDLE][settings.Direction.RIGHT][0]
        self.frame = 0
        self.health = 100
        self.delta = 512
        self.x = x
        self.y = y
        self.change_x = 0
        self.change_y = 0
        self.image = pygame.transform.scale(self.image, (64, 64))
        self.rect = self.image.get_rect()
        self.world_size = (Settings.width, Settings.height)

    def update_image(self):
        if self.state != State.RUN:
            # print("Image #" + str(self.frame % 12))
            self.image = self.images[self.state][self.direction][self.framed]
        else:
            print(str(self.state) + " facing " + str(self.direction) + " #" + str(self.step_count))
            self.image = self.images[self.state][self.direction][self.step_count]



    def move_left(self, time):
        amount = self.delta * time
        self.switch_state(State.RUN)
        if self.direction == settings.Direction.RIGHT:
            self.switch_dir(settings.Direction.LEFT)
        else:
            self.step_count = (self.step_count + 1) % 12
        self.x = self.x - Settings.tile_size // 2
        self.update_image()
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
        self.switch_state(State.RUN)
        if self.direction == settings.Direction.LEFT:
            self.switch_dir(settings.Direction.RIGHT)
        else:
            self.step_count = (self.step_count + 1) % 12
        self.x = self.x + Settings.tile_size // 2
        self.update_image()
        try:
            if self.x + amount > self.world_size[0] - Settings.tile_size:
                raise OffScreenRightException
            else:
                self.x = self.x + amount
                self.update(0)

        except:
            pass

    def jump(self, time):
        self.switch_state(State.JUMP)
        if self.rect.y + self.rect.height >= 364:
            self.change_y = -10

    def reset_idle(self):
        time = pygame.time.get_ticks()
        elapsed = time - self.state_time
        if elapsed > 100 and self.state == State.RUN:
            self.switch_state(State.IDLE)

    def switch_state(self, state):
        time = pygame.time.get_ticks()
        if self.state != state:
            self.state = state
            self.state_time = time

    def switch_dir(self, direction):
        self.direction = direction
        self.step_count = 0

    def load_images_idle(self, path):
        images = {}
        right = {}
        left = {}
        for i in range(0, 4):
            p = path + str(i) + ".png"
            # print("Loading " + p)
            temp = pygame.image.load(p).convert_alpha()
            # temp = pygame.transform.scale(temp, (Settings.tile_size, Settings.tile_size))
            temp = pygame.transform.scale(temp, (Settings.tile_size * 2, Settings.tile_size * 2))
            right[i] = temp
            left[i] = pygame.transform.flip(temp, True, False)
        images[settings.Direction.RIGHT] = right
        images[settings.Direction.LEFT] = left
        return images

    def load_images_attack(self, path):
        images = {}
        right = {}
        left = {}
        for i in range(0, 8):
            p = path + str(i) + ".png"
            # print("Loading " + p)
            temp = pygame.image.load(p).convert_alpha()
            # temp = pygame.transform.scale(temp, (Settings.tile_size, Settings.tile_size))
            temp = pygame.transform.scale(temp, (Settings.tile_size * 2, Settings.tile_size * 2))
            right[i] = temp
            left[i] = pygame.transform.flip(temp, True, False)
        images[settings.Direction.RIGHT] = right
        images[settings.Direction.LEFT] = left
        return images

    def load_images_jump(self, path):
        images = {}
        right = {}
        left = {}
        for i in range(0, 9):
            p = path + str(i) + ".png"
            # print("Loading " + p)
            temp = pygame.image.load(p).convert_alpha()
            # temp = pygame.transform.scale(temp, (Settings.tile_size, Settings.tile_size))
            temp = pygame.transform.scale(temp, (Settings.tile_size * 2, Settings.tile_size * 2))
            right[i] = temp
            left[i] = pygame.transform.flip(temp, True, False)
        images[settings.Direction.RIGHT] = right
        images[settings.Direction.LEFT] = left
        return images
    def load_images_run(self, path):
        images = {}
        right = {}
        left = {}
        for i in range(0, 12):
            p = path + str(i) + ".png"
            # print("Loading " + p)
            temp = pygame.image.load(p).convert_alpha()
            # temp = pygame.transform.scale(temp, (Settings.tile_size, Settings.tile_size))
            temp = pygame.transform.scale(temp, (Settings.tile_size * 2, Settings.tile_size * 2))
            right[i] = temp
            left[i] = pygame.transform.flip(temp, True, False)
        images[settings.Direction.RIGHT] = right
        images[settings.Direction.LEFT] = left
        return images

    def update(self, time):
        self.frame = (self.frame + 1) % Settings.fps
        self.image = self.images[self.state][self.direction][self.frame % 3]
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

