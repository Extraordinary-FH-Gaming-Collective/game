
class CollisionHandler:
    """This is where we detect any collisions."""

    def __init__(self):
        """Please move on. There nothing happening here. Really!"""

        pass

    def check(self, lane, character, scorer) -> None:
        """Check against a collision with a car or train.
        In case the character / player is hit, we will call the hit method to handle that case.

        Please note: As a hit by car may be obvious, it's a little different with trains:

        We'll handle the case that the character is not on a train, as he jumped down to
        the rails, as a hit and handle it equally as a hit by car.
        """

        if self.isHitByCar(character, lane) or self.isNotOnTrain(character, lane):
            character.hit()
            scorer.remove_points(250)

    def isHitByCar(self, character, lane) -> bool:
        """Returns a boolean if hit by a car."""

        if lane.type != 'cars':
            return

        for sprite in lane.sprites:
            if self.rightFromLeftEdge(character, sprite) and self.leftFromRightEdge(
                character, sprite
            ):
                return True

        return False

    def isNotOnTrain(self, character, lane) -> bool:
        """Is the character not on the train? This would mean, he jumped onto the rails.

        Living on the edge? Not tolerated in Frogger City.
        """

        if lane.type == 'cars':
            return False

        for sprite in lane.sprites:
            if self.rightFromLeftEdge(character, sprite) and self.leftFromRightEdge(
                character, sprite
            ):
                return False

        return True

    def rightFromLeftEdge(self, character, sprite) -> bool:
        """Checks if the character is on the right side from the left side the sprite."""

        return character.get_width() + character.position_x > sprite.position_x

    def leftFromRightEdge(self, character, sprite) -> bool:
        """Checks if the character is on the left side from the right side the sprite."""

        return sprite.position_x + sprite.get_width() > character.position_x
