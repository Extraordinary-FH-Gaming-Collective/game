import pygame


class Character:
    def __init__(self, image):
        self.state = LookingUp()
        self.image = image
        self.wrapper = image.get_rect()
        self.position_y = 0
        self.position_x = 0
        self.step_size = 50
        self.row = 0
        

    def move_up(self):
        self.position_y += self.step_size
        self.row += 1
        self.state.look_up(self)

    def move_down(self):
        self.position_y -= self.step_size
        self.row -= 1
        self.state.look_down(self)

    def move_right(self):
        self.position_x += self.step_size
        self.state.look_right(self)

    def move_left(self):
        self.position_x -= self.step_size
        self.state.look_left(self)
        
    def render(self, screen):
        screen.blit(self.image, self.wrapper)



class CharacterState:
    def __init__(self):
        def look_up(self, character: Character):
            raise NotImplementedError

        def look_down(self, character: Character):
            raise NotImplementedError

        def look_right(self, character: Character):
            raise NotImplementedError

        def look_left(self, character: Character):
            raise NotImplementedError


class LookingUp(CharacterState):
    def __init__ (self, character: Character):
        character.image = 
    
    def look_up():
        pass

    def look_down(self, character: Character):
        character.state = LookingDown()

    def look_right(self, character: Character):
        character.state = LookingRight()

    def look_left(self, character: Character):
        character.state = LookingLeft()


class LookingDown(CharacterState):
    def look_up(self, character: Character):
        character.state = LookingUp()

    def look_down():
        pass

    def look_right(self, character: Character):
        character.state = LookingRight()

    def look_left(self, character: Character):
        character.state = LookingLeft()


class LookingRight(CharacterState):
    def look_up(self, character: Character):
        character.state = LookingUp()

    def look_down(self, character: Character):
        character.state = LookingDown()

    def look_right():
        pass

    def look_left(self, character: Character):
        character.state = LookingLeft()


class LookingLeft(CharacterState):
    def look_up():
        pass

    def look_down(self, character: Character):
        character.state.LookingDown()

    def look_right(self, character: Character):
        character.state = LookingRight()

    def look_left(self, character: Character):
        character.state.LookingLeft()
