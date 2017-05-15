from consts import winWidth, marUp, marDown, default_Vel
from math import *
from textura import *

#Sonidos
from soundBank import *
from pygame import mixer
mixer.init()

class Bola():

    #recibe las coordenadas de la bola, la textura y la pantalla
    def __init__(self,x,y,texture,screen):
        self.x = x
        self.y = y
        self.velx = 0.0
        self.vely = 0.0
        self.tex = texture
        self.screen = screen
        self.contPowerup = 0
        return

    #dibuja la bola
    def draw(self):
        self.screen.blit(self.tex.image, (self.x - (self.tex.ancho/2), self.y - (self.tex.alto/2)))
        return

    #cambia la velocidad de la bola
    def setVel(self,vx,vy):
        self.velx = vx
        self.vely = vy
        return

    #lanza una bola en el angulo dado por base y altura y a la
    #velocidad dada por defaultVel
    def lanzar(self,base,altura):
        hipotenusa = sqrt( (base**2) + (altura**2) )
        self.velx = (base/hipotenusa) * default_Vel
        self.vely = -(altura / hipotenusa) * default_Vel
        return

    #Rebote Vertical
    def colisionVer(self,borde):
        self.y = borde
        self.vely *= -1
        pygame.mixer.stop
        blip.play()
        return

    #Rebote Horizontal
    def colisionHor(self,borde):
        self.x = borde
        self.velx *= -1
        pygame.mixer.stop
        blip.play()
        return

    #actualiza la posicion de la bola
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

        if self.contPowerup > 0:
            self.contPowerup -= 1

    #devuelve el x mas a la izquierda de su textura
    def getXin(self):
        return self.x - (self.tex.ancho/2)

    # devuelve el y mas arriba de su textura
    def getYin(self):
        return self.y - (self.tex.alto/2)

    # devuelve el x mas a la derecha de su textura
    def getXfin(self):
        return self.x + (self.tex.ancho/2)

    # devuelve el y mas abajo de su textura
    def getYfin(self):
        return self.y + (self.tex.alto/2)