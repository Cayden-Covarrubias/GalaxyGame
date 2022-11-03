import pygame

from entity import Entity

ENEMY_MISSILE_SPEED = 0.5
ENEMY_MISSILE_DAMAGE = 10
ENEMY_MISSILE_HEALTH = 1

ENEMY_MISSILE_TEXTURE = pygame.image.load('textures/enemy_missile.png')

class EnemyMissile(Entity):

    def __init__(self, world, x, y):
        super().__init__(world, x, y, ENEMY_MISSILE_HEALTH, ENEMY_MISSILE_TEXTURE)

    def update(self):
        self.y += ENEMY_MISSILE_SPEED * self.world.delta_time

        collisions = pygame.sprite.spritecollide(self, self.world.ally_group, False, pygame.sprite.collide_mask)
        if (len(collisions) > 0):
            for other in collisions:
                other.health -= ENEMY_MISSILE_DAMAGE
            self.kill()

        if (self.y > self.world.size[1]):
            self.kill()

        super().update()

