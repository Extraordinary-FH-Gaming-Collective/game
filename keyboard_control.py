from character_commands import ICommandCharacter
from character_commands import (
    MoveDownCommand,
    MoveLeftCommand,
    MoveRightCommand,
    MoveUpCommand,
)


class KeyboardControl:
    def __init__(self, pygame, player):
        self.arrowkey_up = None
        self.arrowkey_down = None
        self.arrowkey_right = None
        self.arrowkey_left = None

        self.key_map = {
            pygame.K_UP: self.press_arrowkey_up,
            pygame.K_DOWN: self.press_arrowkey_down,
            pygame.K_RIGHT: self.press_arrowkey_right,
            pygame.K_LEFT: self.press_arrowkey_left,
        }

        self.assign_arrowkey_up(MoveUpCommand(player))
        self.assign_arrowkey_down(MoveDownCommand(player))
        self.assign_arrowkey_right(MoveRightCommand(player))
        self.assign_arrowkey_left(MoveLeftCommand(player))

    def execute(self, event):
        if event.key in self.key_map:
            self.key_map[event.key]()

    def assign_arrowkey_up(self, command: ICommandCharacter):
        self.arrowkey_up = command

    def assign_arrowkey_down(self, command: ICommandCharacter):
        self.arrowkey_down = command

    def assign_arrowkey_right(self, command: ICommandCharacter):
        self.arrowkey_right = command

    def assign_arrowkey_left(self, command: ICommandCharacter):
        self.arrowkey_left = command

    def press_arrowkey_up(self):
        self.arrowkey_up.execute()

    def press_arrowkey_down(self):
        self.arrowkey_down.execute()

    def press_arrowkey_right(self):
        self.arrowkey_right.execute()

    def press_arrowkey_left(self):
        self.arrowkey_left.execute()
