""" 

This is where we detect any collisions. 

"""
class CollisionHandler:
    
    
    """ 

    Please move on. There nothing happening here. Really!

    """
    def __init__(self):
        pass

    """ 

    Check against a collision with a car or train. 
    In case the character / player is hit, we will call the hit method to handle that case.
    
    Please note: As a hit by car may be obvious, it's a little different with trains:

    We'll handle the case that the character is not on a train, as he jumped down to 
    the rails, as a hit and handle it equally as a hit by car.

    """
    def check(self, lane, character) -> None:
        if self.isHitByCar(character, lane) or self.isNotOnTrain(character, lane):
            character.hit()

    """ 

    Returns a boolean if hit by a car. 

    """
    def isHitByCar(self, character, lane) -> bool:
        if lane.type != 'cars':
            return

        for sprite in lane.sprites:
            if self.rightFromLeftEdge(character, sprite) and self.leftFromRightEdge(character, sprite):
                return True

        return False

    """ 

    Is the character not on the train? This would mean, he jumped onto the rails. 
    Living on the edge? Not tolerated in Frogger city.

    """
    def isNotOnTrain(self, character, lane) -> bool:
        if lane.type == 'cars':
            return False

        for sprite in lane.sprites:
            if self.rightFromLeftEdge(character, sprite) and self.leftFromRightEdge(character, sprite):
                return False

        return True

    """ 

    Checks if the character is on the right side from the left side the sprite.

    """
    def rightFromLeftEdge(self, character, sprite) -> bool:
        return character.getWidth() + character.position_x > sprite.position_x


    """ 

    Checks if the character is on the left side from the right side the sprite.

    """
    def leftFromRightEdge(self, character, sprite) -> bool:
        return sprite.position_x + sprite.getWidth() > character.position_x
