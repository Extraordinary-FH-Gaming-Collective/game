import pygame
from settings import *
from character import Character
from keyboard_control import KeyboardControl
from sprite_generator import SpriteGenerator
from endzone import Endzone
from obstacles import Obstacle
from fence import FenceBottom, FenceTop
from character_commands import (
    MoveDownCommand,
    MoveLeftCommand,
    MoveRightCommand,
    MoveUpCommand,
)

# Initialisierung
pygame.init()
pygame.mixer.init()


# background music
pygame.mixer.music.load('sounds\Jim Hall - Elsewhere.mp3')
pygame.mixer.Channel(0).play(pygame.mixer.Sound('sounds\Jim Hall - Elsewhere.mp3'))

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption(GAME_NAME)
clock = pygame.time.Clock()

running = True

# Create a Character
player = Character()

# Create Lanes including moving Sprites
lanes = SpriteGenerator().generate()

# Create Fences
fence_top = FenceTop()
fence_bottom = FenceBottom()

# Create Obstacles

obs1 = Obstacle(0, 230)
obs2 = Obstacle(283, 140)
obs3 = Obstacle(490, 120)
obs4 = Obstacle(675, 135)
obs5 = Obstacle(875, 110)
obs6 = Obstacle(1050, 600)

obstacle_group = pygame.sprite.Group()
obstacle_group.add(obs1, obs2, obs3, obs4, obs5, obs6)


# Create Endzones
endzone1 = Endzone(243, 165)
endzone2 = Endzone(450, 165)
endzone3 = Endzone(630, 165)
endzone4 = Endzone(830, 165)
endzone5 = Endzone(1010, 165)

endzone_group = pygame.sprite.Group()
endzone_group.add(endzone1, endzone2, endzone3, endzone4, endzone5)


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
    if lanes.isColliding(player):
        # We could doe something in case we want to.
        player.leben -= 1

    # Render / Needs refactoring

    screen.blit(BACKGROUND_IMAGE, (0, 0))
    endzone_group.draw(screen)
    fence_top.render(screen)
    lanes.render(screen)
    player.render(screen)
    fence_bottom.render(screen)

    # Update Rect Positions
    player.update()
    endzone_group.update()
    obstacle_group.update()

    # Collision Detection Player/Obstacles
    obstacle_reached = pygame.sprite.spritecollideany(player, obstacle_group)
    if obstacle_reached:
        player.bounce_back()

    # Collision Detection for Player/Endzones
    endzone_reached = pygame.sprite.spritecollideany(player, endzone_group)

    if endzone_reached:
        player.cheer()
        endzone_reached.reached(player)
        player.back_to_start()
        # TBD:
        # Counter += 1
        # Wenn der Counter auf 5 steht:
        #   Winning Screen anzeigen mit Score z.B.

    # Display
    pygame.display.flip()


pygame.quit()
