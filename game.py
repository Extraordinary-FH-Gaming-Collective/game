import pygame
from settings import *
from character import Character
from fence import FenceBottom, FenceTop
from keyboard_control import KeyboardControl
from sprite_generator import SpriteGenerator
from character_commands import (
    MoveDownCommand,
    MoveLeftCommand,
    MoveRightCommand,
    MoveUpCommand,
)

# Initialisierung
pygame.init()
pygame.mixer.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption(GAME_NAME)
clock = pygame.time.Clock()

running = True

# Create a Character
lanes = SpriteGenerator().generate()
player = Character()
fence_top = FenceTop()
fence_bottom = FenceBottom()

# Create Control for Keyboard Events
keyboard_control = KeyboardControl()

# Map Keys to Keyboard Control
key_map = {
    pygame.K_UP: keyboard_control.press_arrowkey_up,
    pygame.K_DOWN: keyboard_control.press_arrowkey_down,
    pygame.K_RIGHT: keyboard_control.press_arrowkey_right,
    pygame.K_LEFT: keyboard_control.press_arrowkey_left,
}

# Map Character Commands to Control
keyboard_control.assign_arrowkey_up(MoveUpCommand(player))
keyboard_control.assign_arrowkey_down(MoveDownCommand(player))
keyboard_control.assign_arrowkey_right(MoveRightCommand(player))
keyboard_control.assign_arrowkey_left(MoveLeftCommand(player))


while running:
    # Game Loop
    clock.tick(SCREEN_FPS)

    for event in pygame.event.get():

        # Did the user click the window close button?
        if event.type == pygame.QUIT:
            running = False

        # Listen for Keyboard Events and execute mapped Keyboard Control
        if event.type == pygame.KEYDOWN:
            if event.key in key_map:
                key_map[event.key]()

    # Update / Needs refactoring
    lanes.update()
    lanes.collision(player)  # This can't work as it is, as we need to return a result in case something did collide.

    # Render / Needs refactoring
    screen.blit(BACKGROUND_IMAGE, (0, 0))
    fence_top.render(screen)
    player.render(screen)
    fence_bottom.render(screen)

    lanes.render(screen)

    # Display
    pygame.display.flip()


pygame.quit()
