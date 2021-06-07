from settings import CHARACTER_START_POSITION_X, CHARACTER_START_POSITION_Y
import pygame


class CollisionHandler:
    def __init__(self):
        self.treffer = 1


    def check(self, lane, character):
        for sprite in lane.sprites:
            print(character.position_y + character.getHeight())
            if self.hitsCar(lane, character, sprite)is True:
                self.treffer =+ 1
                print(self.treffer)
                character.leben -= 1
                character.position_x = CHARACTER_START_POSITION_X
                character.position_y = CHARACTER_START_POSITION_Y

            #if self.missesTrain(lane, character, sprite):
                #return True

    
    def hitsCar(self, lane, character, sprite):
        if lane.type == 'cars':
            if character.position_x >= sprite.position_x:
                if character.position_x <= sprite.position_x + sprite.getWidth():
                    if character.row == lane.lane:
                        return True
        else:
            return False
        
        
        #if character.position_x >= sprite.position_x and character.position_x <= sprite.position_x + sprite.getWidth() and character.position_y >= sprite.position_y and character.position_y >= sprite.position_y + sprite.getHeight()/2:
            
