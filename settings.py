import pygame

GAME_NAME = "Frogger City"

SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
SCREEN_FPS = 60
BACKGROUND_IMAGE = pygame.image.load("assets/map_1280x720.png")

COLOR_BLACK = (0, 0, 0)
COLOR_WHITE = (255, 255, 255)

CHARACTER_STEP_SIZE = 45

MAP_BOTTOM_PADDING = 12

GENERATE_CARS_FIRETRUCK = 13
GENERATE_CARS_ESTATE = 15
GENERATE_CARS_TRUCK = 15
GENERATE_CARS_SMALL = 13

GENERATE_TRAINS_SMALL = 8
GENERATE_TRAINS_MEDIUM = 8
GENERATE_TRAINS_LARGE = 8

SPRITE_MINIMUM_SPEED = 6
SPRITE_MAXIMUM_SPEED = 12

MINIMUM_CARS_PER_LANE = 5
MAXIMUM_CARS_PER_LANE = 8
MINIMUM_TRAINS_PER_LANE = 1
MAXIMUM_TRAINS_PER_LANE = 3
