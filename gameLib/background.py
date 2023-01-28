import pygame
import random

PARTICLES = 200
TICK_TIMER = 10

class Background:

    def __init__(self, size):
        self._points = []
        self._max_x = size[0]
        self._max_y = size[1]

        for _ in range(PARTICLES):
            self._points.append((
                random.randint(0, self._max_x),
                random.randint(0, self._max_y)
            ))
        self._update_tick_timer = pygame.time.get_ticks()
    
    def draw(self, screen):

        if self._update_tick_timer + TICK_TIMER < pygame.time.get_ticks():
            self._update_tick_timer = TICK_TIMER
            for i in range(len(self._points)):
                self._points[i] = (self._points[i][0], (self._points[i][1] + 1) % self._max_y)
            
            self._update_tick_timer = pygame.time.get_ticks()

        for point in self._points:
            pygame.draw.rect(screen, (255, 255, 255), (point[0], point[1], 2, 2))

