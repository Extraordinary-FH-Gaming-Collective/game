from collision import CollisionHandler
from character import Character
from sprites import Sprite
import settings
import random


class Lanes:
    def __init__(self):
        self.lanes = []
        self.collisionHandler = CollisionHandler()

    def generate(self):
        self.lanes.append(Lane(9, 'large_trains'))
        self.lanes.append(Lane(8, 'medium_trains'))
        self.lanes.append(Lane(7, 'small_trains'))
        self.lanes.append(Lane(5, 'cars'))
        self.lanes.append(Lane(4, 'cars'))
        self.lanes.append(Lane(3, 'cars'))
        self.lanes.append(Lane(2, 'cars'))
        self.lanes.append(Lane(1, 'cars'))

        return self

    def update(self):
        for lane in self.lanes:
            lane.update()

    def render(self, screen):
        for lane in self.lanes:
            lane.render(screen)

    def isColliding(self, character: Character):
        for lane in self.lanes:
            self.collisionHandler.check(lane, character)

    def get(self):
        return self.lanes


class Lane:
    def __init__(self, row: int, type: str):
        self.sprites = []
        self.type = type
        self.spriteCount = random.randrange(5, 8)
        self.speed = random.randrange(6, 12)
        self.position_y = self.calculateYPosition(row)
        self.firstSprite: Sprite
        self.lastSprite: Sprite

    def update(self):
        for sprite in self.sprites:
            sprite.update()

            # check if the first sprite is out of view.
            # If it is, remove it from the sprite and make the next to the first sprite
            # move this sprite back as an inaktive sprite
            if self.outOfView(sprite):
                sprite.position_x = -120

            # After it has been removed, add a new sprite.

    def render(self, screen):
        for sprite in self.sprites:
            sprite.render(screen)

    def firstPlacement(self, sprites: list):
        position_x = 0
        while self.spriteCount > 0:
            self.add(sprites.pop(1), position_x)
            self.spriteCount -= 1
            position_x += 180

    def add(self, sprite: Sprite, position_x: int):
        sprite.position_y = self.position_y
        sprite.position_x = -50 + position_x
        sprite.speed = self.speed
        self.sprites.append(sprite)
        self.lastSprite = sprite

    def outOfView(self, sprite: Sprite):
        return settings.SCREEN_WIDTH < sprite.position_x

    def calculateYPosition(self, row: int):  # TODO: Calculate correctly
        return settings.SCREEN_HEIGHT - (row * settings.CHARACTER_STEP_SIZE) - settings.MAP_BOTTOM_PADDING - 50
