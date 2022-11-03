import pygame
import mediapipe

from enemy import Enemy
from entity import DEFAULT_SIZE

MOVE_DISTANCE = 2
MOVE_TIME = 1
MOVE_PADDING = 20

class Formation(pygame.sprite.Group):

    def __init__(self, world, size, spacing=5):
        super().__init__()

        self._size = 2 * size - 1
        self._spacing = spacing + DEFAULT_SIZE

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

                enemy = Enemy(world, x, y)

                self.ships[i].append(enemy)
                self.add(enemy)

        self._move_x = MOVE_DISTANCE
        self._move_y = 0
        self._move_timer = pygame.time.get_ticks() + 500

        self._min_x = self._width / 2 + MOVE_PADDING
        self._max_x = world.size[0] - self._width / 2 - MOVE_PADDING
        self._min_y = self._height / 2 + MOVE_PADDING
        self._max_y = world.size[1] / 2 - self._height / 2 - MOVE_PADDING
    
    def _update_ship_pos(self):
        for i in range(self._size):
            for j in range(self._size):
                x = self.center_x + self._spacing * (j - self._size // 2)
                y = self.center_y + self._spacing * (i - self._size // 2)

                self.ships[i][j].x = x
                self.ships[i][j].y = y

    def update(self):
        if (self._move_timer <= pygame.time.get_ticks()):
            self.center_x += self._move_x
            self.center_y += self._move_y

            self._update_ship_pos()

            if (self._move_x > 0 and self.center_x > self._max_x):
                self._move_x = 0
                self._move_y = -MOVE_DISTANCE

            elif (self._move_x < 0 and self.center_x < self._min_x):
                self._move_x = 0
                self._move_y = MOVE_DISTANCE

            elif (self._move_y < 0 and self.center_y < self._min_y):
                self._move_x = -MOVE_DISTANCE
                self._move_y = 0

            elif (self._move_y > 0 and self.center_y > self._max_y):
                self._move_x = MOVE_DISTANCE
                self._move_y = 0

            self._move_timer += MOVE_TIME

        pygame.sprite.Group.update(self)
    
