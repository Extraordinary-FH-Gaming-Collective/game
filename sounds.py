
class Sounds:
    def __init__(self, game):
        self.game = game
        self.background_music = ('assets/sounds/Jim Hall - Elsewhere.mp3')
        self.jump_sound = ('assets/sounds/Jump.mp3')
        self.finish_sound = ('assets/sounds/Finish.mp3')
        self.hit_sound = ("assets/sounds/Hit.mp3")

    def loadMusic(self):
        self.game.pygame.mixer.music.load(self.background_music)
        self.game.pygame.mixer.Channel(0).play(self.pygame.mixer.Sound(self.background_music), -1)

    def loadJump(self):
        self.game.pygame.mixer.music.load(self.jump_sound)
        self.game.pygame.mixer.music.play()

    def loadFinish(self):
        self.game.pygame.mixer.music.load(self.finish_sound)
        self.game.pygame.mixer.music.play()

    def loadHit(self):
        self.game.pygame.mixer.music.load(self.hit_sound)
        self.game.pygame.mixer.music.play()
