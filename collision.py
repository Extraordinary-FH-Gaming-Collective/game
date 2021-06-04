import pygame

class CollisionHandler:
    def __init__(self):
        self.hits = 0

    
    
    def check(self, lane, character):
        for sprite in lane.sprites:
            if lane.type == 'cars':
                if character.position_x >= sprite.position_x:
                    if character.position_x <= sprite.position_x+25:
                        if character.position_y >= sprite.position_y:
                            if character.position_y <= sprite.position_y +25:
                                character.position_y = 715
                                character.position_x = 580
                                print(self.hits, 'Hits')
                                self.hits += 1
                                character.leben -=1
                                if character.leben == 0:
                                    pass
                                #Game-Over-Overlay
            #Zug-Lane, need refactoring
            if lane.type != 'cars':
                if character.position_x <= sprite.position_x:
                    if character.position_x >= sprite.position_x+320:
                        if character.position_y <= sprite.position_y:
                           if character.position_y >= sprite.position_y+34:
                                character.position_y = 715
                                character.position_x = 580
                                print('daneben')
                                character.leben -=1

            # jetzt wird eine Kollision entdeckt, sobald es eine Überschneidung gibt -> für Car-Lanes
            # Return False setzen für -> Zug Lanes
           
            # rect1 = character
            # rect2 = sprite

            #if (rect1.x < rect2.x + rect2.width &&
            #    rect1.x + rect1.width > rect2.x &&
            #    rect1.y < rect2.y + rect2.height &&
            #    rect1.y + rect1.height > rect2.y)
            #    // collision detected!


        return False