import pygame
import league
from player import Player
from background2 import Background2


def main():
    e = league.Engine("Knight's Quest")
    e.init_pygame()

    b = Background2(0, 0, 0)
    p = Player(2, 350, 332)

    e.drawables.add(b)
    e.drawables.add(p)

    pygame.time.set_timer(pygame.USEREVENT + 1, 100 // league.Settings.gameTimeFactor)
    e.key_events[pygame.K_a] = p.move_left
    e.key_events[pygame.K_d] = p.move_right
    e.key_events[pygame.K_SPACE] = p.jump
    e.events[pygame.USEREVENT + 1] = p.update
    e.events[pygame.QUIT] = e.stop
    e.run()


if __name__ == '__main__':
    main()

