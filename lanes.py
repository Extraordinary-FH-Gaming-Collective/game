from collision import CollisionHandler
from character import Character
from sprites import Sprite
from spritePool import *
from settings import *
import random


class Lanes:
    """ One lane is defined as a row in our game.

    One row can fx contain different cars moving from one direction to the other.

    To seperate code concerns, a single lane will mostly be handled by the lanes class.
    """

    def __init__(self):
        """ Initialize lanes and the collision handler. """

        self.lanes = []
        self.collisionHandler = CollisionHandler()

    def generate(self):
        """ Generate all needed Lanes.

        As shown the row number, sprite type and driving direction needs to get passed.
        """

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
        """ Update all existing lanes. """

        for lane in self.lanes:
            lane.update()

    def render_cars(self, screen):
        """ Only render cars.

        As the time of rendering does define which images stay on top, a seperate render process is needed.
        See the render method in the Game class.

        Cars will rendered so they will stay on top of the player,
        meaing the player behind the car can't be seen.
        """

        for lane in self.lanes:
            if lane.type != "cars":
                continue

            lane.render(screen)

    def render_trains(self, screen):
        """ Only render trains.

        As the time of rendering does define which images stay on top, a seperate render process is needed.
        See the render method in the Game class.

        Trains will rendered a little so the player will never be hidden by train images.
        This is needed as the player does stand on the train roof.
        """

        for lane in self.lanes:
            if lane.type == "cars":
                continue

            lane.render(screen)

    def check_collision(self, character: Character, scorer):
        """ Check if the character does collide with any sprite in the lane.

        To save some calculation power, collisions will only be deteced in the current character lane.
        """

        for lane in self.lanes:
            if lane.row != character.row:
                continue

            self.collisionHandler.check(lane, character, scorer)

    def get_lane(self, row: int):
        """ Get a lane by row number. """

        for lane in self.lanes:
            if lane.row == row:
                return lane

    def get(self):
        """ Get all lanes. """
        return self.lanes


class Lane:
    """ A single lane.

    On initialization, we randomly choose the speed from a pre defined range, as well as the sprite count.
    """

    def __init__(self, row: int, type: str, direction: str):
        self.sprites = []
        self.type = type
        self.row = row
        self.sprite_count = random.randrange(
            MINIMUM_CARS_PER_LANE if type == 'cars' else MINIMUM_TRAINS_PER_LANE,
            MAXIMUM_CARS_PER_LANE if type == 'cars' else MAXIMUM_TRAINS_PER_LANE,
        )
        self.speed = random.randrange(SPRITE_MINIMUM_SPEED, SPRITE_MAXIMUM_SPEED)
        self.position_y = self.calculate_y_position(row)
        self.left_to_right = True if direction == "left" else False
        self.firstSprite: Sprite
        self.lastSprite: Sprite

    def update(self):
        """ Updates a lane to keep evertthing moving.

        All sprites will be called and updated, so the positions can be adjustes on every frame per second.

        In case a sprite is no longer in the view it will be removed and a new sprite will be added.
        """

        for sprite in self.sprites:
            sprite.update()

            if self.out_of_view(sprite):
                index = self.sprites.index(sprite)
                poppedSprite = self.sprites.pop(index)

                if poppedSprite.type == "car":
                    self.remove_sprite_and_add_a_new_one(poppedSprite, inactive_cars)
                elif poppedSprite.type == "train_small":
                    self.remove_sprite_and_add_a_new_one(poppedSprite, inactive_trains_small)
                elif poppedSprite.type == "train_medium":
                    self.remove_sprite_and_add_a_new_one(poppedSprite, inactive_trains_medium)
                elif poppedSprite.type == "train_large":
                    self.remove_sprite_and_add_a_new_one(poppedSprite, inactive_trains_large)

    def render(self, screen):
        """ Render all lane sprites to the screen. """

        for sprite in self.sprites:
            sprite.render(screen)

    def init_placement(self, sprites: list):
        """ Calculates the first placement of all sprites, before the game starts.

        If not doing this, the screen would start empty. Nahhhh ... that's no good.
        """

        position_x = 0
        while self.sprite_count > 0:
            self.add(sprites.pop(1), position_x)
            self.sprite_count -= 1
            if self.type == "cars":
                position_x += self.lastSprite.get_width() + self.car_distance()
            else:
                position_x += self.lastSprite.get_width() + self.car_distance()

    def add(self, sprite: Sprite, position_x: int):
        """ Adds a new sprite. """

        sprite.speed = self.speed
        sprite.set(position_x, self.position_y)
        sprite.set_direction(self.left_to_right)
        self.sprites.append(sprite)
        self.lastSprite = sprite

    def out_of_view(self, sprite: Sprite):
        """ Is a sprite out of view? """

        if self.left_to_right:
            return SCREEN_WIDTH < sprite.position_x
        else:
            return sprite.position_x + sprite.get_width() < 0

    def calculate_y_position(self, row: int):
        """ Calculates the y position depending on the row. """

        return SCREEN_HEIGHT - (row * CHARACTER_STEP_SIZE) - MAP_BOTTOM_PADDING - 50

    def remove_sprite_and_add_a_new_one(self, poppedSprite: Sprite, list: list):
        """ Remove a sprite and does add a new one

        1. Add the removed sprite to the inactive list / sprite pool.
        2. Fetch a new sprite from the sprite pool.
        3. Calculate a random distance to the next sprite.
        4. If colliding with an existing sprite, the new sprite will be placed behind + a random distance.
        """

        list.append(poppedSprite)
        newSprite = list.pop(1)
        distance = (
            self.car_distance() if newSprite.type == "cars" else self.train_distance()
        )

        if self.left_to_right:
            newStart = -newSprite.get_width() - distance

            if self.lastSprite.position_x <= newStart + newSprite.get_width():
                newStart = self.lastSprite.position_x - newSprite.get_width() - distance

        else:
            newStart = SCREEN_WIDTH + newSprite.get_width() + distance

            if self.lastSprite.position_x + newSprite.get_width() >= newStart:
                newStart = self.lastSprite.position_x + newSprite.get_width() + distance

        self.add(newSprite, newStart)

    def car_distance(self):
        """ Calculates a random distance between two cars. """

        return random.randrange(MINIMUM_CARS_DISTANCE, MAXIMUM_CARS_DISTANCE)

    def train_distance(self):
        """ Calculates a random distance between two trains. """

        return random.randrange(MINIMUM_TRAINS_DISTANCE, MAXIMUM_TRAINS_DISTANCE)

    def sprite_speed(self):
        """ Calculates a random speed value. """

        return random.randrange(SPRITE_MINIMUM_SPEED, SPRITE_MAXIMUM_SPEED)
