from textura import *
from Bolita import *
from consts import *

class Casilla():

    def __init__(self,x,y,texture,contador,screen):
        self.x = x
        self.y = y
        self.tex = texture
        self.cont = contador
        self.screen = screen
        self.id = 1

    def draw(self):
        self.screen.blit(self.tex.image, (self.x - (self.tex.ancho>>1), self.y - (self.tex.alto>>1)))
        return

    def drawCounter(self):
        contText = fuenteCaja.render( str(self.cont), 1, COLOR_White)
        self.screen.blit(contText, (self.x - 18, self.y))

    def colisionBolita(self,bola):

        xin = self.getXin()
        xfin = self.getXfin()
        yin = self.getYin()
        yfin = self.getYfin()

        if bola.getXin() - bola.velx < xin:
            bola.colisionHor(xin-1)
        if bola.getXfin() - bola.velx >= xfin:
            bola.colisionHor(xfin+1)
        if bola.getYin() - bola.vely < yin:
            bola.colisionVer(yin-1)
        if bola.getYfin() - bola.vely > yfin:
            bola.colisionVer(yfin+1)

        self.cont -= 1

    def getXin(self):
        return self.x - (self.tex.ancho/2)

    def getYin(self):
        return self.y - (self.tex.alto/2)

    def getXfin(self):
        return self.x + (self.tex.ancho/2)

    def getYfin(self):
        return self.y + (self.tex.alto/2)

    def setPos(self, x, y):
        self.x = x
        self.y = y



class CasillaVacia():

    def __init__(self):
        self.id = 0