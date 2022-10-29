import pygame

from player import Player

BACKGROUND_COLOR = (0, 0, 0)

class Game:

    def __init__(self, screen_size, keyboard_input=False):
        self.screen = pygame.display.set_mode(screen_size)
        self.all_sprite_group = pygame.sprite.Group()

        self.player = Player(0, 0)
        self.all_sprite_group.add(self.player)
    
    def draw(self):
        self.screen.fill(BACKGROUND_COLOR)
        self.all_sprite_group.draw(self.screen)
        pygame.display.flip()

    def handle_keypress(self, key, press_type):
        pass

    def run(self):

        done = False
        while not done:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True

                elif event.type in [pygame.KEYDOWN, pygame.KEYUP]:
                    self.handle_keypress(event.key, event.type)

            self.all_sprite_group.update()
            self.draw()

def main():
    game = Game((800, 600))
    game.run()

if __name__ == "__main__":
    main()