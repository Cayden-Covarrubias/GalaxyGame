import pygame

from gameLib import *

PLAYER_SPEED = 0.22
PLAYER_PADDING = 24

PLAYER_STARTING_HEALTH = 100

PLAYER_TEXTURE = pygame.image.load('textures/player_ship.png')

class Player(Entity):

    def __init__(self, world, screen_size):
        super().__init__(world, Vector(screen_size[0] / 2, screen_size[1] - DEFAULT_SIZE / 2 - PLAYER_PADDING), PLAYER_STARTING_HEALTH, PLAYER_TEXTURE)

        self._min_x = DEFAULT_SIZE / 2 + PLAYER_PADDING
        self._max_x = screen_size[0] - DEFAULT_SIZE / 2 - PLAYER_PADDING
    
    def fire(self):
        missile = PlayerMissile(self.world, self.position)
        self.world.ally_group.add(missile)

    def update(self):
        pressed = pygame.key.get_pressed()

        if pressed[pygame.K_LEFT]:
            self.position.x -= PLAYER_SPEED * self.world.delta_time

        if pressed[pygame.K_RIGHT]:
            self.position.x += PLAYER_SPEED * self.world.delta_time

        self.position.x = min(self.position.x, self._max_x)
        self.position.x = max(self.position.x, self._min_x)
        
        super().update()
    
    def kill(self):
        print("GAME OVER!")
        print(f'Final Score: {self.world.score}')
        super().kill()
        pygame.event.post(pygame.event.Event(pygame.QUIT))