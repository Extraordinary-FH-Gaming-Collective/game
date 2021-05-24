import pygame
from settings import *
from character import Character

# Initialisierung
pygame.init()
pygame.mixer.init()

background = pygame.image.load("add-visual_content/game_source/grids/player_lines_grid.png") 
# has to be changed in the final version to add-visual_content/game_source/map_1280x720.png
screen = pygame.display.set_mode((1280, 720))
pygame.display.set_caption(GAME_NAME)
clock = pygame.time.Clock()

running = True

# Create a Character
player = Character()


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

    # Update
    # Should be done right

    # Render
    screen.blit(background, (0,0))

    player.render(screen)

    # Display
    pygame.display.flip()


pygame.quit()
