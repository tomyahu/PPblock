import os
import pygame
from pygame.locals import *
from consts import *
from math import *

#Importar Imagenes y sonidos
from imageBank import *
from soundBank import *

#Importar Objetos
from Bolita import Bola
from Casilla import Casilla
from Player import player
from Button import *
from matCas import MatCas

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
player1 = player(surface,pokebola,flecha)
Mat = MatCas(surface,player1)
Mat.nextLevel()

#Contador 1
a = 0
b = 0

def Menu():

    play = Button(winWidth/2,475,playTex,surface)
    restart = Button(winWidth / 2, 375, restartTex, surface)

    while True:

        # Setea el reloj
        clock.tick(FPS)

        # Busca eventos de aplicacion
        for event in pygame.event.get():
            if event.type == QUIT:
                exit()

        # Dibuja la pantalla
        surface.fill(COLOR_Black)

        if play.inArea(mouse.get_pos()[0],mouse.get_pos()[1]):
            if mouse.get_pressed()[0]:
                return
            play.im = 1
        else:
            play.im = 0

        if restart.inArea(mouse.get_pos()[0],mouse.get_pos()[1]):
            if mouse.get_pressed()[0]:
                player1.restart()
                Mat.restart()
                return
            restart.im = 1
        else:
            restart.im = 0

        play.draw()
        restart.draw()

        pygame.display.flip()



Menu()
# Entra en bucle principal
while True:

    # Setea el reloj
    clock.tick(FPS)

    # Busca eventos de aplicacion
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()

    ###########PRUEBA
    if keys.get_pressed()[K_p]:
        Menu()


    base = mouse.get_pos()[0] - player1.x
    altura = marDown - mouse.get_pos()[1]

    if keys.get_pressed()[K_w] and player1.bolitasQuietas():
        player1.lanzarBolita(0,base,altura)
        player1.base = base
        player1.altura = altura
        a = 1

    if a > 0 and a < player1.numBolitas*pix:
        if a%pix == 0:
            player1.lanzarBolita(a/pix,player1.base,player1.altura)
        a+=1


    player1.checkPrimeraBola()
    for i in player1.bolitas:
        Mat.testColision(i)

    if player1.checkUltimaBola() > 0:
        b = 1

    player1.updateBolitas()

    if b > 0:
        b += 1

    if player1.bolitasQuietas() and b == 10:
        Mat.nextLevel()
        player1.numBolitas = len(player1.bolitas)
        b = 0
        a = 0

    #Dibuja
    # Dibuja la pantalla
    surface.fill(COLOR_Black)

    if Mat.contUniversal < 100:
        colorEspacio = COLOR_White[0]*(100 - Mat.contUniversal)/100
        colorLinea = (colorEspacio,colorEspacio,colorEspacio)
        pygame.draw.line(surface, colorLinea, [player1.x, marDown - player1.texBola.alto/2 - 1], [mouse.get_pos()[0], mouse.get_pos()[1]], 2)

    # Dibuja los Margenes
    pygame.draw.line(surface, COLOR_White, [0, marUp], [winWidth, marUp], 2)
    pygame.draw.line(surface, COLOR_White, [0, marDown], [winWidth, marDown], 2)

    player1.draw(mouse)
    player1.drawNumBolitas()
    Mat.draw()



    # Vuelca lo dibujado en pantalla
    pygame.display.flip()