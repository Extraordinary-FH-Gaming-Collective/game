from support import Image
from settings import *
from fence import FenceBottom, FenceTop
import pygame


# Load Images
player_image_dict = {}
dir_assets_player = "assets/player/"
dir_assets_other = "assets/"

player_image_dict["standing_up"] = (
    Image(dir_assets_player, "standing_up.png").get(),
    Image(dir_assets_player, "walking_up1.png").get(),
    Image(dir_assets_player, "walking_up2.png").get(),
)
player_image_dict["standing_down"] = (
    Image(dir_assets_player, "standing_down.png").get(),
    Image(dir_assets_player, "walking_down1.png").get(),
    Image(dir_assets_player, "walking_down2.png").get(),
)
player_image_dict["standing_right"] = (
    Image(dir_assets_player, "standing_right.png").get(),
    Image(dir_assets_player, "walking_right1.png").get(),
    Image(dir_assets_player, "walking_right2.png").get(),
)
player_image_dict["standing_left"] = (
    Image(dir_assets_player, "standing_left.png").get(),
    Image(dir_assets_player, "walking_left1.png").get(),
    Image(dir_assets_player, "walking_left2.png").get(),
)
player_image_dict["cheering"] = Image(dir_assets_player, "player_cheers.png").get()


fence_top = FenceTop()
fence_bottom = FenceBottom()


class Character(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = player_image_dict["standing_up"][0]
        self.rect = self.image.get_rect()
        self.position_y = CHARACTER_START_POSITION_Y
        self.position_x = CHARACTER_START_POSITION_X
        self.step_size = CHARACTER_STEP_SIZE
        self.row = 0
        self.animationCount = 0
        self.state = LookingUp(self)

        self.leben = 3
        self.herzImage = Image(dir_assets_other, "pixelherz64_56.png").get()

    def walk(self):
        if self.animationCount < 2:
            self.animationCount += 1
        else:
            self.animationCount = 0
        pygame.mixer.music.load('assets/sounds/Jump.mp3')
        pygame.mixer.music.play()

    def move_up(self):
        self.state.move_up(self)

    def move_down(self):
        self.state.move_down(self)

    def move_right(self):
        self.state.move_right(self)

    def move_left(self):
        self.state.move_left(self)

    def getWidth(self):
        return self.rect.w

    def cheer(self):
        self.image = player_image_dict["cheering"]

    def bounce_back(self):
        self.position_y += 10

    def render(self, screen):
        screen.blit(self.image, (self.position_x, self.position_y))
        self.herzen(screen)

    def herzen(self, screen):
        if self.leben == 3:
            screen.blit(self.herzImage, (1088, 15))
            screen.blit(self.herzImage, (1152, 15))
            screen.blit(self.herzImage, (1215, 15))
        if self.leben == 2:
            screen.blit(self.herzImage, (1088, 15))
            screen.blit(self.herzImage, (1152, 15))
        if self.leben == 1:
            screen.blit(self.herzImage, (1088, 15))

    def hit(self):
        self.back_to_start()
        self.leben -= 1

        pygame.mixer.music.load('assets/sounds/Hit.mp3')
        pygame.mixer.music.play()

    def update(self):
        self.rect.x = self.position_x
        self.rect.y = self.position_y

    def back_to_start(self):
        self.position_y = CHARACTER_START_POSITION_Y
        self.position_x = CHARACTER_START_POSITION_X
        self.row = 0


class CharacterState:
    def __init__(self, character: Character):
        def move_up(self, character: Character):
            raise NotImplementedError

        def move_down(self, character: Character):
            raise NotImplementedError

        def move_right(self, character: Character):
            raise NotImplementedError

        def move_left(self, character: Character):
            raise NotImplementedError


class LookingUp(CharacterState):
    def __init__(self, character: Character):
        character.walk()
        character.image = player_image_dict["standing_up"][character.animationCount]
        if (character.position_y) > BORDER_TOP:
            character.position_y -= character.step_size
            character.row += 1

    def move_up(self, character: Character):
        character.state = LookingUp(character)

    def move_down(self, character: Character):
        character.state = LookingDown(character)

    def move_right(self, character: Character):
        character.state = LookingRight(character)

    def move_left(self, character: Character):
        character.state = LookingLeft(character)

    def cheer(self, character: Character):
        character.state = Cheering(character)


class LookingDown(CharacterState):
    def __init__(self, character: Character):
        character.walk()
        character.image = player_image_dict["standing_down"][character.animationCount]
        if character.position_y < BORDER_BOTTOM:
            character.position_y += character.step_size
            character.row -= 1

    def move_up(self, character: Character):
        character.state = LookingUp(character)

    def move_down(self, character: Character):
        character.state = LookingDown(character)

    def move_right(self, character: Character):
        character.state = LookingRight(character)

    def move_left(self, character: Character):
        character.state = LookingLeft(character)


class LookingRight(CharacterState):
    def __init__(self, character: Character):
        character.walk()
        character.image = player_image_dict["standing_right"][character.animationCount]
        if (character.rect.x + character.rect.w) < BORDER_RIGHT:
            character.position_x += character.step_size

    def move_up(self, character: Character):
        character.state = LookingUp(character)

    def move_down(self, character: Character):
        character.state = LookingDown(character)

    def move_right(self, character: Character):
        character.state = LookingRight(character)

    def move_left(self, character: Character):
        character.state = LookingLeft(character)


class LookingLeft(CharacterState):
    def __init__(self, character: Character):
        character.walk()
        character.image = player_image_dict["standing_left"][character.animationCount]
        if character.rect.x - character.rect.w > BORDER_LEFT:
            character.position_x -= character.step_size

    def move_up(self, character: Character):
        character.state = LookingUp(character)

    def move_down(self, character: Character):
        character.state = LookingDown(character)

    def move_right(self, character: Character):
        character.state = LookingRight(character)

    def move_left(self, character: Character):
        character.state = LookingLeft(character)
