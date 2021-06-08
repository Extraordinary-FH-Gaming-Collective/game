import pygame


class CollisionHandler:
    def __init__(self):
        self.treffer = 1


    def check(self, lane, character):
        for sprite in lane.sprites:
            self.hitsCar(lane, character, sprite)
            self.missesTrain(lane, character, sprite)

    
    def hitsCar(self, lane, character, sprite):
        if lane.type == 'cars':
            if character.position_x >= sprite.position_x:
                if character.position_x <= sprite.position_x + sprite.getWidth():
                    if character.row == lane.lane:
                        character.leben -= 1
                        character.back_to_start()

        
    def missesTrain(self, lane, character, sprite):
        if lane.type == ('small_trains' or 'medium_trains' or 'large_trains'):
            if character.position_x <= sprite.position_x:
                if character.position_x + character.getWidth() >= sprite.position_x + sprite.getWidth():
                    if character.row == lane.lane:             
                        character.leben -= 1
                        character.back_to_start()


            




            
