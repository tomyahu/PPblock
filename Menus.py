from consts import *
from Button import *
from imageBank import *
from pygame.locals import *
import pygame



#estado click izquierdo Mouse
estdMouse = mouse.get_pressed()[0]

def GameOver(surface,clock,player1,Mat):

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




def Menu(surface,clock,player1,Mat):

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
                Customize(surface,clock,player1,Mat)
            customize.im = 1
        else:
            customize.im = 0

        estdMouse = mouse.get_pressed()[0]

        play.draw()
        restart.draw()
        quitB.draw()
        customize.draw()

        pygame.display.flip()


def Customize(surface,clock,player1,Mat):

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