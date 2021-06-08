class Scorer:
    """Creates a Scorer class to count Points and reached Endzones (Goals)."""

    def __init__(self):
        self.points = 5000
        self.goal = 0
        self.counter = 0

    def reached_goal(self):
        """When the Player reaches one of the Endzone he get´s 500 Points.

        And one goals get`s added (5 is Winner Winner Chicken Dinner)
        """

        self.goal += 1

    def add_points(self, points):
        self.points += points

    def remove_points(self, points):
        self.points -= points

    def countdown_score(self):
        """Counts down on every Frame via the update Method in Game Loop.

        After 60 frames it removes 10 Points and restarts
        """

        self.counter += 1
        if self.counter == 60:
            self.points -= 10
            self.counter = 0

    def reset_score(self):
        self.points = 5000
        self.goal = 0
