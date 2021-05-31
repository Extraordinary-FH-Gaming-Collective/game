from support import Image
from support import *
from sprites import (
    FireTruck,
    EstateCar,
    SmallCar,
    Truck
)

inaktiv_sprites = []

to_create = {}
to_create["firetruck"] = 10
to_create["estate"] = 20
to_create["truck"] = 15
to_create["small"] = 20

lanes = {}

class SpriteGenerator:
    def __init__(self):
        pass

    def generate(self):
        #  self.generateLanes()
        self.generateCars()
        #  self.generateTrains()

        return inaktiv_sprites

    def generateCars(self):
        while to_create["firetruck"] > 0:
            inaktiv_sprites.append(FireTruck())
            to_create["firetruck"] -= 1

        while to_create["estate"] > 0:
            inaktiv_sprites.append(EstateCar())
            to_create["estate"] -= 1

        while to_create["truck"] > 0:
            inaktiv_sprites.append(Truck())
            to_create["truck"] -= 1

        while to_create["small"] > 0:
            inaktiv_sprites.append(SmallCar())
            to_create["small"] -= 1