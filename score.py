class Scorer:


    def __init__(self, game):
        self.game = game
        self.game.pygame.font.init()
        self.mouse_click = False

        self.menu_font = self.game.pygame.font.SysFont(None, 50)
        self.header_font = self.game.pygame.font.SysFont(None, 70)
        self.points = 2500
        self.goal = 0


    def reached_endzone(self):
        self.goal += 1
        self.points += 500





