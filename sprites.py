from support import Image

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
        self.position_x = -9999
        self.position_y = -9999
        self.speed = 0

    def update(self):
        self.position_x += self.speed

    def render(self, screen):
        screen.blit(self.image, (self.position_x, self.position_y))

    def speed(self, speed: int):
        self.speed = speed

    def set(self, position_x: int, position_y: int):
        self.position_x = position_x
        self.position_y = position_y


class SmallCar(Sprite):
    def __init__(self):
        super().__init__()
        self.image = sprite_dict["small"]


class EstateCar(Sprite):
    def __init__(self):
        super().__init__()
        self.image = sprite_dict["estate"]


class Truck(Sprite):
    def __init__(self):
        super().__init__()
        self.image = sprite_dict["truck"]


class FireTruck(Sprite):
    def __init__(self):
        super().__init__()
        self.image = sprite_dict["firetruck"]
