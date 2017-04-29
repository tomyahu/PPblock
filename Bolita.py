from math import *
from consts import winWidth, marUp, marDown, default_Vel
from math import *
from textura import *

#Sonidos
from soundBank import *
from pygame import mixer
mixer.init()

class Bola():

    def __init__(self,x,y,texture,screen):
        self.x = x
        self.y = y
        self.velx = 0
        self.vely = 0
        self.tex = texture
        self.screen = screen
        return

    def draw(self):
        self.screen.blit(self.tex.image, (self.x - (self.tex.ancho>>1), self.y - (self.tex.alto>>1)))
        return

    def setVel(self,vx,vy):
        self.velx = vx
        self.vely = vy
        return

    def lanzar(self,base,altura):
        hipotenusa = sqrt( (base<<1) + (altura<<1) )
        self.velx = (base/hipotenusa) * default_Vel
        self.vely = (altura / hipotenusa) * default_Vel
        return

    def colisionVer(self,borde):
        self.y = borde
        self.vely *= -1
        blip.play()
        return

    def colisionHor(self,borde):
        self.x = borde
        self.velx *= -1
        blip.play()
        return

    def updatePos(self):
        self.x += self.velx
        self.y += self.vely


        if self.x < (self.tex.ancho)>>1:
            self.colisionHor((self.tex.ancho)>>1)

        if self.x > winWidth - ((self.tex.ancho)>>1):
            self.colisionHor(winWidth - ((self.tex.ancho)>>1))

        if self.y < marUp + ((self.tex.alto)>>1):
            self.colisionVer(marUp + ((self.tex.alto)>>1))

        if self.y > marDown - ((self.tex.alto)>>1):
            self.colisionVer(marDown - ((self.tex.alto)>>1))
