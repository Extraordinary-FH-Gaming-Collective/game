import pygame


class Endzone(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([50, 30])
        self.image.fill((255, 0, 0))
        self.position_x = pos_x
        self.position_y = pos_y
        self.rect = self.image.get_rect()

    def draw(self, screen):
        screen.blit(self.image, (self.position_x, self.position_y))

    def update(self):
        self.rect.x = self.position_x
        self.rect.y = self.position_y
