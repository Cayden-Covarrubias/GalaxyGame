import pygame
import time
from enum import Enum

from gameLib import *
from track import HandInput

BACKGROUND_COLOR = (0, 0, 0)

class GameState(Enum):
    IN_MENU = 0
    PLAYING_GAME = 1
    QUIT = 2

class Game:

    def __init__(self, screen_size, camera_input=True, fullscreen=False):
        pygame.init()

        if (fullscreen):
            screen_size = pygame.display.get_desktop_sizes()[0]

        self.screen = pygame.display.set_mode(screen_size)

        if (fullscreen):
            pygame.display.toggle_fullscreen()

        self.state = GameState.IN_MENU

        self.input = None
        if (camera_input):
            self.input = HandInput()

        self.font = pygame.font.Font('8bitOperatorPlus-Regular.ttf', 30)

        self.world = None
        self.player = None

        self.menu = Menu(screen_size, self.font)

    def draw(self):
        self.screen.fill(BACKGROUND_COLOR)

        if self.state == GameState.PLAYING_GAME:
            self.world.draw(self.screen)

            img = self.font.render(f"Score: {self.world.score}", True, (255, 255, 255))

            self.screen.blit(img, (0, 0))
        
        if self.state == GameState.IN_MENU:
            self.menu.group.draw(self.screen)

            if self.poll_process():
                self.start_game()


        pygame.display.flip()

    def handle_keypress(self, key, press_type):
        if (key == pygame.K_ESCAPE and press_type == pygame.KEYDOWN):
            self.state = GameState.QUIT

        if (self.state == GameState.IN_MENU):
            if (key == pygame.K_RETURN and press_type == pygame.KEYDOWN):
                self.start_game()

        if (self.state == GameState.PLAYING_GAME):
            if (key == pygame.K_SPACE and press_type == pygame.KEYDOWN):
                self.player.fire()
    
    def run(self):
        while self.state != GameState.QUIT:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.state = GameState.QUIT

                elif event.type in [pygame.KEYDOWN, pygame.KEYUP]:
                    self.handle_keypress(event.key, event.type)

            if self.state == GameState.PLAYING_GAME:
                process = self.poll_process()

                if process is not None:
                    fire, move = process

                    self.player.position = self.player.position.lerp(Vector((1 - move) * self.world.size[0], self.player.position.y), 0.6)

                    if (fire):
                        self.player.fire()

                self.world.update()

            
            self.draw()

    def start_game(self):
        self.world = World(self.screen.get_size())

        self.player = Player(self.world, self.screen.get_size())
        self.world.ally_group.add(self.player)

        self.state = GameState.PLAYING_GAME
    
    def poll_process(self):
        process = None
        if self.input is not None:
            process = self.input.process_game_input()
        
        return process

def main():
    game = Game((800, 600), camera_input=True, fullscreen=True)
    game.run()

if __name__ == "__main__":
    main()