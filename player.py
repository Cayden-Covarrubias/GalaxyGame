import pygame

PLAYER_SPEED = 0.1

PLAYER_TEXTURE = pygame.image.load('textures/test_ship.png')

class Player(pygame.sprite.Sprite):

    def __init__(self, x, y):
        super().__init__()

        self.image = PLAYER_TEXTURE
        self.color_key = (0, 0, 0)

        self.rect = self.image.get_rect()

        self.x = x
        self.y = y

        self.rect.x = x
        self.rect.y = y
    
    def update(self):

        pressed = pygame.key.get_pressed()

        if pressed[pygame.K_LEFT]:
            self.x -= PLAYER_SPEED

        if pressed[pygame.K_RIGHT]:
            self.x += PLAYER_SPEED

        if pressed[pygame.K_UP]:
            self.y -= PLAYER_SPEED

        if pressed[pygame.K_DOWN]:
            self.y += PLAYER_SPEED
        
        self.rect.x = int(self.x)
        self.rect.y = int(self.y)
        pygame.sprite.Sprite.update(self)