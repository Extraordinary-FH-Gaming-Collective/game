class CollisionHandler:
    def __init__(self):
        self.hits = 0

    def check(self, lane, character):
        for sprite in lane.sprites:
            if lane.type == 'cars':
                if character.position_x >= sprite.position_x:
                    if character.position_x <= sprite.position_x + 25:
                        if character.position_y >= sprite.position_y:
                            if character.position_y <= sprite.position_y + 25:
                                character.position_y = 715
                                character.position_x = 580
                                self.hits += 1
                                character.leben -= 1
                                if character.leben == 0:
                                    pass  # Game-Over-Overlay

            # Zug-Lane, needs refactoring
            if lane.type != 'cars':
                if character.position_x <= sprite.position_x:
                    if character.position_x >= sprite.position_x + 320:
                        if character.position_y <= sprite.position_y:
                            if character.position_y >= sprite.position_y + 34:
                                character.position_y = 715
                                character.position_x = 580
                                character.leben -= 1

        return False
