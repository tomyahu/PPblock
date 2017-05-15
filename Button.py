

class Button():

    #recibe la posicion, la lista de texturas que representa
    #la animacion del boton y la pantalla
    def __init__(self,x,y,textureArr,screen):
        self.x = x
        self.y = y
        self.tex = textureArr
        self.im = 0
        self.screen = screen

    #revisa si un punto esta dentro del boton
    def inArea(self,x1,y1):
        if x1 > self.getXin() and x1 < self.getXfin() and y1 > self.getYin() and y1 < self.getYfin():
            return True
        else:
            return False

    #dbuja el boton
    def draw(self):
        self.screen.blit(self.tex[self.im].image, (self.x - (self.tex[self.im].ancho / 2), self.y - (self.tex[self.im].alto / 2)))

    #se destruye el objetp
    def kill(self):
        del self

    # devuelve el x mas a la izquierda de su textura
    def getXin(self):
        return self.x - (self.tex[self.im].ancho/2)

    # devuelve el y mas arriba de su textura
    def getYin(self):
        return self.y - (self.tex[self.im].alto/2)

    # devuelve el x mas a la derecha de su textura
    def getXfin(self):
        return self.x + (self.tex[self.im].ancho/2)

    # devuelve el y mas abajo de su textura
    def getYfin(self):
        return self.y + (self.tex[self.im].alto/2)

