from sprites import Sprite
from character import Character

class CollisionHandler:
    def __init__(self):
        pass

    def check(self, sprites: list, chracter: Character): 
        for sprite in sprites:
            #  Check right here if the Sprite is colliding with the Character
            #  Something like
            # 
            #  if like sprite.position_x > sprite.position_z
            #      return True
            #     
            return False
        