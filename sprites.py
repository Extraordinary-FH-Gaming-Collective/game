from support import Image
import random

dir_car_assets = "assets/cars/"
speed = 12
sprite_dict = {}

sprite_dict["firetruck"] = Image(dir_car_assets, 'firetruck.png').get()
sprite_dict["estate"] = Image(dir_car_assets, 'estate.png').get()
sprite_dict["truck"] = Image(dir_car_assets, 'truck.png').get()
sprite_dict["small"] = Image(dir_car_assets, 'car.png').get()


class Sprite:
    def __init__(self):
        self.image = None
        self.position_y
        self.position_x
        self.row = None

    def update(self):
        raise NotImplementedError

    def render(self, screen):
        screen.blit(self.image, (self.position_x, self.position_y))


class SmallCar(Sprite):
    def __init__(self):
        self.image = sprite_dict["small"]
        self.position_y = 620
        self.position_x = random.randrange(0, 1200)
        self.row = 1

    def update(self):
        self.position_x += speed

        if (self.position_x > 1300):
            self.position_x = -30


class EstateCar(Sprite):
    def __init__(self):
        self.image = sprite_dict["estate"]
        self.position_y = 320
        self.position_x = 100
        self.row = 1

    def update(self):
        self.position_x += speed

        if (self.position_x > 1300):
            self.position_x = -50


class Truck(Sprite):
    def __init__(self):
        self.image = sprite_dict["truck"]
        self.position_y = 620
        self.position_x = 900
        self.row = 1

    def update(self):
        self.position_x += speed

        if (self.position_x > 1300):
            self.position_x = -50


class FireTruck(Sprite):
    def __init__(self):
        self.image = sprite_dict["firetruck"]
        self.position_y = 620
        self.position_x = 800
        self.row = 1

    def update(self):
        self.position_x += speed

        if (self.position_x > 1300):
            self.position_x = -50