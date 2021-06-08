from support import Image
from settings import *
import pygame
from sounds import *


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


class Character(pygame.sprite.Sprite):
    def __init__(self, lanes):
        pygame.sprite.Sprite.__init__(self)
        self.position_y = None
        self.position_x = None
        self.image = None
        self.state = InitialState(self)
        self.rect = self.image.get_rect()

        self.step_size = CHARACTER_STEP_SIZE

        self.trainSpeed = {}
        self.trainFromLeft = {}
        self.trainSpeed[8] = lanes.get_lane(8).speed
        self.trainFromLeft[8] = lanes.get_lane(8).left_to_right
        self.trainSpeed[9] = lanes.get_lane(9).speed
        self.trainFromLeft[9] = lanes.get_lane(9).left_to_right
        self.trainSpeed[10] = lanes.get_lane(10).speed
        self.trainFromLeft[10] = lanes.get_lane(10).left_to_right
        self.trainSpeed[11] = lanes.get_lane(11).speed
        self.trainFromLeft[11] = lanes.get_lane(11).left_to_right

        self.row = 0
        self.animation_count = 0

        self.life = 3
        self.heart_image = Image(dir_assets_other, "pixelherz64_56.png").get()
        self.sounds = Sounds(self)

    def walk(self):
        if self.animation_count < 2:
            self.animation_count += 1
        else:
            self.animation_count = 0
        self.sounds.playJump()

    def move_up(self):
        self.state.move_up(self)

    def move_down(self):
        self.state.move_down(self)

    def move_right(self):
        self.state.move_right(self)

    def move_left(self):
        self.state.move_left(self)

    def get_width(self):
        return self.rect.w

    def cheer(self):
        self.image = player_image_dict["cheering"]

        pygame.mixer.music.load("assets/sounds/Finish.mp3")
        pygame.mixer.music.play()

    def bounce_back(self):
        self.position_y += 10

    def render(self, screen):
        screen.blit(self.image, (self.position_x, self.position_y))
        self.herzen(screen)

    def herzen(self, screen):
        if self.life == 3:
            screen.blit(self.heart_image, (1088, 15))
            screen.blit(self.heart_image, (1152, 15))
            screen.blit(self.heart_image, (1215, 15))
        if self.life == 2:
            screen.blit(self.heart_image, (1088, 15))
            screen.blit(self.heart_image, (1152, 15))
        if self.life == 1:
            screen.blit(self.heart_image, (1088, 15))

    def hit(self):
        self.back_to_start()
        self.life -= 1
        self.sounds.loadHit(self)

    def update(self):
        self.adoptTrainMovement()

        self.rect.x = self.position_x
        self.rect.y = self.position_y

    def adoptTrainMovement(self):
        if self.row < 8 or self.row > 11:
            return

        if (
            self.trainFromLeft[self.row]
            and self.position_x + self.get_width() < SCREEN_WIDTH
        ):
            self.position_x += self.trainSpeed[self.row]
        elif self.position_x >= 0:
            self.position_x -= self.trainSpeed[self.row]

    def back_to_start(self):
        self.state = InitialState(self)


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


class InitialState(CharacterState):
    def __init__(self, character: Character):
        character.position_y = CHARACTER_START_POSITION_Y
        character.position_x = CHARACTER_START_POSITION_X
        character.image = player_image_dict["standing_up"][0]
        character.row = 0

    def move_up(self, character: Character):
        character.state = LookingUp(character)

    def move_down(self, character: Character):
        character.state = LookingDown(character)

    def move_right(self, character: Character):
        character.state = LookingRight(character)

    def move_left(self, character: Character):
        character.state = LookingLeft(character)


class LookingUp(CharacterState):
    def __init__(self, character: Character):
        character.walk()
        character.image = player_image_dict["standing_up"][character.animation_count]
        if (character.position_y) > BORDER_TOP:
            character.position_y -= character.step_size
            if character.row < 11:
                character.row += 1

    def move_up(self, character: Character):
        character.state = LookingUp(character)

    def move_down(self, character: Character):
        character.state = LookingDown(character)

    def move_right(self, character: Character):
        character.state = LookingRight(character)

    def move_left(self, character: Character):
        character.state = LookingLeft(character)


class LookingDown(CharacterState):
    def __init__(self, character: Character):
        character.walk()
        character.image = player_image_dict["standing_down"][character.animation_count]
        if character.position_y < BORDER_BOTTOM:
            character.position_y += character.step_size
            if character.row > 0:
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
        character.image = player_image_dict["standing_right"][character.animation_count]
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
        character.image = player_image_dict["standing_left"][character.animation_count]
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
