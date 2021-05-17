import pygame
from settings import * # NOQA

# Initialisierung
pygame.init()
pygame.mixer.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption(GAME_NAME)
clock = pygame.time.Clock()

running = True

while running:
    # Game Loop
    clock.tick(SCREEN_FPS)

    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update
    # Should be done right

    # Render
    screen.fill((0, 0, 255))

    # Display
    pygame.display.flip()


pygame.quit()
