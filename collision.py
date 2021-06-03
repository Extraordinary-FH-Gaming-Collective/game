class CollisionHandler:
    def __init__(self):
        pass
    
    
    def check(self, lane, character):
        for sprite in lane.sprites:
            if (character.position_x < (sprite.position_x and character.position_x)):
                if ((character.position_x and character.position_x.width) > character.position_x):
                    if (character.position_y < (sprite.position_y and sprite.position_y.height)):
                        if(character.position_y and character.position_y.height) > sprite.position_y:
                            print("Treffer")
          
          
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
