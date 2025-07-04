import pyxel
from ..constantes import *

class Plataformas:

    def __init__(self):
        pass

    #Metodo para añadir las plataformas a la matriz
    def definir_matriz(self, matriz):
        #Anadimos la primera plataforma a la matriz
        j = 240
        for i in range(PANTALLA_ANCHO):
            #Anadimos a la matriz un 1 en las posiciones en las que esta el borde de arriba de la plataforma
            matriz[i][j] = 1

        #Anadimos la segunda plataforma a la matriz
        j = 208
        for i in range (PANTALLA_ANCHO - 16):
            matriz[i][j] = 1

        #Anadimos la tercera plataforma a la matriz
        j = 187
        for i in range(PLATAFORMA_ANCHO, PANTALLA_ANCHO, PLATAFORMA_ANCHO):
        #for _ in range(inicio, final, paso)
            for r in range(i, i + PLATAFORMA_ANCHO):
                matriz[r][j] = 1
            j -= 1

        #Anadimos la cuarta plataforma a la matriz
        j = 142
        for i in range(0, PANTALLA_ANCHO - PLATAFORMA_ANCHO, PLATAFORMA_ANCHO):
        #for_in range(inicio, final, paso)
            for r in range(i, i + PLATAFORMA_ANCHO):
                matriz[r][j] = 1
            j += 1

        #Anadimos la quinta plataforma a la matriz
        j = 121
        for i in range(PLATAFORMA_ANCHO, PANTALLA_ANCHO, PLATAFORMA_ANCHO):
        #for _ in range(inicio, final, paso)
            for r in range(i, i + PLATAFORMA_ANCHO):
                matriz[r][j] = 1
            j -= 1

        #Anadimos la sexta plataforma a la matriz
        j = 84
        for i in range(0, PANTALLA_ANCHO - PLATAFORMA_ANCHO, PLATAFORMA_ANCHO):
            #Anadimos la parte plana
            if(i < 144):
                for r in range(i, i + PLATAFORMA_ANCHO):
                    matriz[r][j] = 1
            #Anadimos la parte con pendiente
            else:
                j += 1
                for r in range(i, i + PLATAFORMA_ANCHO):
                    matriz[r][j] = 1

        #Anadimos la septima plataforma a la matriz (la mas alta - Pauline)
        j = 56
        for i in range(88, 136):
            matriz[i][j] = 1


    #Metodo para pintar las plataformas
    def draw(self):
        #Primera plataforma
        i = 0
        j = 240
        while i < PANTALLA_ANCHO:
            #Pintamos la plataforma trozo a trozo
            pyxel.blt(i, j, 0, 96, 108, PLATAFORMA_ANCHO, PLATAFORMA_ALTO)

            i += PLATAFORMA_ANCHO

        #Segunda plataforma
        i = 0
        j = 208
        while i < (PANTALLA_ANCHO - 16):
            #Pintamos la plataforma trozo a trozo
            pyxel.blt(i, j, 0, 96, 108, PLATAFORMA_ANCHO, PLATAFORMA_ALTO)

            i += PLATAFORMA_ANCHO

        #Tercera plataforma con pendiente
        i = PLATAFORMA_ANCHO
        j = 187
        while i < PANTALLA_ANCHO:
            pyxel.blt(i, j, 0, 96, 108, PLATAFORMA_ANCHO, PLATAFORMA_ALTO)

            i += PLATAFORMA_ANCHO
            j -= 1

        #Cuarta plataforma con pendiente
        i = 0
        j = 142
        while i < (PANTALLA_ANCHO - PLATAFORMA_ANCHO):
            pyxel.blt(i, j, 0, 96, 108, PLATAFORMA_ANCHO, PLATAFORMA_ALTO)

            i += PLATAFORMA_ANCHO
            j += 1

        #Quinta plataforma con pendiente
        i = PLATAFORMA_ANCHO
        j = 121
        while i < PANTALLA_ANCHO:
            pyxel.blt(i, j, 0, 96, 108, PLATAFORMA_ANCHO, PLATAFORMA_ALTO)

            i += PLATAFORMA_ANCHO
            j -= 1

        #Sexta plataforma plana y con pendiente
        i = 0
        j = 84
        while i < (PANTALLA_ANCHO - PLATAFORMA_ANCHO):
            #Pintamos la parte plana
            if(i < 144):
                pyxel.blt(i, j, 0, 96, 108, PLATAFORMA_ANCHO, PLATAFORMA_ALTO)
            #Pintamos la parte con pendiente
            else:
                j += 1
                pyxel.blt(i, j, 0, 96, 108, PLATAFORMA_ANCHO, PLATAFORMA_ALTO)

            i += PLATAFORMA_ANCHO

        #Septima plataforma (la mas alta - Pauline)
        j = 56
        for i in range(88, 136, PLATAFORMA_ANCHO):
        #for_in range(inicio, final, paso)
            pyxel.blt(i, j, 0, 96, 108, PLATAFORMA_ANCHO, PLATAFORMA_ALTO)

        #Pintamos unos barriles decorativos
        pyxel.blt(4, 84-16, 1, 12, 103, 10, 16)
        pyxel.blt(4, 84-16-16, 1, 12, 103, 10, 16)
        #Pintamos el barril de gasolina y el fuego
        pyxel.blt(0, 240-16, 1, 8, 0, 16, 16)
        pyxel.blt(1, 240-16-15, 1, 24, 1, 15, 15,0)
