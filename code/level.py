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
        self.visible_sprites = YSortCameraGroup()
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

        self.visible_sprites.custom_draw(self.player)
        self.visible_sprites.update()
        # debug(self.player.direction)


class YSortCameraGroup(pygame.sprite.Group):
    def __init__(self):
        """Initialize me daddy"""

        super().__init__()
        self.display_surface = pygame.display.get_surface()
        self.offset = pygame.math.Vector2()

    def custom_draw(self, player):
        """Custom drawing method for objects in view of the camera"""

        # Calculate the offset
        self.offset.x = player.rect.centerx - self.display_surface.get_size()[0] // 2
        self.offset.y = player.rect.centery - self.display_surface.get_size()[1] // 2

        # Applying the offset
        for sprite in sorted(self.sprites(), key = lambda sprite : sprite.rect.centery):
            offset_position = sprite.rect.topleft - self.offset
            self.display_surface.blit(sprite.image, offset_position)
