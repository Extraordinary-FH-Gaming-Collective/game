from support import Image

dir_car_assets = "assets/cars/"
dir_train_assets = "assets/trains/"
car_dict = {}
train_dict = {}

car_dict["firetruck"] = Image(dir_car_assets, 'firetruck.png').get()
car_dict["estate"] = Image(dir_car_assets, 'estate.png').get()
car_dict["truck"] = Image(dir_car_assets, 'truck.png').get()
car_dict["small"] = Image(dir_car_assets, 'car.png').get()
train_dict["green_small"] = Image(dir_train_assets, 'zug_g_57x320.png').get()
train_dict["green_medium"] = Image(dir_train_assets, 'zug_g_97x320.png').get()
train_dict["green_large"] = Image(dir_train_assets, 'zug_g_112x320.png').get()
train_dict["orange_small"] = Image(dir_train_assets, 'zug_o_57x320.png').get()
train_dict["orange_medium"] = Image(dir_train_assets, 'zug_o_97x320.png').get()
train_dict["orange_large"] = Image(dir_train_assets, 'zug_o_112x320.png').get()


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
        self.image = car_dict["small"]


class EstateCar(Sprite):
    def __init__(self):
        super().__init__()
        self.image = car_dict["estate"]


class Truck(Sprite):
    def __init__(self):
        super().__init__()
        self.image = car_dict["truck"]


class FireTruck(Sprite):
    def __init__(self):
        super().__init__()
        self.image = car_dict["firetruck"]

class TrainSmallGreen(Sprite):
    def __init__(self):
        super().__init__()
        self.image = train_dict["green_small"]

class TrainMediumGreen(Sprite):
    def __init__(self):
        super().__init__()
        self.image = train_dict["green_medium"]

class TrainLargeGreen(Sprite):
    def __init__(self):
        super().__init__()
        self.image = train_dict["green_large"]

class TrainSmallOrange(Sprite):
    def __init__(self):
        super().__init__()
        self.image = train_dict["orange_small"]

class TrainMediumOrange(Sprite):
    def __init__(self):
        super().__init__()
        self.image = train_dict["orange_medium"]

class TrainLargeOrange(Sprite):
    def __init__(self):
        super().__init__()
        self.image = train_dict["orange_large"]
