import pygame
import os

# Load Images
player_image_dict = {}
dir_assets_player = os.path.dirname("assets/player/")
player_image_dict["standing_up"] = pygame.image.load(
    os.path.join(dir_assets_player, "standing_up.png")
)
player_image_dict["standing_down"] = pygame.image.load(
    os.path.join(dir_assets_player, "standing_down.png")
)
player_image_dict["standing_right"] = pygame.image.load(
    os.path.join(dir_assets_player, "standing_right.png")
)
player_image_dict["standing_left"] = pygame.image.load(
    os.path.join(dir_assets_player, "standing_left.png")
)


class Character:
    def __init__(self):
        self.image = None
        self.state = LookingDown(self)
        self.position_y = 550
        self.position_x = 400
        self.step_size = 30
        self.row = 0

    def move_up(self):
        self.image = player_image_dict[
            "standing_up"
        ]  # Temp Solution - should update over the State
        self.position_y -= self.step_size
        self.row += 1
        self.state.look_up(self)

    def move_down(self):
        self.image = player_image_dict[
            "standing_down"
        ]  # Temp Solution - should update over the State
        self.position_y += self.step_size
        self.row -= 1
        self.state.look_down(self)

    def move_right(self):
        self.image = player_image_dict[
            "standing_right"
        ]  # Temp Solution - should update over the State
        self.position_x += self.step_size
        self.state.look_right(self)

    def move_left(self):
        self.image = player_image_dict[
            "standing_left"
        ]  # Temp Solution - should update over the State
        self.position_x -= self.step_size
        self.state.look_left(self)

    def render(self, screen):
        screen.blit(self.image, (self.position_x, self.position_y))


class CharacterState:
    def __init__(self, character: Character):
        def look_up(self, character: Character):
            raise NotImplementedError

        def look_down(self, character: Character):
            raise NotImplementedError

        def look_right(self, character: Character):
            raise NotImplementedError

        def look_left(self, character: Character):
            raise NotImplementedError


class LookingUp(CharacterState):
    def __init__(self, character: Character):
        character.image = player_image_dict[
            "standing_up"
        ]  # Doesn`t work - and i don`t know why

    def look_up(self, character: Character):
        pass

    def look_down(self, character: Character):
        character.state = LookingDown(self)

    def look_right(self, character: Character):
        character.state = LookingRight(self)

    def look_left(self, character: Character):
        character.state = LookingLeft(self)


class LookingDown(CharacterState):
    def __init__(self, character: Character):
        character.image = player_image_dict[
            "standing_down"
        ]  # Doesn`t work - and i don`t know why

    def look_up(self, character: Character):
        character.state = LookingUp(self)

    def look_down(self, character: Character):
        pass

    def look_right(self, character: Character):
        character.state = LookingRight(self)

    def look_left(self, character: Character):
        character.state = LookingLeft(self)


class LookingRight(CharacterState):
    def __init__(self, character: Character):
        character.image = player_image_dict[
            "standing_right"
        ]  # Doesn`t work - and i don`t know why

    def look_up(self, character: Character):
        character.state = LookingUp(self)

    def look_down(self, character: Character):
        character.state = LookingDown(self)

    def look_right(self, character: Character):
        pass

    def look_left(self, character: Character):
        character.state = LookingLeft(self)


class LookingLeft(CharacterState):
    def __init__(self, character: Character):
        character.image = player_image_dict[
            "standing_left"
        ]  # Doesn`t work - and i don`t know why

    def look_up(self, character: Character):
        character.state = LookingUp(self)

    def look_down(self, character: Character):
        character.state = LookingDown(self)

    def look_right(self, character: Character):
        character.state = LookingRight(self)

    def look_left(self, character: Character):
        pass
