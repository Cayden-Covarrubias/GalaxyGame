import pygame

from entity import Entity

ENEMY_STARTING_HEALTH = 10

ENEMY_TEXTURE = pygame.image.load('textures/alien_blue.png')

class Enemy(Entity):

    def __init__(self, world, x, y):
        super().__init__(world, x, y, ENEMY_STARTING_HEALTH, ENEMY_TEXTURE)