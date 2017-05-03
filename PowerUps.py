from textura import *
from Bolita import *
from imageBank import *
import pygame
from random import randint

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




