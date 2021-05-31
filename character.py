from support import Image
from settings import *
from fence import FenceBottom, FenceTop


# Load Images
player_image_dict = {}
dir_assets_player = "assets/player/"

player_image_dict["standing_up"] = (
    Image(dir_assets_player, 'standing_up.png').get(),
    Image(dir_assets_player, 'walking_up1.png').get(),
    Image(dir_assets_player, 'walking_up2.png').get(),
)
player_image_dict["standing_down"] = (
    Image(dir_assets_player, 'standing_down.png').get(),
    Image(dir_assets_player, 'walking_down1.png').get(),
    Image(dir_assets_player, 'walking_down2.png').get(),
)
player_image_dict["standing_right"] = (
    Image(dir_assets_player, 'standing_right.png').get(),
    Image(dir_assets_player, 'walking_right1.png').get(),
    Image(dir_assets_player, 'walking_right2.png').get(),
)
player_image_dict["standing_left"] = (
    Image(dir_assets_player, 'standing_left.png').get(),
    Image(dir_assets_player, 'walking_left1.png').get(),
    Image(dir_assets_player, 'walking_left2.png').get(),
)


fence_top = FenceTop()
fence_bottom = FenceBottom()


class Character:
    def __init__(self):
        self.image = None
        self.position_y = 715
        self.position_x = 580
        self.step_size = 45
        self.row = 0
        self.animationCount = 0
        self.state = LookingUp(self)
        self.wrapper = self.image.get_rect()

    def walk(self):
        if self.animationCount < 2:
            self.animationCount += 1
        else:
            self.animationCount = 0

    def move_up(self):
        self.state = LookingUp(self)

    def move_down(self):
        self.state = LookingDown(self)

    def move_right(self):
        self.state = LookingRight(self)

    def move_left(self):
        self.state = LookingLeft(self)

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
        character.walk()  # TODO: Maybe there is a better solution?
        character.image = player_image_dict["standing_up"][character.animationCount]
        if character.position_y > fence_top.position_y:
            character.position_y -= character.step_size
        character.row += 1

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
        character.walk()
        character.image = player_image_dict["standing_down"][character.animationCount]
        if character.position_y < fence_bottom.position_y:
            character.position_y += character.step_size
        character.row -= 1

    def look_up(self, character: Character):
        character.state = LookingUp(character)

    def look_down(self, character: Character):
        pass

    def look_right(self, character: Character):
        character.state = LookingRight(character)

    def look_left(self, character: Character):
        character.state = LookingLeft(character)


class LookingRight(CharacterState):
    def __init__(self, character: Character):
        character.walk()
        character.image = player_image_dict["standing_right"][character.animationCount]
        if character.position_x < (SCREEN_WIDTH - character.wrapper.w):
            character.position_x += character.step_size

    def look_up(self, character: Character):
        character.state = LookingUp(character)

    def look_down(self, character: Character):
        character.state = LookingDown(character)

    def look_right(self, character: Character):
        pass

    def look_left(self, character: Character):
        character.state = LookingLeft(character)


class LookingLeft(CharacterState):
    def __init__(self, character: Character):
        character.walk()
        character.image = player_image_dict["standing_left"][character.animationCount]
        if character.position_x > 0:
            character.position_x -= character.step_size

    def look_up(self, character: Character):
        character.state = LookingUp(character)

    def look_down(self, character: Character):
        character.state = LookingDown(character)

    def look_right(self, character: Character):
        character.state = LookingRight(character)

    def look_left(self, character: Character):
        pass
