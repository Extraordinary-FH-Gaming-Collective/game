from lanes import Lanes
from settings import *
import random
from spritePool import *
from sprites import (
    FireTruck,
    EstateCar,
    SmallCar,
    Truck,
    TrainSmallGreen,
    TrainSmallOrange,
    TrainMediumGreen,
    TrainMediumOrange,
    TrainLargeGreen,
    TrainLargeOrange,
)

to_create = {}
to_create["cars_firetruck"] = GENERATE_CARS_FIRETRUCK
to_create["cars_estate"] = GENERATE_CARS_ESTATE
to_create["cars_truck"] = GENERATE_CARS_TRUCK
to_create["cars_small"] = GENERATE_CARS_SMALL

to_create["trains_small"] = GENERATE_TRAINS_SMALL
to_create["trains_medium"] = GENERATE_TRAINS_MEDIUM
to_create["trains_large"] = GENERATE_TRAINS_LARGE


class SpriteGenerator:
    """ This is the fun part, to auto generate all moving sprites.

    How it works:
    Basically we do generate all needed lanes, sprites, do shuffle them and move sprites to the lanes.

    We are using a sprite pool, to create all sprites before the game starts. From there, sprites will
    be moved to lanes. After they are out of view from the game window, the will be moved backed to
    the sprite pool and another sprite from the pool will be added to the lane again.
    """

    def __init__(self):
        self.lanes = {}

    def generate(self):
        """ Generates everything and does return all lanes. """

        self.generate_lanes()
        self.generate_cars()
        self.generate_trains()
        self.shuffle()
        self.move_to_lanes()

        return self.lanes

    def generate_lanes(self):
        """ For a seperation of concerns, only the Lanes class now about what to generate. """

        self.lanes = Lanes().generate()

    def generate_cars(self):
        """ All needed cars will be created as often as defined in `settings.py`. """

        while to_create["cars_firetruck"] > 0:
            inactive_cars.append(FireTruck())
            to_create["cars_firetruck"] -= 1

        while to_create["cars_estate"] > 0:
            inactive_cars.append(EstateCar())
            to_create["cars_estate"] -= 1

        while to_create["cars_truck"] > 0:
            inactive_cars.append(Truck())
            to_create["cars_truck"] -= 1

        while to_create["cars_small"] > 0:
            inactive_cars.append(SmallCar())
            to_create["cars_small"] -= 1

    def generate_trains(self):
        """ All needed trains will be created as often as defined in `settings.py`. """

        while to_create["trains_small"] > 0:
            inactive_trains_small.append(TrainSmallGreen())
            inactive_trains_small.append(TrainSmallOrange())
            to_create["trains_small"] -= 2

        while to_create["trains_medium"] > 0:
            inactive_trains_medium.append(TrainMediumGreen())
            inactive_trains_medium.append(TrainMediumOrange())
            to_create["trains_medium"] -= 2

        while to_create["trains_large"] > 0:
            inactive_trains_large.append(TrainLargeGreen())
            inactive_trains_large.append(TrainLargeOrange())
            to_create["trains_large"] -= 2

    def shuffle(self):
        """ Shuffle all sprites so it's not predictable which sprite will be the next. """

        random.shuffle(inactive_cars)
        random.shuffle(inactive_trains_small)
        random.shuffle(inactive_trains_medium)
        random.shuffle(inactive_trains_large)

    def move_to_lanes(self):
        """ Loop through all lanes and inject them with our aut generated sprites. """

        for lane in self.lanes.get():
            if lane.type == 'cars':
                sprites = inactive_cars
            if lane.type == 'small_trains':
                sprites = inactive_trains_small
            if lane.type == 'medium_trains':
                sprites = inactive_trains_medium
            if lane.type == 'large_trains':
                sprites = inactive_trains_large

            lane.init_placement(sprites)
