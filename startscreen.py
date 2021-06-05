import pygame
from pygame.locals import *
from settings import *

mainClock = pygame.time.Clock()
pygame.init()
pygame.display.set_caption(GAME_NAME)
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.font.init()
menu_font = pygame.font.SysFont(None, 50)
header_font = pygame.font.SysFont(None, 70)

# Textgenerierer
def text_drawer(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)


# hier läuft später die Gameklasse drin
def game():

    running = True
    while running:
        screen.blit(BACKGROUND_IMAGE, (0, 0))
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
        pygame.display.update()
        mainClock.tick(SCREEN_FPS)

# hier wird die Anleitung generiert
def introduction():


    running = True
    while running:
        screen.blit(START_BACKGROUND_IMAGE, (0, 0))
        text_drawer("Anleitung", menu_font, (COLOR_BLACK), screen, 560, 30)
        text_drawer("Versuche alle Spieler rüber zubringen.", menu_font, (COLOR_BLACK), screen, 50, 150)
        text_drawer("Weiche den Autos aus und bleibe auf den Zügen.", menu_font, (COLOR_BLACK), screen, 50, 200)
        text_drawer("Der Spieler wird mit den Pfeiltasten gesteuert.", menu_font, (COLOR_BLACK), screen, 50, 250)
        text_drawer("Mit der Escape-Taste kommst du zurück ins Menu.", menu_font, (COLOR_BLACK), screen, 50, 300)
        text_drawer("Du hast 3 Leben und somit 3 Versuche.", menu_font, (COLOR_BLACK), screen, 50, 350)
        text_drawer("Beeile dich die Zeit läuft, sowie deine Punkte!", menu_font, (COLOR_BLACK), screen, 50, 400)
        text_drawer("Hab Spaß beim Spielen :)", menu_font, (COLOR_BLACK), screen, 50, 500)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
        pygame.display.update()
        mainClock.tick(SCREEN_FPS)


mouse_click = False

def startscreen():


    while True:
        # Ich denke das könnte man eleganter Lösen
        # Meine Versuche mit Screen_WIDTH/2 -Textlänge haben leider nicht geklappt
        screen.blit(START_BACKGROUND_IMAGE, (0, 0))
        text_drawer("Frogger City", header_font, (COLOR_BLACK), screen, 495, 80)

        mouse_x, mouse_y = pygame.mouse.get_pos()

        # Buttonzeichnung
        start_button = pygame.Rect(SCREEN_WIDTH / 2 - 100, 210, 200, 50)
        introduction_button = pygame.Rect(SCREEN_WIDTH / 2 - 100, 330, 200, 50)
        game_exit_button = pygame.Rect(SCREEN_WIDTH / 2 - 100, 470, 200, 50)

        # Mausclick-Abfragen
        if start_button.collidepoint((mouse_x, mouse_y)):
            if mouse_click:
                game()

        if introduction_button.collidepoint((mouse_x, mouse_y)):
            if mouse_click:
                introduction()

        if game_exit_button.collidepoint((mouse_x, mouse_y)):
            if mouse_click:
                pygame.quit()
                exit()

        # Zeichnung Button für den Start
        pygame.draw.rect(screen, (COLOR_GRAY_WHITE), start_button)
        text_drawer("Start", menu_font, (COLOR_BLACK), screen, 600, 220)

        # Zeichnung Button für die Anleitung
        pygame.draw.rect(screen, (COLOR_GRAY_WHITE), introduction_button)
        text_drawer("Anleitung", menu_font, (COLOR_BLACK), screen, 555, 340)

        # Zeichnung Button für Spiel schließen
        pygame.draw.rect(screen, (COLOR_GRAY_WHITE), game_exit_button)
        text_drawer("Beenden", menu_font, (COLOR_BLACK), screen, 565, 480)

        # Eingabeüberprüfer
        mouse_click = False
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()

            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    exit()

            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    mouse_click = True

        pygame.display.update()
        mainClock.tick(SCREEN_FPS)


startscreen()