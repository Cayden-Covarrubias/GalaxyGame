import pygame
import random

from gameLib import *

MOVE_SPEED = 0.07
MOVE_PADDING = 20

ADVANCE_MIN = 100
ADVANCE_MAX = 1500

class Formation(pygame.sprite.Group):

    def __init__(self, world, size, spacing=5):
        super().__init__()

        self._size = 2 * size - 1
        self._spacing = spacing + DEFAULT_SIZE
        self.world = world

        self.ships = []

        self.center_x = world.size[0] / 2
        self.center_y = world.size[1] / 4

        self._width = self._size * self._spacing - spacing
        self._height = self._size * self._spacing - spacing

        for i in range(self._size):
            self.ships.append([])
            for j in range(self._size):
                x = self.center_x + self._spacing * (j - self._size // 2)
                y = self.center_y + self._spacing * (i - self._size // 2)

                enemy = Enemy(world, Vector(x, y))

                self.ships[i].append(enemy)
                self.add(enemy)

        self._move_x = MOVE_SPEED

        self._min_x = self._width / 2 + MOVE_PADDING
        self._max_x = world.size[0] - self._width / 2 - MOVE_PADDING

        self._advance_timer = pygame.time.get_ticks() + random.randint(ADVANCE_MIN, ADVANCE_MAX)
    
    def _update_ship_pos(self):
        any_ship_alive = False
        for i in range(self._size):
            for j in range(self._size):
                x = self.center_x + self._spacing * (j - self._size // 2)
                y = self.center_y + self._spacing * (i - self._size // 2)

                self.ships[i][j].position.x = x
                self.ships[i][j].position.y = y

                if self.ships[i][j].alive():
                    any_ship_alive = True
        
        return any_ship_alive

    def update(self):
        self.center_x += self._move_x * self.world.delta_time

        reform = not self._update_ship_pos()

        if (reform):
            for i in range(self._size):
                for j in range(self._size):
                    x = self.center_x + self._spacing * (j - self._size // 2)
                    y = self.center_y + self._spacing * (i - self._size // 2)

                    enemy = Enemy(self.world, Vector(x, y))

                    self.ships[i][j] = enemy
                    self.add(enemy)

        if (self._move_x > 0 and self.center_x > self._max_x - random.randint(0, 100)):
            self._move_x = 0
            self._move_x = -MOVE_SPEED

        elif (self._move_x < 0 and self.center_x < self._min_x + random.randint(0, 100)):
            self._move_x = 0
            self._move_x = MOVE_SPEED
        
        if (self._advance_timer < pygame.time.get_ticks()):
            self._advance_timer = pygame.time.get_ticks() + random.randint(ADVANCE_MIN, ADVANCE_MAX)
            random.choice(random.choice(self.ships)).fire()

        pygame.sprite.Group.update(self)
    
