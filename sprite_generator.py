from lanes import Lanes
from settings import *
import random
from sprite_pool import *
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
    def __init__(self):
        self.lanes = {}

    def generate(self):
        self.generateLanes()
        self.generateCars()
        self.generateTrains()
        self.shuffle()
        self.fillLanes()

        return self.lanes

    def generateLanes(self):
        self.lanes = Lanes().generate()

    def generateCars(self):
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

    def generateTrains(self):
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
        random.shuffle(inactive_cars)
        random.shuffle(inactive_trains_small)
        random.shuffle(inactive_trains_medium)
        random.shuffle(inactive_trains_large)

    def fillLanes(self):
        for lane in self.lanes.get():
            if lane.type == 'cars':
                sprites = inactive_cars
            if lane.type == 'small_trains':
                sprites = inactive_trains_small
            if lane.type == 'medium_trains':
                sprites = inactive_trains_medium
            if lane.type == 'large_trains':
                sprites = inactive_trains_large

            lane.firstPlacement(sprites)