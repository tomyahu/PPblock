from textura import *
from Bolita import *

class casilla():

    def __init__(self,x,y,texture,contador,screen):
        self.x = x
        self.y = y
        self.tex = texture
        self.cont = contador
        self.screen = screen

    def draw(self):
        self.screen.blit(self.tex.image, (self.x - (self.tex.ancho>>1), self.y - (self.tex.alto>>1)))
        return

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
        return self.x - (self.tex.ancho>>1)

    def getYin(self):
        return self.y - (self.tex.alto>>1)

    def getXfin(self):
        return self.x + (self.tex.ancho>>1)

    def getYfin(self):
        return self.y + (self.tex.alto>>1)
