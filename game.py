import pygame
from settings import *
from character import Character
from fence import FenceBottom, FenceTop
from keyboard_control import KeyboardControl
from sprite_generator import SpriteGenerator


class Game:
    def __init__(self):
        self.pygame = pygame
        self.pygame.init()
        self.pygame.mixer.init()
        self.pygame.display.set_caption(GAME_NAME)

        self.clock = self.pygame.time.Clock()

        self.screen = self.pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

        self.lanes = SpriteGenerator().generate()
        self.player = Character()
        self.fence_top = FenceTop()
        self.fence_bottom = FenceBottom()

        self.keyboard_control = KeyboardControl(self.pygame, self.player)

    def loop(self):
        self.clock.tick(SCREEN_FPS)

        for event in self.pygame.event.get():

            # Did the user click the window close button?
            if event.type == self.pygame.QUIT:
                self.quit()

            # Listen for Keyboard Events and execute mapped Keyboard Control
            if event.type == self.pygame.KEYDOWN:
                self.keyboard_control.execute(event)

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
