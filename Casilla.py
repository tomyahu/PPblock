from textura import *
from Bolita import *
from consts import *
import pygame

class Casilla():

    #recibe la poscicion, el contador que representa su resistencia y la pantalla
    def __init__(self,x,y,contador,screen):
        self.x = x
        self.y = y
        self.cont = contador
        self.contTotal = contador
        self.screen = screen
        self.id = 1

    #dibuja la casilla
    def draw(self):
        a = COLOR_Red2[0] * self.cont / self.contTotal + COLOR_Yellow[0] * (
            self.contTotal - self.cont) / self.contTotal

        b = COLOR_Red2[1] * self.cont / self.contTotal + COLOR_Yellow[1] * (
            self.contTotal - self.cont) / self.contTotal

        c = COLOR_Red2[2] * self.cont / self.contTotal + COLOR_Yellow[2] * (
            self.contTotal - self.cont) / self.contTotal

        if a < 0 or a > 255:
            a = 0

        if b < 0 or b > 255:
            b = 0

        if c < 0 or c > 255:
            c = 0

        colorCaja = (a, b, c)

        pygame.draw.line(self.screen, colorCaja, [self.x - 20.5, self.y - 20.5], [self.x - 20.5, self.y + 20.5], 2)
        pygame.draw.line(self.screen, colorCaja, [self.x - 20.5, self.y + 20.5], [self.x + 20.5, self.y + 20.5], 2)
        pygame.draw.line(self.screen, colorCaja, [self.x + 20.5, self.y + 20.5], [self.x + 20.5, self.y - 20.5], 2)
        pygame.draw.line(self.screen, colorCaja, [self.x + 20.5, self.y - 20.5], [self.x - 20.5, self.y - 20.5], 2)
        self.drawCounter()
        return

    #se destruye
    def kill(self):
        del self

    #dibuja el contador de resistencia que tiene
    def drawCounter(self):
        contText = fuenteCaja.render( str(self.cont), 1, COLOR_White)
        self.screen.blit(contText, (self.x - 18, self.y))

    #revisa si bola colisiono con la casilla
    def colisionBolita(self,bola):

        xin = self.getXin()
        xfin = self.getXfin()
        yin = self.getYin()
        yfin = self.getYfin()

        if bola.getYin() - bola.vely < yin and bola.vely > 0:
            bola.colisionVer(yin-1)
        if bola.getXin() - bola.velx < xin and bola.velx > 0:
            bola.colisionHor(xin-1)
        if bola.getYfin() - bola.vely > yfin and bola.vely < 0:
            bola.colisionVer(yfin+1)
        if bola.getXfin() - bola.velx > xfin and bola.velx < 0:
            bola.colisionHor(xfin+1)

        self.cont -= 1

    # devuelve el x mas a la izquierda de su textura
    def getXin(self):
        return self.x - (22.5)

    # devuelve el y mas arriba de su textura
    def getYin(self):
        return self.y - (22.5)

    # devuelve el x mas a la derecha de su textura
    def getXfin(self):
        return self.x + (22.5)

    # devuelve el y mas abajo de su textura
    def getYfin(self):
        return self.y + (22.5)

    #ubica la casilla en la posicion definida por x e y
    def setPos(self, x, y):
        self.x = x
        self.y = y

    #revisa si bola esta dentro de la casilla
    def isInArea(self, bola):
        xCenter = bola.x
        yCenter = bola.y

        x1 = self.getXin()
        x2 = self.getXfin()
        y1 = self.getYin()
        y2 = self.getYfin()

        if xCenter > x1 and xCenter < x2 and yCenter > y1 and yCenter < y2:
            return True
        else:
            return False




#Variante de Casilla con doble resistencia
class Casilla2(Casilla):

    def __init__(self,x,y,contador,screen):
        Casilla.__init__(self,x,y,2*contador,screen)

    def draw(self):
        a = COLOR_DarkBlue[0] * self.cont / self.contTotal + COLOR_Cyan[0] * (
            self.contTotal - self.cont) / self.contTotal

        b = COLOR_DarkBlue[1] * self.cont / self.contTotal + COLOR_Cyan[1] * (
            self.contTotal - self.cont) / self.contTotal

        c = COLOR_DarkBlue[2] * self.cont / self.contTotal + COLOR_Cyan[2] * (
            self.contTotal - self.cont) / self.contTotal


        if a < 0 or a > 255:
            a = 0

        if b < 0 or b > 255:
            b = 0

        if c < 0 or c > 255:
            c = 0

        colorCaja = (a, b, c)

        pygame.draw.line(self.screen, colorCaja, [self.x - 20.5, self.y - 20.5], [self.x - 20.5, self.y + 20.5], 2)
        pygame.draw.line(self.screen, colorCaja, [self.x - 20.5, self.y + 20.5], [self.x + 20.5, self.y + 20.5], 2)
        pygame.draw.line(self.screen, colorCaja, [self.x + 20.5, self.y + 20.5], [self.x + 20.5, self.y - 20.5], 2)
        pygame.draw.line(self.screen, colorCaja, [self.x + 20.5, self.y - 20.5], [self.x - 20.5, self.y - 20.5], 2)
        self.drawCounter()
        return



