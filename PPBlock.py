import os
import pygame
from pygame.locals import *
from consts import *
from math import *
from matCas import MatCas

#Importar Imagenes y sonidos
from imageBank import *
from soundBank import *

#Importar Objetos
from Bolita import Bola
from Casilla import Casilla
from Player import player

# Se inician modulos
pygame.init()
os.environ['SDL_VIDEO_CENTERED'] = '1'

# Se inicia la pantalla
surface = pygame.display.set_mode((winWidth, winHeight))
pygame.display.set_caption('PP-Block')

# Se crea el reloj
clock = pygame.time.Clock()

# Mouse y teclas
mouse = pygame.mouse
keys = pygame.key
########PRUEBA
player1 = player(surface,pong,flecha)


i = 0
# Entra en bucle principal
while True:

    # Setea el reloj
    clock.tick(FPS)

    # Busca eventos de aplicacion
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()

    # Dibuja la pantalla
    surface.fill(COLOR_Black)

    # Dibuja los Margenes
    pygame.draw.line(surface, COLOR_White, [0, marUp],[winWidth, marUp], 2)
    pygame.draw.line(surface, COLOR_White, [0, marDown], [winWidth, marDown], 2)

    ###########PRUEBA
    base = mouse.get_pos()[0] - player1.x
    altura = marDown - mouse.get_pos()[1]

    if keys.get_pressed()[K_w] and player1.bolitas[0].vely == 0:
        print 1
        player1.lanzarBolita(0,base,altura)


    player1.updateBolitas()
    player1.draw(mouse)
    player1.checkPrimeraBola()

    # Vuelca lo dibujado en pantalla
    pygame.display.flip()