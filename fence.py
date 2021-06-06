import pygame

# Load Images
fence_top_image = pygame.image.load("assets/boundaries/fence_top.png")
fence_bottom_image = pygame.image.load("assets/boundaries/fence_bottom.png")


class Fence:
    def __init__(self):
        self.image
        self.position_y

    def render(self):
        raise NotImplementedError


class FenceTop(Fence):
    def __init__(self):
        self.image = fence_top_image
        self.position_y = 185
        self.position_x = 0

    def render(self, screen):
        screen.blit(self.image, (self.position_x, self.position_y))


class FenceBottom(Fence):
    def __init__(self):
        self.image = fence_bottom_image
        self.position_y = 645

    def render(self, screen):
        screen.blit(self.image, (0, 0))
