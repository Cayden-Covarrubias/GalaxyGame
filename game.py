import pygame
import time

from gameLib import *

BACKGROUND_COLOR = (0, 0, 0)

Entity

class Game:

    def __init__(self, screen_size, keyboard_input=False, fullscreen=False):
        pygame.init()

        if (fullscreen):
            screen_size = pygame.display.get_desktop_sizes()[0]

        self.screen = pygame.display.set_mode(screen_size)

        if (fullscreen):
            pygame.display.toggle_fullscreen()
        
        self.world = World(screen_size)

        self.player = Player(self.world, screen_size)
        self.world.ally_group.add(self.player)

        self.running = False
    
    def draw(self):
        self.screen.fill(BACKGROUND_COLOR)
        self.world.draw(self.screen)
        pygame.display.flip()

    def handle_keypress(self, key, press_type):
        if (key == pygame.K_ESCAPE and press_type == pygame.KEYDOWN):
            self.running = False

        elif (key == pygame.K_SPACE and press_type == pygame.KEYDOWN):
            self.player.fire()
        
        elif (key == pygame.K_RETURN and press_type == pygame.KEYDOWN):
            list(self.world.enemy_group)[0].fire()
        

    def run(self):
        self.running = True

        timer_0 = time.time()
        timer_1 = timer_0
        while self.running:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

                elif event.type in [pygame.KEYDOWN, pygame.KEYUP]:
                    self.handle_keypress(event.key, event.type)

            self.world.update()
            self.draw()

def main():
    game = Game((800, 600), fullscreen=False)
    game.run()

if __name__ == "__main__":
    main()