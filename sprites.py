import pygame
import os
from support import Image

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
        self.image = Image('assets/cars/', 'car.png').get()
        self.position_y = 620
        self.position_x = 200
        self.row = 1

    def update(self):
        self.position_x += 3

        if (self.position_x > 1300):
            self.position_x = 0