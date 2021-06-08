import pygame
from settings import *
from character import Character
from fence import FenceBottom, FenceTop
from endzone import Endzones
from obstacles import Obstacles
from keyboardControl import KeyboardControl
from spriteGenerator import SpriteGenerator
from textScreen import TextScreen
from score import Scorer
from textDrawer import TextDrawer
from sounds import *


class Game:
    """ The Game class is the backbone of Frogger City

    Basically we do initialize all needed classes, which we later can reference too and am
    looping through our loop method as you can see in `main.py`.
    """

    def __init__(self):
        """ Initialize all needed classes

        This way of building our game does help, if working together with a team. Main information are kept
        in the game class. By passing `self` into a new initialized Class, all needed information can
        be parsed and worked with.

        This does make it possible for a team to work in different classes and to centralize all the logic there.
        """

        self.mode = "menu"
        self.pygame = pygame
        self.pygame.init()
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
        self.sounds = Sounds(self)

        self.keyboard_control = KeyboardControl(self)
        self.sounds.play_music()

    def loop(self):
        """ Can I introduce? Our game loop.

        We'll loop this method as often as defined in our frames per seconds setting in `settings.py`

        Depending on the game mode, we'll call different methods.
        """

        self.clock.tick(SCREEN_FPS)

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

        self.pygame.display.flip()

    def game(self):
        """ The game mode, which show the main game element: A busy boy running through Frogger City. """

        self.keyboard_control.execute()
        self.lanes.check_collision(self.player, self.scorer)

        if self.player.life == 0:
            self.mode = "gameover"

        if self.scorer.goal == 5:
            self.mode = "gamewon"

        self.render()
        self.show_score()
        self.update()

        self.endzones.check_for_reach(self.player, self.scorer)
        self.obstacles.check_for_collision(self.player)

    def render(self):
        """ Render all game elements. """

        self.screen.blit(BACKGROUND_IMAGE, (0, 0))
        self.fence_top.render(self.screen)
        self.endzones.group.draw(self.screen)
        self.fence_bottom.render(self.screen)
        self.lanes.render_trains(self.screen)
        self.player.render(self.screen)
        self.lanes.render_cars(self.screen)

    def update(self):
        """ Update alle game elements, so evertything keeps moving and calculating. """

        self.lanes.update()
        self.endzones.group.update()
        self.obstacles.group.update()
        self.player.update()
        self.scorer.countdown_score()

    def show_score(self):
        """ Renders the score in the game window. """

        self.pygame.font.init()
        font = self.pygame.font.SysFont(None, 40)
        score_text = f"{self.scorer.points} Punkte"
        self.text_drawer.draw(score_text, font, (COLOR_WHITE), 1100, 100)

    def menu(self):
        """ Displays the menu, which is the first screen in the game.

        This is the place we send the player to after each game, why
        we thougth it might make sense to reset the game right here.
        """

        self.text_screen.show_menu()
        self.reset_game()

    def instructions(self):
        """ A referenz to the TextScreen class to show game instructions. """

        self.text_screen.show_instructions()

    def won(self):
        """ Displays the winning screen. """

        self.text_screen.show_winning_screen(self.scorer.points)

    def game_over(self):
        """ Displays the game over screen. """

        self.text_screen.show_game_over_screen()

    def reset_game(self):
        """ Resets the game so you can start all over again. """

        self.scorer.reset_score()
        self.player.life = 3
        self.endzones = Endzones()

    def quit(self):
        """ Quits the game, if you want to leave. """

        self.pygame.quit()
