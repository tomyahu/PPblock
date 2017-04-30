from Bolita import Bola
from consts import *

class player():

    def __init__(self, screen, texture):
        self.x = winWidth/2
        self.tex = texture
        self.bolitas = [Bola(self.x,marDown,self.tex,self.screen)]
        self.numBolitas = 1
        self.screen = screen

    def anadirBolita(self):
        self.bolitas += [Bola(self.x,marDown,self.tex,self.screen)]

    def lanzarBolita(self,x,base,altura):
        self.bolitas[x].lanzar(base,altura)

