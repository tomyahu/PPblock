from Bolita import Bola
from consts import *
import pygame
from math import *



class player():

    def __init__(self, screen, texture, texturaFlecha):
        self.x = winWidth/2
        self.texBola = texture
        self.texFlecha = texturaFlecha
        self.screen = screen
        self.bolitas = [Bola(self.x,marDown - self.texBola.alto/2,self.texBola,self.screen)]
        self.numBolitas = 1
        self.base = 0
        self.altura = 0

    def anadirBolita(self):
        self.bolitas += [Bola(self.x,marDown - self.texBola.alto/2,self.texBola,self.screen)]

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
        if angle > 70:
            angle = 70
        elif angle < -70:
            angle = -70
        Flecha = pygame.transform.rotate(self.texFlecha.image,angle)
        flechaSize = Flecha.get_rect().size


        posDraw = (self.x - flechaSize[0]/2, marDown - flechaSize[1]/2 - self.texBola.alto/2)
        self.screen.blit(Flecha, posDraw)

    def drawNumBolitas(self):
        contText = fuenteCaja.render("Bolas: " + str(self.numBolitas), 1, COLOR_White)
        self.screen.blit(contText, (5, winHeight - 20))

    def draw(self,mouse):
        base = mouse.get_pos()[0] - self.x
        altura = marDown - mouse.get_pos()[1]
        self.drawFlecha(base,altura)

        for i in range(self.numBolitas):
            self.bolitas[i].draw()


    def lanzarBolita(self,x,base,altura):
        if base > 0 and float(altura)/base < tan(pi/9):
            base = cos(pi/9)
            altura = sin(pi/9)
        elif base < 0 and (-1)*float(altura)/base < tan(pi/9):
            base = (-1)*cos(pi / 9)
            altura = sin(pi / 9)
        self.bolitas[x].lanzar(float(base),float(altura))

    def setX(self,x):
        self.x = x

    def updateBolitas(self):
        for i in self.bolitas:
            i.updatePos()
        self.reunirBolas()

    def checkPrimeraBola(self):
        if self.bolitas[0].y > marDown - self.texBola.alto/2 - 1:
            self.setX(self.bolitas[0].x)
            return True
        return False

    def reunirBolas(self):
        lim = marDown - self.texBola.alto / 2 - 1
        for i in self.bolitas:
            if i.y > lim:
                i.x = self.x

    def bolitasQuietas(self):
        for i in self.bolitas:
            if i.vely != 0:
                return False

        return True

    def checkUltimaBola(self):
        suma = 0
        lim = marDown - self.texBola.alto/2 - 1
        for i in range(self.numBolitas):
            if self.bolitas[i].y > lim - default_Vel and self.bolitas[i].vely > 0:
                self.bolitas[i].y = lim
                suma += 1
        return suma

