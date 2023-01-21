import pygame

TITLE_TEXTURE = pygame.image.load('textures/Handaga.png')

class Menu:
    def __init__(self, screen_size, font):
        self.group = pygame.sprite.Group()
        
        title = pygame.sprite.Sprite(self.group)
        title.image = TITLE_TEXTURE
        title.rect = title.image.get_rect()

        screen_x, screen_y = screen_size

        title.rect.x = screen_x / 2 - title.rect.width / 2
        title.rect.y = screen_y / 2 - title.rect.height - 100

        img = font.render("Hold up hands to begin", True, (255, 255, 255))
        info = pygame.sprite.Sprite(self.group)
        info.image = img
        info.rect = img.get_rect()
        info.rect.x = screen_x / 2 - info.rect.width / 2
        info.rect.y = screen_y - info.rect.height - 30