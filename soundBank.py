import pygame.mixer
from Sound import Sound

pygame.mixer.init()

#Efectos de Sonido
blipSo = pygame.mixer.Sound('sonidos/blip.wav')
chans = []
for i in range(1):
    chans += [pygame.mixer.Channel(i)]
    chans[i-1].set_volume(0.1)


blip = Sound(blipSo,chans)

