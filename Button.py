

class Button():

    def __init__(self,x,y,textureArr,screen):
        self.x = x
        self.y = y
        self.tex = textureArr
        self.im = 0
        self.screen = screen

    def inArea(self,x1,y1):
        if x1 > self.getXin() and x1 < self.getXfin() and y1 > self.getYin() and y1 < self.getYfin():
            return True
        else:
            return False

    def draw(self):
        self.screen.blit(self.tex[self.im].image, (self.x - (self.tex[self.im].ancho / 2), self.y - (self.tex[self.im].alto / 2)))

    def kill(self):
        del self

    def getXin(self):
        return self.x - (self.tex[self.im].ancho/2)

    def getYin(self):
        return self.y - (self.tex[self.im].alto/2)

    def getXfin(self):
        return self.x + (self.tex[self.im].ancho/2)

    def getYfin(self):
        return self.y + (self.tex[self.im].alto/2)


class PlayButton(Button):

    def __init__(self,x,y,texture,screen):
        Button.__init__(self,x,y,texture,screen)

