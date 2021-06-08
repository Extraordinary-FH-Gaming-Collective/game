import time
from settings import *

class CollisionHandler:
    def __init__(self):
            self.lastHit = self.currentMilliSecondTime()
            self.protectionTime = PROTECTION_TIME_IN_MILLI_SECONDS

    def check(self, lane, character):
        for sprite in lane.sprites:
            if self.inProtectionTime():
                return

            if self.isHitByCar(character, sprite):
                self.setProtectionTime()
                character.hit()
                return

    def isHitByCar(self, character, sprite):
        if sprite.type != 'car':
            return False

        return self.rightFromLeftEdge(character, sprite) and self.leftFromRightEdge(character, sprite)

    def isHitByTrain(self, character, sprite):
        if sprite.type == 'car':
            return False
        
        print('train')

        return self.rightFromLeftEdge(character, sprite) and not self.leftFromRightEdge(character, sprite)

    def rightFromLeftEdge(self, character, sprite):
        return character.getWidth() + character.position_x > sprite.position_x

    def rightFromLeftEdge(self, character, sprite):
        return character.getWidth() + character.position_x > sprite.position_x

    def leftFromRightEdge(self, character, sprite):
        return sprite.position_x + sprite.getWidth() > character.position_x

    def inProtectionTime(self):
        return self.lastHit + self.protectionTime > self.currentMilliSecondTime()

    def setProtectionTime(self):
        self.lastHit = self.currentMilliSecondTime()

    def currentMilliSecondTime(self):
        return round(time.time() * 1000)
