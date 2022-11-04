import pygame

from game_math import *

from entity import Entity
from enemy_missile import EnemyMissile

ENEMY_STARTING_HEALTH = 10

ENEMY_TEXTURE = pygame.image.load('textures/alien_blue.png')

class Enemy(Entity):

    def __init__(self, world, position : Vector):
        super().__init__(world, position, ENEMY_STARTING_HEALTH, ENEMY_TEXTURE)

    def fire(self):
        if self.alive():
            missile = EnemyMissile(self.world, self.position)
            self.world.enemy_group.add(missile)

    def update(self):
        super().update()