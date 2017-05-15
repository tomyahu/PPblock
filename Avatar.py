#Icono en pantalla que representa al jugador
class Avatar():

    #recibe la imagen, y las coordenadas en donde esta centrada la imagen
    #respecto al borde superior izquierdo de esta
    def __init__(self, image, puntoX, puntoY):
        self.image = image
        self.px = puntoX
        self.py = puntoY