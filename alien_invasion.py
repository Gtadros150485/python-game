import sys
import pygame
import settings
from ship import Ship


class AlienInvasion:
    def __init__(self):
        #recall the initializer of the pygame
        pygame.init()
        self.settings = settings.Settings()
        self.screen =pygame.display.set_mode((self.settings.screen_width,self.settings.screen_height))
        self.bg_color = self.settings.bg_color
        pygame.display.set_caption("Alien Invasion")
        self.screen.fill(self.bg_color)
        self.ship = Ship(self)
    def run_game(self):
        while True:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            self.ship.blitme()
            pygame.display.flip()
if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()