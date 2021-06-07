from support import Image

GAME_NAME = "Frogger City"

SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
SCREEN_FPS = 60
BACKGROUND_IMAGE = Image("assets/", "map_1280x720.png").get()
START_BACKGROUND_IMAGE = Image("assets/", "map_1280x720_gray.png").get()

# Borders of the walkable Area for the Character
BORDER_TOP = 180  # Y Position of Top Border
BORDER_BOTTOM = 675  # Y Position of Bottom Border
BORDER_RIGHT = SCREEN_WIDTH  # X Position Right Border
BORDER_LEFT = 22  # X Position of Left Border

COLOR_BLACK = (0, 0, 0)
COLOR_WHITE = (255, 255, 255)
COLOR_GRAY_WHITE = (230, 230, 230)

CHARACTER_START_POSITION_X = 580
CHARACTER_START_POSITION_Y = BORDER_BOTTOM
CHARACTER_STEP_SIZE = 43

MAP_BOTTOM_PADDING = 12

GENERATE_CARS_FIRETRUCK = 13
GENERATE_CARS_ESTATE = 15
GENERATE_CARS_TRUCK = 15
GENERATE_CARS_SMALL = 13

GENERATE_TRAINS_SMALL = 8
GENERATE_TRAINS_MEDIUM = 8
GENERATE_TRAINS_LARGE = 8

SPRITE_MINIMUM_SPEED = 4
SPRITE_MAXIMUM_SPEED = 9

MINIMUM_CARS_PER_LANE = 4
MAXIMUM_CARS_PER_LANE = 6
MINIMUM_TRAINS_PER_LANE = 2
MAXIMUM_TRAINS_PER_LANE = 3

MINIMUM_CARS_DISTANCE = 20
MAXIMUM_CARS_DISTANCE = 300
MINIMUM_TRAINS_DISTANCE = 40
MAXIMUM_TRAINS_DISTANCE = 300
