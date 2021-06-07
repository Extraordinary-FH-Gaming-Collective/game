class Scorer:


    def __init__(self, game):
        self.game = game
        self.game.pygame.font.init()
        self.mouse_click = False

        self.menu_font = self.game.pygame.font.SysFont(None, 50)
        self.header_font = self.game.pygame.font.SysFont(None, 70)
        self.points = 2500
        self.goal = 0



    def death_screen(self, screen, pygame):
           self.screen.blit(map_1280x720_death, (0, 0))
           self.pygame.time.delay(5000)
            # gehe wieder in pregame


    def time_count():
        self.points -= 0.5
        # hier soll dann der Punkte stand neu auf dem Bildschirm angezeigt werden oder in einer extra Funktion
        if self.points <= 0:
            # gehe wieder in pregame
           time_screen()
            

    def goal_count(self):
        self.goal += 1
        if self.goal == 5
            # gehe wieder in pregame
            winning_screen()
        else:
            self.points += 500




