from settings import CHARACTER_START_POSITION_X, CHARACTER_START_POSITION_Y
import pygame


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
                                character.position_y = CHARACTER_START_POSITION_Y
                                character.position_x = CHARACTER_START_POSITION_X
                                print(self.hits, 'Hits')
                                self.hits += 1
                                character.leben -= 1

                                # plays a hit-sound when hit
                                pygame.mixer.music.load('sounds\Hit.mp3')
                                pygame.mixer.music.play()

                                if character.leben == 0:
                                    pass
                                # Game-Over-Overlay

            # Zug-Lane, needs refactoring
            if lane.type != 'cars':
                if character.position_x <= sprite.position_x:
                    if character.position_x >= sprite.position_x + 320:
                        if character.position_y <= sprite.position_y:
                            if character.position_y >= sprite.position_y + 34:
                                character.position_y = CHARACTER_START_POSITION_Y
                                character.position_x = CHARACTER_START_POSITION_X
                                print('daneben')
                                character.leben -=1

            # jetzt wird eine Kollision entdeckt, sobald es eine Überschneidung gibt -> für Car-Lanes

        return False
