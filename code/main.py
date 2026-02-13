import pygame, sys
from settings import WIDTH, HEIGHT,FPS, TILE_SIZE, WORLD_MAP
from level import Level


class Game:
    def __init__(self):
        """Initialize the Game object"""

        # General setup
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption('Another DM Zelda Clone')
        self.clock = pygame.time.Clock()

        # Set up a Level
        self.level = Level()

    def run(self):
        """Running the Game object's core event loop"""

        while True:
            # Basic event-handling logic
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            self.screen.fill('black')
            self.level.run()
            pygame.display.update()
            self.clock.tick(FPS)


if __name__ == '__main__':
    Game().run()
