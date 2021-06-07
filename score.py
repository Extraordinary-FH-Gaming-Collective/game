class Scorer:
    def __init__(self):
        self.points = 0
        self.goal = 0

    def reached_endzone(self):
        self.goal += 1
        self.points += 500
        print(self.points)

    def lost_life(self):
        self.points -= 250

    def reset_score(self):
        self.points = 0
        self.goal = 0
