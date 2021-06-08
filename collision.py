from settings import *


class CollisionHandler:
    def __init__(self):
        pass

    def check(self, lane, character):
        if self.isHitByCar(character, lane) or self.isNotOnTrain(character, lane):
            character.hit()

    def isHitByCar(self, character, lane):
        if lane.type != 'cars':
            return

        for sprite in lane.sprites:
            if self.rightFromLeftEdge(character, sprite) and self.leftFromRightEdge(character, sprite):
                return True

        return False

    def isNotOnTrain(self, character, lane):
        if lane.type == 'cars':
            return False

        for sprite in lane.sprites:
            if self.rightFromLeftEdge(character, sprite) and self.leftFromRightEdge(character, sprite):
                return False

        return True

    def rightFromLeftEdge(self, character, sprite):
        return character.getWidth() + character.position_x > sprite.position_x

    def rightFromLeftEdge(self, character, sprite):
        return character.getWidth() + character.position_x > sprite.position_x

    def leftFromRightEdge(self, character, sprite):
        return sprite.position_x + sprite.getWidth() > character.position_x
