import os
import pygame
from pygame.locals import *
from consts import *
from math import *
from random import randint

#Importar Imagenes y sonidos
from imageBank import *
from soundBank import *

#Importar Objetos
from Bolita import Bola
from Casilla import Casilla
from Player import player
from Button import *
from matCas import MatCas

#Importar Menus
from Menus import *

# Se inician modulos
pygame.init()
os.environ['SDL_VIDEO_CENTERED'] = '1'

# Se inicia la pantalla
surface = pygame.display.set_mode((winWidth, winHeight))
pygame.display.set_caption('PP-Block')

# Se crea el reloj
clock = pygame.time.Clock()

########PRUEBA
player1 = player(surface,pong,flecha,avatarCisneros)
Mat = MatCas(surface,player1)
Mat.nextLevel()
pausa = Button(winWidth-30,marUp/2,pausaTex,surface)

#Contadores
a = 0
b = 0
c = 0


#estado click izquierdo Mouse
estdMouse = mouse.get_pressed()[0]

Menu(surface,clock,player1,Mat)

# Entra en bucle principal
while True:

    # Setea el reloj
    clock.tick(FPS)

    # Busca eventos de aplicacion
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()

    #inicio del programa

    #pausa
    if keys.get_pressed()[K_p]:
        Menu(surface,clock,player1,Mat)

    #otre forma de poner pausa
    if pausa.inArea(mouse.get_pos()[0], mouse.get_pos()[1]):
        if mouse.get_pressed()[0] and not estdMouse:
            Menu(surface,clock,player1,Mat)
        pausa.im = 1
    else:
        pausa.im = 0

    #constantes de referencia para lanzar las bolas
    base = mouse.get_pos()[0] - player1.x
    altura = marDown - mouse.get_pos()[1]

    #lanza la primera bolita con la tecla w
    if keys.get_pressed()[K_w] and player1.bolitasQuietas() and b == 0:
        player1.lanzarBolita(0,base,altura)
        player1.base = base
        player1.altura = altura
        a = 1

    #va lanzando el resto de las bolitas con el retraso adecuado
    if a > 0 and a < player1.numBolitas*pix:
        if a%pix == 0:
            player1.lanzarBolita(a/pix,player1.base,player1.altura)
        a+=1

    #revisa si han habido choques en la ultima frame
    choques = False
    for i in player1.bolitas:
        choques = choques or Mat.testColision(i)

    #si no han habido choques prepararse para dispersar las pelotas
    if not choques:
        c += 1
    else:
        c = 0

    #si no han habido choques durante 5 segundos se dispersan las pelotas y se muestra un icono de dispersion
    if c == 600:
        for bola in player1.bolitas:
            if bola.vely != 0 or bola.velx != 0:
                base = randint(1, 100)
                altura = randint(1, 100)

                if base > 0 and float(altura) / base < tan(pi / 18):
                    base = cos(pi / 18)
                    altura = sin(pi / 18)
                elif base < 0 and (-1) * float(altura) / base < tan(pi / 18):
                    base = (-1) * cos(pi / 18)
                    altura = sin(pi / 18)
                bola.lanzar(base, altura)

    #despues de un segundo deja de mostrarse el icono y se reinicia el contador
    if c >= 720:
        c = 0

    #si cayo una bolita el contador b toma el valor 1
    if player1.checkUltimaBola() > 0:
        b = 1

    #actualiza la posicion de todas las bolitas
    player1.updateBolitas()

    if b > 0:
        b += 1

    #si todas las bolitas estan quietas (se esperaran 10 frames con b) y se avanzara el nivel
    if player1.bolitasQuietas():
        c = 0
        if b == 10:
            Mat.nextLevel()
            player1.numBolitas = len(player1.bolitas)
            b = 0
            a = 0
            player1.prim = False

    #revisa si el jugador perdio
    if Mat.testDead():
        GameOver(surface,clock,player1,Mat)


    #Dibuja
    # Dibuja la pantalla
    surface.fill(COLOR_Black)

    #dibuja el icono de lanzar las bolitas al azar
    if c >= 600:
        surface.blit(fondoAzarIm, (winWidth/2 - 125, marUp + 100))

    #Dibuja el puntero
    if Mat.contUniversal < 100:
        colorEspacio = COLOR_White[0]*(100 - Mat.contUniversal)/100
        colorLinea = (colorEspacio,colorEspacio,colorEspacio)
        pygame.draw.line(surface, colorLinea, [player1.x, marDown - player1.texBola.alto/2 - 1], [mouse.get_pos()[0], mouse.get_pos()[1]], 2)


    estdMouse = mouse.get_pressed()[0]

    # Dibuja los Margenes
    pygame.draw.line(surface, COLOR_White, [0, marUp], [winWidth, marUp], 2)
    pygame.draw.line(surface, COLOR_White, [0, marDown], [winWidth, marDown], 2)

    #dibuja los objetos
    player1.draw(mouse)
    player1.drawNumBolitas()
    Mat.draw()
    pausa.draw()



    # Vuelca lo dibujado en pantalla
    pygame.display.flip()