import pygame
from settings import *
from character import Character
from sprites import SmallCar
from boundaries import FenceBottom, FenceTop

# Initialisierung
pygame.init()
pygame.mixer.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption(GAME_NAME)
clock = pygame.time.Clock()

running = True

# Create a Character
player = Character()
dummyCar = SmallCar()
fence_top = FenceTop()
fence_bottom = FenceBottom()


while running:
    # Game Loop
    clock.tick(SCREEN_FPS)

    for event in pygame.event.get():

        # Did the user click the window close button?
        if event.type == pygame.QUIT:
            running = False

        # Listen for Keyboard Events
        # TODO Outsource Key Binding ( maybe using Command Pattern)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                player.move_up()

            if event.key == pygame.K_DOWN:
                player.move_down()

            if event.key == pygame.K_RIGHT:
                player.move_right()

            if event.key == pygame.K_LEFT:
                player.move_left()

    # Render / Needs refactoring
    screen.blit(BACKGROUND_IMAGE, (0, 0))
    dummyCar.render(screen)
    fence_top.render(screen)
    player.render(screen)
    fence_bottom.render(screen)

    # Update / Needs refactoring
    dummyCar.update()

    # Display
    pygame.display.flip()


pygame.quit()
