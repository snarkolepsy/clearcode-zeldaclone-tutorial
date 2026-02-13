import pygame
from settings import *
from tile import Tile
from player import Player
from debug import debug


class Level:
    def __init__(self):
        """Initialize the Level object"""

        # Get the display surface
        self.display_surface = pygame.display.get_surface()

        # Define sprite groups
        self.visible_sprites = pygame.sprite.Group()
        self.obstacle_sprites = pygame.sprite.Group()

        # Sprite setup
        self.create_map()

    def create_map(self):
        """Iterate through the textual representation of the map and create the appropriate sprites"""

        for row_index, row in enumerate(WORLD_MAP):
            for col_index, column in enumerate(row):
                x = col_index * TILE_SIZE
                y = row_index * TILE_SIZE
                if column == 'x':
                    Tile((x, y), [self.visible_sprites, self.obstacle_sprites])
                if column == 'p':
                    self.player = Player((x, y) , [self.visible_sprites], self.obstacle_sprites)

    def run(self):
        """Update and draw the Level"""

        self.visible_sprites.draw(self.display_surface)
        self.visible_sprites.update()
        debug(self.player.direction)
