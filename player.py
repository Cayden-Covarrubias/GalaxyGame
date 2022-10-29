import pygame

PLAYER_SPEED = 0.3
PLAYER_SIZE = 48

PLAYER_TEXTURE = pygame.image.load('textures/test_ship.png')

class Player(pygame.sprite.Sprite):

    def __init__(self, screen_size):
        super().__init__()

        self.image = pygame.transform.scale(PLAYER_TEXTURE, (PLAYER_SIZE, PLAYER_SIZE))
        self.color_key = (0, 0, 0)

        self.rect = self.image.get_rect()

        self.x = screen_size[0] // 2
        self.y = screen_size[1] - 70

        self._min_x = PLAYER_SIZE // 2
        self._max_x = screen_size[0] - PLAYER_SIZE

        self.rect.x = self.x
        self.rect.y = self.y
    
    def update(self):

        pressed = pygame.key.get_pressed()

        if pressed[pygame.K_LEFT]:
            self.x -= PLAYER_SPEED

        if pressed[pygame.K_RIGHT]:
            self.x += PLAYER_SPEED

        self.x = min(self.x, self._max_x)
        self.x = max(self.x, self._min_x)
        
        self.rect.x = int(self.x)
        self.rect.y = int(self.y)
        pygame.sprite.Sprite.update(self)