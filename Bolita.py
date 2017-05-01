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
        self.velx = 0.0
        self.vely = 0.0
        self.tex = texture
        self.screen = screen
        return

    def draw(self):
        self.screen.blit(self.tex.image, (self.x - (self.tex.ancho/2), self.y - (self.tex.alto/2)))
        return

    def setVel(self,vx,vy):
        self.velx = vx
        self.vely = vy
        return

    def lanzar(self,base,altura):
        hipotenusa = sqrt( (base**2) + (altura**2) )
        self.velx = (base/hipotenusa) * default_Vel
        self.vely = -(altura / hipotenusa) * default_Vel
        return

    def colisionVer(self,borde):
        self.y = borde
        self.vely *= -1
        pygame.mixer.stop
        blip.play()
        return

    def colisionHor(self,borde):
        self.x = borde
        self.velx *= -1
        pygame.mixer.stop
        blip.play()
        return

    def updatePos(self):
        self.x += self.velx
        self.y += self.vely


        if self.x < (self.tex.ancho)/2:
            self.colisionHor((self.tex.ancho)/2)

        if self.x > winWidth - ((self.tex.ancho)/2):
            self.colisionHor(winWidth - ((self.tex.ancho)/2))

        if self.y < marUp + ((self.tex.alto)/2):
            self.colisionVer(marUp + ((self.tex.alto)/2))

        if self.y > marDown - ((self.tex.alto)/2):
            self.vely = 0
            self.velx = 0
            self.y = marDown - self.tex.alto/2

    def getXin(self):
        return self.x - (self.tex.ancho/2)

    def getYin(self):
        return self.y - (self.tex.alto/2)

    def getXfin(self):
        return self.x + (self.tex.ancho/2)

    def getYfin(self):
        return self.y + (self.tex.alto/2)

    def isInArea(self,x1,x2,y1,y2):
        xCenter = self.x
        yCenter = self.y

        if xCenter > x1 and xCenter < x2 and yCenter > y1 and yCenter < y2:
            return True
        else:
            return False