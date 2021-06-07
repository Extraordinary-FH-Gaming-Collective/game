class Scorer:

    points = 2500
    goal = 0 


    def death_screen():
           self.game.screen.blit(map_1280x720_death, (0, 0))
           self.pygame.time.delay(5000)
            # gehe wieder in pregame


    def time_count():
        self.points -= 0.5
        # hier soll dann der Punkte stand neu auf dem Bildschirm angezeigt werden oder in einer extra Funktion
        if points <= 0:
            # gehe wieder in pregame
           time_screen()
            

    def goal_count():
        if goal >= 5
            # gehe wieder in pregame
            winning_screen()
        else:
            points += 500




