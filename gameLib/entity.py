import pygame

from gameLib import *

DEFAULT_SIZE = 40
WIDTH_CORRECTION = 31 / 32

class Entity(pygame.sprite.Sprite):

    def __init__(self, world, position : Vector, health, texture, size=DEFAULT_SIZE):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.transform.scale(texture, (size, size))
        self.image.set_colorkey((0, 0, 0))

        self.rect = self.image.get_rect()

        self.position = position.copy()

        self.rect.width *= WIDTH_CORRECTION

        self.health = health
        self.world = world

        self.rect.center = self.position.as_tuple()
    
    def update(self):
        if self.health <= 0:
            self.kill()

        self.rect.center = self.position.as_tuple()

        pygame.sprite.Sprite.update(self)
