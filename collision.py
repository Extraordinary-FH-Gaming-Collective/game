from settings import CHARACTER_START_POSITION_X, CHARACTER_START_POSITION_Y
import pygame

class CollisionHandler:
    def __init__(self):
        pass


def check(self, lane, character):
    for sprite in lane.sprites:
        if self.isHit() == True:
                character.position_y = CHARACTER_START_POSITION_Y
                character.position_x = CHARACTER_START_POSITION_X
                character.leben -=1
                pygame.mixer.music.load('sounds/Hit.mp3')
                pygame.mixer.music.play()
        return False


# checks if player is hit by car or hits the train, so only one condition has to be true to detect a hit
def isHit(self, lane, character, sprite):
    if self.isHitByCar() or self.missesTrain():
        return True

# check if player hits the car 
# if lanetpye is train, the iteration breaks
# if lanetype is car a x/y-intersection will be checked
# intersection: true / no intersection: false
def isHitByCar(self, lane, character, sprite):
    if lane.type != 'cars':
        return False
    if self.isWithinXaxis() and self.hitsYAxis():
        return True
    else:
        return False


# checks if player misses the train
# if lane type is car lane, iteration breaks
# if lane type is train it is checked if misses the train
# no miss: false / miss: true
def missesTrain(self, lane, character, sprite):
    if lane.type == 'cars':
        return False
    if self.isWithinXaxis() and (character.position_y > sprite.position_y and character.position_y <= sprite.position_y + 35):
        return False
    else:
        return True

#checks if player is hit at X-Axis
def isWithinXaxis(self, lane, character, sprite):
    if character.position_x > sprite.position_x and character.position_x < sprite.position_x + sprite.getWidth:
        return True
    else:
        return False

# checks, if player is hit at Y-Axis
# if lanetype is not cars it returns false, so trains will not be checked, they have their own logic in missesTrain()
def hitsYAxis(self, lane, character, sprite):
    if lane.type != 'cars':
        return False
    if character.row == sprite.lane:
        return True





      