import pygame


class Obstacle(pygame.sprite.Sprite):
    def __init__(self, start_pos_x, length):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([length, 20])
        self.image.fill((255, 0, 0))
        self.position_x = start_pos_x
        self.position_y = 185
        self.rect = self.image.get_rect()

    def draw(self, screen):
        screen.blit(self.image, (self.position_x, self.position_y))

    def update(self):
        self.rect.x = self.position_x
        self.rect.y = self.position_y
