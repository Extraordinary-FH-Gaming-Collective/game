import pygame
from settings import *
from character import Character
from sprites import SmallCar
from keyboard_control import KeyboardControl
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

player = Character()
dummyCar = SmallCar()


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


# Kollisionsabfrage / draw.rect nur temporär zu Veranschaulichung der Kollision / leider noch buggy, da keine einmalige Kollisionsabfrage
def checkCollision():
    collision_tolerance = 3

    playerRectangle = pygame.Rect(player.position_x, player.position_y, 21, 35)
    pygame.draw.rect(screen, (255,255,0), playerRectangle, 3)

    carRectangle = pygame.Rect(dummyCar.position_x, dummyCar.position_y, 62, 51)
    pygame.draw.rect(screen, (255,255,0), carRectangle, 3)
  
    if playerRectangle.colliderect(carRectangle):
        if abs(playerRectangle.left - carRectangle.right) < collision_tolerance:
            player.leben -=1
        if abs(playerRectangle.right - carRectangle.left) < collision_tolerance:
            player.leben -=1
        if abs(playerRectangle.top - carRectangle.bottom) < collision_tolerance:
            player.leben -=1
        if abs(playerRectangle.bottom - carRectangle.top) < collision_tolerance:
            player.leben -=1


        


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

    # Render / Needs refactoring
    screen.blit(BACKGROUND_IMAGE, (0, 0))
    dummyCar.render(screen)
    player.render(screen)
    checkCollision()

    # Update / Needs refactoring
    dummyCar.update()

    # Display
    pygame.display.flip()


pygame.quit()
