import pygame
from settings import *


class Player(pygame.sprite.Sprite):
    def __init__(self, position, groups, obstacle_sprites):
        """Initialize the Player object

        :param position: (x, y) position in pixels on the screen
        :param groups: the classification(s) of sprite
        :param obstacle_sprites: collection of objects that prevent movement
        """

        super().__init__(groups)
        self.image = pygame.image.load('../graphics/test/player.png').convert_alpha()
        self.rect = self.image.get_rect(topleft = position)
        self.hitbox = self.rect.inflate(0, -26)

        # Vector for determining horizontal and vertical movement
        self.direction = pygame.math.Vector2()
        self.speed = 5

        self.obstacle_sprites = obstacle_sprites

    def input(self):
        """Get input for moving the player character"""

        # Getting keyboard input
        keys = pygame.key.get_pressed()

        if keys[pygame.K_UP]:
            self.direction.y = -1
        elif keys[pygame.K_DOWN]:
            self.direction.y = 1
        else:
            self.direction.y = 0

        if keys[pygame.K_LEFT]:
            self.direction.x = -1
        elif keys[pygame.K_RIGHT]:
            self.direction.x = 1
        else:
            self.direction.x = 0

    def move(self, speed):
        """Moving the Player object

        :param speed: movement speed in pixels
        """

        # Normalize the vector
        if self.direction.magnitude() != 0:
            self.direction = self.direction.normalize()

        # Splitting up horizontal and vertical movement, checking for collisions after each vector is applied
        self.hitbox.x += self.direction.x * speed
        self.collision('horizontal')
        self.hitbox.y += self.direction.y * speed
        self.collision('vertical')

        # Ensuring the sprite graphical center and the hitbox center are in the same location
        self.rect.center = self.hitbox.center

    def collision(self, direction):
        """Check for collisions between Player and obstacles

        :param direction: are we moving horizontally or vertically?
        """

        # Handing horizontal collisions
        if direction == 'horizontal':
            for sprite in self.obstacle_sprites:
                if sprite.hitbox.colliderect(self.hitbox):
                    if self.direction.x > 0: # Player is moving right
                        self.hitbox.right = sprite.hitbox.left
                    if self.direction.x < 0: # Player is moving left
                        self.hitbox.left = sprite.hitbox.right

        # Handling vertical collisions
        if direction == 'vertical':
            for sprite in self.obstacle_sprites:
                if sprite.hitbox.colliderect(self.hitbox):
                    if self.direction.y > 0:  # Player is moving down
                        self.hitbox.bottom = sprite.hitbox.top
                    if self.direction.y < 0:  # Player is moving up
                        self.hitbox.top = sprite.hitbox.bottom

    def update(self):
        """Update the player position, animation, sprite, and miscellaneous properties"""

        self.input()
        self.move(self.speed)
