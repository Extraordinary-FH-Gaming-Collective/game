from character import Character


class ICommandCharacter:
    def __init__(self, character: Character):
        self.character = character

    def execute(self):
        raise NotImplementedError


class MoveUpCommand(ICommandCharacter):
    def execute(self):
        self.character.move_up()


class MoveDownCommand(ICommandCharacter):
    def execute(self):
        self.character.move_down()


class MoveRightCommand(ICommandCharacter):
    def execute(self):
        self.character.move_right()


class MoveLeftCommand(ICommandCharacter):
    def execute(self):
        self.character.move_left()
