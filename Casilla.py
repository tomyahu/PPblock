from textura import *
from Bolita import *
from consts import *
import pygame

class Casilla():

    def __init__(self,x,y,contador,screen):
        self.x = x
        self.y = y
        self.cont = contador
        self.contTotal = contador
        self.screen = screen
        self.id = 1

    def draw(self):
        a = COLOR_Red2[0] * self.cont / self.contTotal + COLOR_Yellow[0] * (
            self.contTotal - self.cont) / self.contTotal

        b = COLOR_Red2[1] * self.cont / self.contTotal + COLOR_Yellow[1] * (
            self.contTotal - self.cont) / self.contTotal

        c = COLOR_Red2[2] * self.cont / self.contTotal + COLOR_Yellow[2] * (
            self.contTotal - self.cont) / self.contTotal

        colorCaja = (a, b, c)

        pygame.draw.line(self.screen, colorCaja, [self.x - 20.5, self.y - 20.5], [self.x - 20.5, self.y + 20.5], 2)
        pygame.draw.line(self.screen, colorCaja, [self.x - 20.5, self.y + 20.5], [self.x + 20.5, self.y + 20.5], 2)
        pygame.draw.line(self.screen, colorCaja, [self.x + 20.5, self.y + 20.5], [self.x + 20.5, self.y - 20.5], 2)
        pygame.draw.line(self.screen, colorCaja, [self.x + 20.5, self.y - 20.5], [self.x - 20.5, self.y - 20.5], 2)
        self.drawCounter()
        return

    def kill(self):
        del self

    def drawCounter(self):
        contText = fuenteCaja.render( str(self.cont), 1, COLOR_White)
        self.screen.blit(contText, (self.x - 18, self.y))

    def colisionBolita(self,bola):

        xin = self.getXin()
        xfin = self.getXfin()
        yin = self.getYin()
        yfin = self.getYfin()

        if bola.getYin() - bola.vely < yin:
            bola.colisionVer(yin-1)
        if bola.getXin() - bola.velx < xin:
            bola.colisionHor(xin-1)
        if bola.getYfin() - bola.vely > yfin:
            bola.colisionVer(yfin+1)
        if bola.getXfin() - bola.velx > xfin:
            bola.colisionHor(xfin+1)

        self.cont -= 1

    def getXin(self):
        return self.x - (22.5)

    def getYin(self):
        return self.y - (22.5)

    def getXfin(self):
        return self.x + (22.5)

    def getYfin(self):
        return self.y + (22.5)

    def setPos(self, x, y):
        self.x = x
        self.y = y



class Casilla2(Casilla):

    def __init__(self,x,y,contador,screen):
        Casilla.__init__(self,x,y,2*contador,screen)

    def draw(self):
        a = COLOR_DarkBlue[0] * self.cont / self.contTotal + COLOR_Cyan[0] * (
            self.contTotal - self.cont) / self.contTotal

        b = COLOR_DarkBlue[1] * self.cont / self.contTotal + COLOR_Cyan[1] * (
            self.contTotal - self.cont) / self.contTotal

        c = COLOR_DarkBlue[2] * self.cont / self.contTotal + COLOR_Cyan[2] * (
            self.contTotal - self.cont) / self.contTotal

        colorCaja = (a, b, c)

        pygame.draw.line(self.screen, colorCaja, [self.x - 20.5, self.y - 20.5], [self.x - 20.5, self.y + 20.5], 2)
        pygame.draw.line(self.screen, colorCaja, [self.x - 20.5, self.y + 20.5], [self.x + 20.5, self.y + 20.5], 2)
        pygame.draw.line(self.screen, colorCaja, [self.x + 20.5, self.y + 20.5], [self.x + 20.5, self.y - 20.5], 2)
        pygame.draw.line(self.screen, colorCaja, [self.x + 20.5, self.y - 20.5], [self.x - 20.5, self.y - 20.5], 2)
        self.drawCounter()
        return



class CasillaVacia():

    def __init__(self):
        self.id = 0
        self.x = 0
        self.y = 0

    def draw(self):
        return

    def kill(self):
        del self