import pyxel
from ..constantes import *

class Contadores:

    def __init__(self):
        #Creamos las variables para el objeto de la clase
        self.contador_vidas = 0
        self.puntos = 0

    #Metodo para actualizar los contadores
    def update(self, vidas_mario, puntos_mario):
        self.contador_vidas = vidas_mario
        self.puntos = puntos_mario

    #Metodo para pintar los contadores
    def draw(self):
        #Pintamos las vidas de mario
        if self.contador_vidas == 1:
            pyxel.blt(9, 24, 1, 131, 8, 7, 8)

        elif self.contador_vidas == 2:
            pyxel.blt(9, 24, 1, 131, 8, 7, 8)
            pyxel.blt(17, 24, 1, 131, 8, 7, 8)

        elif self.contador_vidas == 3:
            pyxel.blt(9, 24, 1, 131, 8, 7, 8)
            pyxel.blt(17, 24, 1, 131, 8, 7, 8)
            pyxel.blt(25, 24, 1, 131, 8, 7, 8)

        #Pintamos el contador de puntos
        pyxel.blt(26, 1, 0, 34, 52, 22, 7)

        #Pintamos los puntos
        pyxel.text(30, 12, str(self.puntos), 7)
