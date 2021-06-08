from collision import CollisionHandler
from character import Character
from sprites import Sprite
from spritePool import *
from settings import *
import settings
import random


class Lanes:
    def __init__(self):
        self.lanes = []
        self.collisionHandler = CollisionHandler()

    def generate(self):
        self.lanes.append(Lane(11, 'large_trains', 'right'))
        self.lanes.append(Lane(10, 'large_trains', 'left'))
        self.lanes.append(Lane(9, 'medium_trains', 'right'))
        self.lanes.append(Lane(8, 'small_trains', 'left'))
        self.lanes.append(Lane(5, 'cars', 'left'))
        self.lanes.append(Lane(4, 'cars', 'right'))
        self.lanes.append(Lane(3, 'cars', 'left'))
        self.lanes.append(Lane(2, 'cars', 'right'))
        self.lanes.append(Lane(1, 'cars', 'left'))

        return self

    def update(self):
        for lane in self.lanes:
            lane.update()

    def renderCars(self, screen):
        for lane in self.lanes:
            if lane.type != 'cars':
                continue

            lane.render(screen)

    def renderTrains(self, screen):
        for lane in self.lanes:
            if lane.type == 'cars':
                continue

            lane.render(screen)

    def checkCollision(self, character: Character):
        for lane in self.lanes:
            if lane.row != character.row:
                continue

            self.collisionHandler.check(lane, character)

    def getLane(self, row: int):
        for lane in self.lanes:
            if lane.row == row:
                return lane

    def get(self):
        return self.lanes


class Lane:
    def __init__(self, row: int, type: str, direction: str):
        self.sprites = []
        self.type = type
        self.row = row
        self.spriteCount = random.randrange(
            settings.MINIMUM_CARS_PER_LANE if type == 'cars' else settings.MINIMUM_TRAINS_PER_LANE,
            settings.MAXIMUM_CARS_PER_LANE if type == 'cars' else settings.MAXIMUM_TRAINS_PER_LANE,
        )
        self.speed = random.randrange(settings.SPRITE_MINIMUM_SPEED, settings.SPRITE_MAXIMUM_SPEED)
        self.position_y = self.calculateYPosition(row)
        self.leftToRight = True if direction == 'left' else False
        self.firstSprite: Sprite
        self.lastSprite: Sprite

    def update(self):
        for sprite in self.sprites:
            sprite.update()

            if self.outOfView(sprite):
                index = self.sprites.index(sprite)
                poppedSprite = self.sprites.pop(index)

                if poppedSprite.type == 'car':
                    self.removeSpriteAndAddANewOne(poppedSprite, inactive_cars)
                elif poppedSprite.type == 'train_small':
                    self.removeSpriteAndAddANewOne(poppedSprite, inactive_trains_small)
                elif poppedSprite.type == 'train_medium':
                    self.removeSpriteAndAddANewOne(poppedSprite, inactive_trains_medium)
                elif poppedSprite.type == 'train_large':
                    self.removeSpriteAndAddANewOne(poppedSprite, inactive_trains_large)

    def render(self, screen):
        for sprite in self.sprites:
            sprite.render(screen)

    def firstPlacement(self, sprites: list):
        position_x = 0
        while self.spriteCount > 0:
            self.add(sprites.pop(1), position_x)
            self.spriteCount -= 1
            if self.type == 'cars':
                position_x += self.lastSprite.getWidth() + self.carDistance()
            else:
                position_x += self.lastSprite.getWidth() + self.carDistance()

    def add(self, sprite: Sprite, position_x: int):
        sprite.speed = self.speed
        sprite.set(position_x, self.position_y)
        sprite.setDirection(self.leftToRight)
        self.sprites.append(sprite)
        self.lastSprite = sprite

    def outOfView(self, sprite: Sprite):
        if self.leftToRight:
            return settings.SCREEN_WIDTH < sprite.position_x
        else:
            return sprite.position_x + sprite.getWidth() < 0

    def calculateYPosition(self, row: int):
        return settings.SCREEN_HEIGHT - (row * settings.CHARACTER_STEP_SIZE) - settings.MAP_BOTTOM_PADDING - 50

    def removeSpriteAndAddANewOne(self, poppedSprite: Sprite, list: list):
        list.append(poppedSprite)
        newSprite = list.pop(1)
        distance = self.carDistance() if newSprite.type == 'cars' else self.trainDistance()

        if self.leftToRight:
            newStart = - newSprite.getWidth() - distance

            if self.lastSprite.position_x <= newStart + newSprite.getWidth():
                newStart = self.lastSprite.position_x - newSprite.getWidth() - distance

        else:
            newStart = settings.SCREEN_WIDTH + newSprite.getWidth() + distance

            if self.lastSprite.position_x + newSprite.getWidth() >= newStart:
                newStart = self.lastSprite.position_x + newSprite.getWidth() + distance

        self.add(newSprite, newStart)

    def carDistance(self):
        return random.randrange(MINIMUM_CARS_DISTANCE, MAXIMUM_CARS_DISTANCE)

    def trainDistance(self):
        return random.randrange(MINIMUM_TRAINS_DISTANCE, MAXIMUM_TRAINS_DISTANCE)

    def spriteSPeed(self):
        return random.randrange(SPRITE_MINIMUM_SPEED, SPRITE_MAXIMUM_SPEED)
