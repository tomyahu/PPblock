from Bolita import Bola
from consts import *
import pygame
from math import *



class player():

    #Recibe:
    #la pantalla (screen)
    #la textura de las Bolitas (texture)
    #la textura de la flecha (texturaFlecha)
    #el avatar del personaje (avatar)
    def __init__(self, screen, texture, texturaFlecha, avatar):
        self.x = winWidth/2
        self.texBola = texture
        self.texFlecha = texturaFlecha
        self.screen = screen
        self.avatar = avatar
        self.bolitas = [Bola(self.x,marDown - self.texBola.alto/2,self.texBola,self.screen)]
        self.numBolitas = 1
        self.base = 0
        self.altura = 0
        self.prim = False

    #Anade una bolita a jugador
    def anadirBolita(self):
        self.bolitas += [Bola(self.x,marDown - self.texBola.alto/2,self.texBola,self.screen)]

    #angulo: num num -> float
    #Recibe la distancia horizontal y la vertical entre 2 puntos y devuelve el angulo
    #esta pensado como un triangulo rectangulo
    def angulo(self,base,altura):
        if altura < 0:
            altura = 0
        if base < 0:
            return (atan(float(altura)/base) + pi/2)/pi * 180.0
        elif base == 0:
            return 0
        else:
            return (atan(float(altura) / base) - pi/2)/pi * 180.0

    #dibuja la flecha
    def drawFlecha(self,base,altura):
        angle = self.angulo(base,altura)
        if angle > 80:
            angle = 80
        elif angle < -80:
            angle = -80
        Flecha = pygame.transform.rotate(self.texFlecha.image,angle)
        flechaSize = Flecha.get_rect().size


        posDraw = (self.x - flechaSize[0]/2, marDown - flechaSize[1]/2 - self.texBola.alto/2)
        self.screen.blit(Flecha, posDraw)

    #Dibuja el contador de bolitas abajo a la izquierda
    def drawNumBolitas(self):
        contText = fuenteCaja.render("Bolas: " + str(self.numBolitas), 1, COLOR_White)
        self.screen.blit(contText, (5, winHeight - 20))

    #dibuja al jugador y todas sus bolitas
    def draw(self,mouse):
        base = mouse.get_pos()[0] - self.x
        altura = marDown - mouse.get_pos()[1]
        self.drawFlecha(base,altura)
        self.screen.blit(self.avatar.image,(self.x - self.avatar.px, marDown - self.avatar.py))

        for i in range(self.numBolitas):
            self.bolitas[i].draw()

    #lanza la bolita x en la direccion dada por la coordenada horizontal base
    #y la coordenada vertical altura
    def lanzarBolita(self,x,base,altura):
        if base > 0 and float(altura)/base < tan(pi/18):
            base = cos(pi/18)
            altura = sin(pi/18)
        elif base < 0 and (-1)*float(altura)/base < tan(pi/18):
            base = (-1)*cos(pi / 18)
            altura = sin(pi / 18)
        self.bolitas[x].lanzar(float(base),float(altura))

    #cambia la posicion horizontal de player
    def setX(self,x):
        self.x = x

    #Actualiza la posicion de las bolitas
    def updateBolitas(self):
        for i in self.bolitas:
            i.updatePos()
        self.reunirBolas()

    #reune las bolitas que ya esten abajo
    def reunirBolas(self):
        lim = marDown - self.texBola.alto / 2 - 1
        for i in self.bolitas:
            if i.y >= lim:
                i.x = self.x

    #retorna True si todas las bolas estan quietas y False si no
    def bolitasQuietas(self):
        for i in self.bolitas:
            if i.vely != 0:
                return False

        return True

    #Devuelve cuantas bolitas han caido en la ultima frame
    #y ademas si cae la primera bolita, entonces actualiza la posicion de Player
    def checkUltimaBola(self):
        suma = 0
        lim = marDown - self.texBola.alto/2 - 1
        for i in range(self.numBolitas):
            if self.bolitas[i].y > lim - default_Vel and self.bolitas[i].vely > 0:
                if not self.prim:
                    self.prim = True
                    self.setX(self.bolitas[i].x)
                self.bolitas[i].y = lim + 1
                self.bolitas[i].vely = 0
                self.bolitas[i].velx = 0
                suma += 1
        return suma

    #Reinicia los atributos de Player
    def restart(self):
        self.x = winWidth / 2
        self.bolitas = [Bola(self.x, marDown - self.texBola.alto / 2, self.texBola, self.screen)]
        self.numBolitas = 1


