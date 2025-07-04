import pyxel
from ..constantes import *

class DonkeyKong:

    def __init__(self):
        #Creamos las variables para cada objeto de la clase
        self.x = 38
        self.y = 84
        self.estado = 0

    #Metodo para actualizar el estado de donkey kong
    def update(self):
        self.estado += 1
        #Con el modulo cuando el estado llega hasta 4 vuelve a ser 0
        self.estado = self.estado % 4

    #Metodo para pintar a donkey kong
    def draw(self):
        #dk cogiendo barril
        if self.estado == 0:
            pyxel.blt(self.x - (DK_ANCHO/2), self.y - DK_ALTO, 1, 50, 58, DK_ANCHO, DK_ALTO)
        #dk con el barril cogido
        if self.estado == 1:
            pyxel.blt(self.x - (DK_ANCHO/2), self.y - DK_ALTO, 1, 5, 212, DK_ANCHO, DK_ALTO)
        #dk lanzando barril
        if self.estado == 2:
            pyxel.blt(self.x - (DK_ANCHO/2), self.y - DK_ALTO, 1, 50, 58, -DK_ANCHO, DK_ALTO)
        #dk sin barril
        if self.estado == 3:
            pyxel.blt(self.x - (DK_ANCHO/2), self.y - DK_ALTO, 1, 5, 58, DK_ANCHO, DK_ALTO)
