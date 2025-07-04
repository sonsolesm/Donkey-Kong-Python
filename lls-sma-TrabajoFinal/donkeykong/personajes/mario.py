import pyxel
import time
from ..constantes import *

class Mario:

    def __init__(self, matriz_juego):
        #Creamos las variables para el objeto de la clase
        self.x = 20
        self.y = 240
        self.vidas = 3
        self.matriz_juego = matriz_juego

        self.__orientacion = -1
        #1 mira a la izquierda y -1 a la derecha

        self.__estado = 0
        # 0 es quieto, 1 saltando

        self.__saltando = False
        self.max_salto = 18
        self.y_antes_salto = 0


    #Metodo para actualizar las variables de Mario
    def update(self):

        x_nuevo = self.x
        y_nuevo = self.y

        #Prueba ganar (ganas al llegar a la posición x:128 y:56)
        if pyxel.btn(pyxel.KEY_T):
            x_nuevo = 132
            y_nuevo = 56

        #Movimiento mario izquierda
        if pyxel.btn(pyxel.KEY_LEFT):
            x_nuevo = max(self.x - 1, MARIO_ANCHO/2)
            self.__orientacion = 1

            #Movimiento Mario izquierda subida escalon
            if self.matriz_juego[int(x_nuevo)][int(y_nuevo - 1)] == 1 or self.matriz_juego[int(x_nuevo)][int(y_nuevo - 1)] >= 3:
                y_nuevo = max(self.y - 1, MARIO_ALTO)

            #Movimiento Mario izquierda bajada escalon
            if self.matriz_juego[int(x_nuevo)][int(y_nuevo + 1)] == 1:
                y_nuevo = max(self.y + 1, MARIO_ALTO)

        #Movimiento Mario derecha
        if pyxel.btn(pyxel.KEY_RIGHT):
            self.__orientacion = -1
            x_nuevo = min(self.x + 1, PANTALLA_ANCHO - (MARIO_ANCHO/2))

            #Movimiento Mario derecha subida escalon
            if self.matriz_juego[int(x_nuevo)][int(y_nuevo - 1)] == 1 or self.matriz_juego[int(x_nuevo)][int(y_nuevo - 1)] >= 3:
                y_nuevo = max(self.y - 1, MARIO_ALTO)

            #Movimiento Mario derecha bajada escalon
            if self.matriz_juego[int(x_nuevo)][int(y_nuevo + 1)] == 1:
                y_nuevo = max(self.y + 1, MARIO_ALTO)

        #Movimiento Mario arriba (salto y escaleras)
        if self.__saltando:
            #Movimiento Mario salto - tramo en el que sube
            if (self.y_antes_salto - self.y) < 2:
                y_nuevo -= 1
            if (self.y_antes_salto - self.y) < self.max_salto:
                y_nuevo -= 1
                self.__estado = 1
            else:
                self.__saltando = False
                self.__estado = 0

            self.x = x_nuevo
            self.y = y_nuevo

        else:
            #Movimiento Mario arriba (por escaleras)
            if pyxel.btn(pyxel.KEY_UP) and self.matriz_juego[int(self.x)][int(self.y)] > 0:
                y_nuevo = max(self.y - 1, MARIO_ALTO)

            #Movimiento Mario abajo (por escaleras)
            if pyxel.btn(pyxel.KEY_DOWN) and self.matriz_juego[int(self.x)][int(self.y)] > 1:
                y_nuevo = min(self.y + 1, PANTALLA_ALTO)

            #Movimiento Mario salto - inicio del salto
            if pyxel.btn(pyxel.KEY_SPACE) and self.matriz_juego[int(self.x)][int(self.y)] != 0\
            and self.matriz_juego[int(self.x)][int(self.y)] != 2:
                self.__saltando = True
                self.y_antes_salto = self.y
                y_nuevo-= 2

            #Comprobacion para derecha e izquierda
            if self.matriz_juego[int(x_nuevo)][int(y_nuevo)] == 1\
            or self.matriz_juego[int(x_nuevo)][int(y_nuevo)] == 0\
            or self.matriz_juego[int(x_nuevo)][int(y_nuevo)] >= 3:
                self.x = x_nuevo
                self.y = y_nuevo

            #Comprobacion para arriba y abajo
            if self.matriz_juego[int(x_nuevo)][int(y_nuevo)] == 2 or self.matriz_juego[int(x_nuevo)][int(y_nuevo)] >= 3:
                self.y = y_nuevo

            #Comprobacion caida al final de plataforma
            #comprobamos si esta en el final de la plataforma intentando caer (intentando ponerse en un 0)
            #entonces ponemos a mario en ese 0
            if (self.matriz_juego[int(self.x)][int(self.y)] == 1 or self.matriz_juego[int(self.x)][int(self.y)] >= 3) \
            and self.matriz_juego[int(x_nuevo)][int(y_nuevo)] == 0 and self.matriz_juego[int(x_nuevo)][int(y_nuevo + 1)] == 0 \
            and self.matriz_juego[int(x_nuevo)][int(y_nuevo - 1)] == 0:
                self.x = x_nuevo
                self.y = y_nuevo
            #si mario esta en un 0 cae
            if self.matriz_juego[int(self.x)][int(self.y)] == 0:
                y_nuevo = min(self.y + 1, PANTALLA_ALTO)
                self.y = y_nuevo


    def draw(self):
        #Pintamos a Mario en la posicion x y definida por el metodo update
        #la posicion (x,y) se define como si estuviera en el centro de los pies justo debajo de Mario
        #por ello se debe corregir cuando lo pintamos (esquina izquierda de arriba)
        if self.__estado == 0:
            pyxel.blt(self.x - (MARIO_ANCHO/2), self.y - MARIO_ALTO, 1, 6, 32, self.__orientacion*MARIO_ANCHO, MARIO_ALTO,0)
        elif self.__estado == 1:
            pyxel.blt(self.x - (MARIO_ANCHO/2), self.y - MARIO_ALTO, 1, 222, 32, self.__orientacion*MARIO_ANCHO, MARIO_ALTO,0)
