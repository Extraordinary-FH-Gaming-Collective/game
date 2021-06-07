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


class Obstacles:
    def __init__(self):
        self.obs1 = Obstacle(0, 230)
        self.obs2 = Obstacle(283, 140)
        self.obs3 = Obstacle(490, 120)
        self.obs4 = Obstacle(675, 135)
        self.obs5 = Obstacle(875, 110)
        self.obs6 = Obstacle(1050, 600)
        self.group = pygame.sprite.Group()
        self.group.add(self.obs1, self.obs2, self.obs3, self.obs4, self.obs5, self.obs6)

    def check_for_collision(self, character):
        collided_obstacle = pygame.sprite.spritecollideany(character, self.group)
        if collided_obstacle:
            character.bounce_back()
