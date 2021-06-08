import pygame

background_music = ('assets/sounds/Jim Hall - Elsewhere.mp3')
jump_sound = ('assets/sounds/Jump.mp3')
finish_sound = ('assets/sounds/Finish.mp3')
hit_sound = ("assets/sounds/Hit.mp3")


def loadMusic():
    pygame.mixer.music.load(background_music)
    pygame.mixer.Channel(0).play(pygame.mixer.Sound(background_music), -1)

def loadJump():
    pygame.mixer.music.load(jump_sound)
    pygame.mixer.music.play()

def loadFinish():
    pygame.mixer.music.load(finish_sound)
    pygame.mixer.music.play()

def loadHit():
    pygame.mixer.music.load(hit_sound)
    pygame.mixer.music.play()
