import pygame

TITLE_TEXTURE = pygame.image.load('textures/Handaga.png')

class Menu:
    def __init__(self, screen_size, font, highscore):
        self.group = pygame.sprite.Group()
        
        title = pygame.sprite.Sprite(self.group)
        title.image = TITLE_TEXTURE
        title.rect = title.image.get_rect()

        screen_x, screen_y = screen_size

        title.rect.x = screen_x / 2 - title.rect.width / 2
        title.rect.y = screen_y / 2 - title.rect.height - 100

        img = font.render("Hold up hands to begin", False, (255, 255, 255))
        info = pygame.sprite.Sprite(self.group)
        info.image = img
        info.rect = img.get_rect()
        info.rect.x = screen_x / 2 - info.rect.width / 2
        info.rect.y = screen_y - info.rect.height - 30

        img = font.render(f"High Score: {highscore}", False, (255, 255, 255))
        hs = pygame.sprite.Sprite(self.group)
        hs.image = img
        hs.rect = img.get_rect()
        hs.rect.x = screen_x / 2 - hs.rect.width / 2
        hs.rect.y = screen_y / 2 - hs.rect.height / 2