#variable de casilla qe equivale a un espacio vacio
class CasillaVacia():

    def __init__(self):
        self.id = 0
        self.x = 0
        self.y = 0

    def draw(self):
        return

    def kill(self):
        del self

#variante de casilla con geometria triangular de esta forma
# |\
# | \
# |  \
# |___\
class CasillaTriangular1(Casilla):

    def __init__(self,x,y,contador,screen):
        Casilla.__init__(self,x,y,contador,screen)
        self.id = 1

    def draw(self):
        a = COLOR_Red2[0] * self.cont / self.contTotal + COLOR_Yellow[0] * (
            self.contTotal - self.cont) / self.contTotal

        b = COLOR_Red2[1] * self.cont / self.contTotal + COLOR_Yellow[1] * (
            self.contTotal - self.cont) / self.contTotal

        c = COLOR_Red2[2] * self.cont / self.contTotal + COLOR_Yellow[2] * (
            self.contTotal - self.cont) / self.contTotal

        if a < 0 or a > 255:
            a = 0

        if b < 0 or b > 255:
            b = 0

        if c < 0 or c > 255:
            c = 0

        colorCaja = (a, b, c)

        pygame.draw.line(self.screen, colorCaja, [self.x - 20.5, self.y - 20.5], [self.x - 20.5, self.y + 20.5], 2)
        pygame.draw.line(self.screen, colorCaja, [self.x - 20.5, self.y + 20.5], [self.x + 20.5, self.y + 20.5], 2)
        pygame.draw.line(self.screen, colorCaja, [self.x + 20.5, self.y + 20.5], [self.x - 20.5, self.y - 20.5], 2)
        self.drawCounter()
        return

    def colisionBolita(self,bola):

        xin = self.getXin()
        yfin = self.getYfin()


        if bola.getXin() - bola.velx < xin and bola.velx > 0:
            bola.colisionHor(xin-1)
            self.cont -= 1
        elif bola.getYfin() - bola.vely > yfin and bola.vely < 0:
            bola.colisionVer(yfin+1)
            self.cont -= 1
        else:
            aux = bola.velx
            bola.velx = bola.vely
            bola.vely = aux
            self.cont -= 1

    def isInArea(self,bola):
        xCenter = bola.x
        yCenter = bola.y

        x1 = self.getXin()
        x2 = self.getXfin()
        y1 = self.getYin()
        y2 = self.getYfin()

        if xCenter > x1-1 and yCenter > y1-1 and xCenter < x2+1 and yCenter < y2+1 and xCenter < x1 + (yCenter - y1)+1:
            return True
        else:
            return False


#variante de casilla con geometria triangular de esta forma
#    /|
#   / |
#  /  |
# /___|
class CasillaTriangular2(Casilla):

    def __init__(self,x,y,contador,screen):
        Casilla.__init__(self,x,y,contador,screen)
        self.id = 1

    def draw(self):
        a = COLOR_Red2[0] * self.cont / self.contTotal + COLOR_Yellow[0] * (
            self.contTotal - self.cont) / self.contTotal

        b = COLOR_Red2[1] * self.cont / self.contTotal + COLOR_Yellow[1] * (
            self.contTotal - self.cont) / self.contTotal

        c = COLOR_Red2[2] * self.cont / self.contTotal + COLOR_Yellow[2] * (
            self.contTotal - self.cont) / self.contTotal

        if a < 0 or a > 255:
            a = 0

        if b < 0 or b > 255:
            b = 0

        if c < 0 or c > 255:
            c = 0

        colorCaja = (a, b, c)

        pygame.draw.line(self.screen, colorCaja, [self.x + 20.5, self.y + 20.5], [self.x - 20.5, self.y + 20.5], 2)
        pygame.draw.line(self.screen, colorCaja, [self.x + 20.5, self.y + 20.5], [self.x + 20.5, self.y - 20.5], 2)
        pygame.draw.line(self.screen, colorCaja, [self.x - 20.5, self.y + 20.5], [self.x + 20.5, self.y - 20.5], 2)
        self.drawCounter()
        return

    def colisionBolita(self,bola):

        xin = self.getXin()
        xfin = self.getXfin()
        yin = self.getYin()
        yfin = self.getYfin()


        if bola.getXfin() - bola.velx > xfin and bola.velx < 0:
            bola.colisionHor(xfin+1)
            self.cont -= 1
        elif bola.getYfin() - bola.vely > yfin and bola.vely < 0:
            bola.colisionVer(yfin+1)
            self.cont -= 1
        else:
            aux = bola.velx
            bola.velx = (-1)*bola.vely
            bola.vely = (-1)*aux
            bola.x = xfin - (bola.y - yin)
            self.cont -= 1

    def isInArea(self,bola):
        xCenter = bola.x
        yCenter = bola.y

        x1 = self.getXin()
        x2 = self.getXfin()
        y1 = self.getYin()
        y2 = self.getYfin()

        if xCenter > x1-1 and yCenter > y1-1 and xCenter < x2+1 and yCenter < y2+1 and xCenter > x2 - (yCenter - y1) - 1:
            return True
        else:
            return False



