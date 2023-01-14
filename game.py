import pygame
import time

from gameLib import *
from track import HandInput

BACKGROUND_COLOR = (0, 0, 0)

class Game:

    def __init__(self, screen_size, camera_input=True, fullscreen=False):
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

        self.input = None
        if (camera_input):
            self.input = HandInput()

        self.font = pygame.font.Font('8bitOperatorPlus-Regular.ttf', 30)
    
    def draw(self):
        self.screen.fill(BACKGROUND_COLOR)
        self.world.draw(self.screen)

        img = self.font.render(f"Score: {self.world.score}", True, (255, 255, 255))

        self.screen.blit(img, (0, 0))

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

            process = None
            if (self.input is not None):
                process = self.input.process()

            if process is not None:
                fire, move = process

                self.player.position = self.player.position.lerp(Vector((1 - move) * self.world.size[0], self.player.position.y), 0.6)

                if (fire):
                    self.player.fire()

            self.world.update()
            self.draw()

def main():
    game = Game((800, 600), fullscreen=True)
    game.run()

if __name__ == "__main__":
    main()