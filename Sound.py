import pygame.mixer

pygame.mixer.init()

class Sound():
    def __init__(self, sound,channels):
        self.sound = sound
        self.channels = channels
        self.ind = 0

    def play(self):
        for ch in self.channels:
            if not ch.get_busy():
                ch.queue(self.sound)
                return

        self.channels[self.ind].queue(self.sound)
        self.ind = (self.ind + 1)%len(self.channels)