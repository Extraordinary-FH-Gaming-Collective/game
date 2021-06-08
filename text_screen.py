from settings import *


class TextScreen:
    def __init__(self, game):
        self.game = game
        self.game.pygame.font.init()
        self.mouse_click = False
        self.text_drawer = self.game.text_drawer

        self.menu_font = self.game.pygame.font.SysFont(None, 50)
        self.header_font = self.game.pygame.font.SysFont(None, 70)

    def show_instructions(self):
        self.game.screen.blit(START_BACKGROUND_IMAGE, (0, 0))

        self.text_drawer.draw("Anleitung", self.menu_font, (COLOR_BLACK), 560, 30)
        self.text_drawer.draw(
            "Versuche alle Spieler rüber zubringen.",
            self.menu_font,
            (COLOR_BLACK),
            50,
            150,
        )
        self.text_drawer.draw(
            "Weiche den Autos aus und bleibe auf den Zügen.",
            self.menu_font,
            (COLOR_BLACK),
            50,
            200,
        )
        self.text_drawer.draw(
            "Der Spieler wird mit den Pfeiltasten gesteuert.",
            self.menu_font,
            (COLOR_BLACK),
            50,
            250,
        )
        self.text_drawer.draw(
            "Mit der Escape-Taste kommst du zurück ins Menu.",
            self.menu_font,
            (COLOR_BLACK),
            50,
            300,
        )
        self.text_drawer.draw(
            "Du hast 3 Leben und somit 3 Versuche.",
            self.menu_font,
            (COLOR_BLACK),
            50,
            350,
        )
        self.text_drawer.draw(
            "Beeile dich die Zeit läuft, sowie deine Punkte!",
            self.menu_font,
            (COLOR_BLACK),
            50,
            400,
        )
        self.text_drawer.draw(
            "Hab Spaß beim Spielen :)",
            self.menu_font,
            (COLOR_BLACK),
            50,
            500,
        )

        for event in self.game.pygame.event.get():
            self.defaultExitOptions(event)

    def show_menu(self):
        self.game.screen.blit(START_BACKGROUND_IMAGE, (0, 0))
        self.text_drawer.draw("Frogger City", self.header_font, (COLOR_BLACK), 495, 80)

        mouse_x, mouse_y = self.game.pygame.mouse.get_pos()

        # Buttonzeichnung
        start_button = self.game.pygame.Rect(SCREEN_WIDTH / 2 - 100, 210, 200, 50)
        instructions_button = self.game.pygame.Rect(
            SCREEN_WIDTH / 2 - 100, 330, 200, 50
        )
        game_exit_button = self.game.pygame.Rect(SCREEN_WIDTH / 2 - 100, 470, 200, 50)

        # Zeichnung Button für den Start
        self.game.pygame.draw.rect(self.game.screen, (COLOR_GRAY_WHITE), start_button)
        self.text_drawer.draw("Start", self.menu_font, (COLOR_BLACK), 600, 220)

        # Zeichnung Button für die Anleitung
        self.game.pygame.draw.rect(
            self.game.screen, (COLOR_GRAY_WHITE), instructions_button
        )
        self.text_drawer.draw("Anleitung", self.menu_font, (COLOR_BLACK), 555, 340)

        # Zeichnung Button für Spiel schließen
        self.game.pygame.draw.rect(
            self.game.screen, (COLOR_GRAY_WHITE), game_exit_button
        )
        self.text_drawer.draw("Beenden", self.menu_font, (COLOR_BLACK), 565, 480)

        for event in self.game.pygame.event.get():
            if event.type == self.game.pygame.MOUSEBUTTONDOWN and event.button == 1:
                self.mouse_click = True

            self.defaultExitOptions(event)

        # Mausclick-Abfragen
        if self.mouse_click and start_button.collidepoint((mouse_x, mouse_y)):
            self.game.mode = "game"

        if self.mouse_click and instructions_button.collidepoint((mouse_x, mouse_y)):
            self.game.mode = "instructions"

        if self.mouse_click and game_exit_button.collidepoint((mouse_x, mouse_y)):
            self.game.quit()

        # Eingabeüberprüfer
        self.mouse_click = False

    # def text_drawer(self, text, font, color, screen, x, y):
    #     textobj = font.render(text, 1, color)
    #     textrect = textobj.get_rect()
    #     textrect.topleft = (x, y)
    #     screen.blit(textobj, textrect)

    def defaultExitOptions(self, event):
        if event.type == self.game.pygame.QUIT:
            self.game.quit()

        if event.type != self.game.pygame.KEYDOWN:
            return  # Do nothing in case it's not a keydown

        if event.key == self.game.pygame.K_ESCAPE:
            self.game.mode = "menu"

        if event.key == self.game.pygame.K_SPACE:
            self.game.reset_game()
            self.game.mode = "game"

    def show_game_over_screen(self):
        self.game.screen.blit(BACKGROUND_DEATH, (0, 0))

        self.text_drawer.draw(
            "Mit der Escape-Taste kommst du zurück ins Menu.",
            self.menu_font,
            (COLOR_BLACK),
            250,
            500,
        )

        for event in self.game.pygame.event.get():
            self.defaultExitOptions(event)

    def show_winning_screen(self, score):
        self.game.screen.blit(START_BACKGROUND_IMAGE, (0, 0))
        scoretext = f"Du hast {score} Punkte erzielt"

        self.text_drawer.draw(
            "Du hast gewonnen!",
            self.header_font,
            (COLOR_BLACK),
            350,
            150,
        )

        self.text_drawer.draw(
            scoretext,
            self.menu_font,
            (COLOR_BLACK),
            300,
            300,
        )
        self.text_drawer.draw(
            "Mit der Escape-Taste kommst du zurück ins Menu.",
            self.menu_font,
            (COLOR_BLACK),
            250,
            500,
        )
        for event in self.game.pygame.event.get():
            self.defaultExitOptions(event)
