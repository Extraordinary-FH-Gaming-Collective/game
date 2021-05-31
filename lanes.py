import pygame
import settings
import random
from sprites import Sprite

lanes = []

class Lanes:
    def __init__(self):
        pass

    def generate(self):
        lanes.append([
            Lane(1),
            Lane(2),
            Lane(3),
            Lane(4),
            Lane(5),
        ])

class Lane:
    def __init__(self, row: int, empty: bool = False):
        self.sprites = {}
        self.maxObjects = 0 if empty else random.randrange(6, 10)
        self.speed = 0 if empty else random.randrange(6, 12)
        self.position_y = self.calculateYPosition(row)
        self.firstSprite: None
        self.lastSprite: None
    
    def update(self):
        for sprite in self.sprites:
            sprite.update()

        # check if the first sprite is out of view. 
        # If it is, remove it from the sprite and make the next to the first sprite
        # move this sprite back as an inaktive sprite

        # After it has been removed, add a new sprite.

    def calculateYPosition(self, row: int):
        return settings.MAP_BOTTOM_PADDING + (row * settings.CHARACTER_STEP_SIZE)