#variante de casilla con geometria triangular de esta forma
# _____
# |   /
# |  /
# | /
# |/
class CasillaTriangular3(Casilla):

    def __init__(self,x,y,contador,screen):
        Casilla.__init__(self,x,y,contador,screen)
        self.id = 1

    def draw(self):
        a = COLOR_Red2[0] * self.cont / self.contTotal + COLOR_Yellow[0] * (
            self.contTotal - self.cont) / self.contTotal

        b = COLOR_Red2[1] * self.cont / self.contTotal + COLOR_Yellow[1] * (
            self.contTotal - self.cont) / self.contTotal

        c = COLOR_Red2[2] * self.cont / self.contTotal + COLOR_Yellow[2] * (
            self.contTotal - self.cont) / self.contTotal

        if a < 0 or a > 255:
            a = 0

        if b < 0 or b > 255:
            b = 0

        if c < 0 or c > 255:
            c = 0

        colorCaja = (a, b, c)

        pygame.draw.line(self.screen, colorCaja, [self.x - 20.5, self.y - 20.5], [self.x - 20.5, self.y + 20.5], 2)
        pygame.draw.line(self.screen, colorCaja, [self.x - 20.5, self.y - 20.5], [self.x + 20.5, self.y - 20.5], 2)
        pygame.draw.line(self.screen, colorCaja, [self.x - 20.5, self.y + 20.5], [self.x + 20.5, self.y - 20.5], 2)
        self.drawCounter()
        return

    def colisionBolita(self,bola):

        xin = self.getXin()
        xfin = self.getXfin()
        yin = self.getYin()
        yfin = self.getYfin()


        if bola.getXin() - bola.velx < xin and bola.velx > 0:
            bola.colisionHor(xin-1)
            self.cont -= 1
        elif bola.getYin() - bola.vely < yin and bola.vely > 0:
            bola.colisionVer(yin-1)
            self.cont -= 1
        else:
            aux = bola.velx
            bola.velx = (-1)*bola.vely
            bola.vely = (-1)*aux
            bola.x = xfin - (bola.y - yin)
            self.cont -= 1

    def isInArea(self,bola):
        xCenter = bola.x
        yCenter = bola.y

        x1 = self.getXin()
        x2 = self.getXfin()
        y1 = self.getYin()
        y2 = self.getYfin()

        if xCenter > x1-1 and yCenter > y1-1 and xCenter < x2+1 and yCenter < y2+1 and xCenter < x1 + (y2 - yCenter ) + 1:
            return True
        else:
            return False

#variante de casilla con geometria triangular de esta forma
# _____
# \   |
#  \  |
#   \ |
#    \|
class CasillaTriangular4(Casilla):

    def __init__(self,x,y,contador,screen):
        Casilla.__init__(self,x,y,contador,screen)
        self.id = 1

    def draw(self):
        a = COLOR_Red2[0] * self.cont / self.contTotal + COLOR_Yellow[0] * (
            self.contTotal - self.cont) / self.contTotal

        b = COLOR_Red2[1] * self.cont / self.contTotal + COLOR_Yellow[1] * (
            self.contTotal - self.cont) / self.contTotal

        c = COLOR_Red2[2] * self.cont / self.contTotal + COLOR_Yellow[2] * (
            self.contTotal - self.cont) / self.contTotal

        if a < 0 or a > 255:
            a = 0

        if b < 0 or b > 255:
            b = 0

        if c < 0 or c > 255:
            c = 0

        colorCaja = (a, b, c)

        pygame.draw.line(self.screen, colorCaja, [self.x - 20.5, self.y - 20.5], [self.x + 20.5, self.y - 20.5], 2)
        pygame.draw.line(self.screen, colorCaja, [self.x + 20.5, self.y - 20.5], [self.x + 20.5, self.y + 20.5], 2)
        pygame.draw.line(self.screen, colorCaja, [self.x - 20.5, self.y - 20.5], [self.x + 20.5, self.y + 20.5], 2)
        self.drawCounter()
        return

    def colisionBolita(self,bola):

        xin = self.getXin()
        xfin = self.getXfin()
        yin = self.getYin()
        yfin = self.getYfin()


        if bola.getXfin() - bola.velx > xfin and bola.velx < 0:
            bola.colisionHor(xfin+1)
            self.cont -= 1
        elif bola.getYin() - bola.vely < yin and bola.vely > 0:
            bola.colisionVer(yin-1)
            self.cont -= 1
        else:
            aux = bola.velx
            bola.velx = bola.vely
            bola.vely = aux
            bola.x = xfin - (bola.y - yin)
            self.cont -= 1

    def isInArea(self,bola):
        xCenter = bola.x
        yCenter = bola.y

        x1 = self.getXin()
        x2 = self.getXfin()
        y1 = self.getYin()
        y2 = self.getYfin()

        if xCenter > x1-1 and yCenter > y1-1 and xCenter < x2+1 and yCenter < y2+1 and xCenter > x2 - (y2 - yCenter) - 1:
            return True
        else:
            return False