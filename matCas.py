from Casilla import *
from PowerUps import *
from consts import marDown, marUp, winWidth, winHeight, tamCas
from random import randint
from soundBank import laser
import pygame

totalFilas = 8
totalColumnas = 7

class MatCas():

    def __init__(self,screen,player):
        self.screen = screen
        self.player = player
        self.matrizCasillas = []
        self.contUniversal = 0
        for i in range(8):
            self.matrizCasillas += [[CasillaVacia(),CasillaVacia(),CasillaVacia(),CasillaVacia(),CasillaVacia(),CasillaVacia(),CasillaVacia()]]

    def casillaRandom(self,fila,columna):
        pos = self.celda2mapa(fila,columna)
        cas = CasillaVacia()
        rand = randint(0,3)

        if (rand > 1):
            if self.contUniversal%10 == 0 and randint(0,1) == 0:
                cas = Casilla2(pos[0],pos[1],self.contUniversal,self.screen)
            else:
                aux = [Casilla(pos[0], pos[1], self.contUniversal, self.screen), CasillaTriangular1(pos[0], pos[1], self.contUniversal, self.screen), CasillaTriangular2(pos[0], pos[1], self.contUniversal, self.screen), CasillaTriangular3(pos[0], pos[1], self.contUniversal, self.screen), CasillaTriangular4(pos[0], pos[1], self.contUniversal, self.screen)]
                cas = aux[randint(0,len(aux) - 1)]
        elif(rand == 1):
            aux = [randomBall(pos[0],pos[1],self.screen),restarFila(pos[0],pos[1],self.screen),restarCol(pos[0],pos[1],self.screen),CasillaVacia()]
            cas = aux[randint(0,len(aux)-1)]
        return cas

    def testDead(self):
        for i in range(7):
            if self.matrizCasillas[7][i].id == 1:
                return True
        return False

    def checkCasillaDead(self,fila,columna):
        cas = self.matrizCasillas[fila][columna]
        if cas.id == 1:
            if cas.cont <= 0:
                cas.kill()
                self.matrizCasillas[fila][columna] = CasillaVacia()
        elif cas.id == 2:
            cas.kill()
            self.matrizCasillas[fila][columna] = CasillaVacia()


    def testColision(self,bola):
        pos = self.mapa2celda(bola.x,bola.y)

        cas = self.matrizCasillas[pos[0]][pos[1]]
        if cas.id == 1:
            if cas.isInArea(bola):
                cas.colisionBolita(bola)
                self.checkCasillaDead(pos[0],pos[1])
                return True
        elif cas.id == 2:
            if cas.isInArea(bola):
                cas.colisionBolita(self.player)
                self.checkCasillaDead(pos[0], pos[1])
                return True
        elif cas.id == 3:
            if cas.isInArea(bola):
                cas.colisionBolita(bola)
                cas.touched = True
                return True
        elif cas.id == 4:
            if cas.isInArea(bola) and bola.contPowerup == 0:
                bola.contPowerup = 10
                cas.colisionBolita(self)
                cas.touched = True
                cas.laser = 3
                laser.play()
                return True
        return False

    def restart(self):
        self.matrizCasillas = []
        self.contUniversal = 0
        for i in range(8):
            self.matrizCasillas += [
                [CasillaVacia(), CasillaVacia(), CasillaVacia(), CasillaVacia(), CasillaVacia(), CasillaVacia(),
                 CasillaVacia()]]
        self.nextLevel()

    def draw(self):
        for i in range(8):
            for j in range(7):
                self.matrizCasillas[i][j].draw()

        contText = fuenteCaja.render("Nivel: " + str(self.contUniversal), 1, COLOR_White)
        self.screen.blit(contText, (5, 40))

    def nextLevel(self):

        for i in range(0,8,1):
            for j in range(7):
                if self.matrizCasillas[i][j].id >= 3:
                    if self.matrizCasillas[i][j].touched:
                        self.matrizCasillas[i][j].kill()
                        self.matrizCasillas[i][j] = CasillaVacia()

                self.matrizCasillas[i][j].y += 45

        for i in [7,6,5,4,3,2,1]:
            for j in range(7):
                self.matrizCasillas[i][j] = self.matrizCasillas[i - 1][j]

        self.contUniversal += 1
        rand = randint(0,6)
        pos = self.celda2mapa(0, rand)
        for k in range(7):
            if k == rand:
                self.matrizCasillas[0][k] = BolaExtra(pos[0],pos[1],self.screen)
            else:
                self.matrizCasillas[0][k] = self.casillaRandom(0,k)


    def celda2mapa(self,fila,columna):
        return ((columna)*45.0 + 22.5, marUp + (fila+1)*45.0 + 22.5)

    def mapa2celda(self,x,y):
        return (int(y - marUp - 45)/45,int(x)/45)