import pygame

from entity import Entity

PLAYER_MISSILE_SPEED = 0.5
PLAYER_MISSILE_DAMAGE = 10
PLAYER_MISSILE_HEALTH = 1

PLAYER_MISSILE_TEXTURE = pygame.image.load('textures/player_missile.png')

class PlayerMissile(Entity):

    def __init__(self, world, x, y):
        super().__init__(world, x, y, PLAYER_MISSILE_HEALTH, PLAYER_MISSILE_TEXTURE)

    def update(self):
        self.y -= PLAYER_MISSILE_SPEED * self.world.delta_time

        collisions = pygame.sprite.spritecollide(self, self.world.enemy_group, False, pygame.sprite.collide_mask)
        if (len(collisions) > 0):
            for other in collisions:
                other.health -= PLAYER_MISSILE_DAMAGE
            self.kill()

        if (self.y < 0):
            self.kill()

        super().update()

