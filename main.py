import pygame
import os
import random
from settings import *


# Initialisierung
pygame.init()
pygame.mixer.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mein Spiel")
clock = pygame.time.Clock()

# Hier Grafiken einbinden
image_dict = {}
game_folder = os.path.dirname(__file__)
image_dict["ball"] = pygame.image.load(os.path.join(game_folder, "ball.png"))


class ISprite:
    def update(self):
        raise NotImplementedError


class Ball(ISprite):
    def __init__(self, x, y, sx, sy, image):
        self.x = x
        self.y = y
        self.sx = sx
        self.sy = sy
        self.image = image
        self.ball_rect = image.get_rect()

    def update(self):
        # Ballbewegung
        self.x = self.x + self.sx
        self.y = self.y + self.sy
        self.ball_rect.topleft = (self.x, self.y)

        if self.ball_rect.right > WIDTH or self.ball_rect.left < 0:
            self.sx = self.sx * -1
        if self.ball_rect.bottom > HEIGHT or self.ball_rect.top < 0:
            self.sy = self.sy * -1

    def render(self, screen):
        screen.blit(self.image, self.ball_rect)


# sprites
sprite_list = []
for _ in range(30):
    ball = Ball(random.randint(20, WIDTH-20),
                random.randint(20, HEIGHT-20), random.randint(3, 7), random.randint(3, 7), image_dict["ball"])
    sprite_list.append(ball)


running = True

while running:
    # Game Loop
    clock.tick(FPS)

    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update
    for sprite in sprite_list:
        sprite.update()

    # Rendern
    screen.fill(BLAU)
    for sprite in sprite_list:
        sprite.render(screen)

    # Display
    pygame.display.flip()

# pygame.quit()
