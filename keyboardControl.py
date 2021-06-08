from characterCommands import ICommandCharacter
from characterCommands import (
    MoveDownCommand,
    MoveLeftCommand,
    MoveRightCommand,
    MoveUpCommand,
)

# KeyboardControl is the steering wheel for the character and maps Character Commands to Keys


class KeyboardControl:
    def __init__(self, game):
        self.arrowkey_up = None
        self.arrowkey_down = None
        self.arrowkey_right = None
        self.arrowkey_left = None
        self.game = game

        # Maps Key Events to the right KeyboardControl Methods
        self.key_map = {
            game.pygame.K_UP: self.press_arrowkey_up,
            game.pygame.K_DOWN: self.press_arrowkey_down,
            game.pygame.K_RIGHT: self.press_arrowkey_right,
            game.pygame.K_LEFT: self.press_arrowkey_left,
        }

        # Maps the imported Character Commands to the Keyboard Control Methods
        self.assign_arrowkey_up(MoveUpCommand(game.player))
        self.assign_arrowkey_down(MoveDownCommand(game.player))
        self.assign_arrowkey_right(MoveRightCommand(game.player))
        self.assign_arrowkey_left(MoveLeftCommand(game.player))

    def execute(self):
        for event in self.game.pygame.event.get():
            if event.type == self.game.pygame.QUIT:
                self.game.quit()

            if event.type != self.game.pygame.KEYDOWN:
                return  # Do nothing in case it's not a keydown

            # Changes Game Mode to Menu over Escape Key
            if event.key == self.game.pygame.K_ESCAPE:
                self.game.mode = "menu"

            # Access the given Keys in the Key Map and compares them to triggered Events
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
