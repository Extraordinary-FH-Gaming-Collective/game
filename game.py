import pygame
from settings import *
from character import Character
from fence import FenceBottom, FenceTop
from keyboard_control import KeyboardControl
from sprite_generator import SpriteGenerator
from preGame import PreGame


class Game:
    def __init__(self):
        self.mode = 'menu'
        self.pygame = pygame
        self.pygame.init()
        self.pygame.mixer.init()
        self.pygame.display.set_caption(GAME_NAME)

        self.preGame = PreGame(self)
       
        self.clock = self.pygame.time.Clock()
        self.screen = self.pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

        self.lanes = SpriteGenerator().generate()
        self.player = Character()
        self.fence_top = FenceTop()
        self.fence_bottom = FenceBottom()

        self.keyboard_control = KeyboardControl(self)

    def loop(self):
        self.beforeLoop()

        if self.mode == 'game':
            self.game()
        elif self.mode == 'introduction':
            self.introduction()
        else:
            self.menu()
    
        self.afterLoop()

    def introduction(self):
        self.preGame.introduction()

    def menu(self):
        self.preGame.menu()

    def game(self):
        self.keyboard_control.execute(self.pygame.event.get())

        self.lanes.update()

        if self.lanes.isColliding(self.player):
            # We could doe something in case we want to.
            self.player.leben -= 1

        self.screen.blit(BACKGROUND_IMAGE, (0, 0))
        self.fence_top.render(self.screen)
        self.player.render(self.screen)
        self.fence_bottom.render(self.screen)

        self.lanes.render(self.screen)

    def gameOver(self):
        pass

    def beforeLoop(self):
        self.clock.tick(SCREEN_FPS)
        self.implementExitOptioins()

    def afterLoop(self):
        self.pygame.display.flip()

    def implementExitOptioins(self):
        for event in self.pygame.event.get():
            if event.type == self.pygame.QUIT:
                self.quit()

            if event.type == self.pygame.KEYDOWN:
                if event.key == self.pygame.K_ESCAPE:
                    self.mode = 'menu'

    def quit(self):
        self.pygame.quit()
