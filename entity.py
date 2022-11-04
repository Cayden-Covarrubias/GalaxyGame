import pygame

DEFAULT_SIZE = 40
WIDTH_CORRECTION = 31 / 32

class Entity(pygame.sprite.Sprite):

    def __init__(self, world, x, y, health, texture, size=DEFAULT_SIZE):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.transform.scale(texture, (size, size))
        self.image.set_colorkey((0, 0, 0))

        self.rect = self.image.get_rect()

        self.x = x
        self.y = y

        self.rect.width *= WIDTH_CORRECTION

        self.health = health
        self.world = world

        self.rect.center = (self.x, self.y)
    
    def update(self):
        if self.health <= 0:
            self.kill()

        self.rect.center = (self.x, self.y)

        pygame.sprite.Sprite.update(self)
