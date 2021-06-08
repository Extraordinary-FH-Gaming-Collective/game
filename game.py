import pygame
from settings import *
from character import Character
from fence import FenceBottom, FenceTop
from endzone import Endzones
from obstacles import Obstacles
from keyboard_control import KeyboardControl
from sprite_generator import SpriteGenerator
from text_screen import TextScreen
from score import Scorer
from text_drawer import TextDrawer


class Game:
    def __init__(self):
        self.mode = "menu"
        self.pygame = pygame
        self.pygame.init()
        self.pygame.mixer.init()
        self.pygame.display.set_caption(GAME_NAME)
        self.scorer = Scorer()

        self.clock = self.pygame.time.Clock()
        self.screen = self.pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

        self.text_drawer = TextDrawer(self.screen)
        self.text_screen = TextScreen(self)

        self.lanes = SpriteGenerator().generate()
        self.player = Character(self.lanes)
        self.fence_top = FenceTop()
        self.fence_bottom = FenceBottom()
        self.endzones = Endzones()
        self.obstacles = Obstacles()

        self.keyboard_control = KeyboardControl(self)

        pygame.mixer.music.load("assets/sounds/Jim Hall - Elsewhere.mp3")
        pygame.mixer.Channel(0).play(
            pygame.mixer.Sound("assets/sounds/Jim Hall - Elsewhere.mp3")
        )

    def loop(self):
        self.beforeLoop()

        if self.mode == "game":
            self.game()
        elif self.mode == "instructions":
            self.instructions()
        elif self.mode == "gameover":
            self.game_over()
        elif self.mode == "gamewon":
            self.won()
        else:
            self.menu()

        self.afterLoop()

    def instructions(self):
        self.text_screen.show_instructions()

    def menu(self):
        self.text_screen.show_menu()
        self.reset_game()

    def won(self):
        self.text_screen.show_winning_screen(self.scorer.points)

    def game_over(self):
        self.text_screen.show_game_over_screen()

    def game(self):
        self.keyboard_control.execute()
        self.lanes.checkCollision(self.player, self.scorer)

        if self.player.leben == 0:
            self.mode = "gameover"

        if self.scorer.goal == 5:
            self.mode = "gamewon"

        self.render()
        self.show_score()
        self.update()

        self.endzones.check_for_reach(self.player, self.scorer)
        self.obstacles.check_for_collision(self.player)

    def render(self):
        self.screen.blit(BACKGROUND_IMAGE, (0, 0))
        self.fence_top.render(self.screen)
        self.endzones.group.draw(self.screen)
        self.fence_bottom.render(self.screen)
        self.lanes.renderTrains(self.screen)
        self.player.render(self.screen)
        self.lanes.renderCars(self.screen)

    def update(self):
        self.lanes.update()
        self.endzones.group.update()
        self.obstacles.group.update()
        self.player.update()
        self.scorer.countdown_score()

    def show_score(self):
        self.pygame.font.init()
        font = self.pygame.font.SysFont(None, 40)
        score_text = f"{self.scorer.points} Punkte"
        self.text_drawer.draw(score_text, font, (COLOR_WHITE), 1100, 100)

    def beforeLoop(self):
        self.clock.tick(SCREEN_FPS)

    def reset_game(self):
        self.scorer.reset_score()
        self.player.leben = 3
        self.endzones = Endzones()

    def afterLoop(self):
        self.pygame.display.flip()

    def quit(self):
        self.pygame.quit()
