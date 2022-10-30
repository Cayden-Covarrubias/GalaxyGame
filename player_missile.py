import pygame

PLAYER_MISSILE_SPEED = 0.3
PLAYER_MISSILE_DAMAGE = 10
PLAYER_MISSILE_SIZE = 24

PLAYER_MISSILE_TEXTURE = pygame.image.load('textures/player_missile.png')

class PlayerMissile(pygame.sprite.Sprite):

    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.transform.scale(PLAYER_MISSILE_TEXTURE, (PLAYER_MISSILE_SIZE, PLAYER_MISSILE_SIZE))
        self.image.set_colorkey((0, 0, 0))

        self.rect = self.image.get_rect()

        self.x = x
        self.y = y

        self.rect.x = x
        self.rect.y = y

    def update(self):
        self.y -= PLAYER_MISSILE_SPEED

        self.rect.x = self.x - PLAYER_MISSILE_SIZE / 2
        self.rect.y = self.y - PLAYER_MISSILE_SIZE / 2

        if (self.y < 0):
            self.kill()

        pygame.sprite.Sprite.update(self)

