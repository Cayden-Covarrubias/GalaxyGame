import pygame
import random

from gameLib import *

MOVE_SPEED = 0.07
MOVE_PADDING = 20

ADVANCE_MIN = 1000
ADVANCE_MAX = 3000

class Formation(pygame.sprite.Group):

    def __init__(self, world, size, spacing=5):
        super().__init__()

        self._size = 2 * size - 1
        self._spacing = spacing + DEFAULT_SIZE
        self._world = world

        self._main_ships = []
        self._assault_ships = []

        self._center_x = world.size[0] / 2
        self._center_y = world.size[1] / 4

        self._width = self._size * self._spacing - spacing
        self._height = self._size * self._spacing - spacing

        self._move_x = MOVE_SPEED

        self._min_x = self._width / 2 + MOVE_PADDING
        self._max_x = world.size[0] - self._width / 2 - MOVE_PADDING

        self._level_generator_instance = None

    def _square_level_generator(self):
        self._main_ships = []
        self._assault_ships = []

        self._center_x = self._world.size[0] / 2
        self._center_y = self._world.size[1] / 4

        advance_timer = pygame.time.get_ticks() + random.randint(ADVANCE_MIN, ADVANCE_MAX)
        enemies_left = True

        # Generate enemies in a square
        for i in range(self._size):
            for j in range(self._size):
                x = self._center_x + self._spacing * (j - self._size // 2)
                y = self._center_y + self._spacing * (i - self._size // 2)

                enemy = Enemy(self._world, Vector(x, y))

                self._main_ships.append(enemy)
                self.add(enemy)

        # Update generator loop
        while enemies_left:
            self._center_x += self._move_x * self._world.delta_time
            if (self._move_x > 0 and self._center_x > self._max_x - random.randint(0, 100)):
                self._move_x = -MOVE_SPEED

            elif (self._move_x < 0 and self._center_x < self._min_x + random.randint(0, 100)):
                self._move_x = MOVE_SPEED
        
            if (advance_timer < pygame.time.get_ticks()):
                advance_timer = pygame.time.get_ticks() + random.randint(ADVANCE_MIN, ADVANCE_MAX)
                random.choice(self._main_ships).fire()

            enemies_left = False
            temp_array = []
            for i in range(len(self._main_ships)):
                ship = self._main_ships[i]
                ship.position.x = ship.position.x + self._move_x * self._world.delta_time

                if ship.alive():
                    enemies_left = True
                    temp_array.append(ship)

            self._main_ships = temp_array

            yield True
        
        yield False

    def update(self):
        if self._level_generator_instance is None:
            self._level_generator_instance = self._square_level_generator()
        
        else:
            if not next(self._level_generator_instance):
                self._level_generator_instance = None

        pygame.sprite.Group.update(self)
    
