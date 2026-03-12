import pygame
from settings import *


class Tile(pygame.sprite.Sprite):
    def __init__(self, position, groups, sprite_type, surface=pygame.Surface((TILE_SIZE, TILE_SIZE))):
        super().__init__(groups)
        self.sprite_type = sprite_type
        self.image = surface

        # special case for objects, which are not always 64x64
        if sprite_type == 'object':
            # Apply an offset
            self.rect = self.image.get_rect(topleft = (position[0], position[1] - TILE_SIZE))
        else:
            self.rect = self.image.get_rect(topleft = position)
        self.hitbox = self.rect.inflate(0, -10)
