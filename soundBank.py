import pygame.mixer
from Sound import Sound

pygame.mixer.init()

#Efectos de Sonido
blipSo = pygame.mixer.Sound('sonidos/blip.wav')
chan = [pygame.mixer.Channel(1)]
chan[0].set_volume(0.1)
blip = Sound(blipSo,chan)

laserSo = pygame.mixer.Sound('sonidos/laser3.wav')
chan2 = [pygame.mixer.Channel(2),pygame.mixer.Channel(3),pygame.mixer.Channel(4)]
chan2[0].set_volume(0.2)
chan2[1].set_volume(0.2)
chan2[2].set_volume(0.2)


laser = Sound(laserSo,chan2)

