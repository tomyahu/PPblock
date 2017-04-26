from math import *
from consts import winWidth, marUp, marDown, default_Vel
from math import *

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
        self.screen.blit(self.tex, (self.x, self.y))
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

    def colisionUp(self):
        if self.y < marUp:
            self.y = marUp
            self.vely *= -1
            blip.play()
        return

    def colisionLeft(self):
        if self.x < 0:
            self.x = 0
            self.velx *= -1
            blip.play()
        return

    def colisionRight(self):
        if self.x > winWidth:
            self.x = winWidth
            self.velx *= -1
            blip.play()
        return

    def colisionDown(self):
        if self.y > marDown:
            self.y = marDown
            self.vely = 0
            self.velx = 0
        return

    def updatePos(self):
        self.x += self.velx
        self.y += self.vely

        self.colisionLeft()
        self.colisionRight()
        self.colisionUp()
        self.colisionDown()
