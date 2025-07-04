import pyxel
import random

from ..constantes import *

class Barriles:

    def __init__(self, matriz_juego):
        #Creamos las variables para cada objeto de la clase
        self.x = 57
        self.y = 84
        self.derecha = True
        self.__orientacion = 1 # 1: derecha / -1: izquierda

        self.bajando = False
        self.__estado = 0

        self.matriz_juego = matriz_juego
        self.aleatorio = 0
        self.aleatorio_ya_calculado = False

        self.frames = pyxel.frame_count

        self.probabilidad_bajar = 4
        self.mario_saltado = False


    #Metodo para actualizar los barriles
    def update(self):
        #Para controlar la animacion de los barriles
        if pyxel.frame_count - self.frames > FRAMES_RODAR:
            self.frames = pyxel.frame_count
            self.__estado += 1
            if self.bajando:
                self.__estado = self.__estado % 2
            else:
                self.__estado = self.__estado % 4

        x_nuevo = self.x
        y_nuevo = self.y

        #Movimiento barril izquierda
        if not self.derecha:
            self.__orientacion = -1
            x_nuevo = max(self.x - 1, BARRIL_ANCHO/2)

            #Movimiento barril izquierda subida escalon
            if self.matriz_juego[int(x_nuevo)][int(y_nuevo - 1)] == 1 \
            or self.matriz_juego[int(x_nuevo)][int(y_nuevo - 1)] >= 3: \
                y_nuevo = max(self.y - 1, BARRIL_ALTO)

            #Movimiento barril izquierda bajada escalon
            if self.matriz_juego[int(x_nuevo)][int(y_nuevo + 1)] == 1:
                y_nuevo = max(self.y + 1, BARRIL_ALTO)

        #Movimiento barril derecha
        if self.derecha:
            self.__orientacion = 1
            x_nuevo = min(self.x + 1, PANTALLA_ANCHO - (BARRIL_ANCHO/2))

            #Movimiento barril derecha subida escalon
            if self.matriz_juego[int(x_nuevo)][int(y_nuevo - 1)] == 1 \
            or self.matriz_juego[int(x_nuevo)][int(y_nuevo - 1)] >= 3:
                y_nuevo = max(self.y - 1, BARRIL_ALTO)

            #Movimiento barril derecha bajada escalon
            if self.matriz_juego[int(x_nuevo)][int(y_nuevo + 1)] == 1:
                y_nuevo = max(self.y + 1, BARRIL_ALTO)

        #Movimiento barril abajo (por escaleras)
        #probabilidad de que baje por una escalera del 25%
        if self.matriz_juego[int(self.x)][int(self.y)] == 4:
        #Calculamos el aleatorio cuando pasa por el centro de la escalera (posicion de matriz con un 4)
            self.aleatorio = random.randint(1, self.probabilidad_bajar)

        if self.matriz_juego[int(self.x)][int(self.y)] == 4 and self.aleatorio == 1:
            y_nuevo = min(self.y + 1, PANTALLA_ALTO)
            self.bajando = True
            self.__estado = 0

        #Si se encuentra en una escalera (posicion 2 de la matriz) desciende
        if self.matriz_juego[int(self.x)][int(self.y)] == 2:
            y_nuevo = min(self.y + 1, PANTALLA_ALTO)


        #Comprobamos si es el ultimo pixel de la caida para cambiar la direccion del barril
        if self.matriz_juego[int(self.x)][int(self.y+1)] == 1:
            self.bajando = False
            self.__estado = 0
            self.aleatorio = 0
            if self.derecha:
                self.derecha = False
            else:
                self.derecha = True

        #Comprobacion para derecha e izquierda
        if self.matriz_juego[int(x_nuevo)][int(y_nuevo)] == 1\
        or self.matriz_juego[int(x_nuevo)][int(y_nuevo)] >= 3:
            self.x = x_nuevo
            self.y = y_nuevo

        #Comprobacion para abajo
        if self.matriz_juego[int(x_nuevo)][int(y_nuevo)] == 2 \
        or self.matriz_juego[int(x_nuevo)][int(y_nuevo)] >= 3:
            self.y = y_nuevo

        #Comprobacion caida al final de plataforma
        if (self.matriz_juego[int(self.x)][int(self.y)] == 1 or self.matriz_juego[int(self.x)][int(self.y)] >= 3) \
        and self.matriz_juego[int(x_nuevo)][int(y_nuevo)] == 0 and self.matriz_juego[int(x_nuevo)][int(y_nuevo + 1)] == 0 \
        and self.matriz_juego[int(x_nuevo)][int(y_nuevo - 1)] == 0:
            self.x = x_nuevo
            self.y = y_nuevo
            self.bajando = True

        #si el barril esta en un 0 cae
        if self.matriz_juego[int(self.x)][int(self.y)] == 0:
            y_nuevo = min(self.y + 1, PANTALLA_ALTO)
            x_nuevo += int(self.__orientacion*random.randint(1,3)/3)
            self.y = y_nuevo
            self.x = x_nuevo
            self.bajando = False


    #Metodo para pintar los barriles
    def draw(self):
        #Pintamos el barril en la posicion x y definida por el metodo update
        if self.bajando:
            #ponemos para que ruede hacia abajo (de frente) cuando baja escaleras
            if self.__estado == 0:
                pyxel.blt(self.x - (BARRIL_ANCHO/2)-2, self.y - BARRIL_ALTO, 1, 129, 106, self.__orientacion*(BARRIL_ANCHO+4), BARRIL_ALTO,0)
            elif self.__estado == 1:
                pyxel.blt(self.x - (BARRIL_ANCHO/2)-2, self.y - BARRIL_ALTO, 1, 153, 106, self.__orientacion*(BARRIL_ANCHO+4), BARRIL_ALTO,0)
        else:
            #si no esta bajando, rueda lateralmente
            if self.__estado == 0:
                pyxel.blt(self.x - (BARRIL_ANCHO/2), self.y - BARRIL_ALTO, 1, 35, 106, self.__orientacion*BARRIL_ANCHO, BARRIL_ALTO,0)
            elif self.__estado == 1:
                pyxel.blt(self.x - (BARRIL_ANCHO/2), self.y - BARRIL_ALTO, 1, 59, 106, self.__orientacion*BARRIL_ANCHO, BARRIL_ALTO,0)
            elif self.__estado == 2:
                pyxel.blt(self.x - (BARRIL_ANCHO/2), self.y - BARRIL_ALTO, 1, 83, 106, self.__orientacion*BARRIL_ANCHO, BARRIL_ALTO,0)
            elif self.__estado == 3:
                pyxel.blt(self.x - (BARRIL_ANCHO/2), self.y - BARRIL_ALTO, 1, 107, 106, self.__orientacion*BARRIL_ANCHO, BARRIL_ALTO,0)
