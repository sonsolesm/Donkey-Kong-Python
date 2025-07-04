import pyxel
from ..constantes import *

class Escaleras:

    #Metodo para añadir las escaleras a la matriz
    def definir_matriz(self, matriz):
        #Ponemos un 2 para el tramo de escalera y un 3 para el borde superior de esta
        #usar diferentes numeros nos sirve para diferenciar en que parte de la matriz estamos exactamente

        #Anadimos la Escalera 1
        for i in range(184, 184 + ESCALERA_ANCHO):
        #for_in range(inicio, final, paso)
            for j in range(208, 240):
                matriz[i][j] = 2
        for i in range(184, 184 + ESCALERA_ANCHO):
            matriz[i][208] = 3

        matriz[184+int(ESCALERA_ANCHO/2)][208] = 4

        #Anadimos la Escalera 2
        for i in range(64, 64 + ESCALERA_ANCHO):
            for j in range(184, 208):
                matriz[i][j] = 2
        for i in range(64, 64 + ESCALERA_ANCHO):
            matriz[i][184] = 3

        matriz[64+int(ESCALERA_ANCHO/2)][184] = 4

        #Anadimos la Escalera 3
        for i in range(24, 24 + ESCALERA_ANCHO):
            for j in range(143, 187):
                matriz[i][j] = 2
        for i in range(24, 24 + ESCALERA_ANCHO):
            matriz[i][143] = 3

        matriz[24+int(ESCALERA_ANCHO/2)][143] = 4

        #Anadimos la Escalera 4
        for i in range(184, 184 + ESCALERA_ANCHO):
            for j in range(153, 177):
                matriz[i][j] = 2
        for i in range(184, 184 + ESCALERA_ANCHO):
            matriz[i][153] = 3

        matriz[184+int(ESCALERA_ANCHO/2)][153] = 4

        #Anadimos la Escalera 5
        for i in range(96, 96 + ESCALERA_ANCHO):
            for j in range(116, 148):
                matriz[i][j] = 2
        for i in range(96, 96 + ESCALERA_ANCHO):
            matriz[i][116] = 3

        matriz[96+int(ESCALERA_ANCHO/2)][116] = 4

        #Anadimos la Escalera 6
        for i in range(184, 184 + ESCALERA_ANCHO):
            for j in range(87, 111):
                matriz[i][j] = 2
        for i in range(184, 184 + ESCALERA_ANCHO):
            matriz[i][87] = 3

        matriz[184+int(ESCALERA_ANCHO/2)][87] = 4

        #Anadimos la Escalera 7 (Pauline)
        for i in range(128, 128 + ESCALERA_ANCHO):
            for j in range(56, 84):
                matriz[i][j] = 2
        for i in range(128, 128 + ESCALERA_ANCHO):
            matriz[i][56] = 3

        #Anadimos la Escalera 8 (Donkey Kong)
        for i in range(80, 80 + ESCALERA_ANCHO):
            for j in range(32, 84):
                matriz[i][j] = 2
        for i in range(80, 80 + ESCALERA_ANCHO):
            matriz[i][32] = 3
        for i in range(80, 80 + ESCALERA_ANCHO):
            #Para que Mario se pueda mover horizontalmente en la escalera que esta junto a la plataforma de Pauline
            matriz[i][56] = 1

        #Anadimos la Escalera 9 (Donkey Kong)
        for i in range(64, 64 + ESCALERA_ANCHO):
            for j in range(32, 84):
                matriz[i][j] = 2
        for i in range(64, 64 + ESCALERA_ANCHO):
            matriz[i][32] = 3


    def draw(self):
        #Pintamos las escaleras
        #Escalera 1
        i = 184
        for j in range(208, 240, ESCALERA_ALTO):
        #for_in range(inicio, final, paso)
            pyxel.blt(i, j, 0, 72, 84, ESCALERA_ANCHO, ESCALERA_ALTO)

        #Escalera 2
        i = 64
        for j in range(184, 208, ESCALERA_ALTO):
            pyxel.blt(i, j, 0, 72, 84, ESCALERA_ANCHO, ESCALERA_ALTO)

        #Escalera 3
        i = 24
        for j in range(143, 187, ESCALERA_ALTO):
            pyxel.blt(i, j, 0, 72, 84, ESCALERA_ANCHO, ESCALERA_ALTO)

        #Escalera 4
        i = 184
        for j in range(153, 177, ESCALERA_ALTO):
            pyxel.blt(i, j, 0, 72, 84, ESCALERA_ANCHO, ESCALERA_ALTO)

        #Escalera 5
        i = 96
        for j in range(116, 148, ESCALERA_ALTO):
            pyxel.blt(i, j, 0, 72, 84, ESCALERA_ANCHO, ESCALERA_ALTO)

        #Escalera 6
        i = 184
        for j in range(87, 111, ESCALERA_ALTO):
            pyxel.blt(i, j, 0, 72, 84, ESCALERA_ANCHO, ESCALERA_ALTO)

        #Escalera 7 (Pauline)
        i = 128
        for j in range(56, 84, ESCALERA_ALTO):
            pyxel.blt(i, j, 0, 72, 84, ESCALERA_ANCHO, ESCALERA_ALTO)

        #Escalera 8 (Donkey Kong)
        i = 80
        for j in range(32, 84, ESCALERA_ALTO):
            pyxel.blt(i, j, 0, 72, 84, ESCALERA_ANCHO, ESCALERA_ALTO)

        #Escalera 9 (Donkey Kong)
        i = 64
        for j in range(32, 84, ESCALERA_ALTO):
            pyxel.blt(i, j, 0, 72, 84, ESCALERA_ANCHO, ESCALERA_ALTO)
