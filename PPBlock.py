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
player1 = player(surface,pong,flecha,avatarCisneros)
Mat = MatCas(surface,player1)
Mat.nextLevel()
pausa = Button(winWidth-30,marUp/2,pausaTex,surface)

#estado click izquierdo Mouse
estdMouse = mouse.get_pressed()[0]

#Contadores
a = 0
b = 0
c = 0

def Customize():

    listaBolas = [pong, pokebola, paty]
    indice = 0
    cambio = False
    bolaDer = Button(winWidth/2 + 100,375,cambioDerTex,surface)
    bolaIzq = Button(winWidth / 2 - 100, 375, cambioIzqTex, surface)
    back = Button(winWidth / 2, 475, backTex, surface)

    while True:

        # Setea el reloj
        clock.tick(FPS)

        # Busca eventos de aplicacion
        for event in pygame.event.get():
            if event.type == QUIT:
                exit()

        # Dibuja la pantalla
        surface.fill(COLOR_Black)

        if bolaDer.inArea(mouse.get_pos()[0],mouse.get_pos()[1]):
            if mouse.get_pressed()[0] and not estdMouse:
                indice = (indice+1)%len(listaBolas)
                player1.texBola = listaBolas[indice]
                player1.restart()
                Mat.restart()
                cambio = True
            bolaDer.im = 1
        else:
            bolaDer.im = 0

        if bolaIzq.inArea(mouse.get_pos()[0],mouse.get_pos()[1]):
            if mouse.get_pressed()[0] and not estdMouse:
                indice = (indice - 1) % len(listaBolas)
                player1.texBola = listaBolas[indice]
                player1.restart()
                Mat.restart()
                cambio = True
            bolaIzq.im = 1
        else:
            bolaIzq.im = 0

        if back.inArea(mouse.get_pos()[0],mouse.get_pos()[1]):
            if mouse.get_pressed()[0] and not estdMouse:
                ind = 0

                return
            back.im = 1
        else:
            back.im = 0

        estdMouse = mouse.get_pressed()[0]

        aviso = fuenteCaja.render("Si es que cambias de bolita", 1, COLOR_White)
        text_rect = (winWidth/2 - aviso.get_rect().width/2 ,50)
        surface.blit(aviso, text_rect)
        aviso = fuenteCaja.render("la partida actual se borrara!", 1, COLOR_White)
        text_rect = (winWidth/2 - aviso.get_rect().width/2 ,66)
        surface.blit(aviso, text_rect)

        if cambio:
            aviso = fuenteCaja.render("yyyyyy  se borro", 1, COLOR_White)
            text_rect = (winWidth / 2 - aviso.get_rect().width / 2, 50 + 16*4)
            surface.blit(aviso, text_rect)


        bolaDer.draw()
        bolaIzq.draw()
        back.draw()
        surface.blit(listaBolas[indice].image,(winWidth / 2 - listaBolas[indice].ancho / 2, 375 - listaBolas[indice].alto / 2))



        pygame.display.flip()


def Menu():

    play = Button(winWidth/2,175,playTex,surface)
    restart = Button(winWidth / 2, 275, restartTex, surface)
    customize = Button(winWidth / 2, 375, customTex, surface)
    quitB = Button(winWidth / 2, 475, quitTex, surface)

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
            if mouse.get_pressed()[0] and not estdMouse:
                return
            play.im = 1
        else:
            play.im = 0

        if restart.inArea(mouse.get_pos()[0],mouse.get_pos()[1]):
            if mouse.get_pressed()[0] and not estdMouse:
                player1.restart()
                Mat.restart()
                return
            restart.im = 1
        else:
            restart.im = 0

        if quitB.inArea(mouse.get_pos()[0],mouse.get_pos()[1]):
            if mouse.get_pressed()[0] and not estdMouse:
                exit()
            quitB.im = 1
        else:
            quitB.im = 0

        if customize.inArea(mouse.get_pos()[0],mouse.get_pos()[1]):
            if mouse.get_pressed()[0] and not estdMouse:
                Customize()
            customize.im = 1
        else:
            customize.im = 0

        estdMouse = mouse.get_pressed()[0]

        play.draw()
        restart.draw()
        quitB.draw()
        customize.draw()

        pygame.display.flip()

def GameOver():

    restart = Button(winWidth / 2, 375, restartTex, surface)
    quitB = Button(winWidth/2, 475,quitTex,surface)

    while True:

        # Setea el reloj
        clock.tick(FPS)

        # Busca eventos de aplicacion
        for event in pygame.event.get():
            if event.type == QUIT:
                exit()

        # Dibuja la pantalla
        surface.fill(COLOR_Black)

        if quitB.inArea(mouse.get_pos()[0],mouse.get_pos()[1]):
            if mouse.get_pressed()[0] and not estdMouse:
                exit()
                return
            quitB.im = 1
        else:
            quitB.im = 0

        if restart.inArea(mouse.get_pos()[0],mouse.get_pos()[1]):
            if mouse.get_pressed()[0] and not estdMouse:
                player1.restart()
                Mat.restart()
                return
            restart.im = 1
        else:
            restart.im = 0

        estdMouse = mouse.get_pressed()[0]

        surface.blit(gameOverScreen,(0,0))
        quitB.draw()
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

    if pausa.inArea(mouse.get_pos()[0], mouse.get_pos()[1]):
        if mouse.get_pressed()[0] and not estdMouse:
            Menu()
        pausa.im = 1
    else:
        pausa.im = 0


    base = mouse.get_pos()[0] - player1.x
    altura = marDown - mouse.get_pos()[1]

    if keys.get_pressed()[K_w] and player1.bolitasQuietas() and b == 0:
        player1.lanzarBolita(0,base,altura)
        player1.base = base
        player1.altura = altura
        a = 1

    if a > 0 and a < player1.numBolitas*pix:
        if a%pix == 0:
            player1.lanzarBolita(a/pix,player1.base,player1.altura)
        a+=1

    choques = False
    for i in player1.bolitas:
        choques = choques or Mat.testColision(i)

    if not choques:
        c += 1
    else:
        c = 0

    if c == 360:
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

    if c >= 480:
        c = 0


    if player1.checkUltimaBola() > 0:
        b = 1

    player1.updateBolitas()

    if b > 0:
        b += 1

    if player1.bolitasQuietas():
        c = 0
        if b == 10:
            Mat.nextLevel()
            player1.numBolitas = len(player1.bolitas)
            b = 0
            a = 0
            player1.prim = False

    if Mat.testDead():
        GameOver()


    #Dibuja
    # Dibuja la pantalla
    surface.fill(COLOR_Black)

    if c >= 360:
        surface.blit(fondoAzarIm, (winWidth/2 - 125, marUp + 100))

    if Mat.contUniversal < 100:
        colorEspacio = COLOR_White[0]*(100 - Mat.contUniversal)/100
        colorLinea = (colorEspacio,colorEspacio,colorEspacio)
        pygame.draw.line(surface, colorLinea, [player1.x, marDown - player1.texBola.alto/2 - 1], [mouse.get_pos()[0], mouse.get_pos()[1]], 2)


    estdMouse = mouse.get_pressed()[0]

    # Dibuja los Margenes
    pygame.draw.line(surface, COLOR_White, [0, marUp], [winWidth, marUp], 2)
    pygame.draw.line(surface, COLOR_White, [0, marDown], [winWidth, marDown], 2)

    player1.draw(mouse)
    player1.drawNumBolitas()
    Mat.draw()
    pausa.draw()



    # Vuelca lo dibujado en pantalla
    pygame.display.flip()