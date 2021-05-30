from character_commands import ICommandCharacter


# Invoker for Character Movement
class KeyboardControl:
    def __init__(self):
        self.arrowkey_up = None
        self.arrowkey_down = None
        self.arrowkey_right = None
        self.arrowkey_left = None

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
