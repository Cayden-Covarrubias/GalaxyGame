import pygame

from player_missile import PlayerMissile

PLAYER_SPEED = 0.18
PLAYER_SIZE = 24
PLAYER_PADDING = 24

PLAYER_STARTING_HEALTH = 100

PLAYER_TEXTURE = pygame.image.load('textures/player_ship.png')

class Player(pygame.sprite.Sprite):

    def __init__(self, screen_size, missile_group : pygame.sprite.Group):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.transform.scale(PLAYER_TEXTURE, (PLAYER_SIZE, PLAYER_SIZE))
        self.image.set_colorkey((0, 0, 0))

        self.rect = self.image.get_rect()

        self.x = screen_size[0] / 2
        self.y = screen_size[1] - PLAYER_SIZE / 2 - PLAYER_PADDING

        self._min_x = PLAYER_SIZE / 2 + PLAYER_PADDING
        self._max_x = screen_size[0] - PLAYER_SIZE / 2 - PLAYER_PADDING

        self.rect.x = self.x
        self.rect.y = self.y

        self.health = PLAYER_STARTING_HEALTH
        self.missile_group = missile_group
    
    def fire(self):
        missile = PlayerMissile(self.x, self.y)
        self.missile_group.add(missile)

    def update(self):
        pressed = pygame.key.get_pressed()

        if pressed[pygame.K_LEFT]:
            self.x -= PLAYER_SPEED

        if pressed[pygame.K_RIGHT]:
            self.x += PLAYER_SPEED

        self.x = min(self.x, self._max_x)
        self.x = max(self.x, self._min_x)
        
        self.rect.x = self.x - self.rect.width / 2
        self.rect.y = self.y - self.rect.height / 2
        pygame.sprite.Sprite.update(self)