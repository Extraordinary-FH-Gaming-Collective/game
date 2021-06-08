class Sounds:
    def __init__(self, game):
        self.game = game
        self.pygame.mixer.init()
        self.background_music = ('assets/sounds/Jim Hall - Elsewhere.mp3')
        self.jump_sound = ('assets/sounds/Jump.mp3')
        self.finish_sound = ('assets/sounds/Finish.mp3')
        self.hit_sound = ("assets/sounds/Hit.mp3")

    def play_music(self):
        self.game.pygame.mixer.music.load(self.background_music)
        self.game.pygame.mixer.Channel(0).play(self.game.pygame.mixer.Sound(self.background_music), -1)

    def play_jump(self):
        self.game.pygame.mixer.music.load(self.jump_sound)
        self.game.pygame.mixer.music.play()

    def play_finish(self):
        self.game.pygame.mixer.music.load(self.finish_sound)
        self.game.pygame.mixer.music.play()

    def play_hit(self):
        self.game.pygame.mixer.music.load(self.hit_sound)
        self.game.pygame.mixer.music.play()
