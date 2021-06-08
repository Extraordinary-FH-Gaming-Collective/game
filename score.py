class Scorer:
    def __init__(self):
        self.points = 5000
        self.goal = 0
        self.counter = 0

    def reached_goal(self):
        self.goal += 1
        self.points += 500

    def add_points(self, points):
        self.points -= points

    def remove_points(self, points):
        self.points -= points

    def countdown_score(self):
        self.counter += 1
        if self.counter == 60:
            self.points -= 10
            self.counter = 0

    def reset_score(self):
        self.points = 5000
        self.goal = 0
