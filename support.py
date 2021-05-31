import pygame
import os


class Image:
    def __init__(self, directory: str, path: str):
        self.image = pygame.image.load(os.path.join(os.path.dirname(directory), path))

    def flip(self):
        self.image = pygame.transform.flip(self.image, True, False)

        return self

    def get(self):
        return self.image