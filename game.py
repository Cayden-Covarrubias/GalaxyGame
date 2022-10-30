import pygame

from player import Player

BACKGROUND_COLOR = (0, 0, 0)

class Game:

    def __init__(self, screen_size, keyboard_input=False):
        self.screen = pygame.display.set_mode(screen_size)
        self.player_group = pygame.sprite.Group()

        self.player = Player(screen_size, self.player_group)
        self.player_group.add(self.player)
    
    def draw(self):
        self.screen.fill(BACKGROUND_COLOR)
        self.player_group.draw(self.screen)
        pygame.display.flip()

    def handle_keypress(self, key, press_type):
        if (key == pygame.K_SPACE and press_type == pygame.KEYDOWN):
            self.player.fire()

    def run(self):

        done = False
        while not done:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True

                elif event.type in [pygame.KEYDOWN, pygame.KEYUP]:
                    self.handle_keypress(event.key, event.type)

            self.player_group.update()
            self.draw()

def main():
    game = Game((800, 600))
    game.run()

if __name__ == "__main__":
    main()