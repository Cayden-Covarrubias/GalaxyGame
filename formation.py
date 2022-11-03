import pygame

from enemy import Enemy
from entity import DEFAULT_SIZE

class Formation(pygame.sprite.Group):

    def __init__(self, world, size, spacing=5):
        super().__init__()

        size = 2 * size - 1

        self.ships = [[]] * size

        spacing += DEFAULT_SIZE

        self.center_x = world.size[0] / 2
        self.center_y = world.size[1] / 4

        for i in range(size):
            for j in range(size):
                x = self.center_x + spacing * (j - size // 2)
                y = self.center_y + spacing * (i - size // 2)

                enemy = Enemy(world, x, y)

                self.ships[i].append(enemy)
                self.add(enemy)
    
    def update(self):
        pygame.sprite.Group.update(self)
    
