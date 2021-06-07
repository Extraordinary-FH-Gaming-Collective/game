from support import Image

dir_car_assets = "assets/cars/"
dir_train_assets = "assets/trains/"
car_dict = {}
train_dict = {}

car_dict["firetruck"] = (
    Image(dir_car_assets, 'firetruck.png').get(),
    Image(dir_car_assets, 'firetruck.png').flip().get()
)
car_dict["estate"] = (
    Image(dir_car_assets, 'estate.png').get(),
    Image(dir_car_assets, 'estate.png').flip().get()
)
car_dict["truck"] = (
    Image(dir_car_assets, 'truck.png').get(),
    Image(dir_car_assets, 'truck.png').flip().get()
)
car_dict["small"] = (
    Image(dir_car_assets, 'car.png').get(),
    Image(dir_car_assets, 'car.png').flip().get()
)
train_dict["green_small"] = (
    Image(dir_train_assets, 'zug_g_57x320.png').get(),
    Image(dir_train_assets, 'zug_g_57x320.png').flip().get()
)
train_dict["green_medium"] = (
    Image(dir_train_assets, 'zug_g_97x320.png').get(),
    Image(dir_train_assets, 'zug_g_97x320.png').flip().get()
)
train_dict["green_large"] = (
    Image(dir_train_assets, 'zug_g_112x320.png').get(),
    Image(dir_train_assets, 'zug_g_112x320.png').flip().get()
)
train_dict["orange_small"] = (
    Image(dir_train_assets, 'zug_o_57x320.png').get(),
    Image(dir_train_assets, 'zug_o_57x320.png').flip().get()
)
train_dict["orange_medium"] = (
    Image(dir_train_assets, 'zug_o_97x320.png').get(),
    Image(dir_train_assets, 'zug_o_97x320.png').flip().get()
)
train_dict["orange_large"] = (
    Image(dir_train_assets, 'zug_o_112x320.png').get(),
    Image(dir_train_assets, 'zug_o_112x320.png').flip().get()
)


class Sprite:
    def __init__(self):
        self.image = None
        self.image_left_to_right = None
        self.image_right_to_left = None
        self.position_x = -9999
        self.position_y = -9999
        self.left_to_right = None
        self.height_correction = 0
        self.speed = 0

    def update(self):
        if self.left_to_right:
            self.position_x += self.speed
        else:
            self.position_x -= self.speed

    def render(self, screen):
        screen.blit(self.image, (self.position_x, self.position_y))

    def setDirection(self, left_to_right: bool):
        if left_to_right:
            self.image = self.image_left_to_right
        else:
            self.image = self.image_right_to_left

        self.left_to_right = left_to_right

    def set(self, position_x: int, position_y: int):
        self.position_x = position_x
        self.position_y = position_y - self.height_correction

    def getWidth(self):
        return self.image.get_rect().w

    def getHeight(self):
        return self.image.get_rect().h


class SmallCar(Sprite):
    def __init__(self):
        super().__init__()
        self.image_left_to_right = car_dict["small"][0]
        self.image_right_to_left = car_dict["small"][1]


class EstateCar(Sprite):
    def __init__(self):
        super().__init__()
        self.height_correction = 4
        self.image_left_to_right = car_dict["estate"][0]
        self.image_right_to_left = car_dict["estate"][1]


class Truck(Sprite):
    def __init__(self):
        super().__init__()
        self.height_correction = 14
        self.image_left_to_right = car_dict["truck"][0]
        self.image_right_to_left = car_dict["truck"][1]


class FireTruck(Sprite):
    def __init__(self):
        super().__init__()
        self.height_correction = 36
        self.image_left_to_right = car_dict["firetruck"][0]
        self.image_right_to_left = car_dict["firetruck"][1]


class TrainSmallGreen(Sprite):
    def __init__(self):
        super().__init__()
        self.height_correction = 22
        self.image_left_to_right = train_dict["green_small"][0]
        self.image_right_to_left = train_dict["green_small"][1]


class TrainSmallOrange(Sprite):
    def __init__(self):
        super().__init__()
        self.height_correction = 22
        self.image_left_to_right = train_dict["orange_small"][0]
        self.image_right_to_left = train_dict["orange_small"][1]


class TrainMediumGreen(Sprite):
    def __init__(self):
        super().__init__()
        self.height_correction = 36
        self.image_left_to_right = train_dict["green_medium"][0]
        self.image_right_to_left = train_dict["green_medium"][1]


class TrainMediumOrange(Sprite):
    def __init__(self):
        super().__init__()
        self.height_correction = 36
        self.image_left_to_right = train_dict["orange_medium"][0]
        self.image_right_to_left = train_dict["orange_medium"][1]


class TrainLargeGreen(Sprite):
    def __init__(self):
        super().__init__()
        self.height_correction = 45
        self.image_left_to_right = train_dict["green_large"][0]
        self.image_right_to_left = train_dict["green_large"][1]


class TrainLargeOrange(Sprite):
    def __init__(self):
        super().__init__()
        self.height_correction = 45
        self.image_left_to_right = train_dict["orange_large"][0]
        self.image_right_to_left = train_dict["orange_large"][1]
