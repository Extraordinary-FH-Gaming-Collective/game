class Character:
    def __init__(self, sprite):
        self.sprite = sprite
        self.position_y = 0
        self.position_x = 0
        self.step = 20
        self.row = 0

    def move_forward(self):
        self.position_y += self.step
        self.row += 1

    def move_backwards(self):
        self.position_y -= self.step
        self.row -= 1

    def move_right(self):
        self.position_x += self.step

    def move_left(self):
        self.position_x -= self.step
