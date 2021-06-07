import pygame


class Endzone(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([20, 20], pygame.SRCALPHA, 32)
        self.image = self.image.convert_alpha()
        self.position_x = pos_x
        self.position_y = pos_y
        self.rect = self.image.get_rect()

    def draw(self, screen):
        screen.blit(self.image, (self.position_x, self.position_y))

    def update(self):
        self.rect.x = self.position_x
        self.rect.y = self.position_y

    def reached(self, player):
        self.image = player.image


class Endzones:
    def __init__(self):
        self.ez1 = Endzone(243, 165)
        self.ez2 = Endzone(450, 165)
        self.ez3 = Endzone(630, 165)
        self.ez4 = Endzone(830, 165)
        self.ez5 = Endzone(1010, 165)
        self.group = pygame.sprite.Group()
        self.group.add(self.ez1, self.ez2, self.ez3, self.ez4, self.ez5)

    def check_for_reach(self, character):
        reached_endzone = pygame.sprite.spritecollideany(character, self.group)
        if reached_endzone:
            character.cheer()
            reached_endzone.reached(character)
            character.back_to_start()
