from Bolita import Bola
from consts import *
import pygame
from math import atan, pi,sin



class player():

    def __init__(self, screen, texture, texturaFlecha):
        self.x = winWidth/2
        self.texBola = texture
        self.texFlecha = texturaFlecha
        self.screen = screen
        self.bolitas = [Bola(self.x,marDown,self.texBola,self.screen)]
        self.numBolitas = 1

    def anadirBolita(self):
        self.bolitas += [Bola(self.x,marDown,self.texBola,self.screen)]

    def angulo(self,base,altura):
        if altura < 0:
            altura = 0
        if base < 0:
            return (atan(float(altura)/base) + pi/2)/pi * 180.0
        elif base == 0:
            return 0
        else:
            return (atan(float(altura) / base) - pi/2)/pi * 180.0

    def drawFlecha(self,base,altura):
        angle = self.angulo(base,altura)
        Flecha = pygame.transform.rotate(self.texFlecha.image,angle)
        flechaSize = Flecha.get_rect().size


        posDraw = (self.x - flechaSize[0]/2, marDown - flechaSize[1]/2)
        self.screen.blit(Flecha, posDraw)

    def draw(self,mouse):
        base = mouse.get_pos()[0] - self.x
        altura = marDown - mouse.get_pos()[1]
        self.drawFlecha(base,altura)

    def lanzarBolita(self,x,base,altura):
        self.bolitas[x].lanzar(base,altura)

    def setX(self,x):
        self.x = x

