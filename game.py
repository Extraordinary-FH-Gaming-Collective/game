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


class Game:
    def __init__(self):
        self.pygame = pygame
        self.pygame.init()
        self.pygame.mixer.init()
        self.pygame.display.set_caption(GAME_NAME)

        self.clock = self.pygame.time.Clock()

        self.screen =  self.pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

        self.lanes = SpriteGenerator().generate()
        self.player = Character()
        self.fence_top = FenceTop()
        self.fence_bottom = FenceBottom()

        self.keyboard_control = KeyboardControl()

        self.key_map = {
            self.pygame.K_UP: self.keyboard_control.press_arrowkey_up,
            self.pygame.K_DOWN: self.keyboard_control.press_arrowkey_down,
            self.pygame.K_RIGHT: self.keyboard_control.press_arrowkey_right,
            self.pygame.K_LEFT: self.keyboard_control.press_arrowkey_left,
        }

        self.keyboard_control.assign_arrowkey_up(MoveUpCommand(self.player))
        self.keyboard_control.assign_arrowkey_down(MoveDownCommand(self.player))
        self.keyboard_control.assign_arrowkey_right(MoveRightCommand(self.player))
        self.keyboard_control.assign_arrowkey_left(MoveLeftCommand(self.player))

    def loop(self):
        self.clock.tick(SCREEN_FPS)

        for event in self.pygame.event.get():

            # Did the user click the window close button?
            if event.type == self.pygame.QUIT:
                self.quit()

            # Listen for Keyboard Events and execute mapped Keyboard Control
            if event.type == self.pygame.KEYDOWN:
                if event.key in self.key_map:
                    self.key_map[event.key]()

        self.lanes.update()

        if self.lanes.isColliding(self.player):
        # We could doe something in case we want to.
            self.player.leben -=1

        self.screen.blit(BACKGROUND_IMAGE, (0, 0))
        self.fence_top.render(self.screen)
        self.player.render(self.screen)
        self.fence_bottom.render(self.screen)

        self.lanes.render(self.screen)

        self.pygame.display.flip()

    def quit(self):
        self.pygame.quit()
