from textura import *
from Bolita import *
from imageBank import *
import pygame
from random import randint
from math import sqrt
from consts import COLOR_White

class PowerUp():

    def __init__(self,x,y,texture,screen):
        self.x = x
        self.y = y
        self.tex = texture
        self.screen = screen
        self.id = 2

    def draw(self):
        self.screen.blit(self.tex.image, (self.x - (self.tex.ancho/2), self.y - (self.tex.alto/2)))
        return

    def getXin(self):
        return self.x - (self.tex.ancho/2)

    def getYin(self):
        return self.y - (self.tex.alto/2)

    def getXfin(self):
        return self.x + (self.tex.ancho/2)

    def getYfin(self):
        return self.y + (self.tex.alto/2)

    def kill(self):
        del self

    def setPos(self, x, y):
        self.x = x
        self.y = y

    def isInArea(self,bola):
        xCenter = bola.x
        yCenter = bola.y

        r1 = float(self.tex.alto) / 2
        r2 = float(bola.tex.alto) / 2

        dist = sqrt((self.x - xCenter)**2 + (self.y - yCenter)**2)

        if dist < (r1 + r2):
            return True
        else:
            return False


class BolaExtra(PowerUp):

    def __init__(self,x,y,screen):
        PowerUp.__init__(self,x,y,bolaExtra,screen)


    def colisionBolita(self, player):
        player.anadirBolita()

class randomBall(PowerUp):

    def __init__(self,x,y,screen):
        PowerUp.__init__(self,x,y,randomThrow,screen)
        self.id = 3
        self.touched = False

    def colisionBolita(self, bola):
        base = randint(1,100)
        altura = randint(1, 100)

        if base > 0 and float(altura)/base < tan(pi/18):
            base = cos(pi/18)
            altura = sin(pi/18)
        elif base < 0 and (-1)*float(altura)/base < tan(pi/18):
            base = (-1)*cos(pi / 18)
            altura = sin(pi / 18)
        bola.lanzar(base,altura)

class restarFila(PowerUp):

    def __init__(self,x,y,screen):
        PowerUp.__init__(self, x, y, blFila, screen)
        self.id = 4
        self.touched = False
        self.laser = 0

    def colisionBolita(self,matCas):
        a = matCas.mapa2celda(self.x,self.y)
        self.resFila(matCas,a[0])

    def resFila(self,matCas,a):
        for i in matCas.matrizCasillas[a]:
            if i.id == 1:
                i.cont -= 1
                b = matCas.mapa2celda(i.x,i.y)
                matCas.checkCasillaDead(b[0],b[1])

    def draw(self):
        PowerUp.draw(self)
        if self.laser > 0:
            pygame.draw.line(self.screen, COLOR_White, [0, self.y], [winWidth, self.y], 2)
            self.laser -= 1


class restarCol(PowerUp):

    def __init__(self,x,y,screen):
        PowerUp.__init__(self, x, y, blCol, screen)
        self.id = 4
        self.touched = False
        self.laser = 0

    def colisionBolita(self,matCas):
        a = matCas.mapa2celda(self.x,self.y)
        self.resCol(matCas,a[1])

    def resCol(self,matCas,a):
        for i in range(len(matCas.matrizCasillas)):
            if matCas.matrizCasillas[i][a].id == 1:
                matCas.matrizCasillas[i][a].cont -= 1
                b = matCas.mapa2celda(matCas.matrizCasillas[i][a].x,matCas.matrizCasillas[i][a].y)
                matCas.checkCasillaDead(b[0],b[1])

    def draw(self):
        PowerUp.draw(self)
        if self.laser > 0:
            pygame.draw.line(self.screen, COLOR_White, [self.x, marDown], [self.x, marUp], 2)
            self.laser -= 1





