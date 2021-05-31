from support import Image
from lanes import Lanes
from support import *
import random
from sprites import (
    FireTruck,
    EstateCar,
    SmallCar,
    Truck
)

inactive_sprites = []

to_create = {}
to_create["firetruck"] = 10
to_create["estate"] = 20
to_create["truck"] = 15
to_create["small"] = 20

class SpriteGenerator:
    def __init__(self):
        self.lanes = {}

    def generate(self):
        self.generateLanes()
        self.generateCars()
        #  self.generateTrains()
        self.shuffle()
        self.fillLanes()

        return self.lanes

    def generateLanes(self):
        self.lanes = Lanes().generate()

    def generateCars(self):
        while to_create["firetruck"] > 0:
            inactive_sprites.append(FireTruck())
            to_create["firetruck"] -= 1

        while to_create["estate"] > 0:
            inactive_sprites.append(EstateCar())
            to_create["estate"] -= 1

        while to_create["truck"] > 0:
            inactive_sprites.append(Truck())
            to_create["truck"] -= 1

        while to_create["small"] > 0:
            inactive_sprites.append(SmallCar())
            to_create["small"] -= 1

    def shuffle(self):
        inaktive_sprites = random.shuffle(inactive_sprites)

    def fillLanes(self):
        for lane in self.lanes.get():
            lane.firstPlacement(inactive_sprites)