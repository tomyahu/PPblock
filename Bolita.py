import pygame
from math import *
from consts import winWidth, winHeight, marDown, marUp, default_Vel
from soundBank import *

class Bola():

    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.velx = 0
        self.vely = 0
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
            blip()
        return

    def colisionLeft(self):
        if self.x < 0:
            self.x = 0
            self.velx *= -1
            blip()
        return

    def colisionRight(self):
        if self.x < winWidth:
            self.x = winWidth
            self.velx *= -1
            blip()
        return

    def updatePos(self):
        self.x += self.velx
        self.y += self.vely

        self.colisionLeft()
        self.colisionRight()
        self.colisionUp()
