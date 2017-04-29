from Casilla import *
from consts import marDown, marUp, winWidth, winHeight, tamCas
from random import randint

totalFilas = 8
totalColumnas = 7

class MatCas():

    def __init__(self,texture,screen):
        self.tex = texture
        self.screen = screen
        self.matrizCasillas = []
        self.contUniversal = 1
        for i in range(8):
            self.matrizCasillas[i] = [CasillaVacia(),CasillaVacia(),CasillaVacia(),CasillaVacia(),CasillaVacia(),CasillaVacia(),CasillaVacia()]

    def casillaRandom(self,fila,columna):
        pos = self.celda2mapa(fila,columna)
        cas = CasillaVacia()

        if (randint(0,1) == 1):
            cas = Casilla(pos[0],pos[1],texture,self.contUniversal,self.screen)
        return cas

    def testDead(self):
        for i in range(7):
            if self.matrizCasillas[7][i].id != 0:
                return True
        return False

    def update(self):
        for i in range(1,8,1):
            for j in range(7):
                self.matrizCasillas[i][j] = self.matrizCasillas[i-1][j]

        for k in range(7):
            self.matrizCasillas[0][k] = self.casillaRandom(0,k)


    def celda2mapa(self,fila,columna):
        return (marUp + (fila+1)*45.0 + 22.5, (columna)*45.0 + 22.5)

    def mapa2celda(self,x,y):
        return (int(x - marUp - 45.0)/45, int(y)/45)