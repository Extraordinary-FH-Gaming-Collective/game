from settings import *


class PreGame:
    def __init__(self, game):
        self.game = game
        self.game.pygame.font.init()
        self.mouse_click = False

        self.menu_font = self.game.pygame.font.SysFont(None, 50)
        self.header_font = self.game.pygame.font.SysFont(None, 70)

    def introduction(self):
        self.game.screen.blit(START_BACKGROUND_IMAGE, (0, 0))

        self.text_drawer(
            "Anleitung",
            self.menu_font, (COLOR_BLACK), self.game.screen, 560, 30
        )
        self.text_drawer(
            "Versuche alle Spieler rüber zubringen.",
            self.menu_font, (COLOR_BLACK), self.game.screen, 50, 150
        )
        self.text_drawer(
            "Weiche den Autos aus und bleibe auf den Zügen.",
            self.menu_font, (COLOR_BLACK), self.game.screen, 50, 200
        )
        self.text_drawer(
            "Der Spieler wird mit den Pfeiltasten gesteuert.",
            self.menu_font, (COLOR_BLACK), self.game.screen, 50, 250
        )
        self.text_drawer(
            "Mit der Escape-Taste kommst du zurück ins Menu.",
            self.menu_font, (COLOR_BLACK), self.game.screen, 50, 300
        )
        self.text_drawer(
            "Du hast 3 Leben und somit 3 Versuche.",
            self.menu_font, (COLOR_BLACK), self.game.screen, 50, 350
        )
        self.text_drawer(
            "Beeile dich die Zeit läuft, sowie deine Punkte!",
            self.menu_font, (COLOR_BLACK), self.game.screen, 50, 400
        )
        self.text_drawer(
            "Hab Spaß beim Spielen :)",
            self.menu_font, (COLOR_BLACK), self.game.screen, 50, 500
        )

        for event in self.game.pygame.event.get():
            self.defaultExitOptions(event)

    def menu(self):
        self.game.screen.blit(START_BACKGROUND_IMAGE, (0, 0))
        self.text_drawer(
            "Frogger City",
            self.header_font, (COLOR_BLACK), self.game.screen, 495, 80
        )

        mouse_x, mouse_y = self.game.pygame.mouse.get_pos()

        # Buttonzeichnung
        start_button = self.game.pygame.Rect(SCREEN_WIDTH / 2 - 100, 210, 200, 50)
        introduction_button = self.game.pygame.Rect(SCREEN_WIDTH / 2 - 100, 330, 200, 50)
        game_exit_button = self.game.pygame.Rect(SCREEN_WIDTH / 2 - 100, 470, 200, 50)

        # Zeichnung Button für den Start
        pygame.draw.rect(self.game.screen, (COLOR_GRAY_WHITE), start_button)
        self.text_drawer("Start", self.menu_font, (COLOR_BLACK), self.game.screen, 600, 220)

        # Zeichnung Button für die Anleitung
        pygame.draw.rect(self.game.screen, (COLOR_GRAY_WHITE), introduction_button)
        self.text_drawer("Anleitung", self.menu_font, (COLOR_BLACK), self.game.screen, 555, 340)

        # Zeichnung Button für Spiel schließen
        pygame.draw.rect(self.game.screen, (COLOR_GRAY_WHITE), game_exit_button)
        self.text_drawer("Beenden", self.menu_font, (COLOR_BLACK), self.game.screen, 565, 480)

        for event in self.game.pygame.event.get():
            if event.type == self.game.pygame.MOUSEBUTTONDOWN and event.button == 1:
                self.mouse_click = True

            self.defaultExitOptions(event)

        # Mausclick-Abfragen
        if self.mouse_click and start_button.collidepoint((mouse_x, mouse_y)):
            self.game.mode = 'game'

        if self.mouse_click and introduction_button.collidepoint((mouse_x, mouse_y)):
            self.game.mode = 'introduction'

        if self.mouse_click and game_exit_button.collidepoint((mouse_x, mouse_y)):
            self.game.quit()

        # Eingabeüberprüfer
        self.mouse_click = False

    def text_drawer(self, text, font, color, screen, x, y):
        textobj = font.render(text, 1, color)
        textrect = textobj.get_rect()
        textrect.topleft = (x, y)
        screen.blit(textobj, textrect)

    def defaultExitOptions(self, event):
        if event.type == self.game.pygame.QUIT:
            self.game.quit()

        if event.type != self.game.pygame.KEYDOWN:
            return  # Do nothing in case it's not a keydown

        if event.key == self.game.pygame.K_ESCAPE:
            self.game.mode = 'menu'

    def death_screen(self):
           self.game.screen.blit(BACKGROUND_DEATH, (0, 0))
